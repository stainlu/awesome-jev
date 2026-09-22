# Featured

The hand-read layer. Every entry here was opened and its use of Jev confirmed in its own README
or source — not inferred from the word "jev" appearing somewhere.

Format: `- owner/repo — why this is worth your afternoon`

Write the note as a reason to click, not a description. The full index already says what each
project is.

## Official

- typesafe-ai/typesafe-sdk-python — The Python client. Start here if you want to feel the three primitives before reading anything else.
- typesafe-ai/typesafe-sdk-js — The TypeScript and JavaScript client.
- typesafe-ai/skills — The official agent skill, installable into Claude Code as a plugin. The fastest way to let an agent you already run start making typed decisions.
- typesafe-ai/system-one-adapter-python — A drop-in replacement for the SDK's evaluation API backed by an ordinary LLM. The honest way to find out whether Jev is actually better for your task, instead of assuming.

## Frameworks that already speak Jev

- pydantic/pydantic-ai — Each field of your `output_type` becomes one Jev question, so a decision agent runs on Jev exactly like on an LLM, and switching back is a one-word model change. The cleanest way to A/B a typed decision against a language model.
- BerriAI/litellm — A guardrail that asks Jev one yes/no question per finished tool exchange — "is this result still needed?" — and blanks the ones it says no to. Context compaction with no summariser in the loop.
- BoundaryML/baml — Jev as a first-class client in BAML's standard library: bools and floats become Noul, enums and unions become Choice, and classes flatten to one question per leaf. The best worked example of mapping a type system onto Jev's three primitives.
- Effect-TS/effect — `@effect/ai-typesafe` makes Jev a decision provider inside Effect's AI modules, so judgments compose with the same error channel and retry policy as everything else in an Effect program.
- 0xPlaygrounds/rig — `rig-typesafeai` brings typed judgments to Rust, which is otherwise the least served language in this ecosystem.
- ax-llm/ax — DSPy for TypeScript, with Jev wired into both decisions and native scoring. Worth reading if you want optimised prompts and calibrated judgments in one pipeline.

## Seeing what it does in production

- comet-ml/opik — Traces System One calls like any other model call, so a Jev decision shows up in the same timeline as the LLM turns around it.
- Arize-ai/openinference — OpenTelemetry instrumentation for the TypeSafe SDK in both Python and JavaScript. Choice, Score and Noul each become spans you can alert on.

## Context compaction

The densest cluster in the ecosystem, because it is the problem Jev happens to fit exactly:
deciding what to throw away is a judgment, and writing the summary is what costs you.

- tamaratran/fast-jev-compaction — Replaces Claude Code's compaction summary with Jev decisions about which tool calls and results are still needed. A real answer to context-window pressure rather than a demo.
- caliber-ai-org/ai-setup — Jev scores each tool call and result, stale ones drop, and everything kept stays byte-for-byte verbatim. The before-and-after diagram makes the case against summarisation better than any argument.
- tamaratran/jev-pruner — Prunes noisy Bash output *after* the command runs but *before* the agent reads it, which is the cheapest place in the loop to intervene.
- kunchenguid/compact-adviser — Asks a different question from everyone else: not what to drop, but whether this is even a safe moment to compact. Two one-sentence questions in a single request.

## Routing

- gargpratyush/jev-router — Per-turn model routing for Claude Code and Codex: Jev sends simple work to the cheap model and keeps the expensive one for the rest.
- 0xNatoshi/jev-codex-router — Picks the model *and* the thinking effort together for each call, which is the pair most routers get wrong by deciding separately.
- BillionsBobby/JevRouter — Treats models, subagents, skills, MCP tools and CLIs as one candidate set and answers "which capability handles this next?" as a single Choice question.

## Guardrails

- AgentiLoop/Agent — Every shell command that already passed the hard-coded safety rules gets sent to Jev, which rates how likely it is to destroy data irreversibly. A second opinion exactly where an agent is most dangerous.
- DevMortimer/pi-warden — Jev judges every write against rules no linter can check — "a TODO must name a ticket", "comments must not restate the code" — and quotes the violation back.

## Browser and computer use

- browser-use/jev-ultrafast — Jev picks the operation and the element; a small LLM writes text only when the action is `TYPE_TEXT`. The clearest demonstration of the split Jev exists for: decide with Jev, generate with an LLM.
- jkudish/jev-browser — Give it a task and a URL. The plainest possible browser agent, which makes it the easiest one to read end to end.
- moritzkremb/jev-voice-browser — A dozen typed questions in one request, and Jev only ever *picks* a candidate span that code extracted — the URL you land on is copied verbatim, never generated. A good pattern for anywhere hallucination would be unacceptable.
- kitze/unclutter — A browser extension that asks Jev which page elements are nonessential, then remembers the answer as a reusable rule. Classification where you can see the result instantly.

## Search and ranking

- xerj-org/xerj — Reranking inside an actual search engine: add `"rerank": {}` to a query and Jev scores each document against the question.
- uehaj/jev-semgrep — Grep by meaning. Every line becomes a typed question, which is either the most obvious use of Jev or the most wasteful, and the write-up argues the case.
- lakeday-org/perch — Semantic code linting: rules stated in English, judged per file, for the things a real linter structurally cannot see.
- ielab/llm-rankers — Jev as a pointwise, pairwise, setwise and listwise reranker, from an IR research group. The closest thing to a controlled evaluation anyone has published.

## Agent tooling

- itsmostafa/typesafe-mcp — An MCP server that gives Claude Code, Claude Desktop, Codex and pi a typed `evaluate` call. The lowest-effort way to put Jev in front of an agent you already use.

## Open reproductions and research

- bespokelabsai/nimble — Data, model and recipe for an open System One model. Scores one answer token per question, and curation flips a single fact to flip the answer. The only serious attempt to reproduce what Jev does.
- wfzyx/von — Implements the `/v1/systemone` protocol itself, so it drops in where Jev does, and publishes a ViZDoom benchmark against Jev on sub-20ms real-time control.

## Applications

- virattt/ai-hedge-fund — Jev sits alongside Anthropic, OpenAI and the rest as a provider for the investor agents, so you can run the same mandate on a decision model and on an LLM and compare.
- Armur-Ai/Pentest-Swarm-AI — The swarm scores candidate attack paths with Jev against live state and pursues the best first. Adaptive search where the scoring function is a judgment.
