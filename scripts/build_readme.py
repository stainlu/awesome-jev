"""Render README.md from the machine-kept index plus the hand-written Featured file.

data/featured.md is the only file a human edits. data/projects.json is owned by
the daily sweep. Neither knows about the other until this script joins them.

Run: python3 scripts/build_readme.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "data" / "projects.json"
FEATURED = ROOT / "data" / "featured.md"
README = ROOT / "README.md"

# GitHub stops rendering a README at 512 KB and shows a truncation notice
# instead. It does not fail, it does not warn, and the table simply disappears —
# so this script refuses to write a file that would cross the line.
RENDER_LIMIT = 512 * 1024
BUDGET = 480 * 1024  # leave room for one sweep's growth between runs

# Raise this to shrink the table when the guard below fires. Every project stays
# in data/projects.json either way; this only controls how many earn a row.
MIN_STARS = 0

HEADER = """# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Every public project built on [Jev](https://typesafe.ai), TypeSafe AI's System One model \
— with the ones worth your afternoon marked.

Jev is not a chat model. You give it program state and a *typed question*; it returns a typed
answer with a calibrated probability, in about 100ms. Three question types: **Choice** (pick one
of N), **Score** (rate on an ordered scale), **Noul** (probability a statement is true). It is a
decision layer for software — routing, classification, moderation, guardrails, scoring — not a
text generator.

The ecosystem went from nothing to thousands of repos in a week, so this list does two jobs.
**Featured** is short and hand-read: every entry was opened and its use of Jev confirmed in the
source, not guessed from its description. **All projects** is the full sweep, run daily.

Not affiliated with TypeSafe AI.
"""

LEGEND = """Swept daily, and listed here if anyone committed to it after the day it was published.
That one filter separates a project from a launch-week drop, and it removes {dormant:,} of the
{total:,} repos in the index.

The complete index — all {total:,}, dormant ones included, with the search signals that found each
— is [`data/projects.json`](data/projects.json). It is generated, so grep it rather than read it.
"""


def parse_featured(text: str) -> list[tuple[str, list[tuple[str, str]]]]:
    """`## Section` headings containing `- owner/repo — why it matters` lines."""
    sections: list[tuple[str, list[tuple[str, str]]]] = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        lines = block.splitlines()
        entries = []
        for line in lines[1:]:
            m = re.match(r"^-\s+([\w.-]+/[\w.-]+)\s+[—-]\s+(.+)$", line.strip())
            if m:
                entries.append((m.group(1), m.group(2).strip()))
        if entries:
            sections.append((lines[0].strip(), entries))
    return sections


def slug(heading: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")


def cell(text: str, limit: int = 110) -> str:
    """Table-safe one-liner.

    These strings come from other people's repo descriptions, so they carry
    characters Markdown reads as syntax: a pipe ends the cell, and a bracket
    starts a link reference that has no definition.
    """
    text = " ".join(text.split())
    for ch in "|[]":
        text = text.replace(ch, "\\" + ch)
    return text[: limit - 1] + "…" if len(text) > limit else text


def main() -> None:
    if not INDEX.exists():
        sys.exit("data/projects.json missing — run scripts/discover.py first")
    index = json.loads(INDEX.read_text())
    sections = parse_featured(FEATURED.read_text()) if FEATURED.exists() else []

    featured_names = {n for _, entries in sections for n, _ in entries}
    live = [r for r in index.values() if not r.get("missing_since")]
    # A repo whose only commit is the day it was created was published and
    # abandoned. It stays in the index; it does not take up a row in the README.
    # Featured entries are not repeated in the table below.
    active = sorted(
        (r for r in live if r["alive"] and r["full_name"] not in featured_names
         and r["stars"] >= MIN_STARS),
        key=lambda r: (-r["stars"], r["full_name"].lower()),
    )

    contents = ["## Contents", ""]
    for heading, _ in sections:
        contents.append(f"- [{heading}](#{slug(heading)})")
    contents.append(f"- [All projects](#all-projects)")

    body = []
    for heading, entries in sections:
        body.append(f"## {heading}\n")
        for name, note in entries:
            repo = index.get(name)
            if repo is None:
                sys.exit(f"featured entry not in index: {name} — run discover.py, or fix the name")
            body.append(f"- [{name}]({repo['url']}) - {note}")
        body.append("")

    body.append(f"## All projects\n")
    body.append(
        f"**{len(active):,} more active projects**, out of {len(live):,} indexed.\n")
    body.append(LEGEND.format(total=len(live), dormant=len(live) - len(active)))
    body.append("| Project | What it is | ★ | Language | Last commit |")
    body.append("| --- | --- | ---: | --- | --- |")
    for r in active:
        desc = cell(r["description"]) or "—"
        body.append(
            f"| [{r['full_name']}]({r['url']}) | {desc} | {r['stars']:,} | "
            f"{r['language'] or '—'} | {r['pushed']} |"
        )

    footer = """
## Contributing

Open a pull request. The index is swept automatically, so you do not need to add a project by
hand — but a Featured entry is a human judgment and always welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).
"""

    text = HEADER + "\n" + "\n".join(contents) + "\n\n" + "\n".join(body) + footer
    size = len(text.encode())
    if size > BUDGET:
        counts = {
            n: sum(1 for r in live if r["alive"] and r["stars"] >= n) for n in (1, 3, 5)
        }
        sys.exit(
            f"README would be {size / 1024:.0f} KB. GitHub stops rendering at "
            f"{RENDER_LIMIT // 1024} KB, so this would silently drop the table.\n"
            f"Raise MIN_STARS in {__file__}:\n"
            + "\n".join(f"  MIN_STARS = {n}  ->  {c:,} rows" for n, c in counts.items())
        )

    README.write_text(text)
    print(f"{len(live)} projects, {len(active)} rows, "
          f"{sum(len(e) for _, e in sections)} featured, {size / 1024:.0f} KB -> {README}")


if __name__ == "__main__":
    main()
