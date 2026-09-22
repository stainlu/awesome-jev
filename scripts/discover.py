"""Daily discovery sweep: find every public repo in the Jev ecosystem.

Strategy: several high-precision GitHub search queries, each sliced by creation
date when it reports more than the 1000 results the search API will page
through. Results are merged into data/projects.json by full_name, so a project
keeps its first_seen date and never loses its place when a signal goes quiet.

Run: python3 scripts/discover.py            sweep GitHub, then merge
     python3 scripts/discover.py --rebuild  re-apply the rules to what is already
                                            on disk, without touching the API
"""
import datetime as dt
import json
import pathlib
import re
import sys
import time

from github import Client

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "data" / "projects.json"
EXCLUDED = ROOT / "data" / "excluded.md"

# The domain definition, in two tiers.
#
# STRONG signals are self-declared: the author tagged the repo for Jev or named
# the model class. A match is the author saying "this is a Jev project".
#
# WEAK signals are word matches. They find far more, and they misfire — GitHub
# tokenises on punctuation, so `typesafe.ai` also matches "typesafe Commerce
# SDK", and `jev` is Japanese encephalitis virus as well as a surname.
#
# Deliberately absent: `topic:typesafe`. It is the generic type-safety topic
# (Go generics libraries, TanStack Router, http4k) and was 437 entries of pure
# noise when measured.
STRONG_SIGNALS = [
    # The vendor's own repositories. Their descriptions say "the TypeSafe API",
    # not "Jev", and the SDKs predate the launch, so nothing else finds them.
    "user:typesafe-ai",
    "topic:jev",
    "topic:typesafe-ai",
    "topic:system-one",
    "topic:system-one-models",
    '"System One model" in:description',
]
WEAK_SIGNALS = [
    "jev in:name",
    "jev in:description",
    "typesafe.ai in:description",
]

# Code signals are the strongest evidence there is — a real endpoint or a real
# credential in the source — and they are the only way to find the entries that
# matter most: established projects that added Jev support without renaming
# themselves or retagging. litellm, pydantic-ai and BAML are all invisible to
# every repository-level query above.
CODE_SIGNALS = [
    '"api.typesafe.ai/v1/systemone"',
    '"@typesafe-ai/sdk"',
    '"TYPESAFE_API_KEY"',
]
SIGNALS = STRONG_SIGNALS + WEAK_SIGNALS

# Jev was announced on this date. A repo older than that cannot have been built
# on it, so a weak match on an older repo is a collision, not a project. An
# older repo that genuinely adopted Jev says so with a topic — a strong signal.
EPOCH = dt.date(2026, 9, 15)


def accept(created: str, signals: list[str]) -> bool:
    """Whether a search hit is evidence of a Jev project."""
    if created >= EPOCH.isoformat():
        return True
    return any(s in STRONG_SIGNALS or s.startswith("code:") for s in signals)


def load_exclusions() -> set[str]:
    """Hand-maintained false positives, one `owner/repo — reason` line each."""
    if not EXCLUDED.exists():
        return set()
    out = set()
    for line in EXCLUDED.read_text().splitlines():
        m = re.match(r"^-\s+([\w.-]+/[\w.-]+)", line.strip())
        if m:
            out.add(m.group(1).lower())
    return out


def date_slices(signal: str, today: dt.date) -> list[str]:
    """`created:` qualifiers that together cover every repo the signal can match.

    One per day since Jev existed, plus a single catch-all for everything older —
    without which a signal that grows past 1000 results would silently drop the
    established projects that adopted Jev, which are the most interesting ones.
    """
    days = (today - EPOCH).days
    per_day = [
        f"created:{(EPOCH + dt.timedelta(days=i)).isoformat()}" for i in range(days + 1)
    ]
    if signal in WEAK_SIGNALS:
        return per_day  # pre-Jev weak matches are rejected by accept() anyway
    return [f"created:<{EPOCH.isoformat()}"] + per_day


def sweep(client: Client, signal: str, today: dt.date) -> dict[str, dict]:
    items, total = client.search_repos(signal)
    if total > 1000:
        # Too many to page through; re-run the query one creation-slice at a time.
        items = []
        for qualifier in date_slices(signal, today):
            chunk, chunk_total = client.search_repos(f"{signal} {qualifier}")
            if chunk_total > 1000:
                print(f"  ! {signal} {qualifier} has {chunk_total}; truncated at 1000",
                      file=sys.stderr)
            items.extend(chunk)
            time.sleep(1)
    print(f"  {signal}: {len(items)} fetched (reported {total})", file=sys.stderr)
    return {r["full_name"]: r for r in items}


def record(repo: dict, signals: list[str], first_seen: str) -> dict:
    created = repo["created_at"][:10]
    pushed = repo["pushed_at"][:10]
    return {
        "full_name": repo["full_name"],
        "url": repo["html_url"],
        "description": (repo.get("description") or "").strip(),
        "stars": repo["stargazers_count"],
        "language": repo.get("language") or "",
        "created": created,
        "pushed": pushed,
        # The one signal that separates a real project from a launch-week drop.
        "alive": pushed > created,
        "archived": repo.get("archived", False),
        "fork": repo.get("fork", False),
        "signals": sorted(signals),
        "first_seen": first_seen,
    }


def keep(entry: dict, exclusions: set[str]) -> bool:
    """Whether an entry already on disk still belongs in the index.

    Applied to carried-forward entries too, so that tightening a rule actually
    removes what it was written to remove instead of leaving it behind.
    """
    return (
        entry["full_name"].lower() not in exclusions
        # A fork is someone else's project with a copy button pressed. The
        # original is already indexed; the copy is noise.
        and not entry.get("fork")
        and accept(entry["created"], entry["signals"])
    )


def main() -> None:
    rebuild = "--rebuild" in sys.argv
    today = dt.date.today()
    existing = json.loads(INDEX.read_text()) if INDEX.exists() else {}
    exclusions = load_exclusions()

    index: dict[str, dict] = {}
    if not rebuild:
        found: dict[str, dict] = {}
        hits: dict[str, list[str]] = {}
        client = Client()
        print("sweeping:", file=sys.stderr)
        for signal in SIGNALS:
            for name, repo in sweep(client, signal, today).items():
                found[name] = repo
                hits.setdefault(name, []).append(signal)

        print("searching code:", file=sys.stderr)
        for signal in CODE_SIGNALS:
            names = client.search_code(signal)
            print(f"  {signal}: {len(names)} repos", file=sys.stderr)
            for name in names:
                if name not in found:
                    repo = client.get_repo(name)
                    if repo is None:
                        continue  # deleted or made private since it was indexed
                    found[name] = repo
                hits.setdefault(name, []).append(f"code:{signal}")

        for name, repo in found.items():
            entry = record(repo, hits[name], existing.get(name, {}).get(
                "first_seen", today.isoformat()))
            if keep(entry, exclusions):
                index[name] = entry

    # A project that drops out of every search (renamed, made private, deleted)
    # is kept but marked, rather than silently vanishing from the list.
    dropped = 0
    for name, old in existing.items():
        if name in index:
            continue
        if not keep(old, exclusions):
            dropped += 1
            continue
        if not rebuild:
            old["missing_since"] = old.get("missing_since", today.isoformat())
        index[name] = old

    INDEX.parent.mkdir(exist_ok=True)
    INDEX.write_text(json.dumps(index, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
    alive = sum(1 for r in index.values() if r.get("alive"))
    if dropped:
        print(f"dropped {dropped} entries that no longer pass the rules", file=sys.stderr)
    print(f"{len(index)} projects ({alive} committed to after day one) -> {INDEX}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
