# Excluded

False positives the sweep keeps finding. One line each, with the reason — so the next person
(or the next sweep) does not re-add them.

Format: `- owner/repo — reason`

`JEV` is also the abbreviation for Japanese encephalitis virus, and a surname. `typesafe` is an
ordinary word in typed languages, and GitHub tokenises on punctuation, so `typesafe.ai` also
matches "typesafe Commerce SDK". Repos created before 2026-09-15 that match only on a weak signal
are dropped automatically; list anything that gets through here.

Each entry below was checked: no reference to Jev in its README, and no file in its tree whose
path mentions jev or typesafe.

- yournextstore/yournextstore — "typesafe Commerce SDK"; unrelated to TypeSafe AI.
- tinystruct/tinystruct — Java framework; `typesafe` in the ordinary sense.
- lucasjinreal/Crane — Rust inference engine; no Jev code.
- Asymptote-Labs/agent-beacon — carries `topic:jev` but has no Jev code or mention.
- killop/anything_about_game — game development resource list; has one Jev page, is not a project built on Jev.
