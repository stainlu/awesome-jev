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

HEADER = """# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Every public project built on [Jev](https://typesafe.ai), TypeSafe AI's System One model \
— with the ones worth your afternoon marked.

Jev is not a chat model. You give it program state and a *typed question*; it returns a typed
answer with a calibrated probability, in about 100ms. Three question types: **Choice** (pick one
of N), **Score** (rate on an ordered scale), **Noul** (probability a statement is true). It is a
decision layer for software — routing, classification, moderation, guardrails, scoring — not a
text generator.

The ecosystem went from nothing to thousands of repos in a week, so this list does two jobs:
**Featured** is hand-read and short. **All projects** is the complete index, swept daily.

Not affiliated with TypeSafe AI.
"""

LEGEND = """Swept daily. `Last commit` is the honest activity signal: a project whose only commit
is the day it was created has not been touched since it was published.
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
    """Table-safe one-liner."""
    text = " ".join(text.split()).replace("|", "\\|")
    return text[: limit - 1] + "…" if len(text) > limit else text


def main() -> None:
    if not INDEX.exists():
        sys.exit("data/projects.json missing — run scripts/discover.py first")
    index = json.loads(INDEX.read_text())
    sections = parse_featured(FEATURED.read_text()) if FEATURED.exists() else []

    live = [r for r in index.values() if not r.get("missing_since")]
    live.sort(key=lambda r: (-r["stars"], r["full_name"].lower()))

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
            body.append(f"- [{name}]({repo['url']}) — {note}")
        body.append("")

    body.append(f"## All projects\n")
    body.append(f"{len(live)} projects.\n")
    body.append(LEGEND)
    body.append("| Project | What it is | ★ | Language | Last commit |")
    body.append("| --- | --- | ---: | --- | --- |")
    for r in live:
        desc = cell(r["description"]) or "—"
        never = "" if r["alive"] else " ⚠"
        body.append(
            f"| [{r['full_name']}]({r['url']}) | {desc} | {r['stars']} | "
            f"{r['language'] or '—'} | {r['pushed']}{never} |"
        )

    footer = """
## Contributing

Open a pull request. The index is swept automatically, so you do not need to add a project by
hand — but a Featured entry is a human judgment and always welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).
"""

    README.write_text(
        HEADER + "\n" + "\n".join(contents) + "\n\n" + "\n".join(body) + footer
    )
    print(f"{len(live)} projects, {sum(len(e) for _, e in sections)} featured -> {README}")


if __name__ == "__main__":
    main()
