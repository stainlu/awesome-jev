# Contributing

## Adding a project

You usually do not need to. `scripts/discover.py` runs daily and picks up any public repo that
carries a Jev signal — the topics `jev`, `typesafe-ai`, `system-one`, or a description naming Jev
or typesafe.ai. If yours is missing, the fastest fix is to add one of those topics to your repo.

If it still does not appear after a day, open an issue and say which signal should have caught it.
That is a bug in the sweep, not a missing entry.

## Adding a Featured entry

Featured is the part a human writes, and it is deliberately short. Edit `data/featured.md`:

```
- owner/repo — why this is worth your afternoon
```

The note should say why you would click, not what the project is — the index below already says
what it is. Two rules:

- The project must still be committed to after the day it was published.
- It should be something you would send to a colleague, not something that merely exists.

Removing a Featured entry that no longer deserves it is as welcome as adding one.

## False positives

`JEV` is also the abbreviation for Japanese encephalitis virus, and a surname. If an unrelated
project shows up in the index, add it to `data/excluded.md` with a reason.

## Rebuilding

```
python3 scripts/discover.py     # sweep GitHub -> data/projects.json
python3 scripts/build_readme.py # data/* -> README.md
```

`README.md` is generated. Edit `data/featured.md` instead; a README-only pull request will be
overwritten by the next sweep.
