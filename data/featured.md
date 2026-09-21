# Featured

The hand-read layer. Every entry here was opened, its README and file tree read, and its actual
use of Jev confirmed — not inferred from the word "jev" appearing somewhere.

Format: `- owner/repo — why this is worth your afternoon`

Write the note as a reason to click, not a description. The full index already says what each
project is.

## Frameworks that already speak Jev

- pydantic/pydantic-ai — Each field of your `output_type` becomes one Jev question, so a decision agent runs on Jev exactly like on an LLM, and switching back is a one-word model change. The cleanest way to A/B a typed decision against a language model.
- BerriAI/litellm — A guardrail that asks Jev one yes/no question per finished tool exchange — "is this result still needed?" — and blanks the ones it says no to. Context compaction with no summariser in the loop.
- BoundaryML/baml — Jev as a first-class client in BAML's standard library: bools and floats become Noul, enums and unions become Choice, and classes flatten to one question per leaf. The best worked example of mapping a type system onto Jev's three primitives.

## Browser and computer use

- browser-use/jev-ultrafast — Jev picks the operation and the element; a small LLM writes text only when the action is `TYPE_TEXT`. The clearest demonstration of the split Jev exists for: decide with Jev, generate with an LLM.

## Coding agents

- tamaratran/fast-jev-compaction — Replaces Claude Code's compaction summary with Jev decisions about which tool calls and results are still needed. A real answer to context-window pressure rather than a demo.
