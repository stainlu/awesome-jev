# Contributing

## Adding a project

You usually do not need to. `scripts/discover.py` runs daily and picks up any public repo that
carries a Jev signal:

- a topic — `jev`, `typesafe-ai`, `system-one`, `system-one-models`
- a description naming Jev, typesafe.ai, or "System One model"
- **code** containing `api.typesafe.ai/v1/systemone`, `@typesafe-ai/sdk`, or `TYPESAFE_API_KEY`

The code signals matter most: they are how an established project that added Jev support gets
found without renaming itself. If your project is missing, the fastest fix is to add one of the
topics. If it still does not appear after a day, open an issue and say which signal should have
caught it — that is a bug in the sweep, not a missing entry.

The README table lists projects that were committed to after the day they were published. The
complete index, dormant projects included, is `data/projects.json`.

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
