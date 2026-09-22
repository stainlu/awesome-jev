# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Every public project built on [Jev](https://typesafe.ai), TypeSafe AI's System One model — with the ones worth your afternoon marked.

Jev is not a chat model. You give it program state and a *typed question*; it returns a typed
answer with a calibrated probability, in about 100ms. Three question types: **Choice** (pick one
of N), **Score** (rate on an ordered scale), **Noul** (probability a statement is true). It is a
decision layer for software — routing, classification, moderation, guardrails, scoring — not a
text generator.

The ecosystem went from nothing to thousands of repos in a week, so this list does two jobs.
**Featured** is short and hand-read: every entry was opened and its use of Jev confirmed in the
source, not guessed from its description. **All projects** is the full sweep, run daily.

Not affiliated with TypeSafe AI.

## Contents

- [Frameworks that already speak Jev](#frameworks-that-already-speak-jev)
- [Browser and computer use](#browser-and-computer-use)
- [Coding agents](#coding-agents)
- [All projects](#all-projects)

## Frameworks that already speak Jev

- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) - Each field of your `output_type` becomes one Jev question, so a decision agent runs on Jev exactly like on an LLM, and switching back is a one-word model change. The cleanest way to A/B a typed decision against a language model.
- [BerriAI/litellm](https://github.com/BerriAI/litellm) - A guardrail that asks Jev one yes/no question per finished tool exchange — "is this result still needed?" — and blanks the ones it says no to. Context compaction with no summariser in the loop.
- [BoundaryML/baml](https://github.com/BoundaryML/baml) - Jev as a first-class client in BAML's standard library: bools and floats become Noul, enums and unions become Choice, and classes flatten to one question per leaf. The best worked example of mapping a type system onto Jev's three primitives.

## Browser and computer use

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Jev picks the operation and the element; a small LLM writes text only when the action is `TYPE_TEXT`. The clearest demonstration of the split Jev exists for: decide with Jev, generate with an LLM.

## Coding agents

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Replaces Claude Code's compaction summary with Jev decisions about which tool calls and results are still needed. A real answer to context-window pressure rather than a demo.

## All projects

**2,670 more active projects**, out of 6,587 indexed.

Swept daily, and listed here if anyone committed to it after the day it was published.
That one filter separates a project from a launch-week drop, and it removes 3,917 of the
6,587 repos in the index.

The complete index — all 6,587, dormant ones included, with the search signals that found each
— is [`data/projects.json`](data/projects.json). It is generated, so grep it rather than read it.

| Project | What it is | ★ | Language | Last commit |
| --- | --- | ---: | --- | --- |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 | 390,231 | TypeScript | 2026-09-22 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you | 247,881 | Python | 2026-09-22 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the to… | 187,482 | Python | 2026-09-22 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | The agent engineering platform. | 146,842 | Python | 2026-09-22 |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastruc… | 87,191 | TypeScript | 2026-09-22 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team | 63,659 | Python | 2026-09-18 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack… | 46,745 | Python | 2026-09-22 |
| [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私… | 46,455 | TypeScript | 2026-09-22 |
| [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 | 42,345 | Go | 2026-09-22 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | OpenHuman is an open source agent harness with local-first memory, agent orchestration, and workflows | 40,024 | Rust | 2026-09-22 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Teams-first Multi-agent orchestration for Claude Code | 39,297 | TypeScript | 2026-09-22 |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more. Makers of the AG-UI P… | 37,461 | TypeScript | 2026-09-22 |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | ⌥ Coding agent with the IDE wired in | 32,433 | TypeScript | 2026-09-22 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | CLI tool for configuring and monitoring Claude Code | 30,898 | Python | 2026-09-22 |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to… | 30,279 | TypeScript | 2026-09-22 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 🚀 The fast, Pythonic way to build MCP servers and clients. | 27,855 | Python | 2026-09-22 |
| [trycua/cua](https://github.com/trycua/cua) | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for training, evaluation, an… | 25,833 | HTML | 2026-09-22 |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Hindsight: Agent Memory That Learns | 24,873 | Python | 2026-09-21 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tra… | 22,188 | Python | 2026-09-22 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | The most RAM efficient harness | 19,996 | Rust | 2026-09-22 |
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | Open source agentic operating system | 19,406 | TypeScript | 2026-09-22 |
| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | The agent engineering platform | 18,214 | TypeScript | 2026-09-22 |
| [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。\| AI-era Berkshire: a value inv… | 16,480 | HTML | 2026-09-21 |
| [Effect-TS/effect](https://github.com/Effect-TS/effect) | Build production-ready applications in TypeScript | 16,167 | TypeScript | 2026-09-22 |
| [theonedev/onedev](https://github.com/theonedev/onedev) | The Unified and Autonomous Development Platform | 15,258 | Java | 2026-09-21 |
| [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | Udemy & Hotmart course downloader, YouTube downloader (yt-dlp GUI, 1,800+ sites) + desktop app for AI agents:… | 14,139 | Rust | 2026-09-21 |
| [elie222/inbox-zero](https://github.com/elie222/inbox-zero) | The world's best AI personal assistant for email. Open source app to help you reach inbox zero fast. | 12,278 | TypeScript | 2026-09-22 |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build … | 11,968 | Python | 2026-09-21 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | AI Observability & Evaluation | 11,567 | Python | 2026-09-22 |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | ⚙️🦀 Build modular and scalable LLM Applications in Rust | 8,693 | Rust | 2026-09-22 |
| [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | git push no-mistakes | 8,598 | Go | 2026-09-22 |
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails… | 8,230 | Go | 2026-09-22 |
| [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | Talk to one agent. Ship with a crew. | 6,946 | Shell | 2026-09-22 |
| [tbphp/gpt-load](https://github.com/tbphp/gpt-load) | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, sched… | 6,946 | Go | 2026-09-22 |
| [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) | The open-source observability database. One columnar engine for metrics, logs, and traces, on object storage. | 6,698 | Rust | 2026-09-22 |
| [op7418/CodePilot](https://github.com/op7418/CodePilot) | A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your … | 6,472 | TypeScript | 2026-09-22 |
| [ThinkInAIXYZ/deepchat](https://github.com/ThinkInAIXYZ/deepchat) | 🐬DeepChat - A smart assistant that connects powerful AI to your personal world | 6,338 | TypeScript | 2026-09-22 |
| [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | A framework for building agentic apps | 6,137 | TypeScript | 2026-09-22 |
| [samchon/typia](https://github.com/samchon/typia) | Super-fast/easy runtime validators and serializers via transformation | 5,913 | TypeScript | 2026-09-22 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | Open-source auth gateway connecting 1500+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAP… | 5,865 | TypeScript | 2026-09-22 |
| [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | Experiential is the open source, zero markup gateway for BYOK, self-hosted and 1000+ marketplace models. It l… | 5,421 | Python | 2026-09-22 |
| [Kiln-AI/Kiln](https://github.com/Kiln-AI/Kiln) | Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation… | 5,078 | Python | 2026-09-22 |
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | Next Generation Agentic Proxy for AI Agents and MCP servers | 4,971 | Rust | 2026-09-21 |
| [aipoch/open-science](https://github.com/aipoch/open-science) | The open-source AI research workbench for scientific research and agent workflows. Local-first, model-agnosti… | 4,897 | TypeScript | 2026-09-22 |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | The platform for LLM evaluations and AI agent testing | 4,854 | TypeScript | 2026-09-22 |
| [daveebbelaar/ai-cookbook](https://github.com/daveebbelaar/ai-cookbook) | Examples and tutorials to help developers build AI systems | 4,559 | Python | 2026-09-21 |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, Py… | 4,405 | Python | 2026-09-22 |
| [crmne/ruby_llm](https://github.com/crmne/ruby_llm) | The Ruby-native AI framework. Chats, agents, tools, images, audio, and video through one consistent API, in p… | 4,396 | Ruby | 2026-09-21 |
| [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | A persistent workspace for development work that self-improves and continues beyond one session. | 4,079 | Python | 2026-09-22 |
| [Ontos-AI/knowhere](https://github.com/Ontos-AI/knowhere) | Knowhere extracts, parses, and outputs structured chunks ready for AI Agents and RAG. | 3,434 | Python | 2026-09-22 |
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. | 3,420 | Python | 2026-09-21 |
| [TanStack/ai](https://github.com/TanStack/ai) | 🤖 Type-safe, provider-agnostic TypeScript AI SDK for streaming chat, tool calling, agents, and multimodal app… | 3,129 | TypeScript | 2026-09-21 |
| [ax-llm/ax](https://github.com/ax-llm/ax) | The pretty much "official" DSPy framework for Typescript | 2,943 | TypeScript | 2026-09-18 |
| [elie222/rakazo](https://github.com/elie222/rakazo) | Open-source Grok Bot alternative. Choose your own model and sandbox. | 2,829 | TypeScript | 2026-09-22 |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own | 2,752 | Python | 2026-09-22 |
| [Armur-Ai/Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) | Autonomous penetration testing using a swarm of AI agents. Orchestrates recon, classification, exploitation, … | 2,558 | Go | 2026-09-22 |
| [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | VCP 部署在 AI 模型 API 与前端应用之间，是面向AGI OS开发和探索的工业级基建示范项目。通过统一指令协议、多层级持久化记忆、分布式插件引擎及多 Agent 协作框架，将原本“无状态、无记忆、无工具调用能力… | 2,323 | JavaScript | 2026-09-22 |
| [xerj-org/xerj](https://github.com/xerj-org/xerj) | XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data withou… | 2,277 | Rust | 2026-09-22 |
| [coder/xum](https://github.com/coder/xum) | A desktop app for isolated, parallel agentic development | 2,034 | TypeScript | 2026-09-22 |
| [SimonSchubert/LinuxCommandLibrary](https://github.com/SimonSchubert/LinuxCommandLibrary) | 2M+ app downloads, 500k+ monthly website visitors, Linux basics, tips and formatted man pages | 2,020 | Kotlin | 2026-09-21 |
| [oficcejo/aiagents-stock](https://github.com/oficcejo/aiagents-stock) | 复合多AI智能体股票团队分析盯盘系统，基于多个ai智能体，模拟证券分析师团队分析过程，提供全方位的股票投资分析和决策建议，新增游资龙虎榜跟踪分析、板块预警轮动分析，支持批量多线程分析，支持实时监测关键点位，发送警报信息… | 1,942 | Python | 2026-09-21 |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 装在手机上的对话副驾：在微信 / QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 | 1,925 | Kotlin | 2026-09-22 |
| [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | One AI trade decision every Monad block. Jev on Kuru MON-USDC. | 1,910 | TypeScript | 2026-09-17 |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline. | 1,885 | Python | 2026-09-21 |
| [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) | Local typed decisions, contrastive data curation, and model evaluation. | 1,536 | Python | 2026-09-20 |
| [nicobailon/pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter) | Token-efficient MCP adapter for Pi coding agent | 1,522 | TypeScript | 2026-09-22 |
| [astaxie/TokenHub](https://github.com/astaxie/TokenHub) | TokenHub gives enterprises a private gateway to unify AI model access and governance, making every request co… | 1,324 | Go | 2026-09-22 |
| [elvisun/newsjack](https://github.com/elvisun/newsjack) | The open-source skills that turn your agent into a full PR team. | 1,297 | Go | 2026-09-19 |
| [caliber-ai-org/ai-setup](https://github.com/caliber-ai-org/ai-setup) | Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files… | 1,278 | TypeScript | 2026-09-19 |
| [heymrun/heym](https://github.com/heymrun/heym) | Build agentic systems. Run them with confidence. Orchestrate agents, automate business processes, inspect eve… | 1,245 | Python | 2026-09-21 |
| [Arize-ai/openinference](https://github.com/Arize-ai/openinference) | OpenTelemetry Instrumentation for AI Observability | 1,228 | Python | 2026-09-22 |
| [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠 | 1,106 | JavaScript | 2026-09-21 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One mode… | 1,092 | Python | 2026-09-21 |
| [wk42worldworld/cybercode](https://github.com/wk42worldworld/cybercode) | 整合 Claude Code 编程能力与 Hermes Agent 自进化能力的智能体 / An AI agent combining Claude Code coding capabilities with Herm… | 1,030 | TypeScript | 2026-09-21 |
| [CelestoAI/celesto](https://github.com/CelestoAI/celesto) | Secure and persistent computer for AI agents -- build your own Grokbot, and Muse. | 959 | Python | 2026-09-21 |
| [konbakuyomu/smartsearch](https://github.com/konbakuyomu/smartsearch) | — | 838 | Python | 2026-09-22 |
| [bastani-inc/atomic](https://github.com/bastani-inc/atomic) | The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, chec… | 813 | TypeScript | 2026-09-22 |
| [reticlehq/reticle](https://github.com/reticlehq/reticle) | AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machi… | 810 | TypeScript | 2026-09-22 |
| [lioensky/VCPChat](https://github.com/lioensky/VCPChat) | VCPChat，VCP原生分布式引擎终端项目，地球上第一个AGI-OS桌面级交互系统，语义级垂直打穿AI-UI/UX-APP以及人类想象力的一切。 | 778 | JavaScript | 2026-09-21 |
| [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) | Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast… | 776 | Python | 2026-09-20 |
| [chujianyun/skills](https://github.com/chujianyun/skills) | WuMing's Claude Skills | 737 | JavaScript | 2026-09-20 |
| [samuelfaj/distill](https://github.com/samuelfaj/distill) | Get FAR MORE done with FAR FEWER tokens 🔥 | 683 | Rust | 2026-09-22 |
| [automateyournetwork/netclaw](https://github.com/automateyournetwork/netclaw) | An AI agent that claws through your network | 664 | Python | 2026-09-20 |
| [milind-soni/tiptour-macos](https://github.com/milind-soni/tiptour-macos) | Open-Source fast local computer use | 644 | Swift | 2026-09-19 |
| [duanebester/gooey](https://github.com/duanebester/gooey) | Gooey is a hybrid immediate/retained mode UI framework designed for building fast, GPU-rendered applications … | 631 | Zig | 2026-09-20 |
| [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent) | AgentiLoop Agent! An Autonomous Agentic Agent for Mac, and exclusive Apple only harnesss. Supports automation… | 624 | Swift | 2026-09-22 |
| [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | The CLI for AI agents to control Chrome. Zero config, agent-agnostic, battle-tested. | 622 | TypeScript | 2026-09-21 |
| [narumiruna/pi-extensions](https://github.com/narumiruna/pi-extensions) | A monorepo of Pi Coding Agent extensions | 599 | TypeScript | 2026-09-22 |
| [nicobailon/pi-interactive-shell](https://github.com/nicobailon/pi-interactive-shell) | Pi coding agent extension that allows Pi to autonomously control interactive CLIs in an observable overlay. F… | 587 | TypeScript | 2026-09-22 |
| [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) | Follow your curiosity. Build across disciplines. Open-source software and hardware for polymaths in the makin… | 562 | C | 2026-09-22 |
| [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) | — | 556 | JavaScript | 2026-09-22 |
| [BennyKok/omg.dev](https://github.com/BennyKok/omg.dev) | omg.dev — Remote control for claude, codex, cursor, opencode, pi, grok, jcocde with mobile client | 535 | TypeScript | 2026-09-22 |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | A staged code-review workflow and local dashboard built with TypeSafe Jev. | 509 | TypeScript | 2026-09-17 |
| [pulseaiclub/phi](https://github.com/pulseaiclub/phi) | a coding agent, rpc plugin, sub-agents, hashline edits, and mcp | 493 | Go | 2026-09-22 |
| [thruwire/foreman](https://github.com/thruwire/foreman) | Software factory foreman based on TypeSafe's Jev model | 479 | Python | 2026-09-20 |
| [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) | Turn any open model into a classifier/jev endpoint | 462 | Python | 2026-09-21 |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | Monorepo & docs | 449 | Rust | 2026-09-22 |
| [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) | Awesome Jev: a source-backed field guide to TypeSafe's System One model, with SDKs, live demos, agent tools, … | 432 | HTML | 2026-09-22 |
| [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j) | Java 8+ agentic SDK: unified LLM access (OpenAI/Anthropic/DashScope/Doubao/DeepSeek...), Tool Calling, MCP, R… | 429 | HTML | 2026-09-22 |
| [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) | VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agen… | 423 | Python | 2026-09-22 |
| [langchain-ai/docs](https://github.com/langchain-ai/docs) | Unified LangChain documentation. | 418 | MDX | 2026-09-22 |
| [bitsocialnet/seedit](https://github.com/bitsocialnet/seedit) | A Bitsocial app with an old.reddit UI | 416 | TypeScript | 2026-09-21 |
| [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (a… | 408 | Python | 2026-09-22 |
| [mrmps/classifier-dev](https://github.com/mrmps/classifier-dev) | Zero-shot text classification over plain HTTP — no API key, no account. One Cloudflare Worker, a CLI, and an … | 408 | TypeScript | 2026-09-21 |
| [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) | An awesome collection of Jev use cases, workflows, and agent skills. | 394 | Python | 2026-09-22 |
| [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) | Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with S… | 390 | TypeScript | 2026-09-20 |
| [wfzyx/von](https://github.com/wfzyx/von) | The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSaf… | 388 | Python | 2026-09-21 |
| [ImChong/Robotics_Notebooks](https://github.com/ImChong/Robotics_Notebooks) | 机器人技术栈资料汇总 | 373 | Python | 2026-09-22 |
| [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) | — | 362 | TypeScript | 2026-09-21 |
| [mohsen1/llm-debugger-vscode-extension](https://github.com/mohsen1/llm-debugger-vscode-extension) | VSCode extension that demonstrates the use of large language models (LLMs) for active debugging of programs | 359 | TypeScript | 2026-09-21 |
| [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) | Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per p… | 358 | TypeScript | 2026-09-20 |
| [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) | 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp. | 340 | JavaScript | 2026-09-19 |
| [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) | Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHu… | 339 | JavaScript | 2026-09-22 |
| [EthanAlgoX/AIStock](https://github.com/EthanAlgoX/AIStock) | A multi-agent AI trading system using LLMs to optimize strategies and adapt to market conditions in real-time. | 331 | Python | 2026-09-21 |
| [rwjdk/agent-framework-samples](https://github.com/rwjdk/agent-framework-samples) | Samples demonstrating the Microsoft Agent Framework in C# | 329 | C# | 2026-09-19 |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | Route to the cheapest model in claude code for your task using jev-router | 319 | JavaScript | 2026-09-19 |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) | A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions. | 318 | — | 2026-09-22 |
| [warmbly/warmbly](https://github.com/warmbly/warmbly) | The largest open-source B2B cold outreach and email warmup service. | 308 | Go | 2026-09-21 |
| [qiz029/dscode](https://github.com/qiz029/dscode) | A DeepSeek coding agent harness: persistent shell, Ultra subagents, auto approval, Chrome MCP and session tel… | 298 | JavaScript | 2026-09-22 |
| [realZachi/pg-jev](https://github.com/realZachi/pg-jev) | Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev. | 291 | Shell | 2026-09-18 |
| [razorback16/openjev](https://github.com/razorback16/openjev) | Open, Jev-compatible System One decision server on DiffusionGemma | 288 | Python | 2026-09-21 |
| [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) | The Complete AI Development Toolkit for Claude Code. 106 skills, 36 agents, 171 hooks. Install `ork` for stab… | 281 | TypeScript | 2026-09-22 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources. | 271 | — | 2026-09-22 |
| [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) | Build calibrated AI Functions from human feedback using Jev and GEPA. | 271 | Python | 2026-09-20 |
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | Jev-compatible API endpoint based on open models (prefill-only) | 259 | Python | 2026-09-21 |
| [Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) | Calibrated 151M Non-Autoregressive Decision Engine beating TypeSafe Jev & Laya on LocalLLaMA/typed-decisions … | 252 | Python | 2026-09-20 |
| [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) | Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools. | 252 | JavaScript | 2026-09-21 |
| [stella/stella](https://github.com/stella/stella) | Open-source legal workspace | 250 | TypeScript | 2026-09-22 |
| [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | Drop-in TypeSafeClient replacement backed by LLM APIs | 249 | Python | 2026-09-18 |
| [cequence-io/openai-scala-client](https://github.com/cequence-io/openai-scala-client) | Scala client for OpenAI API and other major LLM providers | 248 | Scala | 2026-09-18 |
| [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) | A verified, community-maintained catalog of 640 open-source projects built with Jev. | 241 | Astro | 2026-09-22 |
| [DemonDamon/AgenticX](https://github.com/DemonDamon/AgenticX) | AgenticX is a unified, production-ready multi-agent platform — Python SDK + CLI (agx) + Studio server + Machi… | 233 | Python | 2026-09-22 |
| [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) | mcp connector to give your AI agent direct access to typesafe ai's jev model | 233 | Go | 2026-09-21 |
| [jkudish/jev-browser](https://github.com/jkudish/jev-browser) | Browser use using Typesafe's Jev model | 233 | TypeScript | 2026-09-22 |
| [morganlinton/Albatross](https://github.com/morganlinton/Albatross) | Open source, terminal-first AI coding agent with fully transparent multi-model routing. Local (Ollama, LM Stu… | 230 | Rust | 2026-09-21 |
| [hr98w/jev-visual](https://github.com/hr98w/jev-visual) | An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scorin… | 228 | Python | 2026-09-21 |
| [rokbenko/quackd](https://github.com/rokbenko/quackd) | One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a b… | 228 | Python | 2026-09-22 |
| [kitze/skillbox](https://github.com/kitze/skillbox) | Self-hosted, versioned skills library for AI agents. MCP, scoped clients, and optional Jev recommendations. | 224 | TypeScript | 2026-09-19 |
| [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word… | 222 | JavaScript | 2026-09-21 |
| [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | The official TypeScript/JavaScript library for the TypeSafe API | 218 | TypeScript | 2026-09-15 |
| [damianvtran/local-operator](https://github.com/damianvtran/local-operator) | An open-source AI agent hub for your own machine: build organizations of collaborating agents that message ea… | 214 | Python | 2026-09-22 |
| [jmagly/aiwg](https://github.com/jmagly/aiwg) | Cognitive architecture for AI-augmented software development. Specialized agents, structured workflows, and m… | 211 | TypeScript | 2026-09-21 |
| [socai-io/socai](https://github.com/socai-io/socai) | A Browser Use Agent that actually reads social media. Fast. Precise. Deep. | 209 | Rust | 2026-09-21 |
| [receptron/laya](https://github.com/receptron/laya) | Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime | 208 | TypeScript | 2026-09-21 |
| [chunxiaoxx/nautilus-compass](https://github.com/chunxiaoxx/nautilus-compass) | Reliability layer for multi-agent setups — keep agents coordinating without an orchestrator. Cross-dialog con… | 207 | Python | 2026-09-22 |
| [jerryjliu/docjev](https://github.com/jerryjliu/docjev) | A very fast document classifier/splitter using Jev | 207 | Python | 2026-09-21 |
| [logan-markewich/jeff](https://github.com/logan-markewich/jeff) | A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer. | 207 | Python | 2026-09-20 |
| [liuyanghejerry/Clausura](https://github.com/liuyanghejerry/Clausura) | CI-native agent CLI tool for deterministic pipeline gating. | 203 | Rust | 2026-09-20 |
| [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking … | 187 | JavaScript | 2026-09-22 |
| [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) | A source-backed Jev project directory with a reusable Jev-only GitHub review workflow. | 187 | JavaScript | 2026-09-20 |
| [Knuckles92/OpenWhisper](https://github.com/Knuckles92/OpenWhisper) | Local speech-to-text, dictation, and meetings with Whisper and OpenAI API. Optional Windows x64 engines: Para… | 187 | Python | 2026-09-20 |
| [marvikomo/code-lens-ai](https://github.com/marvikomo/code-lens-ai) | — | 182 | TypeScript | 2026-09-20 |
| [kitze/unclutter](https://github.com/kitze/unclutter) | WXT browser extension: Jev-powered page clutter removal with reusable template rules. | 180 | TypeScript | 2026-09-18 |
| [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy) | openworkbuddy — local-first AI office agent: turn requests into real files. Self-hosted, BYOK, MCP, Codex/Cla… | 175 | JavaScript | 2026-09-22 |
| [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser) | "Work appears completed or recorded. Run /compact to save tokens." | 174 | TypeScript | 2026-09-22 |
| [lakeday-org/perch](https://github.com/lakeday-org/perch) | Semantic code linting with Jev | 168 | JavaScript | 2026-09-22 |
| [FBddcz/embodied-jev](https://github.com/FBddcz/embodied-jev) | EmbodiedJev: MuJoCo robot decision workbench with MiniCPM5-2B, Jev and compatible model APIs | 166 | Python | 2026-09-22 |
| [dealerdefi/Jevmind](https://github.com/dealerdefi/Jevmind) | — | 164 | Python | 2026-09-21 |
| [anton-abyzov/specweave](https://github.com/anton-abyzov/specweave) | Spec-first AI development: describe a feature → AI creates spec + plan + tasks, builds autonomously, syncs to… | 163 | TypeScript | 2026-09-22 |
| [glowbom/glowbom-oss](https://github.com/glowbom/glowbom-oss) | Build software like writing a book | 163 | Go | 2026-09-20 |
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | 🔥🔥 Papers, open reproductions and independent evaluations behind System One models and Jev. | 163 | JavaScript | 2026-09-22 |
| [NiceEval/NiceEval](https://github.com/NiceEval/NiceEval) | build eval for your agent in 10 mins | 153 | TypeScript | 2026-09-22 |
| [brainstormity/Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) | — | 151 | Python | 2026-09-22 |
| [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) | A lightweight Jev-powered router for models, tools, and subagents | 149 | TypeScript | 2026-09-21 |
| [AgentEvalHQ/AgentEval](https://github.com/AgentEvalHQ/AgentEval) | AgentEval is the comprehensive .NET toolkit for AI agent evaluation—tool usage validation, RAG quality metric… | 146 | C# | 2026-09-21 |
| [Nine-Minds/alga-psa](https://github.com/Nine-Minds/alga-psa) | An open source MSP PSA from Nine Minds | 141 | TypeScript | 2026-09-22 |
| [PatrickSUDO/fadacai-portfolio](https://github.com/PatrickSUDO/fadacai-portfolio) | Claude Code 投資研究與組合管理框架：skills + MCP + 第一性原理紀律 + thesis ledger | 140 | Python | 2026-09-21 |
| [juspay/neurolink](https://github.com/juspay/neurolink) | One TypeScript interface for 40 AI providers across three inference types — generate, stream, and decide. Dec… | 137 | TypeScript | 2026-09-22 |
| [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) | Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it | 137 | TypeScript | 2026-09-22 |
| [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) | TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, c… | 135 | TypeScript | 2026-09-22 |
| [bitsocialnet/5chan](https://github.com/bitsocialnet/5chan) | A peer-to-peer 4chan alternative. | 132 | TypeScript | 2026-09-21 |
| [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) | Guardrails for Pi that steer instead of interrupt: enforces your project rules on every write, holds only har… | 132 | TypeScript | 2026-09-22 |
| [FerryCorleone/crush-monitor](https://github.com/FerryCorleone/crush-monitor) | Crush 好感监控器：用 Jev 分析微信聊天的情绪、意图和回复表现。本机部署，使用自己的 API Key。 | 131 | TypeScript | 2026-09-22 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | A community directory of projects built on Jev, TypeSafe AI's System One model. | 131 | JavaScript | 2026-09-21 |
| [hyprstream/hyprstream](https://github.com/hyprstream/hyprstream) | HyprStream: agentic infrastructure for continous online-learning applications | 127 | Rust | 2026-09-22 |
| [catlog22/pi-maestro-flow](https://github.com/catlog22/pi-maestro-flow) | Maestro workflow tools as Pi extensions — pi-teammate + pi-maestro-agent | 126 | TypeScript | 2026-09-22 |
| [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outp… | 126 | Python | 2026-09-21 |
| [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) | grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AN… | 125 | JavaScript | 2026-09-21 |
| [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) | Typed decisions with TypeSafe's Jev, the first System One model | 125 | JavaScript | 2026-09-21 |
| [Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | — | 124 | Python | 2026-09-21 |
| [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz | 121 | Python | 2026-09-21 |
| [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway) | An easy way to use jev with your coding agent for tool calling reasoning | 119 | TypeScript | 2026-09-21 |
| [devagrawal09/stanley-code](https://github.com/devagrawal09/stanley-code) | Bounded TypeSafe Jev workflows for coding agents. | 111 | TypeScript | 2026-09-19 |
| [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) | A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creat… | 111 | Python | 2026-09-21 |
| [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) | Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context… | 110 | Rust | 2026-09-22 |
| [miptgirl/miptgirl_medium](https://github.com/miptgirl/miptgirl_medium) | Code for Medium blog posts | 109 | Jupyter Notebook | 2026-09-18 |
| [cookiespiggy/agentic-rl](https://github.com/cookiespiggy/agentic-rl) | Agentic RL 中文零基础教程（25 章）：从概念到 GRPO 实战，含 TRL 最小可跑示例。第 25 章讲清 Jev / TypeSafe System One 判别模型与 RL 的能力边界 \| Chine… | 107 | Python | 2026-09-21 |
| [dom-actions/doma](https://github.com/dom-actions/doma) | The open-source of DomA, an AI automation agent for the browser. | 104 | TypeScript | 2026-09-21 |
| [sonnylazuardi/superterminal](https://github.com/sonnylazuardi/superterminal) | a native multiplexer terminal for Windows, Linux and Mac | 100 | Rust | 2026-09-21 |
| [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) | Live Jev trader on Hyperliquid | 99 | TypeScript | 2026-09-21 |
| [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) | A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fas… | 99 | — | 2026-09-21 |
| [timrogers/formanator](https://github.com/timrogers/formanator) | Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) cl… | 99 | Rust | 2026-09-21 |
| [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) | The system one Harness for system one models | 95 | Python | 2026-09-21 |
| [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) | Code quality and coverage for coding agents | 95 | Rust | 2026-09-21 |
| [agent-labs-dev/fastbrowse](https://github.com/agent-labs-dev/fastbrowse) | A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim… | 94 | Python | 2026-09-22 |
| [daseinlabs/open-jev](https://github.com/daseinlabs/open-jev) | Open Jev implementation with custom finetuning | 94 | Python | 2026-09-19 |
| [tenuo-ai/tenuo](https://github.com/tenuo-ai/tenuo) | Task-scoped authorization for AI agents. Cryptographic warrants constrain tools and arguments, prevent privil… | 92 | Rust | 2026-09-22 |
| [thisisnsh/aithing](https://github.com/thisisnsh/aithing) | AI, Agents, and Automation | 92 | Swift | 2026-09-21 |
| [fabricioctelles/skills](https://github.com/fabricioctelles/skills) | A collection of skills for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusa… | 89 | Python | 2026-09-21 |
| [pithings/advocaat](https://github.com/pithings/advocaat) | A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev. | 89 | TypeScript | 2026-09-18 |
| [savka777/jev-use](https://github.com/savka777/jev-use) | Say it, and your Mac does it. A computer-use harness on Jev that reads the screen through Accessibility. Fast… | 86 | Swift | 2026-09-21 |
| [sdras/jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension) | — | 86 | JavaScript | 2026-09-20 |
| [MarcelMichau/fake-survey-generator](https://github.com/MarcelMichau/fake-survey-generator) | A slightly more-than-trivial full-stack application built with DDD & CQRS concepts | 85 | C# | 2026-09-22 |
| [merefield/discourse-chatbot](https://github.com/merefield/discourse-chatbot) | An AI bot with RAG capability for Topics, Chat & Customer Support in Discourse, currently powered by OpenAI | 84 | Ruby | 2026-09-21 |
| [jev-chat/jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) | 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动 | 83 | Python | 2026-09-22 |
| [walidboulanouar/awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) | Awesome list of TypeSafe AI Jev use cases: 74 demos ranked by likes, 150+ GitHub repos, limits, cost and API … | 83 | — | 2026-09-21 |
| [jexp/neo4jev](https://github.com/jexp/neo4jev) | Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationshi… | 82 | Jupyter Notebook | 2026-09-18 |
| [NanmiCoder/jev-arena](https://github.com/NanmiCoder/jev-arena) | Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、… | 82 | JavaScript | 2026-09-20 |
| [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) | Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification | 81 | C | 2026-09-20 |
| [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) | Detect youtube sponsor segment with live audio and transcript powered by Jev | 81 | JavaScript | 2026-09-18 |
| [monteduro/killmyidea](https://github.com/monteduro/killmyidea) | Describe your startup idea. Jev decides: kill it, fix it or ship it. | 78 | TypeScript | 2026-09-18 |
| [can1357/jegrep](https://github.com/can1357/jegrep) | Semantic grep: find code by describing what you're looking for, powered by Jev. | 76 | Rust | 2026-09-20 |
| [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel) | A WebMCP benchmark, measures WebMCP against other browser-agent interfaces. | 76 | HTML | 2026-09-18 |
| [openclaw/docs](https://github.com/openclaw/docs) | OpenClaw docs + translation | 75 | JavaScript | 2026-09-22 |
| [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) | Curated Jev resources and runnable examples for typed AI decisions. | 74 | Python | 2026-09-22 |
| [baldaworks/callee](https://github.com/baldaworks/callee) | Markdown-defined provider-backed agents and deterministic workflows for ACP runtimes. | 74 | Go | 2026-09-21 |
| [Bodila51/grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) | Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples | 74 | Python | 2026-09-20 |
| [tonone-ai/tonone](https://github.com/tonone-ai/tonone) | One session. Two commands. Full team. Zero meetings. | 73 | Python | 2026-09-20 |
| [yamanoku/awesome-japanese-a11y-companies](https://github.com/yamanoku/awesome-japanese-a11y-companies) | アクセシビリティに取り組む・推進している日本企業まとめ（随時更新） | 73 | TypeScript | 2026-09-19 |
| [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) | JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open. | 71 | Python | 2026-09-21 |
| [rojim666/SztuCode](https://github.com/rojim666/SztuCode) | A local-first AI coding agent with TUI and desktop clients, tool permissions, memory, Skills, Subagents, and … | 71 | Python | 2026-09-22 |
| [escapeboy/agent-fleet-o](https://github.com/escapeboy/agent-fleet-o) | Open-source AI agent orchestration platform — self-hosted mission control for autonomous multi-agent systems.… | 70 | PHP | 2026-09-21 |
| [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) | A decision cache for TypeSafe Jev-class models — memoize decisions so repeats are free, deterministic, and sh… | 70 | — | 2026-09-19 |
| [mizchi/jev-lint](https://github.com/mizchi/jev-lint) | lint text in code by jev scorerer | 70 | TypeScript | 2026-09-21 |
| [cayu-dev/cayu](https://github.com/cayu-dev/cayu) | Cayu is the runtime for long-horizon agents that need explicit environments, durable sessions, controlled too… | 69 | Python | 2026-09-22 |
| [Ratimon/openquok-monorepo](https://github.com/Ratimon/openquok-monorepo) | An agentic social media scheduling workspace engine/tool (CLI + Dashboard) | 69 | TypeScript | 2026-09-22 |
| [Heman10x-NGU/Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) | Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev b… | 68 | Python | 2026-09-20 |
| [SiliconLabAI/OpenJev](https://github.com/SiliconLabAI/OpenJev) | OpenSource Jev | 68 | TypeScript | 2026-09-22 |
| [kevinbadi/jev-voice](https://github.com/kevinbadi/jev-voice) | Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation. | 67 | Python | 2026-09-22 |
| [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) | Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server. | 67 | JavaScript | 2026-09-22 |
| [BrokkAi/mjolnir](https://github.com/BrokkAi/mjolnir) | Manage Codex, Claude Code, Muse Code, Kimi Code, Grok Build, and DeepSeek Harness with durable sessions, isol… | 63 | Rust | 2026-09-22 |
| [danielgshea/jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge) | Using Jev as an evaluator. | 63 | Python | 2026-09-19 |
| [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router) | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered b… | 63 | TypeScript | 2026-09-21 |
| [undefined-ui/second-brain-os](https://github.com/undefined-ui/second-brain-os) | An AI second brain that maintains itself. Full guide, starter vault, agent skills and scripts for a self-orga… | 63 | HTML | 2026-09-22 |
| [jev-chat/jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac) | 微信消息意图识别悬浮窗（macOS）：看屏 + 本地小模型判断意图和风险，再按话术生成回复候选。纯只读、不注入微信。 | 61 | Python | 2026-09-22 |
| [Parcha-ai/parcha-skills](https://github.com/Parcha-ai/parcha-skills) | Skills I use to execute long-running coding agents without breaking my back. | 60 | Python | 2026-09-22 |
| [Dun-sin/HearItFresh](https://github.com/Dun-sin/HearItFresh) | Get a personalized spotify playlist based on your current taste of music | 59 | TypeScript | 2026-09-20 |
| [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enter… | 58 | Python | 2026-09-19 |
| [temporal-community/temporal-agent-harness](https://github.com/temporal-community/temporal-agent-harness) | Temporal-native Durable Multi Agent Harness | 58 | Python | 2026-09-22 |
| [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) | Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。 | 58 | HTML | 2026-09-22 |
| [kyh/vibedgames](https://github.com/kyh/vibedgames) | A game studio for your agent 🎮 | 57 | TypeScript | 2026-09-21 |
| [wobsoriano/oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev) | — | 55 | TypeScript | 2026-09-21 |
| [bilune/jev-design](https://github.com/bilune/jev-design) | Can a model design a dashboard? A console whose whole design system is generated at runtime by Jev from a one… | 54 | TypeScript | 2026-09-21 |
| [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) | Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one … | 54 | Python | 2026-09-22 |
| [caudena/beam_weaver](https://github.com/caudena/beam_weaver) | Elixir-native LangChain, LangGraph, and DeepAgents for traceable LLM apps: OTP workflows, tools, memory, huma… | 54 | Elixir | 2026-09-21 |
| [rexleimo/aios](https://github.com/rexleimo/aios) | Local-first AI agent bootstrap: Playwright Browser MCP + ContextDB for Codex CLI, Claude Code, Gemini CLI, an… | 54 | JavaScript | 2026-09-22 |
| [TimeWarpEngineering/timewarp-architecture](https://github.com/TimeWarpEngineering/timewarp-architecture) | A distributed application template for dotnet. Utilizing Blazor, Web API, gRPC, Tye, YARP etc. | 54 | C# | 2026-09-21 |
| [iamaamir/pi-bifrost](https://github.com/iamaamir/pi-bifrost) | Automatically route each Pi prompt to a model based on task complexity, price, speed, or context length. Smar… | 53 | TypeScript | 2026-09-21 |
| [opencues/opencues](https://github.com/opencues/opencues) | The open standard for omnipresent AI. Claude Code, OpenCode, Gemini CLI, Shell, Chrome, DeepSeek Harness. Mod… | 53 | TypeScript | 2026-09-22 |
| [SuperagenticAI/superqode](https://github.com/SuperagenticAI/superqode) | The harness interoperability layer for coding agent. Agent to Agent connect over ACP, A2A and UHP | 53 | Python | 2026-09-22 |
| [xD3I/PZ_Optimization](https://github.com/xD3I/PZ_Optimization) | Project Zomboid Build 42 performance work: class overrides, harness, findings | 53 | Java | 2026-09-22 |
| [deepanwadhwa/OpenDecision](https://github.com/deepanwadhwa/OpenDecision) | OpenDecision is an open-source semantic decision engine like typesafe's jev. | 52 | Python | 2026-09-21 |
| [Dimweaker/jev-libero](https://github.com/Dimweaker/jev-libero) | Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks. | 52 | Python | 2026-09-21 |
| [openlayer-ai/jevals](https://github.com/openlayer-ai/jevals) | Agent evals and guardrails as Jev decisions: one request per trace, a fraction of a cent, fast enough for the… | 52 | Python | 2026-09-22 |
| [agentsea/nautilo](https://github.com/agentsea/nautilo) | AI goes multiplayer. A self-hosted workspace for people and machine people. Create, code, and work together a… | 51 | TypeScript | 2026-09-21 |
| [achimala/jev-paint](https://github.com/achimala/jev-paint) | Use Jev to make art! | 49 | JavaScript | 2026-09-19 |
| [affirmitv/ghosthands](https://github.com/affirmitv/ghosthands) | Give an agent real hands and eyes: undetectable, DOM-independent GUI automation. A $4 USB-HID microcontroller… | 49 | Python | 2026-09-18 |
| [GinSing1226/ScreenClaw](https://github.com/GinSing1226/ScreenClaw) | Record once, replay anytime & screenshots + percentage-coordinate grids: non-blocking Windows desktop RPA / C… | 49 | Python | 2026-06-23 |
| [everruns/everruns](https://github.com/everruns/everruns) | Headless durable agentic harness engine. Run durable AI agents reliably and scalably. | 48 | Rust | 2026-09-22 |
| [ikermoel/open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) | Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisi… | 47 | Python | 2026-09-22 |
| [RafalWilinski/vibecheck](https://github.com/RafalWilinski/vibecheck) | Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post | 47 | JavaScript | 2026-09-20 |
| [socai-io/jev-social](https://github.com/socai-io/jev-social) | Jev-powered Instagram, TikTok, and LinkedIn research: typed routing, real browser evidence, streamed post car… | 46 | JavaScript | 2026-09-21 |
| [WYRE-AI/msp-claude-plugins](https://github.com/WYRE-AI/msp-claude-plugins) | The community-driven Claude Code plugin marketplace for MSPs — 70+ plugins across PSA, RMM, security, documen… | 46 | Astro | 2026-09-22 |
| [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) | Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as s… | 45 | Python | 2026-09-21 |
| [skeptrunedev/jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) | A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence a… | 44 | Python | 2026-09-19 |
| [r-ms/mini-jev](https://github.com/r-ms/mini-jev) | mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter'… | 42 | Python | 2026-09-18 |
| [AustinAWay/Working-Memory-Jev](https://github.com/AustinAWay/Working-Memory-Jev) | — | 41 | Python | 2026-09-21 |
| [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | — | 41 | Python | 2026-09-22 |
| [dorkitude/webctl](https://github.com/dorkitude/webctl) | Smart web search CLI for agents, backed by Jev. Saves a lot of tokens. | 41 | Go | 2026-09-22 |
| [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) | A source-reviewed gallery of JEV-related projects with 50+ GitHub stars — integrations, tools, open models, e… | 40 | JavaScript | 2026-09-22 |
| [DevMortimer/pi-typesafe](https://github.com/DevMortimer/pi-typesafe) | TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors | 40 | TypeScript | 2026-09-22 |
| [intikhab49/open-jev-typed-decision-engine](https://github.com/intikhab49/open-jev-typed-decision-engine) | Open reproduction of TypeSafe Jev: a 150M typed decision engine (noul/choice/score in one non-autoregressive … | 40 | Python | 2026-09-21 |
| [pinecone-io/cultivar](https://github.com/pinecone-io/cultivar) | Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents. | 40 | Python | 2026-09-18 |
| [Hiwoniu/Jev-Case](https://github.com/Hiwoniu/Jev-Case) | 收集全网优秀 case 的收藏库 \| A curated collection of excellent cases from across the web | 39 | TypeScript | 2026-09-19 |
| [okinaaudio/live-jev](https://github.com/okinaaudio/live-jev) | Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done. | 39 | Python | 2026-09-21 |
| [alp82/goodwatch-monorepo](https://github.com/alp82/goodwatch-monorepo) | GoodWatch is a unique take on discovering movies and shows. | 38 | Python | 2026-09-22 |
| [baggiiiie/pi-stuff](https://github.com/baggiiiie/pi-stuff) | my stuff for pi | 38 | TypeScript | 2026-09-22 |
| [IgorGanapolsky/trading](https://github.com/IgorGanapolsky/trading) | Paper-only SPY put-credit validation lab. Broker-backed ledgers and hard risk gates. Live capital blocked; no… | 38 | Python | 2026-09-22 |
| [zhengxuyu/litjev](https://github.com/zhengxuyu/litjev) | Turn any off-the-shelf LLM into a Jev -like decision layer | 38 | Python | 2026-09-21 |
| [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) | This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev. | 37 | TypeScript | 2026-09-19 |
| [tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge) | ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex… | 37 | TypeScript | 2026-09-21 |
| [TypeLLM/TypeLLM](https://github.com/TypeLLM/TypeLLM) | TypeLLM: LLMs with type-safe generation | 37 | Python | 2026-09-22 |
| [Diogenesoftoronto/keating](https://github.com/Diogenesoftoronto/keating) | The hyperteacher, autoteaching in a metaharness. | 36 | TypeScript | 2026-09-20 |
| [Alurith/jeff](https://github.com/Alurith/jeff) | Catch code issues before they catch you. | 35 | Go | 2026-09-20 |
| [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp) | MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client | 35 | TypeScript | 2026-09-21 |
| [MichelKerkmeester/skilled-agent-harness_spec-driven-loops](https://github.com/MichelKerkmeester/skilled-agent-harness_spec-driven-loops) | AI-assisted coding setup that helps you spend less time re-explaining context, and more time shipping with be… | 35 | TypeScript | 2026-09-21 |
| [kieranklaassen/thinkroom](https://github.com/kieranklaassen/thinkroom) | Thinkroom — where deeper thinking compounds. Try it free at https://thinkroom.kieranklaassen.com | 33 | Ruby | 2026-09-19 |
| [AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo) | 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuc… | 32 | Rust | 2026-09-22 |
| [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer) | Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your e… | 32 | JavaScript | 2026-09-19 |
| [hakari-bench/hakari-bench](https://github.com/hakari-bench/hakari-bench) | ⚖️ HAKARI-Bench is a lightweight IR benchmark that rebuilds retrieval tasks as small Nano-sets, making model … | 32 | Python | 2026-09-19 |
| [maruel/genai](https://github.com/maruel/genai) | The opinionated high performance professional-grade AI package for Go | 32 | Go | 2026-09-21 |
| [nicholasgriffintn/ai-platform](https://github.com/nicholasgriffintn/ai-platform) | A multi-model AI chat platform built to be a complete solution for your own personal assistant or an ai assis… | 32 | TypeScript | 2026-09-22 |
| [piyush97/PiyushMehta.com](https://github.com/piyush97/PiyushMehta.com) | A modern, fast, and SEO-optimized personal website built with Astro, showcasing my work as a Senior Software … | 32 | HTML | 2026-09-22 |
| [seznam/jailoc](https://github.com/seznam/jailoc) | 🔒 Jail your AI agents — sandboxed Docker environments with network isolation for Opencode agents | 32 | Go | 2026-09-20 |
| [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev) | Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev | 32 | TypeScript | 2026-09-20 |
| [samdotmak/jev-recall](https://github.com/samdotmak/jev-recall) | Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev | 31 | TypeScript | 2026-09-20 |
| [qkal/Canny](https://github.com/qkal/Canny) | Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Je… | 30 | TypeScript | 2026-09-21 |
| [tshmieldev/sharp](https://github.com/tshmieldev/sharp) | Filter your X.com feed with Jev or any LLM | 30 | TypeScript | 2026-09-21 |
| [joshuaeroman/plasmallm](https://github.com/joshuaeroman/plasmallm) | A KDE Plasma plasmoid to add desktop chat with LLMs | 29 | QML | 2026-09-18 |
| [KryptSec/oasis](https://github.com/KryptSec/oasis) | Open-source AI security benchmarking CLI. Measure how AI models perform offensive security tasks with MITRE A… | 29 | TypeScript | 2026-09-19 |
| [lykycy123/RoboJEV](https://github.com/lykycy123/RoboJEV) | Two-stage JEV control of a Franka Panda in MuJoCo | 29 | Python | 2026-09-21 |
| [dannote/jev](https://github.com/dannote/jev) | TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer | 28 | Elixir | 2026-09-21 |
| [AlbionaHoti/refgarden](https://github.com/AlbionaHoti/refgarden) | A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked col… | 27 | TypeScript | 2026-09-19 |
| [boozedog/pi-codemode](https://github.com/boozedog/pi-codemode) | — | 27 | TypeScript | 2026-09-21 |
| [braintrustdata/braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) | JavaScript Tracing & Evals library for Braintrust | 27 | TypeScript | 2026-09-21 |
| [DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest) | A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. | 27 | TypeScript | 2026-09-18 |
| [fidecastro/jevify](https://github.com/fidecastro/jevify) | Supersimple way to serve LLMs as a Jev-like endpoint | 27 | Python | 2026-09-20 |
| [JackZeng/Jev_apps](https://github.com/JackZeng/Jev_apps) | 看看 Jev 能做什么：用中英文讲清热门应用、工作原理和各自优缺点。Explore Jev apps with plain-language examples, explanations, and comparison… | 27 | Python | 2026-09-21 |
| [myc0576/SmartMoney-Cub](https://github.com/myc0576/SmartMoney-Cub) | Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible fina… | 26 | Python | 2026-09-21 |
| [soul99soul-glitch/AmberAgent](https://github.com/soul99soul-glitch/AmberAgent) | AmberAgent mobile AI workspace for Android and iOS, with a gradually shared core. | 26 | Kotlin | 2026-09-22 |
| [wundercorp/loki](https://github.com/wundercorp/loki) | The agent that evolves with you 𖤍 | 26 | Python | 2026-09-17 |
| [Hulupeep/Specflow](https://github.com/Hulupeep/Specflow) | Specs that enforce themselves. Turn specs into contracts that can't be broken by helpful LLMs. | 25 | JavaScript | 2026-09-21 |
| [sabeel111/OpenSourceJev](https://github.com/sabeel111/OpenSourceJev) | Turning an LLM model into a Jev like System. | 25 | Python | 2026-09-20 |
| [zadescoxp/Jev-Trades](https://github.com/zadescoxp/Jev-Trades) | Trading bot with the all new TypeSafe AI's first system one model named as Jev | 24 | Python | 2026-09-18 |
| [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) | Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call rece… | 24 | Python | 2026-09-22 |
| [davila7/jev-explained](https://github.com/davila7/jev-explained) | Jev Explained | 23 | TypeScript | 2026-09-20 |
| [Esposter/Esposter](https://github.com/Esposter/Esposter) | A nice and casual place for posting random things. | 23 | TypeScript | 2026-09-22 |
| [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) | JEV HUB · X 上关于 TypeSafe AI「系统一模型」Jev 的长文与演示视频聚合（保留原链与作者）｜ 谁是专家 出品 | 23 | CSS | 2026-09-21 |
| [mossyfield/ST-jeved](https://github.com/mossyfield/ST-jeved) | SillyTavern extension that measures each reply and instructs the narrator only when a rule matches. | 23 | JavaScript | 2026-09-22 |
| [rorshopping/jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) | Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benc… | 23 | Python | 2026-09-17 |
| [jstxn/agentdir](https://github.com/jstxn/agentdir) | Local-first Maildir-inspired work mailstore for software agents | 22 | Python | 2026-09-21 |
| [luantak/is-malicious](https://github.com/luantak/is-malicious) | A codebase scanner that helps you not run malicous code | 22 | TypeScript | 2026-09-21 |
| [altryne/jevify](https://github.com/altryne/jevify) | An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent communit… | 21 | Python | 2026-09-21 |
| [andresguc1/hal-test](https://github.com/andresguc1/hal-test) | HAL-TEST is an Open Source visual automation framework for Playwright that lets developers design and orchest… | 21 | JavaScript | 2026-09-20 |
| [OmniJev/PlayJev](https://github.com/OmniJev/PlayJev) | 🚀🚀 A 0.8B JEV-like multimodal model playing GUI games directly from raw pixels. | 21 | JavaScript | 2026-09-21 |
| [razaanstha/ulka](https://github.com/razaanstha/ulka) | Experimental browser agent powered by FX, Jev, and Vercel AI Gateway. Bring your own API key to read pages an… | 21 | TypeScript | 2026-09-19 |
| [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | High-throughput synthetic and pretraining dataset sifter for TypeSafe Jev. Rust streaming core, Parquet and J… | 20 | Rust | 2026-09-22 |
| [Argos1111/jev_local](https://github.com/Argos1111/jev_local) | Replicating Jev with a local LLM | 20 | Python | 2026-09-22 |
| [colliber/duckdb-jev](https://github.com/colliber/duckdb-jev) | DuckDB extension: typed Jev answers as real SQL types | 20 | C++ | 2026-09-18 |
| [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) | 1v1 Jev quickscope arena — Three.js + TypeSafe System One | 20 | TypeScript | 2026-09-18 |
| [erwins-enkel/shepherd](https://github.com/erwins-enkel/shepherd) | Shepherd — self-hosted mission control for interactive Claude Code (herdr + Bun + SvelteKit) | 20 | TypeScript | 2026-09-21 |
| [mmastrac/djev](https://github.com/mmastrac/djev) | Jev-style structured decisions on DiffusionGemma: the example server from vLLM PR 57250 | 20 | Python | 2026-09-22 |
| [rhighs/jev-code](https://github.com/rhighs/jev-code) | Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation. | 20 | TypeScript | 2026-09-20 |
| [zszz3/Pi-Jev-Guide](https://github.com/zszz3/Pi-Jev-Guide) | — | 20 | TypeScript | 2026-09-21 |
| [braintrustdata/braintrust-sdk-python](https://github.com/braintrustdata/braintrust-sdk-python) | Python Tracing & Evals library for Braintrust | 19 | Python | 2026-09-21 |
| [everyinfra/jev-radar](https://github.com/everyinfra/jev-radar) | 📡 全网最全 · The world's most comprehensive tracker of the Jev (TypeSafe AI System One) ecosystem — 220+ document… | 19 | — | 2026-09-22 |
| [MiaoWuNYA/rikkahub-sillytavern-android](https://github.com/MiaoWuNYA/rikkahub-sillytavern-android) | RikkaHub Plus 华灯版 —— Android AI 聊天客户端 & SillyTavern 安卓酒馆兼容端。接上 API 即聊：前缀缓存省 token、语义记忆 RAG、Jev 智能决策、QuickJS 插… | 19 | Kotlin | 2026-09-22 |
| [mizchi/jev-playground](https://github.com/mizchi/jev-playground) | — | 19 | TypeScript | 2026-09-22 |
| [nico-martin/open-jev](https://github.com/nico-martin/open-jev) | open-jev is a browser-focused TypeScript library for typed decisions: one piece of text (the state) plus any … | 19 | TypeScript | 2026-09-21 |
| [Trampoline-AI/avalanche](https://github.com/Trampoline-AI/avalanche) | Avalanche makes agents first-class steps in typed data pipelines. Compose adaptive agent work with determinis… | 19 | Python | 2026-09-21 |
| [TypeSafeAI/typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground) | Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts,… | 19 | TypeScript | 2026-09-21 |
| [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) | DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider usage, LAN proxy, MCP manager… | 19 | TypeScript | 2026-09-22 |
| [zhangcy122/OpenJev](https://github.com/zhangcy122/OpenJev) | OpenJev: Open-source alternative to TypeSafe Jev. Typed probabilistic decision API (Choice, Noul, Score) powe… | 19 | HTML | 2026-09-21 |
| [2951461586/Jev-Register-Tool](https://github.com/2951461586/Jev-Register-Tool) | TypeSafe（Jev / System One）申请 → 确认邮件 → 获批 → 注册 → 建 API Key 全链路工具，纯 HTTP 无浏览器 | 18 | Python | 2026-09-22 |
| [CheshiAI/Cheshi](https://github.com/CheshiAI/Cheshi) | Jev-powered conversation memory: find past sessions and revisit decisions with original sources. A macOS work… | 18 | C | 2026-09-21 |
| [frankda/jev-poly-crypto-demo](https://github.com/frankda/jev-poly-crypto-demo) | — | 18 | TypeScript | 2026-09-22 |
| [Nasrallah-AL/jev-cli](https://github.com/Nasrallah-AL/jev-cli) | Command-line tool for TypeSafe's Jev AI model | 18 | TypeScript | 2026-09-20 |
| [Ngineer101/turbodiff](https://github.com/Ngineer101/turbodiff) | Requirements in. Working features out. | 18 | TypeScript | 2026-09-20 |
| [philipbrembeck/pi-advisor](https://github.com/philipbrembeck/pi-advisor) | Fully customizable Advisor and Executor flow plugin for the Pi Coding Agent | 18 | TypeScript | 2026-09-22 |
| [BlackJaxDev/XRENGINE](https://github.com/BlackJaxDev/XRENGINE) | This is my custom open-source C# game engine designed from the ground-up for maximum possible performance ren… | 17 | C# | 2026-09-22 |
| [Davidcreador/pi-dcp](https://github.com/Davidcreador/pi-dcp) | Cut LLM token spend in long Pi sessions, automatically. Dedup redundant tool calls, strip errored payloads, a… | 17 | TypeScript | 2026-09-19 |
| [keltokhy/jgrep](https://github.com/keltokhy/jgrep) | grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms … | 17 | Python | 2026-09-22 |
| [keltokhy/jsort](https://github.com/keltokhy/jsort) | sort by meaning: order lines along a plain-English dimension, from pairwise comparisons judged by TypeSafe's … | 17 | Python | 2026-09-22 |
| [Ray-Hughes/jevalyn](https://github.com/Ray-Hughes/jevalyn) | The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, ca… | 17 | Ruby | 2026-09-21 |
| [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi) | Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) fr… | 17 | TypeScript | 2026-09-19 |
| [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) | Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails… | 17 | JavaScript | 2026-09-20 |
| [wd041216-bit/zero-api-key-web-search](https://github.com/wd041216-bit/zero-api-key-web-search) | Jev-powered search infrastructure for AI agents: zero API keys, MCP-ready, LLM-context aware, with local neur… | 17 | Python | 2026-09-21 |
| [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) | Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Ever… | 16 | — | 2026-09-21 |
| [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) | Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases: repos, patterns, benchmarks, and … | 16 | — | 2026-09-20 |
| [andrueandersoncs/lion](https://github.com/andrueandersoncs/lion) | Lisp Object Notation - an advanced data format built on JSON capable of representing arbitrary computations | 16 | JavaScript | 2026-09-21 |
| [chy4pro/jev-for-chrome](https://github.com/chy4pro/jev-for-chrome) | Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community p… | 16 | TypeScript | 2026-09-21 |
| [Qredence/fleet-prime-agent](https://github.com/Qredence/fleet-prime-agent) | User Interface for Prime-Agent | 16 | TypeScript | 2026-09-21 |
| [Brainwires/jevwire](https://github.com/Brainwires/jevwire) | Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code… | 15 | TypeScript | 2026-09-21 |
| [chopratejas/invalidate](https://github.com/chopratejas/invalidate) | The invalidation layer for AI memory. Every fact gets a lease; new evidence ends it. Built on TypeSafe Jev. | 15 | Python | 2026-09-21 |
| [getainode/ainode](https://github.com/getainode/ainode) | Turn any NVIDIA GPU into a local AI platform. Inference + fine-tuning in your browser. One command to start, … | 15 | Python | 2026-09-22 |
| [getaskclaw/amber](https://github.com/getaskclaw/amber) | 琥珀式封存历史回放评测（AMBER）：封进琥珀，重做当时的题 —— 真实事件回放、物理封存、预注册评分的方法规范 | 15 | Python | 2026-09-21 |
| [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) | Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance. | 15 | TypeScript | 2026-09-21 |
| [kyu1204/jgrep](https://github.com/kyu1204/jgrep) | grep for what code does, not what it's called. Semantic code search powered by TypeSafe Jev. | 15 | TypeScript | 2026-09-22 |
| [machina-sports/sportsclaw](https://github.com/machina-sports/sportsclaw) | — | 15 | TypeScript | 2026-09-21 |
| [mayank953/Jev](https://github.com/mayank953/Jev) | — | 15 | JavaScript | 2026-09-21 |
| [oso95/x-scanner](https://github.com/oso95/x-scanner) | Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter | 15 | TypeScript | 2026-09-19 |
| [rlaope/jeval](https://github.com/rlaope/jeval) | Measures what your Jev classifier's confidence is really worth, and sets the human hand-off line from what a … | 15 | Python | 2026-09-21 |
| [shitianfang/jev-use](https://github.com/shitianfang/jev-use) | Claude Code / Codex / pi plugin that hands agent steps needing no text output to Jev (TypeSafe's judgment mod… | 15 | JavaScript | 2026-09-20 |
| [utk2103/jev-studio](https://github.com/utk2103/jev-studio) | if you're experimenting with jev it will be easier from here | 15 | Python | 2026-09-21 |
| [XiaoConstantine/sgrep](https://github.com/XiaoConstantine/sgrep) | semantic grep | 15 | Go | 2026-09-19 |
| [abhishek085/open-spark-jev](https://github.com/abhishek085/open-spark-jev) | Open-source, local decision models inspired by TypeSafe’s Jev and System One - built on Qwen3 for NVIDIA DGX … | 14 | Python | 2026-09-21 |
| [AkashPriyadarshii/jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) | Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed de… | 14 | JavaScript | 2026-09-21 |
| [atanasster/electionsbg](https://github.com/atanasster/electionsbg) | Data statistics for Bulgaria | 14 | TypeScript | 2026-09-21 |
| [carldaws/hunch](https://github.com/carldaws/hunch) | Probabilistic control flow for Ruby and Rails - powered by TypeSafe's Jev | 14 | Ruby | 2026-09-19 |
| [erendikmenn/jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark) | Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG | 14 | Python | 2026-09-20 |
| [hraness/wordcell](https://github.com/hraness/wordcell) | A knowledge base for coding agents, built from Markdown, backlinks, semantic search, and Git context. | 14 | TypeScript | 2026-09-22 |
| [kikoncuo/jevfire](https://github.com/kikoncuo/jevfire) | JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, an… | 14 | JavaScript | 2026-09-18 |
| [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem) | Jev-Mem: System-One Controlled Agentic Memory | 14 | Python | 2026-09-22 |
| [masharratt/claude-flow-novice](https://github.com/masharratt/claude-flow-novice) | Simplified Claude Flow for beginners - AI agent orchestration made easy | 14 | Shell | 2026-09-22 |
| [packstub/filament-flow](https://github.com/packstub/filament-flow) | Visual workflow automation for Filament panels: triggers, conditions and actions drawn on a canvas, run by yo… | 14 | PHP | 2026-09-21 |
| [PanAchy/jevvy](https://github.com/PanAchy/jevvy) | Jev-powered plugins for coding agents | 14 | TypeScript | 2026-09-21 |
| [parth-kp/jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier) | Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. | 14 | Python | 2026-09-20 |
| [tyler-dot-earth/patdown](https://github.com/tyler-dot-earth/patdown) | Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action,… | 14 | TypeScript | 2026-09-21 |
| [whilehq/whileai-sdk](https://github.com/whilehq/whileai-sdk) | Scientific RL and SFT post-training for AI agents: build evals that can fail, simulate situations, judge chec… | 14 | Python | 2026-09-22 |
| [workglow-dev/libs](https://github.com/workglow-dev/libs) | Workflows that glow | 14 | TypeScript | 2026-09-21 |
| [BorisLeMeec/jev](https://github.com/BorisLeMeec/jev) | A claude code plugin for jev | 13 | Go | 2026-09-18 |
| [buberlo/dsh-jev](https://github.com/buberlo/dsh-jev) | Jev-powered decision layer for DeepSeek Harness | 13 | TypeScript | 2026-09-20 |
| [everyai-com/jev-directory](https://github.com/everyai-com/jev-directory) | — | 13 | HTML | 2026-09-21 |
| [genai-craft/openvons](https://github.com/genai-craft/openvons) | openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド | 13 | Python | 2026-09-21 |
| [jon-devlapaz/jev-me](https://github.com/jon-devlapaz/jev-me) | Grill-me with Jev optional each turn | 13 | — | 2026-09-19 |
| [lukstei/slop-grader](https://github.com/lukstei/slop-grader) | Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, n… | 13 | TypeScript | 2026-09-22 |
| [wh000wh000/awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) | Awesome Jev — evidence-graded index of TypeSafe System One: SDKs, MCP tools, agents, apps and open models. 20… | 13 | Python | 2026-09-22 |
| [anpicasso/hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) | TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measu… | 12 | Python | 2026-09-22 |
| [atharvamhaske/typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go) | unofficial go sdk for typesafe ai. not affiliated with or endorsed by typesafe ai. a side project built to fi… | 12 | Go | 2026-09-21 |
| [DECRUX9812/typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router) | TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-… | 12 | Python | 2026-09-21 |
| [keeltrace/hermes-jev](https://github.com/keeltrace/hermes-jev) | Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev. | 12 | Python | 2026-09-22 |
| [koltyakov/varro](https://github.com/koltyakov/varro) | 🤖 An OpenCode workbench for VS Code with project-aware AI chat and parallel agent sessions | 12 | TypeScript | 2026-09-21 |
| [ktaletsk/jevframe](https://github.com/ktaletsk/jevframe) | Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-la… | 12 | Python | 2026-09-21 |
| [lmnr-ai/lmnr-ts](https://github.com/lmnr-ai/lmnr-ts) | TypeScript SDK for Laminar AI | 12 | TypeScript | 2026-09-21 |
| [maplezzk/pi-extensions](https://github.com/maplezzk/pi-extensions) | Extensions for pi coding agent (i18n, distill, tool-supervisor) | 12 | TypeScript | 2026-09-22 |
| [mejiasd3v/pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) | Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway | 12 | JavaScript | 2026-09-21 |
| [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) | Turn any LLM into a Jev-style decision model: typed decisions, real probabilities, no training. | 12 | Python | 2026-09-22 |
| [pst2154/Nemotron_Jev](https://github.com/pst2154/Nemotron_Jev) | — | 12 | HTML | 2026-09-22 |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | A live Haskell notebook where agents compose commands, semantic judgments, and delegation into programs. Agen… | 12 | Rust | 2026-09-19 |
| [trungdq88/jev-tetris](https://github.com/trungdq88/jev-tetris) | Jev play Tetris in real-time against other AI models | 12 | JavaScript | 2026-09-21 |
| [tumf/jev-cli](https://github.com/tumf/jev-cli) | Small dependency-free CLI for TypeSafe Jev | 12 | Python | 2026-09-19 |
| [cocktailpeanut/jevthoven](https://github.com/cocktailpeanut/jevthoven) | AI Music (MIDI) generator powered by Jev | 11 | TypeScript | 2026-09-18 |
| [collapseindex/jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed) | BRRRRRRRRRRRRRRRRRRRRRR | 11 | Python | 2026-09-22 |
| [hotchpotch/jev-reranker](https://github.com/hotchpotch/jev-reranker) | Jev-powered relevance filtering and reranking for RAG in Python. | 11 | Python | 2026-09-21 |
| [iamtoomas/JevLint](https://github.com/iamtoomas/JevLint) | Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. | 11 | TypeScript | 2026-09-20 |
| [kavehmz/typesafe-playground](https://github.com/kavehmz/typesafe-playground) | Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisi… | 11 | JavaScript | 2026-09-22 |
| [kylemclaren/jevql](https://github.com/kylemclaren/jevql) | Semantic SQL for Postgres, powered by Jev | 11 | Go | 2026-09-19 |
| [madeye/pi-jev](https://github.com/madeye/pi-jev) | Jev-assisted file retrieval and request caching for faster Pi workflows | 11 | TypeScript | 2026-09-21 |
| [shaharia-lab/jev-cli](https://github.com/shaharia-lab/jev-cli) | Command-line tool for TypeSafe AI's Jev model. Ask yes/no, multiple-choice and rubric questions about any tex… | 11 | Rust | 2026-09-21 |
| [Synxneuos/jevbrain](https://github.com/Synxneuos/jevbrain) | — | 11 | JavaScript | 2026-09-22 |
| [tickernelz/sub2api](https://github.com/tickernelz/sub2api) | Fork of sub2api some improvements | 11 | Go | 2026-09-21 |
| [tinyhumansai/tinyhivemind](https://github.com/tinyhumansai/tinyhivemind) | Hive mind mechanics for agents. A step closer towards AGI | 11 | Rust | 2026-09-20 |
| [zjunlp/JevLoop](https://github.com/zjunlp/JevLoop) | The agent loop where decisions don't cost a large language model call. Zero deps, runs offline, no API key ne… | 11 | TypeScript | 2026-09-22 |
| [alanagoyal/booklist](https://github.com/alanagoyal/booklist) | a curated collection of the most frequently recommended books on the internet | 10 | TypeScript | 2026-09-20 |
| [bestagentkits/cloud-harness-mcp](https://github.com/bestagentkits/cloud-harness-mcp) | Remote coding harness exposed as a secure Streamable HTTP MCP server | 10 | TypeScript | 2026-09-22 |
| [evoke-build/evoke](https://github.com/evoke-build/evoke) | Software, by reflex. A sentence becomes a call of a small program, chosen by Jev, TypeSafe AI's classifier, a… | 10 | Rust | 2026-09-22 |
| [Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev) | Public examples of Jev used for robot control, 3D modeling and adjacent control tasks, with sources and archi… | 10 | — | 2026-09-21 |
| [HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask) | TypeSafe Jev as the pi coding agent's quiet decision layer | 10 | TypeScript | 2026-09-18 |
| [Jimuelle07/Helm](https://github.com/Jimuelle07/Helm) | Route every coding task to the best AI agent on your machine — Claude Code, Codex, Cursor, Gemini CLI, Aider,… | 10 | Python | 2026-09-22 |
| [kernel/browser-loop](https://github.com/kernel/browser-loop) | Browser tools for your agent: framework-neutral catalog, Kernel-browser execution, and framework bindings. | 10 | TypeScript | 2026-09-18 |
| [manifoldor/xtags](https://github.com/manifoldor/xtags) | 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。 | 10 | JavaScript | 2026-09-21 |
| [MauroPello/stop-the-slop](https://github.com/MauroPello/stop-the-slop) | 🚫 Spot AI-generated YouTube scripts and content farms in real-time. Open-source browser extension for Chrome … | 10 | JavaScript | 2026-09-20 |
| [sunil-sadasivan/jevernetes](https://github.com/sunil-sadasivan/jevernetes) | Live Kubernetes log analysis, contextual investigation, and agent handoff powered by Jev. | 10 | Python | 2026-09-21 |
| [Aias/red-cliff-record](https://github.com/Aias/red-cliff-record) | A local-first, own-your-data approach to personal knowledge management. The spiritual successor to barnsworth… | 9 | TypeScript | 2026-09-21 |
| [akakaule/NimBus](https://github.com/akakaule/NimBus) | — | 9 | C# | 2026-09-22 |
| [Ayi1337/yesorno](https://github.com/Ayi1337/yesorno) | — | 9 | HTML | 2026-09-21 |
| [chengyongru/fastjev](https://github.com/chengyongru/fastjev) | SDK-first, independently maintained SemIf fork for fast, self-hosted semantic decisions. | 9 | Python | 2026-09-22 |
| [ckaraca/awesome-jev](https://github.com/ckaraca/awesome-jev) | A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast,… | 9 | Python | 2026-09-21 |
| [ClassicMiniDIY/classicminidiy](https://github.com/ClassicMiniDIY/classicminidiy) | Classic Mini DIY is the best place to find all the reference material, how-to videos, and much much more for … | 9 | Vue | 2026-09-21 |
| [fellowship-dev/navvi](https://github.com/fellowship-dev/navvi) | Give your AI agent a real browser identity. MCP server with persistent personas, anti-detection browser, and … | 9 | TypeScript | 2026-09-22 |
| [frostney/clean-code-review](https://github.com/frostney/clean-code-review) | Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by … | 9 | TypeScript | 2026-09-21 |
| [healthkey-ai/promop](https://github.com/healthkey-ai/promop) | Django/PostgreSQL project with models for OMOP+oncology plus a flat denormalized table to support fast clinic… | 9 | Python | 2026-09-22 |
| [jiawei686/jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp) | Hand the browser work off: an MCP server where a decision model drives the page for your agent, so a flow cos… | 9 | Python | 2026-09-21 |
| [kushals256/jevcache](https://github.com/kushals256/jevcache) | Skip expensive LLM calls when TypeSafe Jev says same intent. OpenAI-compatible local cache proxy — npx @kusha… | 9 | TypeScript | 2026-09-21 |
| [MadaBurns/bv-mcp](https://github.com/MadaBurns/bv-mcp) | Open-source DNS & email security scanner. One MCP endpoint, 57 checks, zero install. Cloudflare Workers. | 9 | TypeScript | 2026-09-21 |
| [magnus919/SlopSearX](https://github.com/magnus919/SlopSearX) | Cloud-native, stateless, AI-agent-first meta search engine. Drop-in SearXNG replacement built for the GroktoC… | 9 | Python | 2026-09-22 |
| [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) | A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model. | 9 | Python | 2026-09-22 |
| [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs) | Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. | 9 | JavaScript | 2026-09-22 |
| [rottenpen/agent-stardew](https://github.com/rottenpen/agent-stardew) | 星露谷农场小助手：Jev 自主游玩、dsh 插件、独立 CLI 与 SMAPI Mod | 9 | TypeScript | 2026-09-20 |
| [stefw/lkclean](https://github.com/stefw/lkclean) | Chrome extension that cleans up your LinkedIn feed: hides engagement bait, self-promo and off-topic posts usi… | 9 | TypeScript | 2026-09-20 |
| [Tangerg/typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go) | Go SDK for the TypeSafe AI API — typed questions in, probability distributions out. | 9 | Go | 2026-09-19 |
| [TannerMidd/specpi-jev-guard](https://github.com/TannerMidd/specpi-jev-guard) | — | 9 | JavaScript | 2026-09-20 |
| [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) | All things awesome related to Jev | 9 | — | 2026-09-21 |
| [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit) | pre-commit hook: one Jev call judges whether your commit message matches the diff, plus debug leftovers, scop… | 9 | Python | 2026-09-19 |
| [virolea/lintus](https://github.com/virolea/lintus) | A linter whose rules are written in plain language. | 9 | Ruby | 2026-09-21 |
| [ZYHUO/nyat-bot](https://github.com/ZYHUO/nyat-bot) | NyatBot — a Telegram group-chat agent on the path from chatLLM to AGI | 9 | TypeScript | 2026-09-22 |
| [agentiumOS/agentium](https://github.com/agentiumOS/agentium) | Agentium is a TypeScript agent framework for Node.js: models, tools, memory, teams, workflows, and runtime in… | 8 | TypeScript | 2026-09-19 |
| [BigCactusLabs/dead-letter](https://github.com/BigCactusLabs/dead-letter) | Convert .eml email exports to Markdown with YAML front matter | 8 | Python | 2026-09-21 |
| [cablehead/jev.nu](https://github.com/cablehead/jev.nu) | Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities | 8 | Nushell | 2026-09-21 |
| [cristianoliveira/jeq](https://github.com/cristianoliveira/jeq) | What happens when jev meets jq? Intelligence you can pipe | 8 | Go | 2026-09-22 |
| [DGarbs51/solo-orchestrator-skill](https://github.com/DGarbs51/solo-orchestrator-skill) | A skill I have created for using Solo's MCP for creating an orchestration mechanic for making a frontier mode… | 8 | Python | 2026-09-19 |
| [fakoli/anvil](https://github.com/fakoli/anvil) | Anvil — local-first, runtime-neutral project state for humans and AI coding agents (beta). | 8 | Python | 2026-09-21 |
| [harshwasan/jev-sentinel](https://github.com/harshwasan/jev-sentinel) | Pi coding-agent extension: TypeSafe Jev checks for tool calls, tool outputs and replies (prompt injection, ap… | 8 | TypeScript | 2026-09-20 |
| [HexyeDEV/JevPR](https://github.com/HexyeDEV/JevPR) | PR Risk review, automated by Jev | 8 | Python | 2026-09-21 |
| [iamadi11/mcp-ui-poc](https://github.com/iamadi11/mcp-ui-poc) | — | 8 | JavaScript | 2026-09-21 |
| [infiquetra/infiquetra-claude-plugins](https://github.com/infiquetra/infiquetra-claude-plugins) | Claude Code plugins for Infiquetra development workflows | 8 | Python | 2026-09-20 |
| [jekhov/jekhov](https://github.com/jekhov/jekhov) | Policy-bounded Jev target selection for resilient Playwright workflows | 8 | TypeScript | 2026-09-19 |
| [jerryfane/omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction) | Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter | 8 | TypeScript | 2026-09-19 |
| [Kevthetech143/super-jev](https://github.com/Kevthetech143/super-jev) | A small, extensible decision-to-action harness for TypeSafe Jev | 8 | Python | 2026-09-21 |
| [kunko-ai-labs/judge-audit](https://github.com/kunko-ai-labs/judge-audit) | Independent calibration audits for AI judges. The Moody's for AI judgment. | 8 | Python | 2026-09-22 |
| [miikkij/aimeat-protocol](https://github.com/miikkij/aimeat-protocol) | The Linux of AI - an open, federated, self-hosted AI operating system. Humans, AI agents, and local LLMs shar… | 8 | TypeScript | 2026-09-20 |
| [Nancy-Chauhan/hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) | Autonomous multi-source rental search powered by TypeSafe Jev | 8 | JavaScript | 2026-09-21 |
| [PerryLink/jevcore](https://github.com/PerryLink/jevcore) | TypeSafe Jev for DeepSeek Harness, the Model Context Protocol, and plain Node: typed judgments instead of pro… | 8 | TypeScript | 2026-09-21 |
| [Qew7/jev-feels](https://github.com/Qew7/jev-feels) | Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered b… | 8 | Ruby | 2026-09-21 |
| [rajdhakad9826/jev-router](https://github.com/rajdhakad9826/jev-router) | LLM router that picks the cheapest model capable of handling a query, using TypeSafe's Jev for fast classific… | 8 | TypeScript | 2026-09-21 |
| [ranjan2829/AskJev](https://github.com/ranjan2829/AskJev) | AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude) | 8 | TypeScript | 2026-09-18 |
| [rsrini7/Learnings](https://github.com/rsrini7/Learnings) | My public engineering learning OS - daily notes, AI/ML research, agent systems, JVM engineering, architecture… | 8 | Python | 2026-09-22 |
| [SShadowS/DevOpsWorker](https://github.com/SShadowS/DevOpsWorker) | Multi-agent AI pipeline for Azure DevOps + Business Central (AL), built on the Claude Agent SDK. Customizable… | 8 | TypeScript | 2026-09-21 |
| [Towow-ai/jpp](https://github.com/Towow-ai/jpp) | J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，… | 8 | Python | 2026-09-22 |
| [wenerme/ai](https://github.com/wenerme/ai) | AI related stuff | 8 | MDX | 2026-09-22 |
| [alfdav/music-dl](https://github.com/alfdav/music-dl) | CLI tool for downloading music from Tidal | 7 | Python | 2026-09-21 |
| [arunav25/jev-mcp](https://github.com/arunav25/jev-mcp) | Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and m… | 7 | JavaScript | 2026-09-21 |
| [backmeupplz/jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot) | Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev | 7 | TypeScript | 2026-09-21 |
| [cdot65/prisma-airs-cli](https://github.com/cdot65/prisma-airs-cli) | CLI tool that provides full operational coverage over Palo Alto Prisma AIRS AI security capabilities | 7 | TypeScript | 2026-09-21 |
| [grahama1970/agent-skills](https://github.com/grahama1970/agent-skills) | Shared skills for AI agents (Claude Code, Codex, Gemini) | 7 | Python | 2026-09-21 |
| [h1bomb/bluff](https://github.com/h1bomb/bluff) | — | 7 | TypeScript | 2026-09-21 |
| [HsiangNianian/GlyphWeave](https://github.com/HsiangNianian/GlyphWeave) | Infinite-canvas ASCII roguelike tilemap editor. Paint dungeons, weave glyphs. Multi-layer editing, preset roo… | 7 | Rust | 2026-09-20 |
| [inanna-malick/jev-dsl](https://github.com/inanna-malick/jev-dsl) | Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the s… | 7 | Haskell | 2026-09-18 |
| [inso1337/revl](https://github.com/inso1337/revl) | A language for safe, universal spatiotemporal composability (Cordis paradigm) and orchestration. | 7 | Python | 2026-09-22 |
| [joevidev/ui-generator-instinct-jev](https://github.com/joevidev/ui-generator-instinct-jev) | — | 7 | TypeScript | 2026-09-18 |
| [linny006/mcp-servers-live](https://github.com/linny006/mcp-servers-live) | Auto-updated index of MCP servers shipping on GitHub, refreshed every 15 minutes | 7 | HTML | 2026-09-22 |
| [lucasmartins-ai/lcc](https://github.com/lucasmartins-ai/lcc) | Local Context Compiler (lcc): clean, dedupe and compact prompt context before it reaches the model, then repo… | 7 | Python | 2026-09-21 |
| [MoeclubM/PlayJev](https://github.com/MoeclubM/PlayJev) | Better Jev playground | 7 | TypeScript | 2026-09-20 |
| [NeuralNexusPro/startupOS](https://github.com/NeuralNexusPro/startupOS) | Personal Business Operate System. To make AI adapt to human thinking | 7 | TypeScript | 2026-09-21 |
| [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) | Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, bef… | 7 | TypeScript | 2026-09-19 |
| [okooo5km/jev](https://github.com/okooo5km/jev) | Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe's Jev model, via… | 7 | Python | 2026-09-19 |
| [OskarLebuda/precog](https://github.com/OskarLebuda/precog) | Your links, loaded before the click. | 7 | TypeScript | 2026-09-20 |
| [Papr-ai/paprwork](https://github.com/Papr-ai/paprwork) | Papr Work is a local-first app that lets you collaborate with AI agents that can access your computer, rememb… | 7 | TypeScript | 2026-09-21 |
| [PixelML/av](https://github.com/PixelML/av) | Video Memory CLI: index once, search/ask forever (dense captions + transcripts + timestamps). Built for agent… | 7 | Python | 2026-09-21 |
| [taodav/jev_deep_rl](https://github.com/taodav/jev_deep_rl) | — | 7 | Python | 2026-09-20 |
| [thejorgg/omp-jev](https://github.com/thejorgg/omp-jev) | — | 7 | TypeScript | 2026-09-18 |
| [tickernelz/omp-fabric](https://github.com/tickernelz/omp-fabric) | Fabric for OMP: deterministic, LLM-free orchestration of the Oh My Pi host toolchain | 7 | TypeScript | 2026-09-22 |
| [withoneai/awesome-one](https://github.com/withoneai/awesome-one) | ✨ A showcase of One | 7 | TypeScript | 2026-09-21 |
| [ziqi-jin/agent-to-trust](https://github.com/ziqi-jin/agent-to-trust) | Don't trust an Agent. Test it. Open-source lab for agent credit — exams → evidence → explainable, recomputabl… | 7 | TypeScript | 2026-09-22 |
| [24601/Augustus](https://github.com/24601/Augustus) | Agent skill for the decision-model class (classifiers, encoders/decoders, specialized AR heads, System One). … | 6 | Python | 2026-09-22 |
| [BattlesnakeOfficial/arena](https://github.com/BattlesnakeOfficial/arena) | Battlesnake Tournaments | 6 | Rust | 2026-09-22 |
| [berkayturk/appstore-precheck](https://github.com/berkayturk/appstore-precheck) | Read-only iOS App Store pre-submission check: scans 52 rejection vectors, wraps Apple's fastlane precheck, wa… | 6 | Shell | 2026-09-18 |
| [blazejkustra/softlint](https://github.com/blazejkustra/softlint) | Enforce rules a linter can't. A GitHub Action that reviews PRs against plain-English rules, judged by Jev. | 6 | TypeScript | 2026-09-20 |
| [collapseindex/dinostomp](https://github.com/collapseindex/dinostomp) | A verification layer for AI evaluations. Checks the instrument, not just the score: data, scorer, runs, numbe… | 6 | Python | 2026-09-19 |
| [Dino-Kupinic/blackrose](https://github.com/Dino-Kupinic/blackrose) | — | 6 | Python | 2026-09-21 |
| [enoyola/jev-grand-prix](https://github.com/enoyola/jev-grand-prix) | An F1 racing game where TypeSafe's Jev picks the racing line and the pedals, and learns each corner's limit b… | 6 | JavaScript | 2026-09-21 |
| [forvela/jev-agent-browser](https://github.com/forvela/jev-agent-browser) | Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and … | 6 | JavaScript | 2026-09-21 |
| [himomohi/aside-jev](https://github.com/himomohi/aside-jev) | Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, … | 6 | Python | 2026-09-21 |
| [iefnaf/pi-jev](https://github.com/iefnaf/pi-jev) | Pi extension suite powered by Jev: selective context compaction and model routing | 6 | TypeScript | 2026-09-20 |
| [imMamdouhaboammar/get-fable](https://github.com/imMamdouhaboammar/get-fable) | Make the model you already use work more like a frontier model with better planning, persistent context, skil… | 6 | TypeScript | 2026-09-21 |
| [intersoftdatalabs-in/percussioncms](https://github.com/intersoftdatalabs-in/percussioncms) | Percussion CMS — formerly CM1 / Rhythmyx / CM System by Percussion Software. Actively maintained by Intersoft… | 6 | Java | 2026-09-22 |
| [jackbarunz/jev-tool-router](https://github.com/jackbarunz/jev-tool-router) | Jev-powered MCP tool routing for Codex | 6 | JavaScript | 2026-09-21 |
| [jagsan-cyber/reflex-gate](https://github.com/jagsan-cyber/reflex-gate) | Local Jev / System One–compatible gateway — not TypeSafe’s Jev. Fast, privacy-first, offline. | 6 | Go | 2026-09-21 |
| [joshmn/typesafe-sdk](https://github.com/joshmn/typesafe-sdk) | Ruby client for typesafe.ai | 6 | Ruby | 2026-09-19 |
| [kitfunso/luminus](https://github.com/kitfunso/luminus) | Real-time European & UK electricity grid data via MCP | 6 | TypeScript | 2026-09-18 |
| [larguesa/jev-search](https://github.com/larguesa/jev-search) | Experimental semantic line search with TypeSafe Jev via OpenRouter. Python CLI with no runtime dependencies. | 6 | Python | 2026-09-20 |
| [muratmirgun/owncode](https://github.com/muratmirgun/owncode) | An experimental terminal coding agent with configurable models, Witch orchestration, and multiple context com… | 6 | Go | 2026-09-21 |
| [Nyarlathoteppppp/pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context) | Model performance first. Token savings second. A Pi extension with freshness-aware read dedupe, Jev log filte… | 6 | TypeScript | 2026-09-21 |
| [rashedInt32/jev-mcp](https://github.com/rashedInt32/jev-mcp) | MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Sh… | 6 | TypeScript | 2026-09-20 |
| [saibimajdi/typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) | Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structur… | 6 | C# | 2026-09-18 |
| [scale-venture-partners/riff](https://github.com/scale-venture-partners/riff) | A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model | 6 | Python | 2026-09-18 |
| [smartaces/jev-plays-streetfighter-2](https://github.com/smartaces/jev-plays-streetfighter-2) | — | 6 | Python | 2026-09-21 |
| [syumai/jevyoumean](https://github.com/syumai/jevyoumean) | Semantic "Did you mean?" for any CLI — wraps commands and uses TypeSafe's Jev to match subcommand typos by in… | 6 | Go | 2026-09-22 |
| [tontoko/jev-browser](https://github.com/tontoko/jev-browser) | One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations an… | 6 | JavaScript | 2026-09-22 |
| [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) | Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibrat… | 6 | Python | 2026-09-19 |
| [alexgreensh/eval-genius](https://github.com/alexgreensh/eval-genius) | Teach your agent to work with evals: WHEN you actually need an eval or benchmark, HOW to build one that holds… | 5 | Python | 2026-09-21 |
| [alexwestco/llm-to-jev](https://github.com/alexwestco/llm-to-jev) | Convert LLM prompts to Jev prompts | 5 | JavaScript | 2026-09-21 |
| [AlkaidSTART/coderelay](https://github.com/AlkaidSTART/coderelay) | — | 5 | TypeScript | 2026-09-22 |
| [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) | Can a decision model beat dedicated rerankers? TypeSafe Jev vs Cohere Rerank 4 vs ZeroEntropy zerank-2 vs a c… | 5 | Python | 2026-09-17 |
| [buchmark/claude-jev](https://github.com/buchmark/claude-jev) | Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — cal… | 5 | TypeScript | 2026-09-21 |
| [buluoray/JevOnly](https://github.com/buluoray/JevOnly) | Pure Jev that can "type" and drive towards task completion. | 5 | Python | 2026-09-21 |
| [cyberofficial/dsh-plugin-jev](https://github.com/cyberofficial/dsh-plugin-jev) | — | 5 | JavaScript | 2026-09-20 |
| [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) | TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai) | 5 | TypeScript | 2026-09-22 |
| [docxology/daf-jev](https://github.com/docxology/daf-jev) | daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confiden… | 5 | Python | 2026-09-21 |
| [doronp/jevc](https://github.com/doronp/jevc) | Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the … | 5 | TypeScript | 2026-09-22 |
| [endomorphosis/JevOps](https://github.com/endomorphosis/JevOps) | — | 5 | Python | 2026-09-22 |
| [gabrielmoreira/awesome-ai-rabbit-holes](https://github.com/gabrielmoreira/awesome-ai-rabbit-holes) | A never-complete, already-outdated catalog of AI agents and tools. | 5 | TypeScript | 2026-09-21 |
| [hndrr/ComfyUI-Jev](https://github.com/hndrr/ComfyUI-Jev) | Jev text interpretation and judgments for ComfyUI. | 5 | Python | 2026-09-20 |
| [human-bee/PRESENT](https://github.com/human-bee/PRESENT) | REALTIME MEETING PRODUCER?ASSISTANT AGENT PROJECT | 5 | TypeScript | 2026-09-22 |
| [jaibhasin/jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver) | A Chrome extension that covers distracting YouTube videos with Jev. Show anyway whenever you want. | 5 | JavaScript | 2026-09-20 |
| [jammaru/jev-lab](https://github.com/jammaru/jev-lab) | 100 AI NPCs live in a tiny town. Jev chooses the next action; the world writes the story. | 5 | TypeScript | 2026-09-18 |
| [johnhughes3/LegalForecastBench](https://github.com/johnhughes3/LegalForecastBench) | LegalForecast-MTD benchmark alpha and official evaluation workflows | 5 | Python | 2026-09-22 |
| [LeahyCC/kungfu-kanban](https://github.com/LeahyCC/kungfu-kanban) | Local-first kanban board where Claude Code agents work your cards — dependency chains with merge gates, an AI… | 5 | JavaScript | 2026-09-18 |
| [lhemerly/mcts-agent](https://github.com/lhemerly/mcts-agent) | Discriminative Monte Carlo Tree Search using TypeSafe Jev System One Primitives and Gemini | 5 | Python | 2026-09-22 |
| [mastepanoski/ce-ai](https://github.com/mastepanoski/ce-ai) | ce-ai orchestrates distributions of the open-source Compound Engineering Plugin — a suite of specialized skil… | 5 | Rust | 2026-09-22 |
| [mertcicekci0/S1Code](https://github.com/mertcicekci0/S1Code) | Rust-native, decision-first coding agent. | 5 | Rust | 2026-09-19 |
| [muthuishere/toolnexus](https://github.com/muthuishere/toolnexus) | One agent SDK, hand-ported to 7 languages — JavaScript, Python, Go, Java, C#, Elixir, Clojure — every port he… | 5 | MDX | 2026-09-22 |
| [Nanako0129/NyanCogs](https://github.com/Nanako0129/NyanCogs) | Cogs for Red Discord Bot | 5 | Python | 2026-09-22 |
| [npipeline/NPipeline](https://github.com/npipeline/NPipeline) | High-performance, streaming data pipelines for .NET | 5 | C# | 2026-09-22 |
| [nshkrdotcom/typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) | An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM int… | 5 | Elixir | 2026-09-20 |
| [oldmoldycake/jev_vampire_survivors](https://github.com/oldmoldycake/jev_vampire_survivors) | TypeSafe's Jev model plays Vampire Survivors on Steam: BepInEx plugin + Python brain + live decision dashboar… | 5 | Python | 2026-09-19 |
| [Peu77/JevFind](https://github.com/Peu77/JevFind) | Fast semantic code search powered by Jev. Find the relevant files, line ranges, and snippets | 5 | Rust | 2026-09-20 |
| [ponyo877/jev-telop-live](https://github.com/ponyo877/jev-telop-live) | — | 5 | JavaScript | 2026-09-19 |
| [raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury) | DiffJury — TypeSafe Jev PR risk router + code review coach | 5 | TypeScript | 2026-09-18 |
| [reallygood83/jev-router](https://github.com/reallygood83/jev-router) | — | 5 | Python | 2026-09-21 |
| [redwood-labs-ai/cambium](https://github.com/redwood-labs-ai/cambium) | — | 5 | TypeScript | 2026-09-18 |
| [ronadin2002/jev-cua](https://github.com/ronadin2002/jev-cua) | Voice and text control for macOS. One floating bar, live UI action selection with Jev, and a continuous obser… | 5 | Swift | 2026-09-22 |
| [rorz/rorz.io](https://github.com/rorz/rorz.io) | My personal website. | 5 | TypeScript | 2026-09-22 |
| [rupeshpoojary9/poorjev](https://github.com/rupeshpoojary9/poorjev) | Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.17… | 5 | Python | 2026-09-21 |
| [sametcn99/my-stars-atlas](https://github.com/sametcn99/my-stars-atlas) | A generated catalog of starred GitHub repositories, grouped into stable categories. | 5 | TypeScript | 2026-09-19 |
| [SaratAngajalaoffl/jeeva](https://github.com/SaratAngajalaoffl/jeeva) | Modular trading framework for Mid-Frequency Trading | 5 | TypeScript | 2026-09-22 |
| [Shashank-H/pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator) | A Jev based context curator for pi | 5 | TypeScript | 2026-09-21 |
| [sinhaparth5/coraza-waf-mod](https://github.com/sinhaparth5/coraza-waf-mod) | A single-binary Web Application Firewall + reverse proxy for Go, built on Coraza (OWASP CRS) with a built-in … | 5 | Go | 2026-09-21 |
| [Softtor/nestjs-hexagonal](https://github.com/Softtor/nestjs-hexagonal) | Claude Code plugin for building NestJS bounded contexts with Hexagonal Architecture, DDD, CQRS, and event-dri… | 5 | TypeScript | 2026-09-21 |
| [sugarforever/tryjev](https://github.com/sugarforever/tryjev) | Jev Playground | 5 | Svelte | 2026-09-20 |
| [topce/pizx](https://github.com/topce/pizx) | zx fork with native Pi AI — shell scripting with AI agents (π text, Π coding agent, α any ACP agent), user-de… | 5 | TypeScript | 2026-09-22 |
| [ufec/jev-block-android-ad](https://github.com/ufec/jev-block-android-ad) | JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides… | 5 | Kotlin | 2026-09-19 |
| [who/ortus](https://github.com/who/ortus) | Ortus autonomously closes a backlog of bd-tracked issues using Claude Code, ChatGPT Codex, Grok Build, or loc… | 5 | Python | 2026-09-22 |
| [y0usaf/jev-lm](https://github.com/y0usaf/jev-lm) | A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-toke… | 5 | TypeScript | 2026-09-19 |
| [yohanargentina-oss/Foq](https://github.com/yohanargentina-oss/Foq) | ⚡ Foq — the FREE, local, open-source alternative to Jev. Typed System 1 decisions in ~25 ms — no waitlist, no… | 5 | Python | 2026-09-20 |
| [yzfly/edgejev](https://github.com/yzfly/edgejev) | 离线可用的本地类型化决策：4 核 CPU 单题 15.6ms。Local & offline Jev / System One inference on CPU — ONNX + INT8, no torch at r… | 5 | Python | 2026-09-21 |
| [Adityakhalkar/JevNQL](https://github.com/Adityakhalkar/JevNQL) | — | 4 | Rust | 2026-09-20 |
| [AiPersonacademy/Awesome-jev-use](https://github.com/AiPersonacademy/Awesome-jev-use) | A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources - curated by APA (… | 4 | — | 2026-09-21 |
| [akash-kamat/system-one-gemma](https://github.com/akash-kamat/system-one-gemma) | Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decision… | 4 | Python | 2026-09-18 |
| [andrelandgraf/safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) | Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing. | 4 | TypeScript | 2026-09-18 |
| [antonpictures/ANTON-SIFTA](https://github.com/antonpictures/ANTON-SIFTA) | #SIFTA Swarm Robotics: Crypto Stigmergic Organism | 4 | Python | 2026-09-19 |
| [araray/llmcore](https://github.com/araray/llmcore) | A unified, async Python framework for LLM applications—chat, autonomous agents, RAG, and sandboxed code execu… | 4 | Python | 2026-09-21 |
| [Bald0Wang/jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh) | Jev 模型（TypeSafe AI）官方使用文档的中文翻译 \| Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — htt… | 4 | Jupyter Notebook | 2026-09-22 |
| [BenjaminG/ai-skills](https://github.com/BenjaminG/ai-skills) | — | 4 | Python | 2026-09-21 |
| [caiovicentino/jev-align](https://github.com/caiovicentino/jev-align) | Calibrated alignment verifier for LLM responses and agent plans — powered by Jev | 4 | JavaScript | 2026-09-20 |
| [chenmingtang830/jevarena](https://github.com/chenmingtang830/jevarena) | Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency. | 4 | TypeScript | 2026-09-20 |
| [christian-taillon/opencode-jev-compactor](https://github.com/christian-taillon/opencode-jev-compactor) | Jev powered OpenCode compaction | 4 | TypeScript | 2026-09-20 |
| [doeixd/jev-pref](https://github.com/doeixd/jev-pref) | Turn your AGENTS.md preferences into a fast, Jev-powered AI linter. | 4 | JavaScript | 2026-09-18 |
| [easyhaloo/afk](https://github.com/easyhaloo/afk) | — | 4 | TypeScript | 2026-09-22 |
| [FogMoe/necro](https://github.com/FogMoe/necro) | Abandoned Qwen3.5-0.8B LoRA fine-tuning experiments for Jev-like typed judgments, with datasets, adapters, ev… | 4 | Python | 2026-09-21 |
| [Gachon-Cocone-School/gcs-pulse](https://github.com/Gachon-Cocone-School/gcs-pulse) | — | 4 | Python | 2026-09-21 |
| [gokulnair2001/Convoy](https://github.com/gokulnair2001/Convoy) | Semantic end-to-end agent testing for iOS, Android, and web. | 4 | TypeScript | 2026-09-21 |
| [hallelx2/vectorless-engine](https://github.com/hallelx2/vectorless-engine) | A retrieval engine that reasons over document structure — not embeddings. No chunking, no top-K, no vector DB. | 4 | Go | 2026-09-21 |
| [harrymunro/beadsort](https://github.com/harrymunro/beadsort) | The intelligence layer for beads: typed, calibrated labels for your backlog | 4 | Python | 2026-09-18 |
| [hraness/algal](https://github.com/hraness/algal) | ALGAL is a new take on the agent graph: a language and runtime for agentic program evolution. | 4 | TypeScript | 2026-09-22 |
| [inteligenciamilgrau/jevstudio](https://github.com/inteligenciamilgrau/jevstudio) | Jev Studio para criar programas usando Jev da TypeSafe | 4 | Python | 2026-09-20 |
| [jerryxff26-alt/session-top](https://github.com/jerryxff26-alt/session-top) | Session Top — htop for AI coding sessions, making usage, quota, and token consumption observable and explaina… | 4 | Go | 2026-09-21 |
| [jkrup/jeveryword](https://github.com/jkrup/jeveryword) | Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev. | 4 | JavaScript | 2026-09-20 |
| [jon-devlapaz/tink-route](https://github.com/jon-devlapaz/tink-route) | Dynamic, confidence-aware Agent Skill routing with TypeSafe Jev and Tink | 4 | Python | 2026-09-22 |
| [Kavishann/svara](https://github.com/Kavishann/svara) | An open-source macOS app that helps blind and low-vision users browse Google Chrome with Sinhala voice comman… | 4 | JavaScript | 2026-09-19 |
| [Kelbie/hunch](https://github.com/Kelbie/hunch) | Semantic code review with Jev, plain-English rules and Agent Skills. | 4 | TypeScript | 2026-09-22 |
| [keltokhy/jlink](https://github.com/keltokhy/jlink) | Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, c… | 4 | Python | 2026-09-22 |
| [kenhuangus/jev-usecases](https://github.com/kenhuangus/jev-usecases) | Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic | 4 | Python | 2026-09-21 |
| [Kushwho/jev-codes](https://github.com/Kushwho/jev-codes) | Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI age… | 4 | TypeScript | 2026-09-19 |
| [maayanlevy/mysql-ailike](https://github.com/maayanlevy/mysql-ailike) | Natural-language row filtering for MySQL, powered by TypeSafe Jev. | 4 | C++ | 2026-09-20 |
| [maple-kit/maple](https://github.com/maple-kit/maple) | Open-source visual UX review comments on deployed previews, with a CI merge gate and an agent loop | 4 | TypeScript | 2026-09-22 |
| [maxlibin/moomoo-jev-trader](https://github.com/maxlibin/moomoo-jev-trader) | Live Moomoo trading dashboard with TypeSafe Jev market reviews | 4 | Python | 2026-09-20 |
| [mblode/taste-lint](https://github.com/mblode/taste-lint) | Catch AI slop before you ship. | 4 | TypeScript | 2026-09-21 |
| [milanboers/jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) | Playing Pokemon Red using TypeSafe Jev | 4 | Python | 2026-09-18 |
| [mkotlikov/jev-grug](https://github.com/mkotlikov/jev-grug) | Helping JEV speak <3 | 4 | TypeScript | 2026-09-18 |
| [muhammedilyasy/jev-mail](https://github.com/muhammedilyasy/jev-mail) | Chrome extension that triages Gmail with TypeSafe's Jev model: category, priority, spam % and reply % on ever… | 4 | JavaScript | 2026-09-20 |
| [nibzard/decision-model-benchmark](https://github.com/nibzard/decision-model-benchmark) | Independent, reproducible benchmark: a decision model (jev), eight constrained LLMs, and deterministic baseli… | 4 | Python | 2026-09-19 |
| [NobleSpartan6/otto](https://github.com/NobleSpartan6/otto) | Open-source native computer use for macOS and Windows: TypeSafe Jev, local OCR, and selective planning. | 4 | TypeScript | 2026-09-21 |
| [nozomi-koborinai/jev-spec](https://github.com/nozomi-koborinai/jev-spec) | ⚡ Catch spec drift on every commit: check your code against your Markdown specs with TypeSafe AI's Jev model. | 4 | TypeScript | 2026-09-21 |
| [perixtar/jev-e2e](https://github.com/perixtar/jev-e2e) | Natural-language end-to-end tests for web apps, powered by Jev and Playwright. | 4 | TypeScript | 2026-09-19 |
| [Pinutss/jev-model-router](https://github.com/Pinutss/jev-model-router) | Route among multiple LLMs and multi-model provider keys without leaking secrets. | 4 | Python | 2026-09-18 |
| [polarsen-io/padwan-ai](https://github.com/polarsen-io/padwan-ai) | Minimal, provider-agnostic Python client for large language models, built on niquests. | 4 | Python | 2026-09-21 |
| [prateekmedia/ly](https://github.com/prateekmedia/ly) | Manipulate images via chat, uses Jev like model to classify prompt | 4 | JavaScript | 2026-09-19 |
| [RahulBalakavi/claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev) | Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks | 4 | Python | 2026-09-19 |
| [rupeshpoojary9/awesome-open-system-one](https://github.com/rupeshpoojary9/awesome-open-system-one) | Curated list of the open System One ecosystem: open models, independent benchmarks, calibration and constrain… | 4 | — | 2026-09-22 |
| [season179/pi-ecosystem](https://github.com/season179/pi-ecosystem) | — | 4 | TypeScript | 2026-09-21 |
| [shamazharikh/qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd) | Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B | 4 | Python | 2026-09-17 |
| [ShuhanSun/jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel) | Catch breaking API behavior hidden in OpenAPI prose with deterministic checks and TypeSafe JEV System One sem… | 4 | Python | 2026-09-20 |
| [Stumble/jev-go](https://github.com/Stumble/jev-go) | Community Go SDK for TypeSafe AI Jev / System One | 4 | Go | 2026-09-18 |
| [takkub/agent-takkub](https://github.com/takkub/agent-takkub) | Desktop cockpit for orchestrating Claude Code dev teammates on Windows (PyQt6 + pywinpty + pyte) | 4 | Python | 2026-09-22 |
| [theodorexli/Caret](https://github.com/theodorexli/Caret) | Cursor tab-style completion in every app, aware of who you are, what you’ve been doing, and capable of using … | 4 | Swift | 2026-09-20 |
| [tonyzdev/pijev](https://github.com/tonyzdev/pijev) | PiJev: a terminal coding agent with Jev in the loop — Jev ranks the repository's files before the first call,… | 4 | TypeScript | 2026-09-20 |
| [TypeSafeAI/typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui) | shadcn-style reusable components and blocks for using TypeSafe AI. | 4 | TypeScript | 2026-09-20 |
| [Xubqpanda/JevRepo](https://github.com/Xubqpanda/JevRepo) | — | 4 | Python | 2026-09-22 |
| [y0usaf/typesafe-cli](https://github.com/y0usaf/typesafe-cli) | Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose | 4 | TypeScript | 2026-09-19 |
| [Yasserbhb/conflict-atlas](https://github.com/Yasserbhb/conflict-atlas) | An interactive world map of geopolitical conflicts, genocides, occupations and atrocities from 1490 to today.… | 4 | Python | 2026-09-21 |
| [Yeping-Hu/ai-workshop-tracker](https://github.com/Yeping-Hu/ai-workshop-tracker) | Find AI/ML/Robotics workshop deadlines and search across thousands of accepted papers, all in one place. | 4 | JavaScript | 2026-09-22 |
| [yijunyu/jev-rs](https://github.com/yijunyu/jev-rs) | System One judgments (noul/choice/score) from any LLM in one prefill — a Rust, Jev-compatible /v1/systemone e… | 4 | Rust | 2026-09-22 |
| [yqlizeao/TCER](https://github.com/yqlizeao/TCER) | Token-to-Code Efficiency Ratio | 4 | Python | 2026-09-21 |
| [zcoder-run/rust-sysone](https://github.com/zcoder-run/rust-sysone) | System One TypeSafe AI Rust Client (unofficial) | 4 | Rust | 2026-09-21 |
| [zhangxaochen/dsh-jev](https://github.com/zhangxaochen/dsh-jev) | Jev (System One decision model) plugin suite for DeepSeek Harness (dsh) | 4 | TypeScript | 2026-09-21 |
| [0x7067/jev-browse](https://github.com/0x7067/jev-browse) | Browser automation with Jev (TypeSafe) as decision model | 3 | JavaScript | 2026-09-21 |
| [0xtrou/rubikjev](https://github.com/0xtrou/rubikjev) | Challenge the Jev's intelligence in Rubik Cube puzzles | 3 | TypeScript | 2026-09-20 |
| [2456868764/jevguide](https://github.com/2456868764/jevguide) | Curated Jev showcases from X, organized by category with media previews and direct source links. | 3 | — | 2026-09-22 |
| [24601/rh-guard](https://github.com/24601/rh-guard) | Reward-hack radar for coding agents: structural denies + TypeSafe Jev System One sidecar for Claude Code & Cu… | 3 | TypeScript | 2026-09-22 |
| [a-dev/quizbun](https://github.com/a-dev/quizbun) | Quizbun is a static, explanation-first quiz catalog built around the Quiz Object Standard | 3 | TypeScript | 2026-09-21 |
| [adamnroman/slop-filter](https://github.com/adamnroman/slop-filter) | Chrome extension that hides AI-generated posts and comments on X, LinkedIn, and Reddit. Scored by TypeSafe Je… | 3 | JavaScript | 2026-09-22 |
| [alexsatch/omp-auto-mode](https://github.com/alexsatch/omp-auto-mode) | Plugin for oh-my-pi that uses Typesafe Jev API to classify tool calls as safe/unsafe/ask | 3 | TypeScript | 2026-09-19 |
| [andrelandgraf/rate-my-pricing](https://github.com/andrelandgraf/rate-my-pricing) | How confusing is that pricing page? An AI agent on Neon Functions scores pricing pages — Lighthouse, but for … | 3 | TypeScript | 2026-09-18 |
| [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) | Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducib… | 3 | Python | 2026-09-19 |
| [antiyro/jevdroid](https://github.com/antiyro/jevdroid) | A typed Python framework for controlling Android over ADB with Jev. | 3 | Python | 2026-09-19 |
| [ariel-frischer/jevkit](https://github.com/ariel-frischer/jevkit) | Fast Rust CLI for TypeSafe Jev: typed decisions, offline linting before you pay | 3 | Rust | 2026-09-19 |
| [baronunread/leanest](https://github.com/baronunread/leanest) | Local-first test selector using Jev judgments to determine which tests are affected by a code change | 3 | TypeScript | 2026-09-21 |
| [beamnxw/minelog](https://github.com/beamnxw/minelog) | MineLog harness - GPT-6 Astra plans, Jev decides, one Minecraft body. Backend behind minelog.xyz | 3 | JavaScript | 2026-09-21 |
| [benjamincanac/tia](https://github.com/benjamincanac/tia) | Triage Issue Agent for GitHub, built with Eve and Jev. | 3 | TypeScript | 2026-09-21 |
| [casungo/noflow-runtime](https://github.com/casungo/noflow-runtime) | Tired of knowing exactly what your button does? NoFlow lets buttons describe intent and picks from your regis… | 3 | TypeScript | 2026-09-19 |
| [Charlyhno-eng/jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification) | JEV Document Classification enables the rapid and cost-effective classification of text-based documents using… | 3 | TypeScript | 2026-09-19 |
| [cheeaun/jevmoji](https://github.com/cheeaun/jevmoji) | Type anything. Get related emojis scored 0–3 with Jev. | 3 | JavaScript | 2026-09-21 |
| [ChosenXu/newsletter-link-harvester](https://github.com/ChosenXu/newsletter-link-harvester) | Agent Skill: harvest links from newsletter emails into Raindrop.io with the author editorial context attached… | 3 | Python | 2026-09-20 |
| [choxos/jevchess](https://github.com/choxos/jevchess) | Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app… | 3 | JavaScript | 2026-09-20 |
| [chris-wozniczek/jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control) | Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-… | 3 | Swift | 2026-09-21 |
| [ClemensSchartmueller/jev-guard](https://github.com/ClemensSchartmueller/jev-guard) | — | 3 | Go | 2026-09-21 |
| [clusterflick/scripts](https://github.com/clusterflick/scripts) | Common scripts for managing cinema data | 3 | JavaScript | 2026-09-22 |
| [cobusgreyling/Jev](https://github.com/cobusgreyling/Jev) | Unofficial TypeSafe Jev showcase — System One decisions, not chat. | 3 | Python | 2026-09-20 |
| [codeitlikemiley/typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust) | Rust SDK for the TypeSafe AI API | 3 | Rust | 2026-09-17 |
| [collapseindex/jev-builder](https://github.com/collapseindex/jev-builder) | A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request… | 3 | JavaScript | 2026-09-20 |
| [crackalamoo/blog-demos](https://github.com/crackalamoo/blog-demos) | — | 3 | Python | 2026-09-22 |
| [dnplus/genio-one](https://github.com/dnplus/genio-one) | The control plane for every AI agent and resource | 3 | TypeScript | 2026-09-22 |
| [eachann1024/pi-jev-reply](https://github.com/eachann1024/pi-jev-reply) | Pi extension: clearer replies via Jev review + optional rewrite/visuals | 3 | TypeScript | 2026-09-20 |
| [EmreKaplaner/rag-jev](https://github.com/EmreKaplaner/rag-jev) | Make room for useful evidence. Inspectable context selection for RAG, with Jev reranking and open benchmark s… | 3 | Python | 2026-09-19 |
| [EugeneBoondock/jevsql](https://github.com/EugeneBoondock/jevsql) | SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by mea… | 3 | JavaScript | 2026-09-19 |
| [ever-just/agentskills](https://github.com/ever-just/agentskills) | Agent skills for Claude Code and other file-reading coding agents — 130+ SKILL.md procedures for deep researc… | 3 | Python | 2026-09-18 |
| [Friedjof/jev-mobile](https://github.com/Friedjof/jev-mobile) | Fast structured Android control loops with TypeSafe Jev and Mobile MCP | 3 | Python | 2026-09-18 |
| [fritzprix/systemone-lite](https://github.com/fritzprix/systemone-lite) | Toy local System One–style decision API (Jev-shaped). Not affiliated with TypeSafe. | 3 | Python | 2026-09-21 |
| [glud123/jev-assist](https://github.com/glud123/jev-assist) | Don't burn your expensive main model on grep-and-guess grunt work — let jev rank the whole repo, and save the… | 3 | JavaScript | 2026-09-22 |
| [godspede/construct-auto-classifier](https://github.com/godspede/construct-auto-classifier) | Effect-based safety gate for AI coding agents' shell commands (OpenCode, Antigravity): fast structural rules,… | 3 | TypeScript | 2026-09-19 |
| [gudcks0305/jev-java](https://github.com/gudcks0305/jev-java) | Unofficial Java SDK for TypeSafe Jev and Vercel AI Gateway, with Spring Boot and WebClient support | 3 | Java | 2026-09-21 |
| [guybrush1984/purelink](https://github.com/guybrush1984/purelink) | Chrome plugin to highlight AI generated posts | 3 | JavaScript | 2026-09-20 |
| [huonanwholovecomputer/h_n-printer](https://github.com/huonanwholovecomputer/h_n-printer) | 全自动打印，支持PDF、Word和图片类型，拥有订单和用户管理系统、支持小程序和APP远程发起打印任务，但没有提供微信支付功能，订单数据仅作为统计和数据展示。 | 3 | Python | 2026-09-22 |
| [iamvatsalpatel/tiershift](https://github.com/iamvatsalpatel/tiershift) | Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No… | 3 | TypeScript | 2026-09-21 |
| [ishantanu/jevmetrics](https://github.com/ishantanu/jevmetrics) | — | 3 | Go | 2026-09-21 |
| [ismaelsoilet/jev-harness](https://github.com/ismaelsoilet/jev-harness) | Zero-dependency System One decision harness: 5 semantic gates saving frontier AI agent tokens on trivial erro… | 3 | Python | 2026-09-22 |
| [JanOstrowka/typesafe-assist](https://github.com/JanOstrowka/typesafe-assist) | Home Assistant Assist conversation agent powered by TypeSafe's Jev (System One) model | 3 | Python | 2026-09-21 |
| [jcressler/jev-codex-token-saver](https://github.com/jcressler/jev-codex-token-saver) | Experimental Jev evidence selection for token-efficient Codex investigations | 3 | JavaScript | 2026-09-21 |
| [jeremy341/Poorup](https://github.com/jeremy341/Poorup) | Real-time multiplayer board game with an authoritative Node.js/Socket.IO server, reconnect recovery, automate… | 3 | JavaScript | 2026-09-20 |
| [jevbook/jevscan](https://github.com/jevbook/jevscan) | Typed onchain verdicts for EVM tokens: ape / watch /avoid with calibrated probabilities. CLI + library +MCP s… | 3 | JavaScript | 2026-09-19 |
| [jmanhype/jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) | Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows | 3 | Python | 2026-09-20 |
| [jtnkminimal/awesome-jev](https://github.com/jtnkminimal/awesome-jev) | A curated projects built with Jev, TypeSafe's System One model. | 3 | Python | 2026-09-21 |
| [justrach/folio](https://github.com/justrach/folio) | Architecture for Folio, a Next.js workspace for site readiness, SEO context, and agent evidence reviews. | 3 | TypeScript | 2026-09-19 |
| [jzone3/nice-chat](https://github.com/jzone3/nice-chat) | — | 3 | JavaScript | 2026-09-20 |
| [kanta13jp1/my_web_app](https://github.com/kanta13jp1/my_web_app) | — | 3 | Dart | 2026-09-22 |
| [kiendle/hophacks-2026](https://github.com/kiendle/hophacks-2026) | — | 3 | Python | 2026-09-20 |
| [kitze/pagegrade](https://github.com/kitze/pagegrade) | Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev. | 3 | TypeScript | 2026-09-18 |
| [koksalkapucuoglu/resume-enhance](https://github.com/koksalkapucuoglu/resume-enhance) | An open-source, AI-powered resume builder designed to craft high-impact resumes. Features smart content enhan… | 3 | Python | 2026-09-20 |
| [konstantinosbotonakis/codex-context-diet](https://github.com/konstantinosbotonakis/codex-context-diet) | Codex plugin: Jev-guided dieting of bulky tool results | 3 | TypeScript | 2026-09-20 |
| [kotoba-lang/typed-decisions](https://github.com/kotoba-lang/typed-decisions) | Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) o… | 3 | Python | 2026-09-21 |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | Like a garden, you reap what you sow, but mostly pull weeds. | 3 | Shell | 2026-09-22 |
| [kvnloo/z0intelligence](https://github.com/kvnloo/z0intelligence) | Can we run something like Jev on a 3090 at home? | 3 | Python | 2026-09-22 |
| [kyrylosyzonenko/jev-browse](https://github.com/kyrylosyzonenko/jev-browse) | — | 3 | JavaScript | 2026-09-17 |
| [LeanKhan/fs-pro](https://github.com/LeanKhan/fs-pro) | Football Simulator | 3 | Vue | 2026-09-21 |
| [leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) | Codex plugin: verbatim Jev-guided context restoration around session compaction. Port of tamaratran/fast-jev-… | 3 | TypeScript | 2026-09-19 |
| [Level6me/antigravity-feishu-bot](https://github.com/Level6me/antigravity-feishu-bot) | antigravity可用的飞书插件 | 3 | Python | 2026-09-21 |
| [lynellf/pi-conductor](https://github.com/lynellf/pi-conductor) | — | 3 | TypeScript | 2026-09-22 |
| [malevrigns/agent-jev](https://github.com/malevrigns/agent-jev) | AgentJev-0.6B - a fast 'System One' decision model for AI Agents: feed it any unstructured state (diffs, trac… | 3 | Python | 2026-09-22 |
| [MartinSWDev/gen-ui](https://github.com/MartinSWDev/gen-ui) | — | 3 | TypeScript | 2026-09-17 |
| [miniLV/Jev-Auto-Router](https://github.com/miniLV/Jev-Auto-Router) | Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local … | 3 | TypeScript | 2026-09-20 |
| [Mintzs/jevify](https://github.com/Mintzs/jevify) | An optimized inference engine to turn LLMs into Jev-like machines: optimized for quick, lightweight, and accu… | 3 | Python | 2026-09-19 |
| [mondaychen/semantic-assert](https://github.com/mondaychen/semantic-assert) | Testing lib for asserting the real requirement. | 3 | TypeScript | 2026-09-21 |
| [MongLong0214/jev-gate](https://github.com/MongLong0214/jev-gate) | Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prot… | 3 | TypeScript | 2026-09-21 |
| [morcoan/JMP](https://github.com/morcoan/JMP) | JMP — Joint Model Participation. A local coding workspace where Jev routes actions and OpenAI, DeepSeek, or l… | 3 | Python | 2026-09-20 |
| [mstf-svndk/jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice) | Türkçe ve İngilizce doğal konuşmayla Windows 10/11 bilgisayar kontrolü: OpenAI Realtime, local Whisper, Jev, … | 3 | JavaScript | 2026-09-20 |
| [nocoo/signoff.now](https://github.com/nocoo/signoff.now) | ✍️ Developer and Git activity analytics | 3 | TypeScript | 2026-09-21 |
| [noetion/dsh-jev](https://github.com/noetion/dsh-jev) | DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers. | 3 | TypeScript | 2026-09-18 |
| [Olti1947/jev-java](https://github.com/Olti1947/jev-java) | Idiomatic Java SDK for TypeSafe AI Jev System One decision engine | 3 | Java | 2026-09-21 |
| [open-gsd/gsd-path](https://github.com/open-gsd/gsd-path) | Disk-backed pipeline that takes AI coding agents from raw idea to shipped code — gated phases, orchestrated s… | 3 | Python | 2026-09-21 |
| [OpeOginni/oc-plugins](https://github.com/OpeOginni/oc-plugins) | — | 3 | TypeScript | 2026-09-21 |
| [ozkannceylan/rag-configurator](https://github.com/ozkannceylan/rag-configurator) | A low-code platform for building and deploying custom RAG pipelines through a visual interface. | 3 | Python | 2026-09-21 |
| [paulsmith/computer-use-jev](https://github.com/paulsmith/computer-use-jev) | macOS computer use driven by Jev (TypeSafe System One) as the decision maker | 3 | Go | 2026-09-17 |
| [prasanthj/duckdb-jev](https://github.com/prasanthj/duckdb-jev) | High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scorin… | 3 | C++ | 2026-09-21 |
| [Premo-Cloud/typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java) | Community Java client for the TypeSafe System One API (unofficial) | 3 | Java | 2026-09-21 |
| [qtnx/omppp](https://github.com/qtnx/omppp) | OMP++ | 3 | TypeScript | 2026-09-21 |
| [Ravinder82/jev-flash-router](https://github.com/Ravinder82/jev-flash-router) | open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of… | 3 | TypeScript | 2026-09-20 |
| [replynodes/jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer) | See what Jev thinks about your SaaS website — powered by ReplyNodes web context and Vercel AI Gateway. | 3 | TypeScript | 2026-09-21 |
| [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study) | Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verifi… | 3 | Python | 2026-09-17 |
| [rizafahmi/pi-jev-task-router](https://github.com/rizafahmi/pi-jev-task-router) | Per-prompt model routing for the Pi coding agent: classify each prompt with Jev, pick a model tier, and switc… | 3 | TypeScript | 2026-09-22 |
| [robertnowell/tranquility-base](https://github.com/robertnowell/tranquility-base) | Lead a team of claude code and codex agents with two keyboard keys, your voice, and your ears. | 3 | Swift | 2026-09-22 |
| [rstropek/2026-claude-classroom](https://github.com/rstropek/2026-claude-classroom) | — | 3 | TypeScript | 2026-09-22 |
| [samat2003/mini-Jev](https://github.com/samat2003/mini-Jev) | — | 3 | Python | 2026-09-21 |
| [SamuelSacco/jev-exploration](https://github.com/SamuelSacco/jev-exploration) | Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code | 3 | Python | 2026-09-21 |
| [satviksinha/jev-model-router](https://github.com/satviksinha/jev-model-router) | Model router for Claude Code using Jev | 3 | TypeScript | 2026-09-21 |
| [savka777/jev-search](https://github.com/savka777/jev-search) | Fast deep research for the pi coding agent: reads up to 100 pages in full per round, Jev keeps only the passa… | 3 | TypeScript | 2026-09-20 |
| [sd109/typesafe-go](https://github.com/sd109/typesafe-go) | A collection of typesafe.ai API utilities | 3 | Go | 2026-09-20 |
| [SeeAPI/awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases) | Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model … | 3 | Python | 2026-09-20 |
| [sgaabdu4/capture](https://github.com/sgaabdu4/capture) | Private Mac voice diary: local Parakeet transcription, Jev sorting, Notion library | 3 | Dart | 2026-09-21 |
| [skywrite/sky](https://github.com/skywrite/sky) | A plaintext, markdown-first personal operating system for continuous self-improvement | 3 | TypeScript | 2026-09-20 |
| [smithclay/dbt_jev](https://github.com/smithclay/dbt_jev) | use jev in dbt | 3 | Python | 2026-09-22 |
| [spoonnotfound/soupbase](https://github.com/spoonnotfound/soupbase) | Jev x 海龟汤 | 3 | TypeScript | 2026-09-21 |
| [sriinnu/kosha-discovery](https://github.com/sriinnu/kosha-discovery) | Discovery registry for AI models, credentials, and pricing across local and cloud providers. Library, CLI, an… | 3 | TypeScript | 2026-09-19 |
| [stardeckai/lgtm](https://github.com/stardeckai/lgtm) | Prove that your tests actually test something. Powered by Jev and your own API Key. | 3 | TypeScript | 2026-09-21 |
| [SuperInstance/AI-Writings](https://github.com/SuperInstance/AI-Writings) | Creative writing, essays, and philosophical explorations from the Exocortex project | 3 | HTML | 2026-09-22 |
| [teempai/jev-in-codex](https://github.com/teempai/jev-in-codex) | Jev-powered tool and skill selection, context search, and output triage for Codex via MCP | 3 | TypeScript | 2026-09-21 |
| [thisyearnofear/VOISSS](https://github.com/thisyearnofear/VOISSS) | next-generation decentralized voice recording platform that transforms how we capture, organize, and share au… | 3 | TypeScript | 2026-09-21 |
| [tseitz/TuneWrangler](https://github.com/tseitz/TuneWrangler) | Application to wrangle my tunes | 3 | Python | 2026-09-22 |
| [TypeSafeAI/typesafe-router](https://github.com/TypeSafeAI/typesafe-router) | Route models and tools with TypeSafe | 3 | TypeScript | 2026-09-19 |
| [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip) | YouTube sponsor skipper that reads the captions and decides at watch time: a probability heatmap on the seek … | 3 | TypeScript | 2026-09-19 |
| [valentynkit/jev.nvim](https://github.com/valentynkit/jev.nvim) | Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, pro… | 3 | Lua | 2026-09-19 |
| [virolea/jev](https://github.com/virolea/jev) | Ruby client for the typesafe AI Jev model | 3 | Ruby | 2026-09-20 |
| [wolvesdotink/owlat](https://github.com/wolvesdotink/owlat) | Self-hosted, modular email platform: marketing campaigns, team inbox, personal mailbox, and an AI agent, gate… | 3 | TypeScript | 2026-09-22 |
| [yangyu666/dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune) | Jev-judged context compaction for DeepSeek Harness: semantic tool-result pruning + deterministic receipt comp… | 3 | JavaScript | 2026-09-22 |
| [Zoverions/AXIOM-MESH](https://github.com/Zoverions/AXIOM-MESH) | AXIOM Mesh 0.12.0-dev.3: local-first, fail-closed coordination substrate for human and machine principals, wi… | 3 | JavaScript | 2026-09-22 |
| [0x7067/claude-jev](https://github.com/0x7067/claude-jev) | Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing | 2 | Python | 2026-09-22 |
| [0xtrou/yggdrasight](https://github.com/0xtrou/yggdrasight) | Inteligence crypto currency terminal | 2 | TypeScript | 2026-09-17 |
| [455-dIAO/windows-save-token-jev-setup](https://github.com/455-dIAO/windows-save-token-jev-setup) | Windows Codex Skill：通过 npx 或 Git 安装，安全配置 save-token-jev 的 PreCompact/SessionStart Hooks，并提供信任、原生压缩与旧内容隔离验证。 | 2 | PowerShell | 2026-09-21 |
| [4anti/jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab) | Testing Lab for Jev AI | 2 | JavaScript | 2026-09-20 |
| [aadhil-kh/jevx](https://github.com/aadhil-kh/jevx) | Jev-powered Chrome extension that categorizes X posts and classifies replies in context. | 2 | JavaScript | 2026-09-20 |
| [abhishekmamdapure/jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction) | Parsing the PDF and extracting the relevant information | 2 | Python | 2026-09-21 |
| [abhishekswe/agent-fastpath](https://github.com/abhishekswe/agent-fastpath) | Jev MCP server: a decision layer for coding agents, built on TypeSafe Jev (System One model). Ship gates, ris… | 2 | TypeScript | 2026-09-22 |
| [abhixhek/feedwall](https://github.com/abhixhek/feedwall) | Your feed, your rules, in plain English. A browser extension that filters X, YouTube, Reddit, LinkedIn and Ha… | 2 | JavaScript | 2026-09-19 |
| [AboveColin/jevclient](https://github.com/AboveColin/jevclient) | Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse. | 2 | Python | 2026-09-21 |
| [agent-chaperone/agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) | Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy p… | 2 | TypeScript | 2026-09-21 |
| [aibangjuxin/knowledge](https://github.com/aibangjuxin/knowledge) | My knowledge | 2 | HTML | 2026-09-21 |
| [AkashPriyadarshii/jev-git](https://github.com/AkashPriyadarshii/jev-git) | Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev | 2 | Rust | 2026-09-21 |
| [AkashPriyadarshii/jev-scout](https://github.com/AkashPriyadarshii/jev-scout) | Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring | 2 | Rust | 2026-09-21 |
| [alee792/robojev](https://github.com/alee792/robojev) | Natural-language control of a WidowX AI arm with Jev typed judgments (Doom-style loop) | 2 | Python | 2026-09-18 |
| [AmartyaKumar11/X-Ceed](https://github.com/AmartyaKumar11/X-Ceed) | An AI-Based complete Job portal for both the applicant and recruiter | 2 | JavaScript | 2026-09-22 |
| [Amrit-Nigam/jev-royal](https://github.com/Amrit-Nigam/jev-royal) | — | 2 | TypeScript | 2026-09-18 |
| [andrueandersoncs/jev-semantic-linter](https://github.com/andrueandersoncs/jev-semantic-linter) | — | 2 | TypeScript | 2026-09-18 |
| [andrueandersoncs/visual-jev](https://github.com/andrueandersoncs/visual-jev) | Image-native typed decisions with shared visual encoding and Qwen3-VL | 2 | Python | 2026-09-20 |
| [antTing/jev-accounts-hub](https://github.com/antTing/jev-accounts-hub) | A multi-account manager and API gateway for TypeSafe / Jev. 一个用于 TypeSafe / Jev 的多账户管理器和 API 网关。交流群：1102910606 | 2 | Go | 2026-09-22 |
| [AppSprout-dev/Unsga3](https://github.com/AppSprout-dev/Unsga3) | U-NSGA-III multi-objective evolutionary optimization for .NET (Seada & Deb) — ZDT/DTLZ, IGD oracle vs pymoo | 2 | C# | 2026-09-22 |
| [ARCJ137442/jev-2048](https://github.com/ARCJ137442/jev-2048) | An instrumented 2048 web lab where every move is a Jev (TypeSafe AI System One) Choice, with no heuristic fal… | 2 | TypeScript | 2026-09-21 |
| [Aryan2624/Aryan2624](https://github.com/Aryan2624/Aryan2624) | # Hi, I'm Aryan Dubey 👋 ## B.Tech AI & ML Student Building Intelligent Systems, One Model at a Time | 2 | — | 2026-09-16 |
| [Ashfaqbs/jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring) | Java/Spring Boot MCP server for TypeSafe Jev | 2 | Java | 2026-09-21 |
| [bensyverson/goodall](https://github.com/bensyverson/goodall) | A simple and extensible agent loop for Golang projects | 2 | Go | 2026-09-18 |
| [bojansandhaus/jev-decisions](https://github.com/bojansandhaus/jev-decisions) | Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evi… | 2 | Python | 2026-09-20 |
| [brainstormity/Jev-For-Dummies](https://github.com/brainstormity/Jev-For-Dummies) | — | 2 | Python | 2026-09-21 |
| [Brasth/Rig](https://github.com/Brasth/Rig) | One terminal. Codex or Grok can kick off Claude or each other. | 2 | Python | 2026-09-22 |
| [brnyxx/jev-ra](https://github.com/brnyxx/jev-ra) | Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every ste… | 2 | Python | 2026-09-22 |
| [Charlyhno-eng/jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot) | A Codex overlay incorporating JEV to make the best decisions regarding model selection and depth of reasoning… | 2 | TypeScript | 2026-09-21 |
| [chat-prompt/gpters-ai-toolkit](https://github.com/chat-prompt/gpters-ai-toolkit) | GPTers AI Toolkit - Skills, Agents, and Prompts Catalog for Claude Code | 2 | TypeScript | 2026-09-22 |
| [ChenneyZhuang/laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent) | Local, open-source Jev alternative: browser agent decisions with Laya (System One model) on your own machine.… | 2 | Python | 2026-09-22 |
| [coco-research/jev-use](https://github.com/coco-research/jev-use) | Voice-driven control layer for macOS. Jev is the fallback, not the router. Rust core, Tauri shell. | 2 | Rust | 2026-09-21 |
| [codefionn/llmleaf](https://github.com/codefionn/llmleaf) | A fast llm proxy | 2 | Rust | 2026-09-20 |
| [coo-quack/jev-pii-checker](https://github.com/coo-quack/jev-pii-checker) | CLI that finds PII in text with TypeSafe Jev: presence, sensitivity, and located spans | 2 | TypeScript | 2026-09-20 |
| [croll83/jarvis](https://github.com/croll83/jarvis) | AI driven smart home | 2 | Python | 2026-09-21 |
| [CrowdLinker/JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach) | Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improvin… | 2 | TypeScript | 2026-09-20 |
| [da-vinci-noob/pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router) | Route pi prompts to task-appropriate model tiers with TypeSafe Jev typed judgments. Budget-aware, with automa… | 2 | TypeScript | 2026-09-20 |
| [Devonance/rover-claude-jev-demo](https://github.com/Devonance/rover-claude-jev-demo) | Just a weekend project with Claude as system two, and Jev as system One. | 2 | JavaScript | 2026-09-21 |
| [Dimesio/typesafe-chess](https://github.com/Dimesio/typesafe-chess) | FUn little experiment with Typesafe AI Jev Model playing chess against stockfish :) | 2 | JavaScript | 2026-09-20 |
| [DreamBlooms/dohnuts.cpp](https://github.com/DreamBlooms/dohnuts.cpp) | The same decisions, on CPU. System One model that can run on your Personal Computer. | 2 | C++ | 2026-09-22 |
| [drewling/zero](https://github.com/drewling/zero) | Keep every Gmail inbox at only what still needs you — reversibly. A macOS menu-bar app: agent-judged open loo… | 2 | Python | 2026-09-22 |
| [droid-Q/jev-skill-router](https://github.com/droid-Q/jev-skill-router) | — | 2 | JavaScript | 2026-09-19 |
| [dwamianm/prism](https://github.com/dwamianm/prism) | Portable Relational Memory Engine — local-first memory substrate for LLM-powered systems | 2 | Python | 2026-09-19 |
| [Eliran-Turgeman/reaper](https://github.com/Eliran-Turgeman/reaper) | Semantic linter for AI coding agents and CI code review. Detects silent failures, weakened tests, scope creep… | 2 | Go | 2026-09-21 |
| [elpumberto/barrunto](https://github.com/elpumberto/barrunto) | A Chrome extension that brings TypeSafe's Jev to X.com to analyze posts as you browse | 2 | TypeScript | 2026-09-20 |
| [Embodied-AI-System/Qwen3.5-OneForward](https://github.com/Embodied-AI-System/Qwen3.5-OneForward) | Jev-style typed decisions from Qwen3.5-2B logits — one forward pass, zero decoding, zero fine-tuning. | 2 | Python | 2026-09-22 |
| [embwl0x/native-agent](https://github.com/embwl0x/native-agent) | A Swift-native macOS and iOS personal agent runtime. | 2 | Swift | 2026-09-20 |
| [enovikov11/tigor-ai](https://github.com/enovikov11/tigor-ai) | Personal AI monorepo | 2 | Jupyter Notebook | 2026-09-22 |
| [etweisberg/jev-ui](https://github.com/etweisberg/jev-ui) | React components that resolve which component to render, how to order a list, and whether to show an affordan… | 2 | TypeScript | 2026-09-21 |
| [evanzyang91/jevis](https://github.com/evanzyang91/jevis) | — | 2 | Python | 2026-09-20 |
| [ferraroroberto/local-llm-hub](https://github.com/ferraroroberto/local-llm-hub) | playground to use different local LLM models as a API hub | 2 | Python | 2026-09-22 |
| [FindMalek/guesswork](https://github.com/FindMalek/guesswork) | Fish-style zsh history autosuggestions, ranked by an AI model instead of prefix matching | 2 | TypeScript | 2026-09-21 |
| [FirasSX914/Janus](https://github.com/FirasSX914/Janus) | Measure when to use Jev and other models on your data, then route accordingly. | 2 | Python | 2026-09-18 |
| [gaborishka/jevtown](https://github.com/gaborishka/jevtown) | Jevtown: a social network where people write and 10,000 AI personas react | 2 | JavaScript | 2026-09-22 |
| [geocine/geocine-pi](https://github.com/geocine/geocine-pi) | Local-first control layer for Pi. TypeSafe routes tasks, manages cache-aware model leases, gates bounded spec… | 2 | TypeScript | 2026-09-18 |
| [geofffranks/polytoken-quota](https://github.com/geofffranks/polytoken-quota) | — | 2 | Go | 2026-09-20 |
| [gholtzap/jev-codex-model-and-effort-router](https://github.com/gholtzap/jev-codex-model-and-effort-router) | — | 2 | Python | 2026-09-22 |
| [glamboyosa/docket](https://github.com/glamboyosa/docket) | A Go TUI that uses Jev to classify documents, assess sensitivity and urgency, and determine whether action is… | 2 | Go | 2026-09-20 |
| [govindup63/skillpick](https://github.com/govindup63/skillpick) | Pick the right agent skill for every prompt with TypeSafe's Jev. Hooks for Claude Code, Codex, Gemini CLI, Dr… | 2 | TypeScript | 2026-09-20 |
| [guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector) | Conservative CI task selection for GitHub Actions with Jev, a pure policy engine, and shadow mode by default. | 2 | TypeScript | 2026-09-21 |
| [h3y6e/blog](https://github.com/h3y6e/blog) | my blog | 2 | TypeScript | 2026-09-22 |
| [hamakyo/jev-starter](https://github.com/hamakyo/jev-starter) | Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation,… | 2 | TypeScript | 2026-09-18 |
| [Hand-In/openjev-multimodal](https://github.com/Hand-In/openjev-multimodal) | Local multimodal decisions on your Mac. Jev-compatible typed probabilities with Qwen, llama.cpp and Metal. | 2 | Python | 2026-09-22 |
| [Hawxy/TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) | .NET SDK for the TypeSafe AI platform | 2 | C# | 2026-09-19 |
| [hellogumbo/should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all) | We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actua… | 2 | JavaScript | 2026-09-18 |
| [hemanth/jev-chess](https://github.com/hemanth/jev-chess) | Chess moves, evaluations, persona opponents, and game classification with TypeSafe AI System One | 2 | TypeScript | 2026-09-21 |
| [IAnMove/jev-game-agent](https://github.com/IAnMove/jev-game-agent) | Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your o… | 2 | Python | 2026-09-18 |
| [ibrahemid/git-jev-stage](https://github.com/ibrahemid/git-jev-stage) | Select Git changes for staging with a plain-language description. | 2 | TypeScript | 2026-09-20 |
| [ibrahemid/jevprune](https://github.com/ibrahemid/jevprune) | Filter command output for coding agents using a task description. | 2 | TypeScript | 2026-09-20 |
| [iii-hq/harness-e2e](https://github.com/iii-hq/harness-e2e) | Longitudinal capability and complexity E2E system for Harness | 2 | Rust | 2026-09-22 |
| [imrishit98/jev.aitools.fyi](https://github.com/imrishit98/jev.aitools.fyi) | Jev is all the rage right now and this directory lists all things Jev! Docs, SDKs, and the full tool map one … | 2 | TypeScript | 2026-09-22 |
| [innocentdiaz/s1_ruby](https://github.com/innocentdiaz/s1_ruby) | Makes S1-model 'measurement' (and the collapse that follows it) a Ruby primitive. | 2 | Ruby | 2026-09-21 |
| [Intellinfinity/edupi-desktop](https://github.com/Intellinfinity/edupi-desktop) | EduPi teacher agent desktop | 2 | TypeScript | 2026-09-22 |
| [ItisShikhar/gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez) | Fast, drop-in profanity and toxicity screener for Node.js, powered by TypeSafe AI Jev. Catches leetspeak, cha… | 2 | TypeScript | 2026-09-22 |
| [jb2197/pydantic-jev](https://github.com/jb2197/pydantic-jev) | A thin shim between Pydantic and Jev. | 2 | Python | 2026-09-18 |
| [jev-ids/jev-ids](https://github.com/jev-ids/jev-ids) | Blazing-Fast Token-Efficient Intrusion Detection System (IDS) based on TypeSafe's Jev | 2 | Python | 2026-09-22 |
| [jexp/watfile](https://github.com/jexp/watfile) | Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model | 2 | Python | 2026-09-21 |
| [JGalbss/cod4-macos](https://github.com/JGalbss/cod4-macos) | Native Apple Silicon Call of Duty 4 multiplayer client | 2 | C++ | 2026-09-22 |
| [jiangkoumo/ego-jev](https://github.com/jiangkoumo/ego-jev) | Drive the ego lite browser with Jev (TypeSafe System One): one indexed element table in, one operation + targ… | 2 | JavaScript | 2026-09-22 |
| [jimmyliao/jev-storyboard-lab](https://github.com/jimmyliao/jev-storyboard-lab) | Google ADK vs Microsoft Agent Framework for structured-output agents, with TypeSafe Jev as a vendor-neutral Q… | 2 | Python | 2026-09-22 |
| [jorgeasaurus/EndpointJobs](https://github.com/jorgeasaurus/EndpointJobs) | Focused job board for Endpoint Engineering, macOS, Windows, MDM, UEM, client platform, and endpoint security … | 2 | TypeScript | 2026-09-22 |
| [jsagir/mindrian-os-plugin](https://github.com/jsagir/mindrian-os-plugin) | The AI co-founder that pushes back. Bring a real problem worth solving and it reframes what you are actually … | 2 | JavaScript | 2026-09-17 |
| [jtsang4/jev-cli](https://github.com/jtsang4/jev-cli) | CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out | 2 | TypeScript | 2026-09-18 |
| [Justmalhar/awesome-jev-apps](https://github.com/Justmalhar/awesome-jev-apps) | Awesome Collection of apps built with Jev - a System One model | 2 | Python | 2026-09-19 |
| [jzhg6/jev-embodied-media-agent](https://github.com/jzhg6/jev-embodied-media-agent) | Jev-based local-first gesture and gaze media-control agent with guarded page-close intent. | 2 | TypeScript | 2026-09-20 |
| [KamilPostrozny/pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction) | Fast JEV compaction extension for pi | 2 | TypeScript | 2026-09-20 |
| [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) | Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation. | 2 | JavaScript | 2026-09-19 |
| [kbitgood/jev-cdp](https://github.com/kbitgood/jev-cdp) | A small Jev-powered bridge to Chrome through the Chrome DevTools Protocol. | 2 | TypeScript | 2026-09-18 |
| [kcc989/keeled](https://github.com/kcc989/keeled) | — | 2 | TypeScript | 2026-09-22 |
| [kindintelligence/jev-rust-review](https://github.com/kindintelligence/jev-rust-review) | Rust-aware code review for Claude Code and coding agents, powered by TypeSafe Jev | 2 | Rust | 2026-09-20 |
| [krimvp/goaly](https://github.com/krimvp/goaly) | Deterministic goal cli for your harness | 2 | TypeScript | 2026-09-17 |
| [KsanaDock/verdict-lab](https://github.com/KsanaDock/verdict-lab) | An experiment comparing the capabilities and costs of the JEV model and LLM models in the field of content mo… | 2 | Python | 2026-09-20 |
| [kuhung/understanding-jev](https://github.com/kuhung/understanding-jev) | 深入解读 Jev 模型：毫秒级判定与工程边界 | 2 | HTML | 2026-09-22 |
| [lgy1027/jevshield](https://github.com/lgy1027/jevshield) | Sub-100ms security gate for AI agent tool calls, powered by TypeSafe's Jev (System-1) decision model. Single-… | 2 | Python | 2026-09-22 |
| [liao96312/jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev) | 完全本地的 NanoJev 网格决策游戏实验场，支持中文 Pygame、多关卡与 GTX 1660S 训练 | 2 | Python | 2026-09-22 |
| [lithdew/hands](https://github.com/lithdew/hands) | General Learning Hacks 2026 (1st place) | 2 | TypeScript | 2026-09-21 |
| [lmvdz/rpg-jev](https://github.com/lmvdz/rpg-jev) | A living-world RPG whose NPCs are decided by TypeSafe's Jev judge model; code owns rules, numbers and state. | 2 | TypeScript | 2026-09-21 |
| [LonelyFellas/jev-codex-cua](https://github.com/LonelyFellas/jev-codex-cua) | — | 2 | TypeScript | 2026-09-22 |
| [luxus/ha-conversation-jev](https://github.com/luxus/ha-conversation-jev) | Home Assistant custom component: Conversation agent with Jev fast-path + Grok fallback | 2 | Python | 2026-09-19 |
| [Mani212005/aideos](https://github.com/Mani212005/aideos) | Explainer video as data one canvas, one camera, two aspect ratios. Built with Remotion. | 2 | TypeScript | 2026-09-21 |
| [maruthiprithivi/break-free](https://github.com/maruthiprithivi/break-free) | — | 2 | TypeScript | 2026-09-21 |
| [masa-med-ai/typesafe-screening-mcp](https://github.com/masa-med-ai/typesafe-screening-mcp) | MCP server: screen PubMed titles/abstracts against a query or clinical question with TypeSafe Jev | 2 | Python | 2026-09-19 |
| [mastwet/dsh-fast-jev-compaction](https://github.com/mastwet/dsh-fast-jev-compaction) | fast-jev-compaction dsh插件 | 2 | JavaScript | 2026-09-20 |
| [MatheusLarcher/agent-code](https://github.com/MatheusLarcher/agent-code) | — | 2 | TypeScript | 2026-09-22 |
| [MaTriXy/Monkey.D.Loopy](https://github.com/MaTriXy/Monkey.D.Loopy) | Factory for runnable, crash-resumable agent loops. | 2 | TypeScript | 2026-09-17 |
| [memovai/openevals](https://github.com/memovai/openevals) | Fast and cheap agent evals. jev as judge. | 2 | TypeScript | 2026-09-20 |
| [merefield/clai](https://github.com/merefield/clai) | A command line ai helper | 2 | Go | 2026-09-20 |
| [mjdileep/OpenJev](https://github.com/mjdileep/OpenJev) | OpenJev | 2 | HTML | 2026-09-22 |
| [molis-ai/jev-workbench](https://github.com/molis-ai/jev-workbench) | Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your bac… | 2 | TypeScript | 2026-09-18 |
| [Mrlyk/jev-browser](https://github.com/Mrlyk/jev-browser) | Browser automation CLI for AI agents, powered by the Jev model's millisecond decisions and near-zero inferenc… | 2 | Rust | 2026-09-21 |
| [n3ndor/n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev) | n8n community node for TypeSafe Jev structured AI decisions | 2 | TypeScript | 2026-09-19 |
| [Nachom3/jevTrader](https://github.com/Nachom3/jevTrader) | A High Frecuncy Trader made in Rust using Jev as a decision maker. | 2 | Rust | 2026-09-20 |
| [Nainish-Rai/jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa) | Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo. | 2 | Python | 2026-09-18 |
| [NAlexPear/scruple](https://github.com/NAlexPear/scruple) | Semantic-aware linting for enforcing taste | 2 | TypeScript | 2026-09-21 |
| [newuser7171/antivirus](https://github.com/newuser7171/antivirus) | — | 2 | Python | 2026-09-20 |
| [newuser7171/jev-gamepilot](https://github.com/newuser7171/jev-gamepilot) | — | 2 | Python | 2026-09-21 |
| [nexibeo/jev-browser-control](https://github.com/nexibeo/jev-browser-control) | Let Claude code, chatgpt codex or control your own Chrome. Chrome extension + MCP server: Jev, TypeSafe's dec… | 2 | JavaScript | 2026-09-21 |
| [noripto/pigeonhole](https://github.com/noripto/pigeonhole) | Classify notes with Jev and file them into folders by attribute. | 2 | TypeScript | 2026-09-21 |
| [nourhelmi/pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction) | Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals wit… | 2 | TypeScript | 2026-09-21 |
| [nshkrdotcom/system_one_sdk](https://github.com/nshkrdotcom/system_one_sdk) | Provider-neutral Elixir/BEAM SDK for System One semantics: typed Noul, Choice and Score decisions, prepared e… | 2 | Elixir | 2026-09-21 |
| [obetomuniz/auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo) | A Paseo provider that uses TypeSafe Jev to route each Codex turn. | 2 | TypeScript | 2026-09-22 |
| [omkarghugarkar007/actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev) | Open-source Jev tool-calling authorization gateway for AI agents: deterministic policy, exact-action single-u… | 2 | TypeScript | 2026-09-20 |
| [overfit-lab/OpenJev](https://github.com/overfit-lab/OpenJev) | — | 2 | Python | 2026-09-20 |
| [oxwen11/awesome-jev](https://github.com/oxwen11/awesome-jev) | A curated list of what people built with Jev | 2 | — | 2026-09-21 |
| [pCwOrM/werr](https://github.com/pCwOrM/werr) | Zero-memory System-1 decision engine & TypeSafe Jev wire-compatible runtime powered by Mandelbrot wave dynami… | 2 | Python | 2026-09-21 |
| [phureewat29/jev-got](https://github.com/phureewat29/jev-got) | Jev (TypeSafe AI) PoC through Game of Thrones | 2 | TypeScript | 2026-09-19 |
| [phyous/tsai-civ2](https://github.com/phyous/tsai-civ2) | TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-g… | 2 | Python | 2026-09-18 |
| [PingpowerTW/7-Phase-Agentic-Workflow](https://github.com/PingpowerTW/7-Phase-Agentic-Workflow) | 「整合 Spec-Driven Development 與 Karpathy 的精準開刀原則，建立完整的 Phase 0-6 協作架構。並導入 Rule #8 Token 經濟學，結合 /teamwork 多代理人品質… | 2 | Python | 2026-09-20 |
| [pokertools-arena/pokertools-arena.github.io](https://github.com/pokertools-arena/pokertools-arena.github.io) | A browser-first AI poker benchmark. Seat Jev and OpenAI-compatible models at the same no-limit Texas Hold'em … | 2 | JavaScript | 2026-09-21 |
| [Programalyst/realtime-vision-decision-agent](https://github.com/Programalyst/realtime-vision-decision-agent) | Combining YOLO and Jev models to play a mobile game. | 2 | Jupyter Notebook | 2026-09-21 |
| [pulkitxm/jev-chess-agent](https://github.com/pulkitxm/jev-chess-agent) | A chess bot opponent player with typed move selection and browser controls | 2 | JavaScript | 2026-09-20 |
| [r4ai/laya-web](https://github.com/r4ai/laya-web) | Laya typed decisions in the browser with ONNX Runtime WebGPU and Wasm | 2 | TypeScript | 2026-09-21 |
| [Ramneet-Singh/jevopt](https://github.com/Ramneet-Singh/jevopt) | Making intelligent compiler optimisation decisions with Jev | 2 | Python | 2026-09-21 |
| [RevocGG/typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge) | Use the TypeSafe Jev decision model (System One) anywhere: zero-dependency OpenAI-compatible bridge for 9Rout… | 2 | JavaScript | 2026-09-21 |
| [revsmoke/promptrejectormcp](https://github.com/revsmoke/promptrejectormcp) | Open-source MCP and HTTPS screening for prompts, skills, and tool descriptions using TypeSafe AI Jev, determi… | 2 | TypeScript | 2026-09-21 |
| [rikkooo/jev-trade](https://github.com/rikkooo/jev-trade) | A market-data trading simulator powered by auditable Jev judgments | 2 | TypeScript | 2026-09-20 |
| [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) | Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Cod… | 2 | TypeScript | 2026-09-20 |
| [rivendale/hsi-operator](https://github.com/rivendale/hsi-operator) | Keep a human at the strategic level of agent work: surface only what needs a person, and establish what 'done… | 2 | Python | 2026-09-22 |
| [Roberdan/roberdan-os](https://github.com/Roberdan/roberdan-os) | Copilot CLI-first workflows for AI agents: shared instructions, reusable skills, multi-model delegation, huma… | 2 | Shell | 2026-09-20 |
| [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) | A curated list of resources for Jev — TypeSafe AI's System One decision model. Maintained by RoboKrunch. | 2 | — | 2026-09-22 |
| [rorshopping/jev-browser-local](https://github.com/rorshopping/jev-browser-local) | Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, mea… | 2 | Python | 2026-09-19 |
| [ruban-24/switchboard](https://github.com/ruban-24/switchboard) | An open-source, model-agnostic decision router for Claude Code and Codex. | 2 | TypeScript | 2026-09-21 |
| [Saik0s/diffusiongemma-jev-macos](https://github.com/Saik0s/diffusiongemma-jev-macos) | Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples. | 2 | Python | 2026-09-19 |
| [sanjayarun07/orbit](https://github.com/sanjayarun07/orbit) | — | 2 | Python | 2026-09-22 |
| [SecurityMindedSolutions/ai-skills](https://github.com/SecurityMindedSolutions/ai-skills) | Skills that let a coding agent do real work on a codebase: auditing, vulnerability remediation, and unattende… | 2 | Python | 2026-09-20 |
| [ShahriarBijoy/eslint-plugin-jev](https://github.com/ShahriarBijoy/eslint-plugin-jev) | Today's linters read the shape of your code. This one would read what it means. | 2 | TypeScript | 2026-09-20 |
| [sifrious/molly](https://github.com/sifrious/molly) | Local AI coding tasks for Laravel, with Pest verification and visible complexity review. | 2 | PHP | 2026-09-22 |
| [sightmap/jev-turbo](https://github.com/sightmap/jev-turbo) | Jev-powered semantic browser use | 2 | Go | 2026-09-20 |
| [simota/tenbin](https://github.com/simota/tenbin) | MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score… | 2 | TypeScript | 2026-09-21 |
| [simxnherrera/jevr](https://github.com/simxnherrera/jevr) | A native R client for Jev System 1 model decisions | 2 | R | 2026-09-20 |
| [Skyvern-AI/destroy-email-spam](https://github.com/Skyvern-AI/destroy-email-spam) | Gmail triage with Jev: flag urgent mail and archive cold pitches using Google Apps Script. | 2 | JavaScript | 2026-09-19 |
| [SomeshSampat2/jev-android-super](https://github.com/SomeshSampat2/jev-android-super) | — | 2 | Kotlin | 2026-09-22 |
| [SoundBlaster/Jev4Mellea](https://github.com/SoundBlaster/Jev4Mellea) | Jev adapter for Mellea | 2 | Python | 2026-09-21 |
| [sseanliu/Jev-Vision](https://github.com/sseanliu/Jev-Vision) | Open-weight step verifier for computer-use agents: calibrated ground/skip/effect/done judgments from screensh… | 2 | Python | 2026-09-21 |
| [stanprokopenko/skell-e-router](https://github.com/stanprokopenko/skell-e-router) | Simple AI router using LiteLLM. | 2 | Python | 2026-09-21 |
| [superradcompany/multiverse-of-madness](https://github.com/superradcompany/multiverse-of-madness) | Jev and Microsandbox explore alternate game futures with a reusable TypeScript learning harness | 2 | TypeScript | 2026-09-19 |
| [tanayvasishtha/Slither-Me-Jev](https://github.com/tanayvasishtha/Slither-Me-Jev) | 8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time | 2 | JavaScript | 2026-09-20 |
| [tangle-network/agent-eval](https://github.com/tangle-network/agent-eval) | Evaluate and improve AI agents from the data they produce. | 2 | TypeScript | 2026-09-20 |
| [TheOnlyArtz/TheOnlyArtz.github.io](https://github.com/TheOnlyArtz/TheOnlyArtz.github.io) | ג'ב — יועצת בחירת מפלגה. Hebrew/RTL React app ranking the 14 Knesset-26 lists against your ideology. | 2 | JavaScript | 2026-09-18 |
| [tu11aa/squadrant](https://github.com/tu11aa/squadrant) | Multi-project agent orchestration for Claude Code. One command session controls everything. | 2 | TypeScript | 2026-09-22 |
| [tylerjharden/ailerix](https://github.com/tylerjharden/ailerix) | Type-safe model router. Jev (System One) banks each request to a typed catalog route. | 2 | TypeScript | 2026-09-20 |
| [typakon4/jev-layer](https://github.com/typakon4/jev-layer) | Portable System-1 decision layer for agent harnesses with host-owned routing, receipts, replay, and fail-open… | 2 | JavaScript | 2026-09-21 |
| [TypeSafeAI/clarity-judge](https://github.com/TypeSafeAI/clarity-judge) | Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its o… | 2 | TypeScript | 2026-09-21 |
| [undeemed/Jcyber](https://github.com/undeemed/Jcyber) | Agent-driven bug bounty / pentest framework: one gated chain over five systems (Caido, HexStrike, Jev, Memgra… | 2 | Python | 2026-09-21 |
| [unownone/jevsume](https://github.com/unownone/jevsume) | ATS-friendly resume review powered by Jev (TypeSafe System One). The frontend extracts resume text the way a … | 2 | TypeScript | 2026-09-21 |
| [VakeDomen/DIY-Jev](https://github.com/VakeDomen/DIY-Jev) | — | 2 | Rust | 2026-09-21 |
| [vieitesss/dotfiles](https://github.com/vieitesss/dotfiles) | Simple dotfiles. Work on my machine. Configuration files and agent skills. UNIX only. Just a script and symli… | 2 | Shell | 2026-09-20 |
| [VladyslavHontar/clear-head](https://github.com/VladyslavHontar/clear-head) | Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using … | 2 | Python | 2026-09-19 |
| [Waxmell114514/jev-compaction](https://github.com/Waxmell114514/jev-compaction) | A context compactor that can only score, never write — so an agent's memory can't hold a fact the transcript … | 2 | Python | 2026-09-22 |
| [wodsmith/thewodapp](https://github.com/wodsmith/thewodapp) | — | 2 | TypeScript | 2026-09-21 |
| [wyattjoh/skills](https://github.com/wyattjoh/skills) | A curated public collection of reusable Agent Skills and Claude Code agents for software development workflow… | 2 | TypeScript | 2026-09-22 |
| [XyraSinclair/llmsort](https://github.com/XyraSinclair/llmsort) | Score a list by any fuzzy attribute with an LLM judge: pairwise ratio questions fitted into consistent scores… | 2 | Rust | 2026-09-22 |
| [y9Finsi/jev-mcp](https://github.com/y9Finsi/jev-mcp) | — | 2 | JavaScript | 2026-09-21 |
| [zdenham/jev-lint](https://github.com/zdenham/jev-lint) | Lint JavaScript and TypeScript against plain-English project conventions with Jev. | 2 | TypeScript | 2026-09-20 |
| [zkjoie/jevbus](https://github.com/zkjoie/jevbus) | A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The r… | 2 | Rust | 2026-09-21 |
| [1cyberlangke1/minicpm-jev-like](https://github.com/1cyberlangke1/minicpm-jev-like) | 只是取输出首 token 的 logits | 1 | Python | 2026-09-22 |
| [207studio/jev-codex-tools](https://github.com/207studio/jev-codex-tools) | Experimental opt-in Jev decision tools for bounded Codex session reading and guarded UI workflows. | 1 | JavaScript | 2026-09-20 |
| [4esv/jev-eval](https://github.com/4esv/jev-eval) | Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calib… | 1 | Python | 2026-09-21 |
| [a-Fig/jev-score](https://github.com/a-Fig/jev-score) | Local-first document evaluation workspaces powered by Jev | 1 | JavaScript | 2026-09-21 |
| [AbsoluteGeist/code-geist](https://github.com/AbsoluteGeist/code-geist) | An experimental local coding-agent workbench using Jev for model routing, with tool execution and verificatio… | 1 | TypeScript | 2026-09-22 |
| [acoyfellow/nightglass](https://github.com/acoyfellow/nightglass) | Owned, deterministic classifier for checking whether agent claims are supported by evidence, with optional Je… | 1 | JavaScript | 2026-09-19 |
| [Acurioustractor/grantscope](https://github.com/Acurioustractor/grantscope) | Open-source Australian funding transparency platform — government grants, philanthropic foundations, corporat… | 1 | TypeScript | 2026-09-22 |
| [adammichaelwood/jev-music-theory-1](https://github.com/adammichaelwood/jev-music-theory-1) | — | 1 | TypeScript | 2026-09-18 |
| [Adrian-lzr/jev-spire-brain](https://github.com/Adrian-lzr/jev-spire-brain) | — | 1 | Python | 2026-09-22 |
| [ady95/jev_tutorial](https://github.com/ady95/jev_tutorial) | — | 1 | Python | 2026-09-21 |
| [afurm/typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby) | Unofficial Ruby SDK for the TypeSafe AI API (Jev model) - typed questions, retries, and typed errors. Communi… | 1 | Ruby | 2026-09-21 |
| [Ai-trainee/awesome-jev](https://github.com/Ai-trainee/awesome-jev) | — | 1 | — | 2026-09-22 |
| [ajanm007/jevrag](https://github.com/ajanm007/jevrag) | A pluggable decision substrate for RAG pipelines; explicit, calibrated state → Decision → confidence → action… | 1 | Python | 2026-09-21 |
| [ajayk/jev-go-sdk](https://github.com/ajayk/jev-go-sdk) | Dependency-free Go client for TypeSafe AI's System One API and the Jev model | 1 | Go | 2026-09-21 |
| [ajmeese7/hdd-analyzer](https://github.com/ajmeese7/hdd-analyzer) | Use Jev to quickly search your old hard drives and identify anything of value. | 1 | Python | 2026-09-21 |
| [albri/nxk](https://github.com/albri/nxk) | Your agent can't ask people what they think. nxk gives it a crowd to ask. | 1 | JavaScript | 2026-09-21 |
| [AleksaZCodes/fiducial](https://github.com/AleksaZCodes/fiducial) | Declare each fact once. Derive every artifact from it. | 1 | Rust | 2026-09-21 |
| [Alex314618-create/JevRev](https://github.com/Alex314618-create/JevRev) | Think 100. Run 5. Ship 1. | 1 | TypeScript | 2026-09-22 |
| [alexkarpandrus/tickettrain](https://github.com/alexkarpandrus/tickettrain) | Provider-neutral ticket tool (ttt) linking change requests to tracker issues | 1 | Clojure | 2026-09-22 |
| [alitrack/jev-clone](https://github.com/alitrack/jev-clone) | Local, contract-compatible System One decision server (typed questions -> calibrated probabilities, zero gene… | 1 | Rust | 2026-09-22 |
| [alperenerol/jev-1.13-mini-benchmark](https://github.com/alperenerol/jev-1.13-mini-benchmark) | Mini benchmark of TypeSafe's jev-1.13 structured decision model (OpenRouter Decisions API) on labeled support… | 1 | Python | 2026-09-21 |
| [alsoleg89/decide](https://github.com/alsoleg89/decide) | Bulk decisions for AI agents. Jev classifies files and logs; your agent reviews exceptions. Reproducible cost… | 1 | Python | 2026-09-20 |
| [Amal-David/awesome-jev](https://github.com/Amal-David/awesome-jev) | — | 1 | Python | 2026-09-22 |
| [amishah1998/said-done](https://github.com/amishah1998/said-done) | Report card for your AI coding agent: grades every Claude Code session on disk with Jev, cheaply | 1 | JavaScript | 2026-09-20 |
| [anderescaray/every-hackspain](https://github.com/anderescaray/every-hackspain) | Score de salud financiera explicable con trayectoria, Cash Truth y optimizador de tesorería para grupos empre… | 1 | Python | 2026-09-20 |
| [andragon3110/laya-mcp](https://github.com/andragon3110/laya-mcp) | MCP server exposing Laya's typed-decision tools to coding agents. Optional, self-hosted, 7x faster than Jev. | 1 | Python | 2026-09-21 |
| [andrei10k/claude-jev-model-router](https://github.com/andrei10k/claude-jev-model-router) | A local proxy that sits between Claude Code and the Anthropic API and uses TypeSafe's Jev to route each subag… | 1 | TypeScript | 2026-09-21 |
| [andyhorn/jev](https://github.com/andyhorn/jev) | — | 1 | Dart | 2026-09-21 |
| [andyrewlee/awesome-system-one](https://github.com/andyrewlee/awesome-system-one) | Curated list of tools related to system one models | 1 | — | 2026-09-21 |
| [antoniofulg/jev-parser](https://github.com/antoniofulg/jev-parser) | Experimental bounded semantic verbalizer for Jev judgments: SRR, protected values, compact-model training, an… | 1 | Python | 2026-09-20 |
| [aoprisan/typesafe-ai-rust-sdk](https://github.com/aoprisan/typesafe-ai-rust-sdk) | — | 1 | Rust | 2026-09-21 |
| [aranlucas/ai-shopping-mcp](https://github.com/aranlucas/ai-shopping-mcp) | Kroger MCP server | 1 | TypeScript | 2026-09-19 |
| [Arasz/pi-badger-integration](https://github.com/Arasz/pi-badger-integration) | Canonical pi coding-agent extensions (subagent, monitor, router-fallback, cron, MCP tools) with publish flow … | 1 | HTML | 2026-09-21 |
| [auggie246/dsh-jev](https://github.com/auggie246/dsh-jev) | Jev integration to Deepseek harness | 1 | JavaScript | 2026-09-20 |
| [avgon/jev-seo-geo](https://github.com/avgon/jev-seo-geo) | AI visibility toolkit. Measure and optimize how AI models see your brand. GEO (Generative Engine Optimization… | 1 | Python | 2026-09-21 |
| [avshalomd/longjev](https://github.com/avshalomd/longjev) | Long inputs for TypeSafe AI's Jev decision model. An experiment. | 1 | Python | 2026-09-19 |
| [az9713/jev-model-router](https://github.com/az9713/jev-model-router) | Jev (TypeSafe) model router on the Vercel AI Gateway | 1 | JavaScript | 2026-09-20 |
| [azterizm/jev-vs-sovereign-benchmark](https://github.com/azterizm/jev-vs-sovereign-benchmark) | — | 1 | Python | 2026-09-22 |
| [Barneyjm/circuit](https://github.com/Barneyjm/circuit) | Open-weights System One models (text, images, audio) and the harness that trains and measures them: LoRA plus… | 1 | Python | 2026-09-22 |
| [Barneyjm/decision-circuits](https://github.com/Barneyjm/decision-circuits) | Decision circuits: typed questions to a System One model, calibrated probabilities back, gates in code. Zero-… | 1 | Python | 2026-09-21 |
| [bchaney/jev_speedway](https://github.com/bchaney/jev_speedway) | Uses jev to control race cars on a virtual track | 1 | JavaScript | 2026-09-19 |
| [beto11-gif/jev-trading-backend](https://github.com/beto11-gif/jev-trading-backend) | — | 1 | TypeScript | 2026-09-19 |
| [bgrablin/hermes-switchyard](https://github.com/bgrablin/hermes-switchyard) | Jev-powered decision plugin for Hermes Agent: automatic skill selection, policy-constrained model routing, ty… | 1 | Python | 2026-09-22 |
| [binnash/typesafe-sdk](https://github.com/binnash/typesafe-sdk) | PHP & Laravel SDK for TypeSafe AI's JEV Model series | 1 | PHP | 2026-09-18 |
| [bitomule/jevi](https://github.com/bitomule/jevi) | Ask typed questions about a text and branch on the answer. A shell front end for TypeSafe's Jev. | 1 | Rust | 2026-09-21 |
| [bmccarn/tracecheck](https://github.com/bmccarn/tracecheck) | Evidence-backed code review for AI coding agents, powered by Jev. | 1 | TypeScript | 2026-09-18 |
| [BoxPistols/dev-album](https://github.com/BoxPistols/dev-album) | — | 1 | TypeScript | 2026-09-21 |
| [Bthornton1994/Manipulation-score](https://github.com/Bthornton1994/Manipulation-score) | — | 1 | JavaScript | 2026-09-22 |
| [buckmoon/jev-issue-router](https://github.com/buckmoon/jev-issue-router) | Jev recommends model and reasoning settings for GitHub issues across OpenAI, Claude, and Grok | 1 | Python | 2026-09-20 |
| [BYK/jev-mcp](https://github.com/BYK/jev-mcp) | An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, s… | 1 | TypeScript | 2026-09-18 |
| [CarlosCaoLopez/HACKSPAIN-2026](https://github.com/CarlosCaoLopez/HACKSPAIN-2026) | Taiafox filters a hundred incoming messages down to the three that matter, coordinates responders by voice, a… | 1 | Python | 2026-09-21 |
| [cdepuy/hermes-skill-router](https://github.com/cdepuy/hermes-skill-router) | Hermes plugin: Jev-style skill pre-routing with a local Laya model (421M System-1). Injects the top-N relevan… | 1 | Python | 2026-09-22 |
| [cephalization/jev-triage](https://github.com/cephalization/jev-triage) | Uses typeful jev, zero sync to pull and sync large repositories for issue triage | 1 | TypeScript | 2026-09-20 |
| [chahero/driving-jev](https://github.com/chahero/driving-jev) | Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews. | 1 | Python | 2026-09-19 |
| [chy4pro/jev-dev-kit](https://github.com/chy4pro/jev-dev-kit) | Framework for agents on TypeSafe Jev: turns candidates into valid Jev questions and answers into validated ch… | 1 | TypeScript | 2026-09-21 |
| [chy4pro/jev-in-mcp](https://github.com/chy4pro/jev-in-mcp) | MCP relay that adds use_jev to every server: Jev picks the tool calls, the calling model writes the values Je… | 1 | TypeScript | 2026-09-21 |
| [clouatre-labs/decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp) | Typed decisions for AI agents as an MCP tool: yes/no probability (noul), choice, and score in one fast reques… | 1 | JavaScript | 2026-09-22 |
| [clownware/bouncer](https://github.com/clownware/bouncer) | Jev-powered Judgment layer for Claude Code. Stops paying reasoning prices for if-statements: a PreToolUse hoo… | 1 | TypeScript | 2026-09-20 |
| [codesoda/openjev-rs](https://github.com/codesoda/openjev-rs) | Local typed decisions from frozen GGUF model logits: Rust workspace and CLI | 1 | Rust | 2026-09-21 |
| [CompleteDotTech/jev-factorio-agent](https://github.com/CompleteDotTech/jev-factorio-agent) | Jev picks what, code owns how - a System One Factorio agent driven by TypeSafe's Jev on FLE | 1 | Python | 2026-09-22 |
| [CompleteDotTech/paper-package](https://github.com/CompleteDotTech/paper-package) | Jev research manuscript, evidence, and reproducible paper package | 1 | Python | 2026-09-20 |
| [ctaxnagomi/dgui-hypermem](https://github.com/ctaxnagomi/dgui-hypermem) | DGUI-HyperMem (DeckerGUI HyperMemory) - self-hosted hybrid memory MCP server on Cloudflare Workers with a JEV… | 1 | TypeScript | 2026-09-22 |
| [dagfinndybvig/Fight](https://github.com/dagfinndybvig/Fight) | An arcade style fighting game controllable by Jev | 1 | JavaScript | 2026-09-20 |
| [daidr/browser-jev](https://github.com/daidr/browser-jev) | Run Jev-like decisions in your browser with the Prompt API. | 1 | TypeScript | 2026-09-21 |
| [danielhirt/jev-lab](https://github.com/danielhirt/jev-lab) | Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM … | 1 | TypeScript | 2026-09-20 |
| [DanielKillenberger/telperion](https://github.com/DanielKillenberger/telperion) | A procedural tree generator. Authored silhouette, space colonization, conserved thickness, one continuous pla… | 1 | Rust | 2026-09-20 |
| [danielyedaniel/jevme](https://github.com/danielyedaniel/jevme) | Talk to your Mac and it does it — in any app, while you're still talking. Open-source voice agent that gets f… | 1 | Python | 2026-09-22 |
| [day253/microjev](https://github.com/day253/microjev) | GPT-2 124M with Jev-style typed probabilistic decisions on Apple Silicon (MLX), plus a pure-Python teaching m… | 1 | Python | 2026-09-21 |
| [de-niji/jev-hermes](https://github.com/de-niji/jev-hermes) | Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter | 1 | Python | 2026-09-20 |
| [DECRUX9812/openjev-lm](https://github.com/DECRUX9812/openjev-lm) | open-Jev LM arm: Qwen2.5-0.5B + LoRA reproducing a hosted decision model's judgment at 92.9% on hand-labelled… | 1 | Python | 2026-09-20 |
| [dees91/agent-skill-manager](https://github.com/dees91/agent-skill-manager) | A macOS app, TUI, and CLI to manage skills for AI coding tools. Turn skills on or off without deleting them. | 1 | Go | 2026-09-22 |
| [Dev916/mech-crate](https://github.com/Dev916/mech-crate) | AI-native meta-framework for standing up and operating service ecosystems: Docker scaffolding with recipes, a… | 1 | Rust | 2026-09-19 |
| [DevJonasMax/resume-ai](https://github.com/DevJonasMax/resume-ai) | — | 1 | TeX | 2026-09-21 |
| [dglazkov/jev2ui](https://github.com/dglazkov/jev2ui) | Jev + A2UI = ? | 1 | TypeScript | 2026-09-22 |
| [Dharundp6/jev-carryforward](https://github.com/Dharundp6/jev-carryforward) | What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written … | 1 | TypeScript | 2026-09-19 |
| [dhava-gautama/noulgate](https://github.com/dhava-gautama/noulgate) | A gate for your agent's expensive steps, powered by TypeSafe Jev (System One). Offline-first, OpenRouter or d… | 1 | Python | 2026-09-19 |
| [digitopvn/clarkcant](https://github.com/digitopvn/clarkcant) | Conversation-first agent platform: portable runtime, paired execution nodes, rich widgets and capability packs | 1 | TypeScript | 2026-09-22 |
| [djhoomin/local-system-one](https://github.com/djhoomin/local-system-one) | Local stand-ins for TypeSafe Jev's System One interface: typed calibrated decisions from small models, with a… | 1 | Python | 2026-09-19 |
| [DonaldMurillo/system-one-playground](https://github.com/DonaldMurillo/system-one-playground) | Readable scripting, semantic code checks, a Go System One client, and Studio. | 1 | Go | 2026-09-22 |
| [DowLucas/devscope](https://github.com/DowLucas/devscope) | Real-time monitoring dashboard for Claude Code developer sessions | 1 | TypeScript | 2026-09-21 |
| [dperezcabrera/jev-chess](https://github.com/dperezcabrera/jev-chess) | Chess against Jev, TypeSafe AI's System One model, through OpenRouter. Built with the pico framework. | 1 | Python | 2026-09-22 |
| [drafael/coding-harness](https://github.com/drafael/coding-harness) | Reusable agent skills and workflows for everyday development. | 1 | HTML | 2026-09-21 |
| [dtduc-git/jevnav](https://github.com/dtduc-git/jevnav) | Page truth for browser agents — and decisions that replay, test and audit. Jev picks the element, risky actio… | 1 | Python | 2026-09-22 |
| [dtheofr/typesafe-jev-ruby](https://github.com/dtheofr/typesafe-jev-ruby) | Ruby client for Jev, TypeSafe's System One model: typed questions, probabilistic answers. Zero runtime depend… | 1 | Ruby | 2026-09-21 |
| [dwisiswant0/typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go) | Go SDK for TypeSafe AI. | 1 | Go | 2026-09-19 |
| [edgardcham/huncho](https://github.com/edgardcham/huncho) | Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journa… | 1 | TypeScript | 2026-09-21 |
| [EffNine/CodeBro](https://github.com/EffNine/CodeBro) | Persistent engineering context and memory for AI coding agents, exposed through MCP. | 1 | Rust | 2026-09-18 |
| [EkagraAgarwal/Steve](https://github.com/EkagraAgarwal/Steve) | Steve | 1 | Python | 2026-09-20 |
| [ellistev/typesafe-minecraft-demo](https://github.com/ellistev/typesafe-minecraft-demo) | A Minecraft Java player controlled by TypeSafe AI, with live decisions, Canadian flag building, and a side-by… | 1 | JavaScript | 2026-09-17 |
| [EnesYilmazcode/JevMinesweeper](https://github.com/EnesYilmazcode/JevMinesweeper) | Jev Plays Minesweeper | 1 | Python | 2026-09-21 |
| [ennsharma/scrollpatrol](https://github.com/ennsharma/scrollpatrol) | Mute feed posts by meaning. An open-source Chrome extension powered by Jev. | 1 | TypeScript | 2026-09-22 |
| [Enucatl/docker-airflow](https://github.com/Enucatl/docker-airflow) | — | 1 | Python | 2026-09-18 |
| [EpicEric/safe-sh](https://github.com/EpicEric/safe-sh) | Static shell script analysis with Jev. | 1 | Nix | 2026-09-19 |
| [erboland/jev-fund](https://github.com/erboland/jev-fund) | Open-source paper hedge fund. Jev decides. Public tape of holdings, buys, and losses. | 1 | TypeScript | 2026-09-22 |
| [etnt/unsafe-c-finder](https://github.com/etnt/unsafe-c-finder) | Classify C/C++ snippets via TypeSafe Jev through OpenRouter. | 1 | Python | 2026-09-19 |
| [fajarhide/askgrep](https://github.com/fajarhide/askgrep) | grep for the questions you cannot write as a pattern. Reads every function instead of sampling a few. Powered… | 1 | Rust | 2026-09-22 |
| [fanly/Jev-awesome](https://github.com/fanly/Jev-awesome) | — | 1 | Python | 2026-09-20 |
| [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) | Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model. | 1 | JavaScript | 2026-09-20 |
| [fengliner/jev-tank-battle](https://github.com/fengliner/jev-tank-battle) | — | 1 | JavaScript | 2026-09-22 |
| [fiale-plus/jev-cli](https://github.com/fiale-plus/jev-cli) | — | 1 | TypeScript | 2026-09-19 |
| [finetuningsingh/jev-chatbot](https://github.com/finetuningsingh/jev-chatbot) | Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time | 1 | JavaScript | 2026-09-19 |
| [fraserxu/node-decision-model](https://github.com/fraserxu/node-decision-model) | Node client for decision models such as Typesafe Jev | 1 | TypeScript | 2026-09-19 |
| [frimoldi/jev-palette](https://github.com/frimoldi/jev-palette) | A palette generator using Jev | 1 | TypeScript | 2026-09-20 |
| [g0runmezadam/what-is-jev](https://github.com/g0runmezadam/what-is-jev) | Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public reposito… | 1 | Python | 2026-09-21 |
| [gaborishka/jev-wrapped](https://github.com/gaborishka/jev-wrapped) | Telegram channel X-ray: Jev judges a year of posts, you get a card. One Cloudflare Worker. | 1 | JavaScript | 2026-09-21 |
| [galitianu/jev4j](https://github.com/galitianu/jev4j) | Java SDK for the TypeSafe AI API. Typed questions, typed answers, Java 21. | 1 | Java | 2026-09-21 |
| [gargpratyush/journey-evals](https://github.com/gargpratyush/journey-evals) | Drive a real browser or a real LangGraph agent through one declared user journey, and report what actually ha… | 1 | Python | 2026-09-22 |
| [gecm0/jev-judge-mcp](https://github.com/gecm0/jev-judge-mcp) | MCP server exposing TypeSafe's Jev as a judge tool: typed judgments with calibrated probabilities, for any MC… | 1 | JavaScript | 2026-09-20 |
| [Gerry9000/awesome-jev](https://github.com/Gerry9000/awesome-jev) | Curated directory of real-world tools, interactive video teardowns, empirical benchmarks, and fast System One… | 1 | — | 2026-09-22 |
| [gmaxxxie/jev-cli](https://github.com/gmaxxxie/jev-cli) | — | 1 | Python | 2026-09-22 |
| [golergka/jev-plays-starcraft-2](https://github.com/golergka/jev-plays-starcraft-2) | — | 1 | Python | 2026-09-20 |
| [goodruizhan/pi-jev-control](https://github.com/goodruizhan/pi-jev-control) | System-One control plane for Pi Coding Agent powered by TypeSafe Jev. | 1 | TypeScript | 2026-09-22 |
| [grayrepo-byte/jev_filter_for_x](https://github.com/grayrepo-byte/jev_filter_for_x) | A browser extension that scores and filters X posts in real time with Jev, folding low-signal content while k… | 1 | TypeScript | 2026-09-20 |
| [greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi) | Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) p… | 1 | Python | 2026-09-18 |
| [gregb100/gavel](https://github.com/gregb100/gavel) | Stop burning LLM calls on classification. Route bugs, triage failures, and gate PRs in 200ms for $0.00002. Op… | 1 | Python | 2026-09-19 |
| [GregDixonMXN/annalist](https://github.com/GregDixonMXN/annalist) | Local-first flight recorder for autonomous coding agents (Zig + SQLite) | 1 | Zig | 2026-09-17 |
| [Growth-Kinetics/jev-context](https://github.com/Growth-Kinetics/jev-context) | — | 1 | TypeScript | 2026-09-20 |
| [guchengod/typesafe-sdk-go](https://github.com/guchengod/typesafe-sdk-go) | Go SDK for TypeSafe AI — classification and rating primitives over text and JSON | 1 | Go | 2026-09-20 |
| [haibt163/jev](https://github.com/haibt163/jev) | — | 1 | TypeScript | 2026-09-19 |
| [HAR5HA-7663/hunch](https://github.com/HAR5HA-7663/hunch) | ⚡ Browser agent that acts on a hunch: Jev (TypeSafe System One) picks every click in ~150 ms, an LLM is only … | 1 | Python | 2026-09-22 |
| [hello-wy/sub2api](https://github.com/hello-wy/sub2api) | — | 1 | Go | 2026-09-20 |
| [hemanth/hfjev](https://github.com/hemanth/hfjev) | Classify Hugging Face datasets across typed semantic dimensions with TypeSafe Jev System One. | 1 | TypeScript | 2026-09-21 |
| [hemanth/jevish](https://github.com/hemanth/jevish) | — | 1 | JavaScript | 2026-09-21 |
| [hemanth/traffic-guard](https://github.com/hemanth/traffic-guard) | Empirical, zero-dependency reverse-proxy traffic classifier and bot mitigator in <100μs | 1 | Python | 2026-09-21 |
| [herval/openclaw-jev-plugin](https://github.com/herval/openclaw-jev-plugin) | Jev as a message gate to determine if agents should respond | 1 | TypeScript | 2026-09-21 |
| [hfnissum-byte/Hunkpick](https://github.com/hfnissum-byte/Hunkpick) | Resolve git merge conflicts by enumeration and judgment: code enumerates every valid resolution, a TypeSafe S… | 1 | JavaScript | 2026-09-22 |
| [hide-G/magi-system-on-jev](https://github.com/hide-G/magi-system-on-jev) | MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate … | 1 | JavaScript | 2026-09-18 |
| [HiepPP/hiep-paseo-plugin](https://github.com/HiepPP/hiep-paseo-plugin) | Local Paseo plugin exposing Jev evaluations through MCP | 1 | TypeScript | 2026-09-22 |
| [HisuiKoh/jev-vtuber-ime-core](https://github.com/HisuiKoh/jev-vtuber-ime-core) | 読み→VTuber表記を Web検索の根拠 + Jev で解決。辞書データなし。 | 1 | TypeScript | 2026-09-21 |
| [hongsoonil02-maker/okx_auto_trading](https://github.com/hongsoonil02-maker/okx_auto_trading) | — | 1 | Python | 2026-09-22 |
| [howtimeschange/listingfy](https://github.com/howtimeschange/listingfy) | — | 1 | TypeScript | 2026-09-21 |
| [Hugo-DDT/JevTape](https://github.com/Hugo-DDT/JevTape) | Jev 决策的 Record / Replay 工具：CLI + 本地代理 + JSON 磁带，回放彻底离线。 | 1 | Java | 2026-09-21 |
| [HusDev/LinguaTrace](https://github.com/HusDev/LinguaTrace) | The lesson notebook that writes itself. A live tutoring lesson becomes structured notes and a personalised Le… | 1 | TypeScript | 2026-09-20 |
| [ianrtracey/www](https://github.com/ianrtracey/www) | ian.so | 1 | TypeScript | 2026-09-19 |
| [ibnuh/Flow.Launcher.Plugin.JevFileSearch](https://github.com/ibnuh/Flow.Launcher.Plugin.JevFileSearch) | Flow Launcher predictive file search with Jev intent reranking. Type natural language like 'the pdf I just do… | 1 | C# | 2026-09-19 |
| [ieee0824/jev-mcp](https://github.com/ieee0824/jev-mcp) | A Rust MCP server for TypeSafe AI Jev structured decisions | 1 | Rust | 2026-09-21 |
| [inematds/jev](https://github.com/inematds/jev) | Análise crítica e plano de aplicação do Jev em decisões estruturadas | 1 | Python | 2026-09-21 |
| [integrate-your-mind/jev-nethack](https://github.com/integrate-your-mind/jev-nethack) | Jev x NetHack: bounded runner, research code, and completed recording releases | 1 | Python | 2026-09-21 |
| [isthatdebbiej/jevgap](https://github.com/isthatdebbiej/jevgap) | — | 1 | Python | 2026-09-22 |
| [JabbaKadabra/SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet) | .NET client for TypeSafe System One (Jev) — typed questions in, typed answers with probabilities and confiden… | 1 | C# | 2026-09-21 |
| [jackboykin/quarry](https://github.com/jackboykin/quarry) | Let agents read web sources themselves, with Exa and Jev | 1 | Go | 2026-09-21 |
| [jacks3tr/Jev-Desktop](https://github.com/jacks3tr/Jev-Desktop) | — | 1 | Python | 2026-09-22 |
| [JacobLinCool/Weave-In](https://github.com/JacobLinCool/Weave-In) | Keep the thread. Weave everyone in. | 1 | TypeScript | 2026-09-18 |
| [jaewilson07/vendor-docs-sync](https://github.com/jaewilson07/vendor-docs-sync) | Mirrored vendor documentation (Domo, Letta, Trigger.dev skills, Claude Code) synced into mdrag by trigger-dev… | 1 | MDX | 2026-09-21 |
| [jamesward/evals-demo](https://github.com/jamesward/evals-demo) | — | 1 | Shell | 2026-09-20 |
| [jangya/jev-in-action](https://github.com/jangya/jev-in-action) | — | 1 | JavaScript | 2026-09-19 |
| [jay1803/ship-skills](https://github.com/jay1803/ship-skills) | Skills for Codex to ship your idea automatically. | 1 | Python | 2026-09-20 |
| [jcressler/fast-jev-compaction-codex](https://github.com/jcressler/fast-jev-compaction-codex) | Task-aware Jev evidence selection and exact local recovery around native Codex compaction. | 1 | JavaScript | 2026-09-19 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | MASC - Multi-Agent Shared Context | 1 | OCaml | 2026-09-22 |
| [JeronimoRepetto/DwarfAI-Miners](https://github.com/JeronimoRepetto/DwarfAI-Miners) | Local desktop panel that turns your AI coding sessions into an isometric dwarf mining colony - watch, message… | 1 | TypeScript | 2026-09-22 |
| [jev-ids/jev-ids.github.io](https://github.com/jev-ids/jev-ids.github.io) | Jev IDS website: one flow. one request. one verdict. | 1 | HTML | 2026-09-22 |
| [jjd-lab/jev-synthetic-survey](https://github.com/jjd-lab/jev-synthetic-survey) | Jev vs GPT-4.1 as synthetic survey respondents on Twin-2K-500. How you ask mattered more than which model you… | 1 | Python | 2026-09-22 |
| [JLegends/opencode-jev-compaction](https://github.com/JLegends/opencode-jev-compaction) | opencode plugins that replace lossy compaction with Jev decisions: score every tool call and result, drop or … | 1 | TypeScript | 2026-09-21 |
| [JoacoMarc/jev-harness-router](https://github.com/JoacoMarc/jev-harness-router) | Per-turn router for agent harnesses: one 350ms Jev call picks the model tier, effort, tools and skill, behind… | 1 | TypeScript | 2026-09-21 |
| [JoeSun-421/robotic_agent_use_jev](https://github.com/JoeSun-421/robotic_agent_use_jev) | A UR5e arm use jev and qwen to gain an ability like neural reflexes | 1 | Python | 2026-09-21 |
| [jonathanavis96/jev-kit](https://github.com/jonathanavis96/jev-kit) | Everything you need to run TypeSafe's Jev with Claude Code: a tool-call guard, tier guard, file search, brows… | 1 | Python | 2026-09-21 |
| [Joymfl/dag-jev](https://github.com/Joymfl/dag-jev) | DAG creation out of unordered items via Jev | 1 | Rust | 2026-09-21 |
| [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev) | A curated list of TypeSafe Jev resources, SDKs, agents, MCP servers, integrations, benchmarks, examples, and … | 1 | — | 2026-09-22 |
| [jstdlee/jev-spaceshooter-demo](https://github.com/jstdlee/jev-spaceshooter-demo) | Space shooter demo of bounded Jev movement choices, swept collision prediction, stale-response rejection, and… | 1 | — | 2026-09-20 |
| [juanlentino/jev-connector](https://github.com/juanlentino/jev-connector) | WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core C… | 1 | PHP | 2026-09-20 |
| [jyatesdotdev/jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) | Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed. | 1 | Python | 2026-09-20 |
| [JYeswak/jev_playground](https://github.com/JYeswak/jev_playground) | Measure what Jev can actually do before you build on it. Graded findings, ruled-out candidates, and recipes w… | 1 | JavaScript | 2026-09-22 |
| [Kadihx/jev-x-kit](https://github.com/Kadihx/jev-x-kit) | Offline $0 decision layer for coding agents: Choice/Score/Noul primitives, BELKI confidence gatekeeper, ultra… | 1 | TypeScript | 2026-09-22 |
| [Kaidera-AI/skills](https://github.com/Kaidera-AI/skills) | Kaidera Skills Marketplace for vetted reusable agent skills | 1 | JavaScript | 2026-09-19 |
| [kairugakuo2/jev-arena](https://github.com/kairugakuo2/jev-arena) | Small local projects built on Vercel's Jev model: a real-time AI fighting game and a live hotter/colder codin… | 1 | JavaScript | 2026-09-22 |
| [Kaos599/jev-writer](https://github.com/Kaos599/jev-writer) | Find out which qualities of your writing actually predict engagement. Rates every post you have published aga… | 1 | JavaScript | 2026-09-21 |
| [kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search) | Recursive semantic file search using TypeSafe Jev and fzf | 1 | JavaScript | 2026-09-21 |
| [keiffff/jev-kit](https://github.com/keiffff/jev-kit) | Jev toolkit for building fast, testable AI decision points for agent permissions, routing, semantic change de… | 1 | TypeScript | 2026-09-21 |
| [KennethAshley/fez](https://github.com/KennethAshley/fez) | Orchestrate your own AI agents and build extensions for them — summon an agent by name, watch it think, ship … | 1 | TypeScript | 2026-09-21 |
| [kentaro/jevex](https://github.com/kentaro/jevex) | Jev inference as composable Elixir expressions, with typed requests and runtime-configurable backends | 1 | Elixir | 2026-09-21 |
| [KevinArce/ExoNotes](https://github.com/KevinArce/ExoNotes) | Do astronomers' notes carry disposition signal beyond numeric catalogues? Pre-registered study on TESS Object… | 1 | Python | 2026-09-22 |
| [khaledsAlshibani/jev-ci-classifier](https://github.com/khaledsAlshibani/jev-ci-classifier) | CI example using Jev to classify failed PR checks and return structured decisions with probabilities. | 1 | TypeScript | 2026-09-20 |
| [kilolonion/excelmanus](https://github.com/kilolonion/excelmanus) | ExcelManus - AI-powered Excel Agent | 1 | Python | 2026-09-22 |
| [kingkillery/oh-my-pk](https://github.com/kingkillery/oh-my-pk) | ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subag… | 1 | TypeScript | 2026-09-22 |
| [KKiJJ1024/crush-monitor2](https://github.com/KKiJJ1024/crush-monitor2) | 基于大佬-劈个茄子的开源项目，免去了jev模型钥匙的获取，直接接入deepseek，效果会有差异，但可以暂时满足一定趣味性 | 1 | — | 2026-09-21 |
| [kleosr/cursor-clijev-compaction](https://github.com/kleosr/cursor-clijev-compaction) | TypeSafe Jev-scored context recovery for Cursor CLI (agent). Capture tool I/O, score keep/drop, re-inject aft… | 1 | TypeScript | 2026-09-19 |
| [krlmrr/dotfiles](https://github.com/krlmrr/dotfiles) | — | 1 | Lua | 2026-09-22 |
| [kspviswa/chakravyuha-jev](https://github.com/kspviswa/chakravyuha-jev) | Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: t… | 1 | JavaScript | 2026-09-18 |
| [kuoruan/pi-mono](https://github.com/kuoruan/pi-mono) | PI Agent extension packages. | 1 | TypeScript | 2026-09-21 |
| [kw2828/OpenJev](https://github.com/kw2828/OpenJev) | Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control | 1 | Python | 2026-09-22 |
| [kyledickey/jev-go](https://github.com/kyledickey/jev-go) | TypeSafe.ai Jev Go SDK | 1 | Go | 2026-09-22 |
| [laguagu/jev-skills](https://github.com/laguagu/jev-skills) | Practical agent skills and examples for building with Jev. API setup, routing, ranking, and evidence checks. | 1 | — | 2026-09-21 |
| [lazniak/jevskill](https://github.com/lazniak/jevskill) | Teach your coding agent to stop burning context. Jev (System One) via OpenRouter or TypeSafe: 325ms, 0.000013… | 1 | Python | 2026-09-21 |
| [lbyxiaolizi/sub2api](https://github.com/lbyxiaolizi/sub2api) | Sub2API-CRS2 一站式开源中转服务，让 Claude、Openai 、Gemini、Antigravity订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 | 1 | Go | 2026-09-20 |
| [Leoguy77/pi-packages.nix](https://github.com/Leoguy77/pi-packages.nix) | Nix-native pi.dev packages — 5,755 pi extensions, skills, and themes as Nix derivations with an Attic binary … | 1 | JavaScript | 2026-09-21 |
| [leojacinto/my-name-jev](https://github.com/leojacinto/my-name-jev) | — | 1 | TypeScript | 2026-09-21 |
| [levi-qiao/SemaLoom](https://github.com/levi-qiao/SemaLoom) | Ontology-driven business layer for serious AI Q&A over existing data sources, with deterministic semantics, e… | 1 | Python | 2026-09-22 |
| [LiuHao-1443/jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis) | Table tennis vs. TypeSafe's Jev (System One). Every paddle move on the right is a live model decision — no lo… | 1 | Python | 2026-09-21 |
| [liuqihonggit/JoinCode](https://github.com/liuqihonggit/JoinCode) | This is Coding Agent | 1 | C# | 2026-09-22 |
| [llt22/jev-lab](https://github.com/llt22/jev-lab) | Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score pri… | 1 | Python | 2026-09-21 |
| [logicrw/ask-jev](https://github.com/logicrw/ask-jev) | Ultra-fast, fail-open advisory decisions and verbatim extractive reading view for AI coding agents and CLI pi… | 1 | Python | 2026-09-21 |
| [loktar00/llm-lan-party](https://github.com/loktar00/llm-lan-party) | A language model plays Unreal Tournament 99 on real Windows 98 hardware by answering small typed questions, s… | 1 | TypeScript | 2026-09-21 |
| [luhayes/jev-agent-router](https://github.com/luhayes/jev-agent-router) | — | 1 | Python | 2026-09-22 |
| [luigivis/jev-sdk-java](https://github.com/luigivis/jev-sdk-java) | Type-safe Java 21 client for the TypeSafe AI Jev (System One) decision API | 1 | Java | 2026-09-22 |
| [m0rphtail/triagedy](https://github.com/m0rphtail/triagedy) | Alert triage as a UNIX filter: JSONL security alerts in, typed decisions out. Runs on TypeSafe Jev or a local… | 1 | Rust | 2026-09-21 |
| [maddygoround/typesafeai-cli](https://github.com/maddygoround/typesafeai-cli) | Give your AI agent a CLI companion who has access to TypeSafe AI's Jev. | 1 | Python | 2026-09-22 |
| [majiayu000/awesome-jev](https://github.com/majiayu000/awesome-jev) | A curated list of Jev / TypeSafe System One projects, SDKs, tutorials, and evaluations. English and 简体中文. | 1 | Python | 2026-09-22 |
| [makefinks/jev-feed-filter](https://github.com/makefinks/jev-feed-filter) | Smart, dynamic AI filtering for X and YouTube feeds using Jev | 1 | TypeScript | 2026-09-19 |
| [Mani212005/GameTester](https://github.com/Mani212005/GameTester) | Interactive 3D Game Physics & Collision Simulator built with Three.js, Cannon-es, and Playwright automated vi… | 1 | TypeScript | 2026-09-19 |
| [markjaquith/typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground) | A playground for experiments around Jev, TypeSafe's System One model. | 1 | Rust | 2026-09-18 |
| [marszhongx/pi-jev-score](https://github.com/marszhongx/pi-jev-score) | — | 1 | TypeScript | 2026-09-22 |
| [MartinPuli/f1](https://github.com/MartinPuli/f1) | JEV Prix: five AI drivers, unknown procedural circuits, Formula-inspired racing, BYOK Jev and saved replays. | 1 | JavaScript | 2026-09-21 |
| [mattneel/typesafe](https://github.com/mattneel/typesafe) | An idiomatic Elixir client for the TypeSafe AI API | 1 | Elixir | 2026-09-17 |
| [maxcorrads/hivemind](https://github.com/maxcorrads/hivemind) | — | 1 | TypeScript | 2026-09-21 |
| [maximebrmd/relanmo](https://github.com/maximebrmd/relanmo) | Autonomous prospecting for freelancers. | 1 | TypeScript | 2026-09-21 |
| [mcftira/jev-route](https://github.com/mcftira/jev-route) | — | 1 | Python | 2026-09-22 |
| [micahchoo/qualitative-query](https://github.com/micahchoo/qualitative-query) | Saved questions that select source passages with Jev scoring and connect them through native Obsidian block e… | 1 | TypeScript | 2026-09-21 |
| [mingleiw/jev-oncall](https://github.com/mingleiw/jev-oncall) | Incident triage on TypeSafe Jev — the model judges, plain code decides. Routing on probability distributions … | 1 | Python | 2026-09-22 |
| [miounet11/jevcode](https://github.com/miounet11/jevcode) | JevCode — Jev (TypeSafe System One) 技术解决方案与最佳实践 · https://www.jevcode.ai | 1 | TypeScript | 2026-09-21 |
| [Mist-wu/qqbot](https://github.com/Mist-wu/qqbot) | QQ 群聊机器人：jev 决定该不该说话，deepseek-flash 决定说什么。基于 NapCat，支持表情包、联网搜索、长期记忆。 | 1 | TypeScript | 2026-09-22 |
| [Mistertelecom/NEXUS-AI-Gateway-with-JEV](https://github.com/Mistertelecom/NEXUS-AI-Gateway-with-JEV) | AI gateway that validates before it executes: Lead plans, JEV validates, Worker generates. Local-first contro… | 1 | TypeScript | 2026-09-21 |
| [misty-step/harness](https://github.com/misty-step/harness) | Shared agent primitives and thin pi/OMP harness adapters; one versioned workspace | 1 | TypeScript | 2026-09-22 |
| [misty-step/polymorph](https://github.com/misty-step/polymorph) | Chrome extension: collapse posts that match rules you wrote in English. Jev is the judge. | 1 | TypeScript | 2026-09-20 |
| [Momen-devv/multitenant-ecommerce](https://github.com/Momen-devv/multitenant-ecommerce) | Production-ready multi-tenant e-commerce API built with NestJS, PostgreSQL, Drizzle ORM, Better Auth, Stripe,… | 1 | TypeScript | 2026-09-21 |
| [montaguegabe/answerfit](https://github.com/montaguegabe/answerfit) | One AI answer, fitted to what each reader already knows — a personalization overlay that re-renders Claude Co… | 1 | TypeScript | 2026-09-21 |
| [MrDesjardins/jevrealtimecodecheck](https://github.com/MrDesjardins/jevrealtimecodecheck) | — | 1 | TypeScript | 2026-09-18 |
| [mrmt/elevator-three](https://github.com/mrmt/elevator-three) | Jev に判断を任せる自動生成のエレクトロの楽器 | 1 | HTML | 2026-09-21 |
| [MumuTW/awesome-jev](https://github.com/MumuTW/awesome-jev) | Get Jev fast — TypeSafe’s sharp System One for typed decisions, plus kindred models the community is buzzing … | 1 | — | 2026-09-19 |
| [muratmirgun/compact-engine](https://github.com/muratmirgun/compact-engine) | — | 1 | Go | 2026-09-21 |
| [muse0509/jev-preflight](https://github.com/muse0509/jev-preflight) | A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection. | 1 | Go | 2026-09-20 |
| [Nabsku/pi-follow-through](https://github.com/Nabsku/pi-follow-through) | Nudge your agent, when jev deems it so! | 1 | TypeScript | 2026-09-21 |
| [nanami-0713/dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide) | DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrate… | 1 | JavaScript | 2026-09-21 |
| [naveenreddy61/jev-experiments](https://github.com/naveenreddy61/jev-experiments) | experiments with system one model jev | 1 | Python | 2026-09-21 |
| [nekowasabi/jev-routing](https://github.com/nekowasabi/jev-routing) | Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server. | 1 | Go | 2026-09-22 |
| [Nicksxs/Nicksxs.github.io](https://github.com/Nicksxs/Nicksxs.github.io) | my personal blog for tech and life | 1 | HTML | 2026-09-20 |
| [nkkmd/bao-la-kiswahili-game](https://github.com/nkkmd/bao-la-kiswahili-game) | — | 1 | JavaScript | 2026-09-22 |
| [Nolane-x/JEV-language](https://github.com/Nolane-x/JEV-language) | Give your Jev language, i'm not finish now | 1 | TypeScript | 2026-09-20 |
| [NomaDamas/kojev](https://github.com/NomaDamas/kojev) | Quick experiment for Korean specialized Jev-style decision model | 1 | Python | 2026-09-21 |
| [nottelabs/notte-jevmaxxing](https://github.com/nottelabs/notte-jevmaxxing) | Run Jev on Notte browser sessions | 1 | TypeScript | 2026-09-21 |
| [nowwcastle-sudo/github-trending-daily](https://github.com/nowwcastle-sudo/github-trending-daily) | — | 1 | JavaScript | 2026-09-22 |
| [nurf-ai/ai](https://github.com/nurf-ai/ai) | Multimodal Go AI module with realistic cost tracking, not just tokens. | 1 | Go | 2026-09-20 |
| [Obrais-cloud/typesafe-mcp](https://github.com/Obrais-cloud/typesafe-mcp) | MCP server exposing TypeSafe (Jev/System One) to the fleet: judge, rerank, systemone | 1 | Python | 2026-09-21 |
| [omribenami/Omarchy-AI](https://github.com/omribenami/Omarchy-AI) | — | 1 | Python | 2026-09-22 |
| [onlyjq04/jev-agent-hooks](https://github.com/onlyjq04/jev-agent-hooks) | TypeSafe Jev hooks for Claude Code, Codex and pi: per-turn skill suggestion and subagent model routing | 1 | JavaScript | 2026-09-21 |
| [OpenScribbler/syllago-docs](https://github.com/OpenScribbler/syllago-docs) | Documentation site for Syllago—the package manager for AI coding tool content | 1 | MDX | 2026-09-21 |
| [osuki-dev/opencode-osuki-agent](https://github.com/osuki-dev/opencode-osuki-agent) | Effect-native OpenCode coordinator with Jev routing and persistent goals | 1 | TypeScript | 2026-09-21 |
| [ourines/hermes-jev](https://github.com/ourines/hermes-jev) | Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill | 1 | Python | 2026-09-19 |
| [Pasblinn/jev-lab](https://github.com/Pasblinn/jev-lab) | Open lab: Jev (TypeSafe System One) routing in front of Claude Code - measured bugs, patch, and a hard fallba… | 1 | TypeScript | 2026-09-22 |
| [patiently/anti-tangent-mcp](https://github.com/patiently/anti-tangent-mcp) | Keep your coding agent focused and prevent it from drifting out on a tangent. | 1 | Go | 2026-09-20 |
| [Pinutss/jev-mcp-router](https://github.com/Pinutss/jev-mcp-router) | Select relevant MCP tools under a context-token budget, without executing them. | 1 | Python | 2026-09-18 |
| [pjdurden/jevkit-js](https://github.com/pjdurden/jevkit-js) | jevkit for JavaScript/TypeScript: static linter and shared record format for building on TypeSafe's Jev (Syst… | 1 | TypeScript | 2026-09-21 |
| [pksw4u/jev-research-agent](https://github.com/pksw4u/jev-research-agent) | Jev Powered Research Harness | 1 | Python | 2026-09-22 |
| [plenoai/pleno-anonymize](https://github.com/plenoai/pleno-anonymize) | Small Language Model(SLM) for PII Detect and Anonymize | 1 | Python | 2026-09-21 |
| [powerset-co/powerpacks](https://github.com/powerset-co/powerpacks) | — | 1 | Python | 2026-09-22 |
| [Pranavk098/turnstile](https://github.com/Pranavk098/turnstile) | Turnstile — a margin profiler for voice-AI agents (instrument · price · adjudicate · replay). Honest, tier-la… | 1 | Python | 2026-09-21 |
| [proshunsuke/jev-tab-order](https://github.com/proshunsuke/jev-tab-order) | Organize Chrome tabs and groups by meaning with a single Jev API request. | 1 | TypeScript | 2026-09-22 |
| [pulkitxm/jev-form-filler](https://github.com/pulkitxm/jev-form-filler) | Browser extension that fills forms from your profiles and portfolio in one click, powered by Jev. | 1 | JavaScript | 2026-09-21 |
| [purplesmoke05/opencode-plugin-jev-auto-model-router](https://github.com/purplesmoke05/opencode-plugin-jev-auto-model-router) | Opt-in Auto (Jev) model routing for OpenCode with a configurable model allowlist | 1 | TypeScript | 2026-09-20 |
| [Pyjalal/Monash-Hack](https://github.com/Pyjalal/Monash-Hack) | — | 1 | TypeScript | 2026-09-21 |
| [pZacca/askjev](https://github.com/pZacca/askjev) | Unofficial MCP server for Jev (Typesafe AI) | 1 | TypeScript | 2026-09-18 |
| [qwts/agentic-code-analysis](https://github.com/qwts/agentic-code-analysis) | Semantic, agent-powered checks for code structure and maintainability. | 1 | TypeScript | 2026-09-17 |
| [RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev) | A crawler-maintained directory of projects built on Jev, TypeSafe AI's System One model. Daily GitHub + npm s… | 1 | JavaScript | 2026-09-21 |
| [rashedInt32/jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim) | Neovim popup for jev-lens verdicts: do I need to look, which files, strip the debris | 1 | Lua | 2026-09-20 |
| [rashedInt32/jury.nvim](https://github.com/rashedInt32/jury.nvim) | Calibrated picks for Neovim, judged by TypeSafe Jev. First source: effect-error-pretty.nvim | 1 | Lua | 2026-09-21 |
| [redrossa/pi-model-router](https://github.com/redrossa/pi-model-router) | Pi extension that classifies each prompt with TypeSafe's Jev and routes it to the best model you're logged in… | 1 | TypeScript | 2026-09-18 |
| [reiswaffel78/jev-agent-toolkit](https://github.com/reiswaffel78/jev-agent-toolkit) | Jev-first portable Agent Skill and optional MCP bridge for Claude Code, Codex, Cursor and compatible agents. | 1 | JavaScript | 2026-09-20 |
| [relliex/self_jev](https://github.com/relliex/self_jev) | Share a very simple idea for building your own jev model | 1 | Python | 2026-09-22 |
| [remotehostai/jg](https://github.com/remotehostai/jg) | MIT-licensed semantic code search CLI for coding agents, powered by Jev. | 1 | JavaScript | 2026-09-21 |
| [renchris/claude-infrastructure](https://github.com/renchris/claude-infrastructure) | Custom Claude Code infrastructure — versioned updates, lifecycle hooks, backup system, session search, agent … | 1 | Shell | 2026-09-22 |
| [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev) | Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself. | 1 | TypeScript | 2026-09-21 |
| [RIA-Spec/one-agent](https://github.com/RIA-Spec/one-agent) | The `one tool to rule them all` agent that implements Re in Act pattern | 1 | TypeScript | 2026-09-21 |
| [Ripwords/photobook-generator](https://github.com/Ripwords/photobook-generator) | Turn a folder of photos into a print-ready photobook, analysed entirely on your Mac | 1 | Rust | 2026-09-20 |
| [Robertzu43/system-one-security-triage](https://github.com/Robertzu43/system-one-security-triage) | Recorded comparison of Jev, Terra, and Opus on 100 synthetic security-triage cases, five passes each, with a … | 1 | TypeScript | 2026-09-21 |
| [robokrunch/jev-physical-ai](https://github.com/robokrunch/jev-physical-ai) | Putting TypeSafe's Jev to work on robots, fleets, and edge hardware — real measured numbers, honestly caveate… | 1 | Python | 2026-09-20 |
| [rogeriochaves/jev-experiments](https://github.com/rogeriochaves/jev-experiments) | — | 1 | Go | 2026-09-19 |
| [rolottr/x-jev-classifier](https://github.com/rolottr/x-jev-classifier) | Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev … | 1 | JavaScript | 2026-09-19 |
| [RudyJunyu/Jev-MCP](https://github.com/RudyJunyu/Jev-MCP) | Jev MCP Hub is a small Go gateway that exposes TypeSafe's Jev model through the Model Context Protocol. | 1 | Go | 2026-09-21 |
| [russellromney/jevons](https://github.com/russellromney/jevons) | — | 1 | TypeScript | 2026-09-18 |
| [russfranky/jev-crawlers](https://github.com/russfranky/jev-crawlers) | Jev learns your repo's decision norms, then adversarially judges past decisions against them. Unix-style prim… | 1 | JavaScript | 2026-09-21 |
| [ryantsai/jev-llm-router](https://github.com/ryantsai/jev-llm-router) | — | 1 | Python | 2026-09-21 |
| [ryanzen9/XFlow](https://github.com/ryanzen9/XFlow) | Jev for your X. XFlow is a Manifest V3 browser extension powered by Jev, with customizable filtering policies… | 1 | TypeScript | 2026-09-22 |
| [S-O-A-TECH/Jev-search-Kor](https://github.com/S-O-A-TECH/Jev-search-Kor) | — | 1 | TypeScript | 2026-09-20 |
| [sago-cream/mini-sago](https://github.com/sago-cream/mini-sago) | A Discord bot for... everything? | 1 | TypeScript | 2026-09-21 |
| [saivivekvenna/jevy-graph](https://github.com/saivivekvenna/jevy-graph) | Fast, source-grounded text-to-RDF knowledge graph compiler using deterministic candidate generation and Jev v… | 1 | Python | 2026-09-22 |
| [sathariels/jevcheck](https://github.com/sathariels/jevcheck) | Behavioral contracts for TypeSafe Jev — pin production expectations, eval model upgrades, catch flips and con… | 1 | Python | 2026-09-21 |
| [sathariels/jevtriage](https://github.com/sathariels/jevtriage) | GitHub Action + CLI: triage PRs with TypeSafe Jev (ready / needs review / risky) with confidence gates and je… | 1 | Python | 2026-09-21 |
| [satyawikananda/gits](https://github.com/satyawikananda/gits) | Gits is a browser extension powered by Jev to search the leads data on the Google Maps | 1 | TypeScript | 2026-09-21 |
| [scarif-labs/jev-software-decision-benchmark](https://github.com/scarif-labs/jev-software-decision-benchmark) | Reproducible benchmark evaluating JEV as a software decision primitive for dependency-update automation under… | 1 | TypeScript | 2026-09-19 |
| [seahsky/kelpie](https://github.com/seahsky/kelpie) | Delegation policy for Claude Code, cut down to what its own benchmark supports: two pinned roles, and a skill… | 1 | JavaScript | 2026-09-22 |
| [seanperkins/omp-jev-watchdog](https://github.com/seanperkins/omp-jev-watchdog) | Experimental shadow-only watchdog for OMP using TypeSafe Jev. Records verification and tool-action instructio… | 1 | TypeScript | 2026-09-19 |
| [segavvy/mnist-text-input-benchmark](https://github.com/segavvy/mnist-text-input-benchmark) | 手書き数字データセットMNISTのテストデータから、各数字（0〜9）をランダムに10枚ずつ、計100枚抽出した簡易的な評価です。 同じ100枚でJev・GPT-5 nano・GPT-5.6 Lunaの入力表現・精度・費… | 1 | HTML | 2026-09-21 |
| [senoldogann/chatgpt-system](https://github.com/senoldogann/chatgpt-system) | Secure local MCP authority gateway for controlled filesystem, Git, process, and future computer-use access fr… | 1 | TypeScript | 2026-09-21 |
| [sergey9519546/STORYMACHINE](https://github.com/sergey9519546/STORYMACHINE) | Deterministic screenplay analysis engine — 3,216 corpus-measured rules, a 14-pass Script Doctor, and a Founta… | 1 | TypeScript | 2026-09-21 |
| [Shashank-H/jev-trader](https://github.com/Shashank-H/jev-trader) | An automated trader using SystemOne model - TypesafeAI Jev | 1 | JavaScript | 2026-09-21 |
| [shauryajain07/ghost-user](https://github.com/shauryajain07/ghost-user) | — | 1 | TypeScript | 2026-09-20 |
| [shibadogcap/kyotsu-ai-bench](https://github.com/shibadogcap/kyotsu-ai-bench) | AI benchmark on Japan's 2026 Common Test: Jev vs luna-none vs luna-low (static dashboard) | 1 | HTML | 2026-09-17 |
| [shinpr/agent-clinic](https://github.com/shinpr/agent-clinic) | Diagnostic plugins for Claude Code and Codex: why a session went wrong, and whether a proposed change is too … | 1 | Python | 2026-09-21 |
| [siddicky/omp-typesafe](https://github.com/siddicky/omp-typesafe) | TypeSafe AI (Jev) adversarial reviewer and typesafe_ask tool for the omp coding agent | 1 | TypeScript | 2026-09-19 |
| [sirkirby/routr](https://github.com/sirkirby/routr) | TUI harness orchestration with herdr and jev to efficiently distribute work across your coding subscriptions. | 1 | JavaScript | 2026-09-21 |
| [skamprogiannis/system-manifest](https://github.com/skamprogiannis/system-manifest) | A Flake-based NixOS configuration featuring a glassmorphism Hyprland environment, Dank Material Shell, and a … | 1 | Nix | 2026-09-20 |
| [skastr0/prism](https://github.com/skastr0/prism) | — | 1 | TypeScript | 2026-09-18 |
| [skastr0/pulsar](https://github.com/skastr0/pulsar) | pulsar | 1 | TypeScript | 2026-09-18 |
| [skcache/jevtrafficsim](https://github.com/skcache/jevtrafficsim) | TypeSafe AI's first model Jev takes on an entire city's traffic | 1 | TypeScript | 2026-09-22 |
| [skhlo/rlcd-brwsr](https://github.com/skhlo/rlcd-brwsr) | Fast browser execution for Pi using Jev classification and Chrome DevTools CLI | 1 | — | 2026-09-20 |
| [Solido/jev_dart](https://github.com/Solido/jev_dart) | Typesafe Jev Api | 1 | Dart | 2026-09-21 |
| [sontakey/awesome-jev](https://github.com/sontakey/awesome-jev) | Unofficial list of insanely useful TypeSafe AI Jev / System One projects | 1 | Python | 2026-09-21 |
| [spate141/jev-wordfeel](https://github.com/spate141/jev-wordfeel) | Turn any word into probability distributions over taste, material, scent, and shape. Powered by Jev. | 1 | TypeScript | 2026-09-19 |
| [sriharsha8991/JEV-use_cases](https://github.com/sriharsha8991/JEV-use_cases) | — | 1 | — | 2026-09-22 |
| [sstehniy/jev-calculator](https://github.com/sstehniy/jev-calculator) | iOS 6-inspired Jev calculator demo with a lifetime API budget | 1 | TypeScript | 2026-09-18 |
| [stoopid-computers/jev-bot](https://github.com/stoopid-computers/jev-bot) | Computer Use Agent developed with Jev | 1 | TypeScript | 2026-09-20 |
| [sungatetop/Jev-robot](https://github.com/sungatetop/Jev-robot) | System One\Two Driven Robot demo | 1 | TypeScript | 2026-09-21 |
| [sunholo-data/ailang-demos](https://github.com/sunholo-data/ailang-demos) | AILANG vertical demos: ecommerce with AI, BigQuery, capability budgets | 1 | HTML | 2026-09-22 |
| [SupratikB23/JevCanvas](https://github.com/SupratikB23/JevCanvas) | Jev-driven interfaces with on-demand diffusion visuals and constrained rendering. | 1 | TypeScript | 2026-09-21 |
| [syabdulr/responsible-ai-harness](https://github.com/syabdulr/responsible-ai-harness) | A model-agnostic, Jev-first Responsible AI harness for assessing AI systems for prompt injection, secret/PII … | 1 | TypeScript | 2026-09-20 |
| [taman-spirit/guardrail-chatbot-jev](https://github.com/taman-spirit/guardrail-chatbot-jev) | Content safety guardrails for AI chatbots: input, output and conversation checks over one policy file, in Pyt… | 1 | Python | 2026-09-22 |
| [taslabs-net/homeflare-kit](https://github.com/taslabs-net/homeflare-kit) | A collection of what I use to keep things consitent | 1 | TypeScript | 2026-09-22 |
| [Tatuck/jev-boe-demo](https://github.com/Tatuck/jev-boe-demo) | Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE). | 1 | TypeScript | 2026-09-21 |
| [Tech-Byte-Frontier/jevgate](https://github.com/Tech-Byte-Frontier/jevgate) | File-scoped maintainability review with TypeSafe Jev | 1 | Rust | 2026-09-22 |
| [tenfingerseddy/voicebind](https://github.com/tenfingerseddy/voicebind) | Natural voice control, dictation and workspace bookmarks for Omarchy. Local Whisper with optional Jev interpr… | 1 | Python | 2026-09-22 |
| [tenuo-ai/safe-upgrade](https://github.com/tenuo-ai/safe-upgrade) | Safe dependency upgrade agent: LangGraph orchestration, Jev decisions, Tenuo task-scoped delegation | 1 | TypeScript | 2026-09-22 |
| [the-metafactory/sage](https://github.com/the-metafactory/sage) | Botanical-named code review agent on pi.dev substrate, speaking Myelin envelopes | 1 | TypeScript | 2026-09-20 |
| [TheBous/jev-flash-review](https://github.com/TheBous/jev-flash-review) | — | 1 | TypeScript | 2026-09-19 |
| [thehumanworks/jevgrep](https://github.com/thehumanworks/jevgrep) | — | 1 | Rust | 2026-09-21 |
| [themacdonald/BiasGuard](https://github.com/themacdonald/BiasGuard) | Framework for Model Bias Detection & Mitigation | 1 | Python | 2026-09-21 |
| [themsquared/jev-benchmark](https://github.com/themsquared/jev-benchmark) | Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and w… | 1 | Python | 2026-09-19 |
| [theSekyi/jevusecases](https://github.com/theSekyi/jevusecases) | What people are actually shipping with Jev — real builds, tracked as they ship. | 1 | TypeScript | 2026-09-20 |
| [Thneoly/r2r-jev](https://github.com/Thneoly/r2r-jev) | Persistent governance for AI agents — turn Jev judgments into replayable relation state with R2R. | 1 | Rust | 2026-09-22 |
| [thomasbrueggemann/jeffrey](https://github.com/thomasbrueggemann/jeffrey) | A coding agent CLI where Jev (TypeSafe System One) or Laya decide what to do next and a configurable LLM does… | 1 | TypeScript | 2026-09-20 |
| [timoconnellaus/frockbot](https://github.com/timoconnellaus/frockbot) | Cordis-first desktop environment for persistent conversational bots | 1 | TypeScript | 2026-09-22 |
| [tisztamo/Meditator](https://github.com/tisztamo/Meditator) | — | 1 | JavaScript | 2026-09-20 |
| [TomRichner/can-jev-bayes](https://github.com/TomRichner/can-jev-bayes) | Can Jev Bayes? No. Testing TypeSafe AI's Jev model against Bayesian-optimal strategies. | 1 | Python | 2026-09-21 |
| [tonyarcher/webapp-workbench](https://github.com/tonyarcher/webapp-workbench) | Sandbox of small web apps - personal tools and a portfolio | 1 | TypeScript | 2026-09-22 |
| [TOSUKUi/jev-bridge](https://github.com/TOSUKUi/jev-bridge) | Jev-style /v1/systemone API in front of any OpenAI-compatible LLM server (one-token logprob scoring, MIT) | 1 | Python | 2026-09-21 |
| [tpaulshippy/syft-listening](https://github.com/tpaulshippy/syft-listening) | Real time speech analysis | 1 | JavaScript | 2026-09-22 |
| [trajectoire-ai/hermes-structured-aux-models](https://github.com/trajectoire-ai/hermes-structured-aux-models) | A Hermes Agent model-provider plugin that routes selected auxiliary tasks through bounded Jev decision calls … | 1 | Python | 2026-09-20 |
| [tripathiarpan20/openarm-jev-lab](https://github.com/tripathiarpan20/openarm-jev-lab) | — | 1 | JavaScript | 2026-09-19 |
| [Tsagaanbayr1/jev-tetris](https://github.com/Tsagaanbayr1/jev-tetris) | Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched… | 1 | JavaScript | 2026-09-21 |
| [tsu-ld/chamuy0](https://github.com/tsu-ld/chamuy0) | Feed slop classifier using Jev. LinkedIn only for now. | 1 | HTML | 2026-09-21 |
| [tubone24/jev-practice-speed](https://github.com/tubone24/jev-practice-speed) | A WebGL demo where you play the card game Speed against a CPU whose brain is TypeSafe AI's Jev. The whole poi… | 1 | JavaScript | 2026-09-21 |
| [tututwo/app-map](https://github.com/tututwo/app-map) | — | 1 | TypeScript | 2026-09-22 |
| [TwoPartDesign/project-os](https://github.com/TwoPartDesign/project-os) | Spec-driven development scaffold for Claude Code — workflow pipeline, memory system, sub-agent orchestration,… | 1 | TypeScript | 2026-09-21 |
| [u007/ocode](https://github.com/u007/ocode) | — | 1 | Go | 2026-09-22 |
| [Umbylicus/umby-jev-stack](https://github.com/Umbylicus/umby-jev-stack) | Portable agent skill: TypeSafe Jev as a cheap code-review classifier (HTTP + optional jev-review MCP) | 1 | JavaScript | 2026-09-22 |
| [umstek/zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench) | Zero-shot information extraction & classification: GLiNER 2.5 vs GLiFormer vs Laya vs Jev — demos, cross-benc… | 1 | Python | 2026-09-21 |
| [using76/TypeEvacSafe](https://github.com/using76/TypeEvacSafe) | 화재 피난자 개인별 판단 엔진 — 타입 안전 판독(Bonsai 2 27B / TypeSafe Jev) + 소셜포스 이동, FDS-GPU 화재장 위에서 역할·구조·경로 결정 · Meteor Simu… | 1 | Python | 2026-09-19 |
| [uspraveen/Jevify](https://github.com/uspraveen/Jevify) | Turn Any Open-LLM into a System-one Jev model | 1 | Python | 2026-09-22 |
| [valsecchi75/squint](https://github.com/valsecchi75/squint) | Claude reads the part of a large file that answers your question, not the whole file. A PreToolUse hook. Meas… | 1 | TypeScript | 2026-09-21 |
| [Vankleben/jev-arm-lab](https://github.com/Vankleben/jev-arm-lab) | Typed-judgment model (TypeSafe Jev) driving task-level decisions on a simulated xArm7: reliability measuremen… | 1 | Python | 2026-09-22 |
| [venumadhav7484/jev-bot](https://github.com/venumadhav7484/jev-bot) | — | 1 | Python | 2026-09-21 |
| [vhwg06/ExHarness](https://github.com/vhwg06/ExHarness) | — | 1 | JavaScript | 2026-09-22 |
| [Victor-Casado/if-ai](https://github.com/Victor-Casado/if-ai) | Plain-English pull request checks powered by Jev. One condition, a minimum confidence, one check. | 1 | TypeScript | 2026-09-20 |
| [vinilana/jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench) | Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off | 1 | JavaScript | 2026-09-19 |
| [vinnie357/typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex) | Typesafe AI SDK in Elixir using Req | 1 | Elixir | 2026-09-18 |
| [vvedantb/vmem](https://github.com/vvedantb/vmem) | Universal Memory Layer/Context Engine for LLMs | 1 | TypeScript | 2026-09-21 |
| [waddle-zoo/signal-weave](https://github.com/waddle-zoo/signal-weave) | Typed decisions for operational signals in BI. Powered by TypeSafeAI Jev | 1 | Python | 2026-09-21 |
| [watany-dev/jev-playground](https://github.com/watany-dev/jev-playground) | — | 1 | TypeScript | 2026-09-18 |
| [Waxmell114514/jev-trade](https://github.com/Waxmell114514/jev-trade) | — | 1 | Python | 2026-09-22 |
| [waynesutton/ask-jev-ai](https://github.com/waynesutton/ask-jev-ai) | A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answ… | 1 | JavaScript | 2026-09-22 |
| [wcleeah/qurom](https://github.com/wcleeah/qurom) | — | 1 | TypeScript | 2026-09-22 |
| [Whamp/skills](https://github.com/Whamp/skills) | Public agent skills authored and maintained by Will Hampson. | 1 | Shell | 2026-09-21 |
| [wieslawsoltes/XamoraStudio](https://github.com/wieslawsoltes/XamoraStudio) | — | 1 | JavaScript | 2026-09-20 |
| [willfish/pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev) | Jev decides what to keep. Compaction never rewrites the transcript. | 1 | TypeScript | 2026-09-19 |
| [Wionerlol/wechat-jev-hud](https://github.com/Wionerlol/wechat-jev-hud) | — | 1 | C# | 2026-09-21 |
| [wotai-dev/typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools) | A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 1… | 1 | TypeScript | 2026-09-22 |
| [wsoule/dispatch](https://github.com/wsoule/dispatch) | Source-available, git-native task tracking and AI-agent orchestration — tasks are markdown files in your repo | 1 | TypeScript | 2026-09-21 |
| [wustep/jev-playground](https://github.com/wustep/jev-playground) | Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI. | 1 | TypeScript | 2026-09-21 |
| [wuxie888/jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat) | 微信里的话不知道怎么接？macOS 悬浮聊天助手：识别消息意图与沟通风险，GPT 生成多种话术，Jev 评估候选，一键填入微信。话我帮你想，发送你来定。 | 1 | Python | 2026-09-22 |
| [wyattjoh/zen-bookmarks](https://github.com/wyattjoh/zen-bookmarks) | Extract, parse, and rewrite the Zen browser sidebar (pinned tabs, folders, workspaces) as portable JSON, YAML… | 1 | TypeScript | 2026-09-21 |
| [xienda/dsh-jev-verify](https://github.com/xienda/dsh-jev-verify) | Jev (TypeSafe System One) decision tools + live verification benchmark for DeepSeek Harness: jev_decision (ch… | 1 | JavaScript | 2026-09-22 |
| [xinyao27/jevonian](https://github.com/xinyao27/jevonian) | — | 1 | TypeScript | 2026-09-22 |
| [Xy2002/poker-jev-test-bench](https://github.com/Xy2002/poker-jev-test-bench) | Jev test bench — Texas Hold'em edition: live-fire testing of TypeSafe's Jev evaluation model through a React … | 1 | JavaScript | 2026-09-20 |
| [ynitto/sandbox](https://github.com/ynitto/sandbox) | — | 1 | Python | 2026-09-22 |
| [youshinh/md-memo](https://github.com/youshinh/md-memo) | A zero-latency, local-first Markdown scratchpad with offline AI (Ollama/vLLM) and autonomous IME control. Bui… | 1 | JavaScript | 2026-09-22 |
| [YuSa0-6/jeviews](https://github.com/YuSa0-6/jeviews) | Jev で repo 全体をコードレビューする CLI | 1 | TypeScript | 2026-09-20 |
| [Z761293629/pi-jev-helm](https://github.com/Z761293629/pi-jev-helm) | Pi extension that uses Jev task classification (via OpenRouter) to route each run to explicitly configured mo… | 1 | TypeScript | 2026-09-21 |
| [zadescoxp/kadeconsole](https://github.com/zadescoxp/kadeconsole) | Kade console is a bloomberg terminal type of analytical tool. | 1 | Python | 2026-09-21 |
| [zbush/jev-context](https://github.com/zbush/jev-context) | Codex code-search plugin using Jev relevance filtering with auditable token metrics | 1 | JavaScript | 2026-09-19 |
| [zerodegress/jevinf](https://github.com/zerodegress/jevinf) | Jev-like model inference engine + Jev-compatible API | 1 | Python | 2026-09-20 |
| [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) | awesome-awesome-jev | 1 | Python | 2026-09-22 |
| [zhirschtritt/typesafe-go](https://github.com/zhirschtritt/typesafe-go) | Idiomatic Go SDK for the TypeSafe AI API | 1 | Go | 2026-09-17 |
| [ZHYsfl/learn-jev](https://github.com/ZHYsfl/learn-jev) | a repo that helps you learn jev model. | 1 | Python | 2026-09-20 |
| [ziyu/system-one-sdk](https://github.com/ziyu/system-one-sdk) | Unified interface wrapper for system one models | 1 | JavaScript | 2026-09-20 |
| [zsoXi/FeedGate](https://github.com/zsoXi/FeedGate) | Safe-controls Chrome feed filter (v3.3.0) with TypeSafe Jev judgments, temporal topic mutes, repeat grouping,… | 1 | JavaScript | 2026-09-19 |
| [zurfyx/jev-browser-skill](https://github.com/zurfyx/jev-browser-skill) | Let Jev, TypeSafe's ~100ms decision model, drive your browser. A plug-and-play skill for Claude Code and Code… | 1 | JavaScript | 2026-09-21 |
| [0-kay/fillo-career-glide](https://github.com/0-kay/fillo-career-glide) | — | 0 | TypeScript | 2026-09-22 |
| [007M7/jev-chat](https://github.com/007M7/jev-chat) | — | 0 | Python | 2026-09-22 |
| [0M4R0/jev-discord-bot](https://github.com/0M4R0/jev-discord-bot) | — | 0 | Python | 2026-09-21 |
| [0x1f/pi-jev-multi-provider](https://github.com/0x1f/pi-jev-multi-provider) | Pi Jev System One integration with TypeSafe Direct and Vercel AI Gateway transports | 0 | TypeScript | 2026-09-22 |
| [0xagentlabs/jev-xiangqi](https://github.com/0xagentlabs/jev-xiangqi) | Jev System One powered Chinese chess arena | 0 | TypeScript | 2026-09-22 |
| [0xArx/jevegis](https://github.com/0xArx/jevegis) | Guardrails for LLM apps in one API call. Prompt injection, jailbreaks, leaks, unsafe content. Built on TypeSa… | 0 | TypeScript | 2026-09-18 |
| [0xm0w/ship-checklist](https://github.com/0xm0w/ship-checklist) | The final check pass for shipping web apps: mechanical gates + AI-judged quality scoring + is-agentic measure… | 0 | Python | 2026-09-21 |
| [121212165/jev-ecosystem-analysis](https://github.com/121212165/jev-ecosystem-analysis) | JEV 生态普查全量过程资产：259 库清单 · 9 批 stay/go 矩阵 · 11 深读档 · 复审 gold 数据集（CC-BY-4.0 + MIT） | 0 | Python | 2026-09-20 |
| [14-TR/jev-empirical](https://github.com/14-TR/jev-empirical) | Jev empirical studies and hybrid Incident Room app: https://14-tr.github.io/jev-empirical/apps/incident-room/ | 0 | Python | 2026-09-21 |
| [1aifanatic/jev-uipath-coded-agent](https://github.com/1aifanatic/jev-uipath-coded-agent) | FINS demo: a UiPath coded agent for AML alert triage where every decision is made by TypeSafe's Jev model (No… | 0 | Python | 2026-09-21 |
| [1npo/jev-gmail-labeler](https://github.com/1npo/jev-gmail-labeler) | A tool that uses Jev and the GMail API to organize your emails with labels. | 0 | Python | 2026-09-21 |
| [1ove9/yaf-goai-semifinal](https://github.com/1ove9/yaf-goai-semifinal) | Auditable antenna exploration environment for GOAI 2026 Track 3, with preregistration, solver-gated validatio… | 0 | Python | 2026-09-20 |
| [2389-research/jev-plays-pokemon](https://github.com/2389-research/jev-plays-pokemon) | — | 0 | Python | 2026-09-21 |
| [2389-research/judgement](https://github.com/2389-research/judgement) | A Go CLI for TypeSafe Jev judgments, with JSON input/output and optional caching | 0 | Go | 2026-09-20 |
| [2686521696/panwatch-Jev](https://github.com/2686521696/panwatch-Jev) | — | 0 | Python | 2026-09-21 |
| [2commits/typesafe-systemone](https://github.com/2commits/typesafe-systemone) | Unofficial async Rust client for the TypeSafe System One API (Jev) | 0 | Rust | 2026-09-21 |
| [2nd1st/Jevsus](https://github.com/2nd1st/Jevsus) | What Jev answers when the only options are true and false. 3,539 statements put to TypeSafe's System One mode… | 0 | Python | 2026-09-21 |
| [33Audits/jev-auto](https://github.com/33Audits/jev-auto) | Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibr… | 0 | — | 2026-09-20 |
| [4esv/jev-joust](https://github.com/4esv/jev-joust) | TypeSafe Jev vs Jev in NES Joust, bring your own ROM | 0 | Python | 2026-09-21 |
| [54k41/darkforest-swordholder](https://github.com/54k41/darkforest-swordholder) | Chatbot web em um único arquivo HTML com roteamento de modelos via Jev (modos Pro e Lite) e RAG vetorial com … | 0 | HTML | 2026-09-21 |
| [674019130/674019130.github.io](https://github.com/674019130/674019130.github.io) | — | 0 | Vue | 2026-09-22 |
| [7starsseeker/dsh-jev-guard](https://github.com/7starsseeker/dsh-jev-guard) | DeepSeek Harness (DSH) 执行前安全阀门:bash/pwsh 真正执行前先经静态规则 + TypeSafe Jev 语义判定,破坏性操作按 允许/修正/拦截/上报人工 四态处置,含额度降级与审计日志。 | 0 | JavaScript | 2026-09-21 |
| [99hansling/bb-jev-browser](https://github.com/99hansling/bb-jev-browser) | — | 0 | JavaScript | 2026-09-21 |
| [9KenM/sentimoiji](https://github.com/9KenM/sentimoiji) | Generates expressive emoji based on the emotional sentiment of a piece of text | 0 | TypeScript | 2026-09-19 |
| [9sako6/learn-jev](https://github.com/9sako6/learn-jev) | — | 0 | — | 2026-09-20 |
| [aamanlamba/jev-explore](https://github.com/aamanlamba/jev-explore) | An example repository for exploring Jev - the System One model | 0 | Python | 2026-09-19 |
| [aarora79/jev-samples](https://github.com/aarora79/jev-samples) | Runnable samples for Jev, TypeSafe AI's System One model. Send state and questions carrying their own answer … | 0 | — | 2026-09-20 |
| [abdelrahmanmagdii/jevci](https://github.com/abdelrahmanmagdii/jevci) | — | 0 | Go | 2026-09-20 |
| [AbdelStark/reachy-jev](https://github.com/AbdelStark/reachy-jev) | Typed Jev decision primitives for Reachy Mini applications. | 0 | TypeScript | 2026-09-22 |
| [abhay-2108/agent-foundry](https://github.com/abhay-2108/agent-foundry) | — | 0 | Python | 2026-09-20 |
| [abhibansal60/tidy](https://github.com/abhibansal60/tidy) | Keeps your YouTube subscriptions current: Jev judges, code sets the limits, you approve. Watch-history discov… | 0 | Python | 2026-09-21 |
| [abhishekmishragithub/semantic-microscope](https://github.com/abhishekmishragithub/semantic-microscope) | Label every sentence of a document with calibrated probabilities from Jev, rendered as a heatmap | 0 | Python | 2026-09-22 |
| [abinashray008/fraud-classifier](https://github.com/abinashray008/fraud-classifier) | Real-time card-transaction fraud classifier: Jev (System One) with an optional LLM investigation tier. | 0 | Python | 2026-09-22 |
| [ably-labs/jev-pong](https://github.com/ably-labs/jev-pong) | Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and ag… | 0 | TypeScript | 2026-09-19 |
| [AbstractFruitFactory/loremaster](https://github.com/AbstractFruitFactory/loremaster) | — | 0 | TypeScript | 2026-09-22 |
| [acoyfellow/edit](https://github.com/acoyfellow/edit) | A small, approval-first Pi tool for safe, checked code changes. | 0 | Elixir | 2026-09-21 |
| [adagora/jev-experiments](https://github.com/adagora/jev-experiments) | — | 0 | TypeScript | 2026-09-21 |
| [adamjralph/skill-broker](https://github.com/adamjralph/skill-broker) | Deterministic pre-agent skill routing for Hermes agents: audit, canonical catalog, profile policy, and bounde… | 0 | Python | 2026-09-21 |
| [adamtopaz/jevhammer](https://github.com/adamtopaz/jevhammer) | — | 0 | Lean | 2026-09-22 |
| [adamtopaz/jevhammer_benchmark](https://github.com/adamtopaz/jevhammer_benchmark) | — | 0 | Python | 2026-09-22 |
| [adamtopaz/jevselector](https://github.com/adamtopaz/jevselector) | — | 0 | Lean | 2026-09-22 |
| [adebmbng/jev-trade-prediction](https://github.com/adebmbng/jev-trade-prediction) | — | 0 | TypeScript | 2026-09-20 |
| [adhamelhayek-lab/jev-connector](https://github.com/adhamelhayek-lab/jev-connector) | — | 0 | JavaScript | 2026-09-20 |
| [adigulalkari/Jev_GC](https://github.com/adigulalkari/Jev_GC) | — | 0 | Python | 2026-09-22 |
| [adihex/typesafeai-fafo](https://github.com/adihex/typesafeai-fafo) | Jev-as-merge-adjudicator fafo: selector-not-generator harness | 0 | TypeScript | 2026-09-20 |
| [adlternative/tally](https://github.com/adlternative/tally) | Turn a pile of comments into an auditable distribution: Jev judges each item, code counts the percentages. Re… | 0 | Python | 2026-09-22 |
| [adnanlah/scopus-smart-search](https://github.com/adnanlah/scopus-smart-search) | Smart Scopus search with Jev | 0 | TypeScript | 2026-09-20 |
| [AdoCbl/JEV-RESUME-POLISHER](https://github.com/AdoCbl/JEV-RESUME-POLISHER) | AI resume polisher that fact-checks every line it writes against your real resume — no invented metrics, no i… | 0 | Python | 2026-09-22 |
| [advayc/instructional-agent](https://github.com/advayc/instructional-agent) | teach you how to do anything on your computer (using jev and openrouter) | 0 | Swift | 2026-09-21 |
| [advision-development/jevicle](https://github.com/advision-development/jevicle) | Jev LLM Skills | 0 | Python | 2026-09-20 |
| [aesgalexis/model-switch](https://github.com/aesgalexis/model-switch) | Local model and reasoning router for OpenAI Codex, powered by TypeSafe Jev. | 0 | JavaScript | 2026-09-21 |
| [agaches/jev-test](https://github.com/agaches/jev-test) | Hook PreToolUse Claude Code adossé à Jev : décision de sécurité typée, pré-filtre anti-exfiltration local, re… | 0 | Shell | 2026-09-21 |
| [agentik-os/jev-radar](https://github.com/agentik-os/jev-radar) | — | 0 | JavaScript | 2026-09-22 |
| [Ahmadnmic/autocorrecter](https://github.com/Ahmadnmic/autocorrecter) | Inline contextual autocorrect: web preview, desktop app (macOS/Windows), Android keyboard, Jev + Claude Haiku… | 0 | TypeScript | 2026-09-22 |
| [ahtcfg24/codex-speculator](https://github.com/ahtcfg24/codex-speculator) | Read-only speculative tool execution PoC for Codex with Jev: explicit metrics, safe candidate tools, and loca… | 0 | TypeScript | 2026-09-22 |
| [AHTOOOXA/jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit) | Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliabilit… | 0 | Python | 2026-09-21 |
| [AI-PM-Wiki/aipm-annotation-server](https://github.com/AI-PM-Wiki/aipm-annotation-server) | AI-PM Wiki 自建批注后端:GitHub OAuth + 公开/私有批注存储 + Jev/LLM 智能高亮 judge(子模块,主仓库 AI-PM-Wiki/AIPM) | 0 | TypeScript | 2026-09-22 |
| [aidanobrien5599/smartpaste](https://github.com/aidanobrien5599/smartpaste) | Cmd-V pastes the answer the field is asking for, chosen from your own resume by Jev. Chrome extension + CLI. | 0 | JavaScript | 2026-09-22 |
| [aieo-product/jev-gamebenchmark](https://github.com/aieo-product/jev-gamebenchmark) | Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-… | 0 | Python | 2026-09-18 |
| [AiPersonacademy/jev-sales-radar](https://github.com/AiPersonacademy/jev-sales-radar) | Live Sub-25ms Sales AI Teleprompter & Objection Anticipation Engine in Rust. Anticipates prospect subtext and… | 0 | HTML | 2026-09-21 |
| [Aitejiu/jev-harness-lab](https://github.com/Aitejiu/jev-harness-lab) | — | 0 | Python | 2026-09-21 |
| [aiwithenoch/Jev-Skill](https://github.com/aiwithenoch/Jev-Skill) | Open-source Jev harness for TypeSafe, OpenJev, LocalJev, Ollama, vLLM, LM Studio, llama.cpp. Typed decisions,… | 0 | Python | 2026-09-22 |
| [akaiHuang/btc-dual-ai-trader](https://github.com/akaiHuang/btc-dual-ai-trader) | Dual-AI crypto trading system: one model for strategy/analysis and another for low-latency execution. | 0 | Python | 2026-02-11 |
| [akanthed/jev-migrate](https://github.com/akanthed/jev-migrate) | — | 0 | TypeScript | 2026-09-21 |
| [akash-kamat/jev-llm](https://github.com/akash-kamat/jev-llm) | An LLM built without a language model — using TypeSafe Jev's non-generative AI for contextual response select… | 0 | JavaScript | 2026-09-21 |
| [akeldgord/JevDeck](https://github.com/akeldgord/JevDeck) | — | 0 | TypeScript | 2026-09-21 |
| [AkhilBod/Tidy](https://github.com/AkhilBod/Tidy) | Rules + Jev classification that keep a Mac organized. Reversible, privacy-conscious, never deletes. | 0 | TypeScript | 2026-09-22 |
| [AkiraWinds/jev-game](https://github.com/AkiraWinds/jev-game) | — | 0 | Python | 2026-09-20 |
| [akollegger/zebra-space](https://github.com/akollegger/zebra-space) | — | 0 | TypeScript | 2026-09-21 |
| [akrupa-appto/sash](https://github.com/akrupa-appto/sash) | Browser tasks with Jev, optional LLM planning, and Anchor Browser. | 0 | JavaScript | 2026-09-21 |
| [Alberto-Codes/judgevet](https://github.com/Alberto-Codes/judgevet) | Typed client, CLI and MCP server for TypeSafe's Jev (System One) judgment model | 0 | Python | 2026-09-22 |
| [aldemirkonuk/RestaurantAIAutomation](https://github.com/aldemirkonuk/RestaurantAIAutomation) | Full Business Backend for Restaurant Inventory Systems | 0 | TypeScript | 2026-09-22 |
| [alecstein/rceb-repair-form](https://github.com/alecstein/rceb-repair-form) | — | 0 | JavaScript | 2026-09-17 |
| [alektebel/jev-mindustry](https://github.com/alektebel/jev-mindustry) | — | 0 | Python | 2026-09-20 |
| [Aleskyy/Jevsona](https://github.com/Aleskyy/Jevsona) | — | 0 | TypeScript | 2026-09-21 |
| [alex-sun-kuo/jev-consumer-research](https://github.com/alex-sun-kuo/jev-consumer-research) | Consumer research explorations using TypeSafe's Jev | 0 | Jupyter Notebook | 2026-09-18 |
| [AlexanderJiazx/AutoJev](https://github.com/AlexanderJiazx/AutoJev) | — | 0 | Python | 2026-09-22 |
| [alexbejan/jevkit](https://github.com/alexbejan/jevkit) | TypeSafe Jev as a bounded judgement layer for computer use: verify, pick, classify over Cua Driver and phone-… | 0 | Python | 2026-09-18 |
| [alexei-led/pi-model-router](https://github.com/alexei-led/pi-model-router) | Independent Pi extension for four-tier model routing with optional privacy-gated Jev advice, deterministic ba… | 0 | TypeScript | 2026-09-21 |
| [alexhawat/jev-catalog-gate](https://github.com/alexhawat/jev-catalog-gate) | Pre-LLM catalog gate: TypeSafe/Jev scores tools & skills; keep only high-probability items | 0 | — | 2026-09-19 |
| [alexhawat/judge-jev](https://github.com/alexhawat/judge-jev) | Jev-native LLM output judge kit (skill + agents + core) | 0 | Rust | 2026-09-21 |
| [alexshpunt/pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman) | Send Pi agents back to work when they stop before the job is done. | 0 | TypeScript | 2026-09-17 |
| [alexykn/jevscan](https://github.com/alexykn/jevscan) | custom linter with treesitter + jev | 0 | Python | 2026-09-20 |
| [ali-abassi/pi-jev](https://github.com/ali-abassi/pi-jev) | Jev advisor for the pi coding agent: loop detection + goal-alignment steers | 0 | Shell | 2026-09-18 |
| [alibowbow/jev](https://github.com/alibowbow/jev) | — | 0 | JavaScript | 2026-09-21 |
| [AliyuYahaya/ritza-typesafe-trial](https://github.com/AliyuYahaya/ritza-typesafe-trial) | — | 0 | — | 2026-08-14 |
| [AliZareh-CoE/JevRev](https://github.com/AliZareh-CoE/JevRev) | Narrow a literature review with Jev: typed, calibrated relevance judgments over abstracts and paragraphs. | 0 | Python | 2026-09-21 |
| [allenporter/home-assistant-laya](https://github.com/allenporter/home-assistant-laya) | Conversation agent based on Laya, a multilingual, non-autoregressive System 1 decision model. | 0 | Python | 2026-09-22 |
| [allenporter/home-assistant-typesafe](https://github.com/allenporter/home-assistant-typesafe) | Home Assistant conversation integration powered by the Jev / TypeSafe AI API for fast, structured intent rout… | 0 | Python | 2026-09-21 |
| [alMohimanul/jev-play](https://github.com/alMohimanul/jev-play) | — | 0 | TypeScript | 2026-09-21 |
| [alonsarias/adjudge](https://github.com/alonsarias/adjudge) | — | 0 | TypeScript | 2026-09-20 |
| [alperiox/audio-jevlike](https://github.com/alperiox/audio-jevlike) | Prosodia: an audio-native Jev-shaped decision model — typed calibrated decisions from speech, no ASR | 0 | Python | 2026-09-21 |
| [alsoleg89/jev-bouncer](https://github.com/alsoleg89/jev-bouncer) | Claude Code plugin: a 3-cent bouncer for your agent's shell. Jev typed probabilities auto-allow routine comma… | 0 | Python | 2026-09-20 |
| [ALucky1/jevf-cursor](https://github.com/ALucky1/jevf-cursor) | A drop-in custom cursor for the web that plays a sound when you click. | 0 | HTML | 2026-09-21 |
| [amaljithkuttamath/amaljithkuttamath.github.io](https://github.com/amaljithkuttamath/amaljithkuttamath.github.io) | — | 0 | TypeScript | 2026-09-19 |
| [amansoory/JEV2048](https://github.com/amansoory/JEV2048) | — | 0 | C++ | 2026-09-19 |
| [amapara27/jev-pilot](https://github.com/amapara27/jev-pilot) | control your desktop smoothly. powered by typesafe's jev. | 0 | Swift | 2026-09-22 |
| [amberwhitehead/jevscript](https://github.com/amberwhitehead/jevscript) | — | 0 | JavaScript | 2026-09-17 |
| [Amidwestnoob/being-compacted](https://github.com/Amidwestnoob/being-compacted) | Lossless tool-row context compact. No summarizer. No Jev. | 0 | TypeScript | 2026-09-19 |
| [amoreX/jevvy](https://github.com/amoreX/jevvy) | Some cool experiments with jev jevvy | 0 | TypeScript | 2026-09-21 |
| [an-author-1/gisbey-lab](https://github.com/an-author-1/gisbey-lab) | Gibsey Lab explores Field Intelligence through QDPI: a laboratory for context assembly, literary navigation, … | 0 | Python | 2026-09-20 |
| [andrewdeng318/paperclip-plugin-jev](https://github.com/andrewdeng318/paperclip-plugin-jev) | Community Paperclip plugin for Jev-powered issue triage and automatic routing. | 0 | TypeScript | 2026-09-21 |
| [andreylukin/jev-bcp](https://github.com/andreylukin/jev-bcp) | BrowseComp-Plus with a cheap LLM and Jev (TypeSafe's non-generative classifier): agent pipeline, the jevlog l… | 0 | Python | 2026-09-21 |
| [anduriroshan/jev-doom-game](https://github.com/anduriroshan/jev-doom-game) | — | 0 | Python | 2026-09-21 |
| [Andymulb/jev_the_philosopher](https://github.com/Andymulb/jev_the_philosopher) | Measuring a decision model's moral judgements: constant latency regardless of difficulty, sensitivity to fram… | 0 | TeX | 2026-09-21 |
| [AndyTheFactory/jev-skill](https://github.com/AndyTheFactory/jev-skill) | — | 0 | Python | 2026-09-21 |
| [angadjosan/Jevplayground](https://github.com/angadjosan/Jevplayground) | — | 0 | Python | 2026-09-19 |
| [angribot/pi-jev](https://github.com/angribot/pi-jev) | Single-file pi extension for batched TypeSafe Jev judgments | 0 | TypeScript | 2026-09-22 |
| [aninibread/jev-dino](https://github.com/aninibread/jev-dino) | — | 0 | TypeScript | 2026-09-22 |
| [aniruddh-krovvidi/switchboard](https://github.com/aniruddh-krovvidi/switchboard) | Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/… | 0 | Python | 2026-09-20 |
| [ankitdey01/tract](https://github.com/ankitdey01/tract) | — | 0 | TypeScript | 2026-09-21 |
| [ankitkapooor/autocode](https://github.com/ankitkapooor/autocode) | OrthoCode AI is an evidence-first orthopedic medical-coding platform. Its runtime is constrained to a normali… | 0 | Python | 2026-09-20 |
| [annadmin-cyber/jevvvvvvvvvvvvvvvvv](https://github.com/annadmin-cyber/jevvvvvvvvvvvvvvvvv) | — | 0 | — | 2026-09-20 |
| [ansidium/jev-codex-bridge](https://github.com/ansidium/jev-codex-bridge) | Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates | 0 | JavaScript | 2026-09-20 |
| [anthony-maio/codex-decision-layer](https://github.com/anthony-maio/codex-decision-layer) | Shadow-mode evidence selection for Codex with Jev, local Eve FP32, and Q8 GGUF. CLI, MCP server, plugin, and … | 0 | Python | 2026-09-21 |
| [AnthusAI/Jev-Flywheel](https://github.com/AnthusAI/Jev-Flywheel) | Jev plus a decision head that learns from feedback: can a loop name a bias we planted in our own dataset? | 0 | Python | 2026-09-22 |
| [antoniofaical/digital-twin-classifier-jev](https://github.com/antoniofaical/digital-twin-classifier-jev) | — | 0 | Python | 2026-09-22 |
| [Antony-Jia/JevChromePlugin](https://github.com/Antony-Jia/JevChromePlugin) | Chrome extension for scoring X and Weibo posts with Jev, with optional LLM deep analysis and Tavily-powered w… | 0 | JavaScript | 2026-09-21 |
| [Anxiety471/idle-mmo-bot](https://github.com/Anxiety471/idle-mmo-bot) | Deterministic Idle MMO browser automation with Jev hooks for non-deterministic decisions | 0 | TypeScript | 2026-09-22 |
| [AnyEvalOrg/eval-jevbench](https://github.com/AnyEvalOrg/eval-jevbench) | JevBench (typed decision models) as an AnyEval-format inspect_ai eval | 0 | Python | 2026-09-22 |
| [AO-HyS/development-system](https://github.com/AO-HyS/development-system) | Canonical, installable, and reversible AOHYS multi-harness development contract. | 0 | JavaScript | 2026-09-22 |
| [aoi-yoneda/haikyuBattleJev](https://github.com/aoi-yoneda/haikyuBattleJev) | Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風 | 0 | HTML | 2026-09-20 |
| [aoprisan/jev-demo](https://github.com/aoprisan/jev-demo) | — | 0 | Rust | 2026-09-19 |
| [aoprisan/jev-ts-repl](https://github.com/aoprisan/jev-ts-repl) | — | 0 | TypeScript | 2026-09-21 |
| [api-evangelist/typesafe-ai](https://github.com/api-evangelist/typesafe-ai) | TypeSafe AI is a San Francisco AI lab building System One models — a class of model trained to return typed, … | 0 | — | 2026-09-20 |
| [ar077685-beep/jevansrot](https://github.com/ar077685-beep/jevansrot) | — | 0 | TypeScript | 2026-09-18 |
| [Arby2026/PolyJev](https://github.com/Arby2026/PolyJev) | — | 0 | Python | 2026-09-21 |
| [ariasnico/jevtest](https://github.com/ariasnico/jevtest) | Un laboratorio para construir algo creativo, divertido y útil con Jev de TypeSafe AI. | 0 | JavaScript | 2026-09-21 |
| [arieprasetyo-ecomindo/scorer_cli](https://github.com/arieprasetyo-ecomindo/scorer_cli) | deterministic and system-one model tools to determine the quality of a project | 0 | Python | 2026-09-22 |
| [aryamangoenka/traceassert](https://github.com/aryamangoenka/traceassert) | you already test your code. this tests what your agent actually did (powered by jev) | 0 | Python | 2026-09-22 |
| [Ascurse/typed-judge-kit](https://github.com/Ascurse/typed-judge-kit) | Typed questions to a model, verdict in code, thresholds from your labels | 0 | Python | 2026-09-21 |
| [AseemPrasad/JevGuard](https://github.com/AseemPrasad/JevGuard) | JevGuard : Deterministic Runtime Governance, Reliability & Evaluation Engine for Structured AI Systems | 0 | Go | 2026-09-20 |
| [asfarsadewa/werewolf](https://github.com/asfarsadewa/werewolf) | Werewolf against seven villagers whose suspicions are calibrated probabilities from TypeSafe Jev | 0 | TypeScript | 2026-09-19 |
| [ashaazami/river-run-typesafe](https://github.com/ashaazami/river-run-typesafe) | River shooter game in Python, inspired by Atari's River Raid, played by a TypeSafe AI pilot | 0 | Python | 2026-09-18 |
| [Ashadeepa/typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase) | Next.js UI showing off TypeSafe's System One model (Jev) — parallel Noul judgments and a Choice-based citatio… | 0 | TypeScript | 2026-09-21 |
| [Ashton-Sidhu/solus](https://github.com/Ashton-Sidhu/solus) | — | 0 | TypeScript | 2026-09-20 |
| [asmirrr/DriftLab](https://github.com/asmirrr/DriftLab) | Reproducible quantitative research CLI for testing momentum strategies and auditing research methodology with… | 0 | Python | 2026-09-21 |
| [AustinDKB/grass-optimizer](https://github.com/AustinDKB/grass-optimizer) | Daily SK lawn watering and winter shutdown schedule — hydrology in code, Jev for growth/rain/freeze judgments. | 0 | Python | 2026-09-21 |
| [automaticdai/jev-linux-cleaner](https://github.com/automaticdai/jev-linux-cleaner) | — | 0 | Python | 2026-09-21 |
| [AutoPasha/jevcode](https://github.com/AutoPasha/jevcode) | Coding agent driven by a model that cannot write text | 0 | Python | 2026-09-21 |
| [aviz85/jev-lab](https://github.com/aviz85/jev-lab) | — | 0 | TypeScript | 2026-09-22 |
| [AydinAdnan/ai-email-agent](https://github.com/AydinAdnan/ai-email-agent) | AI email agent simulation using Jev + LLM hybrid model | 0 | HTML | 2026-09-20 |
| [Ayush0054/menso](https://github.com/Ayush0054/menso) | — | 0 | Swift | 2026-09-18 |
| [az9713/jev-email-triage](https://github.com/az9713/jev-email-triage) | Email triage with Jev (TypeSafe) over the Vercel AI Gateway | 0 | JavaScript | 2026-09-20 |
| [az9713/jev-projects](https://github.com/az9713/jev-projects) | Small demos of Jev (TypeSafe) through the Vercel AI Gateway: wiki race, town of agents, bullet chess, and more | 0 | JavaScript | 2026-09-21 |
| [azumag/soviet_now](https://github.com/azumag/soviet_now) | Soviet Game Auto Play with AI | 0 | Python | 2026-09-22 |
| [B0und/jev_content_filter](https://github.com/B0und/jev_content_filter) | — | 0 | TypeScript | 2026-09-19 |
| [badroneai/eventlive-sa](https://github.com/badroneai/eventlive-sa) | — | 0 | JavaScript | 2026-09-21 |
| [bahramzada/jev-canvas](https://github.com/bahramzada/jev-canvas) | — | 0 | JavaScript | 2026-09-21 |
| [bahramzada/jev-taxi-dispatch](https://github.com/bahramzada/jev-taxi-dispatch) | Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə | 0 | JavaScript | 2026-09-18 |
| [Bald0Wang/jev-playground](https://github.com/Bald0Wang/jev-playground) | Jev 决策模型游乐场：斗地主 / 21点 / 数独（纯标准库）+ TypeSafe Mario 真机复现研究 | 0 | Python | 2026-09-22 |
| [basmilius/homey-jev](https://github.com/basmilius/homey-jev) | Jev - AI decisions in your Homey Flows. | 0 | TypeScript | 2026-09-21 |
| [bavovna/jev-like-srv](https://github.com/bavovna/jev-like-srv) | jev HTTP router framework compatible with typesafe API | 0 | Makefile | 2026-09-22 |
| [bdecrem/hilma](https://github.com/bdecrem/hilma) | — | 0 | TypeScript | 2026-09-22 |
| [bebe0307mz/jevs-kitchen-chaos](https://github.com/bebe0307mz/jevs-kitchen-chaos) | 3D Overcooked-style AI benchmark: four chefs driven per-decision by the Jev decision model or frontier LLMs (… | 0 | TypeScript | 2026-09-19 |
| [beejsbj/voice-gate](https://github.com/beejsbj/voice-gate) | Self-hosted Jev voice and text decision engine. HTTP, CLI and MCP integrations for your devices and assistant… | 0 | Python | 2026-09-21 |
| [behindthedash/worktrail](https://github.com/behindthedash/worktrail) | Spec-format-agnostic task orchestration: parallel git-worktree fan-out execution, a deterministic route class… | 0 | Python | 2026-09-21 |
| [beingcognitive/jev-go](https://github.com/beingcognitive/jev-go) | Can you beat Jev at Gomoku, Go or chess? Play TypeSafe's System One decision model on Cloudflare Pages, with … | 0 | JavaScript | 2026-09-22 |
| [BeLazy167/argus](https://github.com/BeLazy167/argus) | Self-hostable AI code review GitHub App — multi-pass specialist review pipeline posts inline PR comments with… | 0 | Go | 2026-09-21 |
| [benson/inflection](https://github.com/benson/inflection) | Explore how small wording changes shift Jev's probability distributions | 0 | TypeScript | 2026-09-21 |
| [bestony/bestony-userscripts](https://github.com/bestony/bestony-userscripts) | Personal userscripts | 0 | JavaScript | 2026-09-20 |
| [bfalkowski/jev-experiments](https://github.com/bfalkowski/jev-experiments) | — | 0 | Python | 2026-09-21 |
| [bidurkhatri/jev-mcp-lab](https://github.com/bidurkhatri/jev-mcp-lab) | — | 0 | JavaScript | 2026-09-19 |
| [Bigthap/canvas-quiz-ai-solver](https://github.com/Bigthap/canvas-quiz-ai-solver) | High-performance Canvas LMS quiz assistant & scraper designed for TypeSafe AI System One decision primitives | 0 | JavaScript | 2026-09-20 |
| [BILLKISHORE/opensysone](https://github.com/BILLKISHORE/opensysone) | Open System One model for Apple Silicon: typed decisions with calibrated probabilities from one forward pass. | 0 | Python | 2026-09-21 |
| [binbandit/local-laya](https://github.com/binbandit/local-laya) | — | 0 | TypeScript | 2026-09-21 |
| [BingelsWorth/JudgeJev](https://github.com/BingelsWorth/JudgeJev) | DeepThink meets llm as judge. Use heavy prefill caching to run the same request in parallel and let Jev give … | 0 | TypeScript | 2026-09-21 |
| [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines | 0 | Jupyter Notebook | 2026-09-18 |
| [Biztactix/n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe) | Typesafe AI Node for N8N | 0 | TypeScript | 2026-09-21 |
| [blazskufca/typesafe-sdk-go](https://github.com/blazskufca/typesafe-sdk-go) | Community SDK for Typesafe.ai in Go | 0 | Go | 2026-09-19 |
| [blck-snwmn/playground-jev](https://github.com/blck-snwmn/playground-jev) | Small apps for experimenting with Jev. | 0 | TypeScript | 2026-09-21 |
| [BleedingDev/fastest-e2e](https://github.com/BleedingDev/fastest-e2e) | — | 0 | TypeScript | 2026-09-21 |
| [blisspixel/fragr](https://github.com/blisspixel/fragr) | Agentic-first retro 3D arena FPS: Rust authoritative server, Godot client, MCP door for agents, in-game pirat… | 0 | Rust | 2026-09-22 |
| [BlueLvRen/lvren-jev](https://github.com/BlueLvRen/lvren-jev) | 自用codex对接jev的工具 | 0 | Python | 2026-09-21 |
| [bogusweb/cv-by-jev](https://github.com/bogusweb/cv-by-jev) | — | 0 | TypeScript | 2026-09-20 |
| [bogusweb/ship-game-with-jev](https://github.com/bogusweb/ship-game-with-jev) | — | 0 | TypeScript | 2026-09-21 |
| [bojansandhaus/jev-lcm-dsh-compaction](https://github.com/bojansandhaus/jev-lcm-dsh-compaction) | Calibrated Jev ranking before lossless context condensation | 0 | TypeScript | 2026-09-22 |
| [bojansandhaus/jev-lcm-hermes-compaction](https://github.com/bojansandhaus/jev-lcm-hermes-compaction) | Calibrated Jev ranking before lossless context condensation | 0 | Python | 2026-09-22 |
| [bonsai/furui](https://github.com/bonsai/furui) | エラトステネスの篩 — jev + ML埋め込みでフォルダを意味ごとに振るう整理の槍 (py/ts/rs) | 0 | Python | 2026-09-21 |
| [boredrhino/Jevston](https://github.com/boredrhino/Jevston) | Jevston's code (Partially) + CA: 0xaE9CB22e1cd73eC92D00903F2C2c41cC805b9C52 | 0 | HTML | 2026-09-22 |
| [boriscardano/herdr-jev-router](https://github.com/boriscardano/herdr-jev-router) | Mandatory Jev-based routing for Herdr-managed agent spawns | 0 | Python | 2026-09-21 |
| [bornakapusta/slop-guard](https://github.com/bornakapusta/slop-guard) | Guideline-driven code review bot for Ruby: code finds what to inspect, TypeSafe Jev judges it, explicit rules… | 0 | Ruby | 2026-09-20 |
| [bottlebrushes/jev-orb](https://github.com/bottlebrushes/jev-orb) | Siri-style push-to-talk voice orb for autonomous browser control with Jev and Metal Whisper | 0 | Makefile | 2026-09-19 |
| [box-community/box-jev-incident-triage](https://github.com/box-community/box-jev-incident-triage) | — | 0 | Python | 2026-09-18 |
| [bramtechs/Focus](https://github.com/bramtechs/Focus) | Browser extension that blocks distracting websites using TypeSafe: Jev | 0 | JavaScript | 2026-09-20 |
| [brandonbryant12/transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard) | ACME live support-call scoring demo with TypeSafe AI, Effect, SQLite, React, Vite, and Turborepo | 0 | TypeScript | 2026-09-17 |
| [braposo/bernardo-fit](https://github.com/braposo/bernardo-fit) | — | 0 | JavaScript | 2026-09-22 |
| [braustin20/pi-jev-guard](https://github.com/braustin20/pi-jev-guard) | A Jev-powered safety gate for Pi tool and shell calls | 0 | TypeScript | 2026-09-20 |
| [BrendanH18/jev-lab](https://github.com/BrendanH18/jev-lab) | Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do | 0 | Python | 2026-09-18 |
| [BrendanH18/jev_fsd](https://github.com/BrendanH18/jev_fsd) | JEV AI Model Demo with FSD | 0 | JavaScript | 2026-09-19 |
| [brickfrog/moongate](https://github.com/brickfrog/moongate) | moonbit CI gate with jev | 0 | MoonBit | 2026-09-20 |
| [brokensbone/media-collection-manager](https://github.com/brokensbone/media-collection-manager) | — | 0 | Python | 2026-09-21 |
| [BrunoAccorsi/reflex-lab](https://github.com/BrunoAccorsi/reflex-lab) | Jev playground and testing env | 0 | TypeScript | 2026-09-22 |
| [btcjon/agent-tools](https://github.com/btcjon/agent-tools) | Practical, guarded tools for AI agents—maintenance, skill discovery, email triage, harness routing, and conte… | 0 | Python | 2026-09-21 |
| [Btheriot83/jev-academy](https://github.com/Btheriot83/jev-academy) | Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot | 0 | TypeScript | 2026-09-19 |
| [BubbatheVTOG/pi-jev-anti-slop](https://github.com/BubbatheVTOG/pi-jev-anti-slop) | — | 0 | TypeScript | 2026-09-20 |
| [BubbatheVTOG/pi-jev-redact](https://github.com/BubbatheVTOG/pi-jev-redact) | — | 0 | TypeScript | 2026-09-21 |
| [buberlo/jev-pastepilot](https://github.com/buberlo/jev-pastepilot) | Explicit paste-to-action launcher that routes text to useful tools without automatic side effects. | 0 | TypeScript | 2026-09-20 |
| [Bud-ro/jev-demos](https://github.com/Bud-ro/jev-demos) | Demos to test the effectiveness of TypeSafe's "Jev" System One Model | 0 | Dart | 2026-09-18 |
| [bugkiwi/turing-jail](https://github.com/bugkiwi/turing-jail) | Turing Jail - Let's get out! | 0 | TypeScript | 2026-09-18 |
| [buildwithgagan/zynn-explorer](https://github.com/buildwithgagan/zynn-explorer) | Zynn Explorer: browse any Postgres database and query it in plain English, powered by TypeSafe Jev | 0 | JavaScript | 2026-09-21 |
| [builtbyrishabh/jev-plays-emerald](https://github.com/builtbyrishabh/jev-plays-emerald) | Watch Jev choose a starter and play Pokemon Emerald live, with deterministic emulator control. | 0 | Python | 2026-09-22 |
| [BunsDev/river-oaks](https://github.com/BunsDev/river-oaks) | NPCs of River Oaks Houston, Texas using Jev to power NPCs | 0 | JavaScript | 2026-09-22 |
| [bvicsay/adaptmypage](https://github.com/bvicsay/adaptmypage) | IntentFlags — semantic feature flags for websites, powered by Jev. Infers what a visitor is trying to do and … | 0 | TypeScript | 2026-09-21 |
| [caelaxie/crosshands](https://github.com/caelaxie/crosshands) | Local computer-use runtime for coding agents — JSON CLI + stdio MCP | 0 | TypeScript | 2026-09-22 |
| [cagbal/awesome-jev](https://github.com/cagbal/awesome-jev) | Curated list of jev related stuff | 0 | — | 2026-09-19 |
| [calebl/text-adventure](https://github.com/calebl/text-adventure) | AI generated text choose your own adventure game | 0 | Ruby | 2026-09-22 |
| [camodeny/new_dnd_testing_lol](https://github.com/camodeny/new_dnd_testing_lol) | — | 0 | Python | 2026-09-22 |
| [CamonZ/vertebrae](https://github.com/CamonZ/vertebrae) | — | 0 | Rust | 2026-09-21 |
| [capybara-brain346/jevtrieval](https://github.com/capybara-brain346/jevtrieval) | Jevtrieval is a retrieval-augmented generation demo. It retrieves documents from Qdrant, scores their relevan… | 0 | Python | 2026-09-22 |
| [caras-new-voices/jev-test-1](https://github.com/caras-new-voices/jev-test-1) | — | 0 | TypeScript | 2026-09-22 |
| [carlaiau/readwithjev](https://github.com/carlaiau/readwithjev) | A Demo of using JEV to classify various attributes of a book, and present that to the reader to augment the r… | 0 | TypeScript | 2026-09-19 |
| [carlchou0dailyfresh/jev-gates](https://github.com/carlchou0dailyfresh/jev-gates) | Composable three-valued semantic logic circuits powered by JEV. Stack small judgments into auditable decision… | 0 | TypeScript | 2026-09-22 |
| [cassiomc1/fast-jev-compaction-alt](https://github.com/cassiomc1/fast-jev-compaction-alt) | Continuous, verbatim context compaction for LLM agents using TypeSafe's Jev model. | 0 | TypeScript | 2026-09-19 |
| [catsonkeyboard/sgs](https://github.com/catsonkeyboard/sgs) | Lua/LÖVE2D 三国杀身份局：纯 Lua 规则引擎 + 牌桌 UI + LLM 驱动的 AI 玩家——任意座位可交给大模型托管，带跨步骤记忆推理隐藏身份，牌桌实时展示 AI 的身份猜测过程，支持联机对局。 | 0 | Lua | 2026-09-21 |
| [CeciliaW888/jev-town](https://github.com/CeciliaW888/jev-town) | A 3D town where 50 AI citizens each decide how to react to your broadcast, in parallel, in under a second - p… | 0 | TypeScript | 2026-09-20 |
| [cedarmuse-creator/jev-decision-maker-at-meteora](https://github.com/cedarmuse-creator/jev-decision-maker-at-meteora) | Decision Maker at Meteora - a decision agent for Meteora DLMM liquidity on Solana. Named after Jev, TypeSafe … | 0 | Python | 2026-09-21 |
| [cedrecs/jev-yarn](https://github.com/cedrecs/jev-yarn) | Y.A.R.N. inspired party game - everyone writes the next line in the story! TypeSafe's Jev (AI) judges your su… | 0 | JavaScript | 2026-09-22 |
| [Ceobe-dev/routerBasedJev](https://github.com/Ceobe-dev/routerBasedJev) | — | 0 | Python | 2026-09-22 |
| [chaewonkong/claude_evaluator](https://github.com/chaewonkong/claude_evaluator) | Claude answer evaluator with Jev | 0 | TypeScript | 2026-09-22 |
| [chalkychalk42/jev](https://github.com/chalkychalk42/jev) | A guide-directed leveling agent for a private TBC 2.4.3 server, built so it gets cheaper to run the longer it… | 0 | Python | 2026-09-21 |
| [chanrute/jev-ui](https://github.com/chanrute/jev-ui) | — | 0 | TypeScript | 2026-09-21 |
| [chanwata/jev-bassist](https://github.com/chanwata/jev-bassist) | — | 0 | Swift | 2026-09-22 |
| [chapel/hermes-jev-skills](https://github.com/chapel/hermes-jev-skills) | — | 0 | Python | 2026-09-17 |
| [charliejimi/reliable-hook-workshop](https://github.com/charliejimi/reliable-hook-workshop) | 自學工作坊：確定性 Cursor hook + deferred Jev 加註，六關 PR 驗收 | 0 | Python | 2026-09-21 |
| [CharryLee0426/jev-test](https://github.com/CharryLee0426/jev-test) | Testing TypeSafe's Jev model on real-time browser games (flappybird.io, play.tetris.com) | 0 | TypeScript | 2026-09-20 |
| [ChasLui/ds2jev](https://github.com/ChasLui/ds2jev) | — | 0 | TypeScript | 2026-09-20 |
| [ChasLui/vai2jev](https://github.com/ChasLui/vai2jev) | vercel ai-gateway 转换为标准TypeSafe-AI接口 | 0 | JavaScript | 2026-09-21 |
| [chaspy/jev-education](https://github.com/chaspy/jev-education) | — | 0 | HTML | 2026-09-21 |
| [chenhg5/jev-3d-world](https://github.com/chenhg5/jev-3d-world) | jev-3d-world | 0 | JavaScript | 2026-09-22 |
| [chewcw/project-scale-jev-demonstration](https://github.com/chewcw/project-scale-jev-demonstration) | — | 0 | TypeScript | 2026-09-21 |
| [chocochu/keeclub](https://github.com/chocochu/keeclub) | 棋聚 Kee Club — Jungle and Aeroplane Chess with friends, AI opponents, and offline same-device play. | 0 | TypeScript | 2026-09-18 |
| [chocopc123/jev-ai-ppon-grand-prix](https://github.com/chocopc123/jev-ai-ppon-grand-prix) | — | 0 | TypeScript | 2026-09-20 |
| [ChosenXu/raindrop-collection-governance](https://github.com/ChosenXu/raindrop-collection-governance) | Agent Skills-compatible skill: govern a Raindrop.io library's collection structure via raindrop-mcp — audit, … | 0 | Python | 2026-09-21 |
| [ChristianTracy/jev-terrarium-dinosaurs](https://github.com/ChristianTracy/jev-terrarium-dinosaurs) | Autonomous dinosaur ecosystem where code runs the physics and TypeSafe's Jev decides each creature's intent f… | 0 | Python | 2026-09-21 |
| [chuehnone/news](https://github.com/chuehnone/news) | 每日新聞重要性評分：5 面向 100 分制，SQLite + 靜態站 | 0 | Python | 2026-09-20 |
| [chungsubeen0/jevmcp](https://github.com/chungsubeen0/jevmcp) | Unofficial MCP for Jev | 0 | Python | 2026-09-18 |
| [Chunky83/jev-workbench](https://github.com/Chunky83/jev-workbench) | Jev Workbench: a C++ desktop workspace with Python diagnostics and structured TypeSafe evaluations | 0 | Python | 2026-09-21 |
| [cinjoff/firehorse](https://github.com/cinjoff/firehorse) | Firehorse agentic skills framework | 0 | TypeScript | 2026-09-21 |
| [cipherTing/sael](https://github.com/cipherTing/sael) | Go client for the TypeSafe System One API (Jev) — the first piece of sael, a content-safety classifier for an… | 0 | Go | 2026-09-22 |
| [cis2042/orca_agent](https://github.com/cis2042/orca_agent) | Oagent: Native Multi-Agent Orchestration & Desktop Workspace with Cursor CLI Resume & A2A Bridge | 0 | TypeScript | 2026-09-21 |
| [cjy5507/zerocode](https://github.com/cjy5507/zerocode) | Rust-native coding agent CLI with managed GitHub Release updates | 0 | Rust | 2026-09-22 |
| [claudialu0720/jevaiworks](https://github.com/claudialu0720/jevaiworks) | — | 0 | HTML | 2026-09-22 |
| [claudiuthree/dualtron-jev-parts-finder](https://github.com/claudiuthree/dualtron-jev-parts-finder) | — | 0 | JavaScript | 2026-09-21 |
| [clduab11/jev-test](https://github.com/clduab11/jev-test) | Pre-registered benchmark: can a 2B local model (Gemma 4 E2B) answer web questions without making things up wh… | 0 | Python | 2026-09-21 |
| [cloudbtl/JevRAG](https://github.com/cloudbtl/JevRAG) | Option-ready retrieval for decision models on the CloudBTL landing layer | 0 | Python | 2026-09-22 |
| [Clueless-Creations/Brigade](https://github.com/Clueless-Creations/Brigade) | Consumer-business primitives for AI agents: capabilities, providers, recipes, and evidence through a CLI, MCP… | 0 | TypeScript | 2026-09-22 |
| [Clueless-Creations/jev-ios-ultrafast](https://github.com/Clueless-Creations/jev-ios-ultrafast) | Run iOS Simulator goals with Jev, compare decision models, and replay every attempt. Python CLI and Brigade h… | 0 | Python | 2026-09-21 |
| [cmartinez9/jev-judge-bench](https://github.com/cmartinez9/jev-judge-bench) | Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and a… | 0 | — | 2026-09-18 |
| [cmk404/UGRP-Multi-Robot-Collaboration-Project](https://github.com/cmk404/UGRP-Multi-Robot-Collaboration-Project) | Private source for ugrp | 0 | Python | 2026-09-22 |
| [CN-AlbertWu96/DoomJev](https://github.com/CN-AlbertWu96/DoomJev) | — | 0 | Python | 2026-09-21 |
| [co1smos/jev-demo](https://github.com/co1smos/jev-demo) | Historical paper-trading simulator for evaluating TypeSafe AI JEV decisions | 0 | Python | 2026-09-22 |
| [codaaiteam/jev-mcp](https://github.com/codaaiteam/jev-mcp) | MCP server for Jev (TypeSafe AI's System One model) — give any agent typed, calibrated decisions: classify, s… | 0 | JavaScript | 2026-09-22 |
| [codebooker/NotchPilot](https://github.com/codebooker/NotchPilot) | A compact voice-first macOS assistant with local speech recognition, visible desktop actions, and a tiny notc… | 0 | Swift | 2026-09-22 |
| [CodeCampusCo/jev-mcp](https://github.com/CodeCampusCo/jev-mcp) | MCP server exposing one tool: ask Jev a typed question and get a short answer back. | 0 | TypeScript | 2026-09-20 |
| [coderexpert123/jev-browser-wingman](https://github.com/coderexpert123/jev-browser-wingman) | Browser automation where TypeSafe's Jev model picks each step. Attaches to an existing Chrome via CDP and run… | 0 | TypeScript | 2026-09-22 |
| [codesoda/systemone](https://github.com/codesoda/systemone) | One CLI and Jev-compatible API for local and hosted typed-decision backends (planning) | 0 | HTML | 2026-09-22 |
| [coding-hermes/auger](https://github.com/coding-hermes/auger) | Auger — spec drilling for the coding-hermes fleet: a CLI that interrogates a project into a git-backed spec o… | 0 | Python | 2026-09-21 |
| [cog-pr/jev-hackathon](https://github.com/cog-pr/jev-hackathon) | — | 0 | HTML | 2026-09-20 |
| [cognesy/instructor-polyglot](https://github.com/cognesy/instructor-polyglot) | \[READ-ONLY\] Access LLMs via unified API | 0 | PHP | 2026-09-17 |
| [colazeta/criminal_infiltration_in_legal_economy_review](https://github.com/colazeta/criminal_infiltration_in_legal_economy_review) | This repository is meant to store a systematic review on the topic of criminal infiltration in the legal econ… | 0 | Python | 2026-09-21 |
| [colbyford/jev-binder-classification](https://github.com/colbyford/jev-binder-classification) | Zero-Shot Classification of Protein Binders with Jev | 0 | Jupyter Notebook | 2026-09-21 |
| [colinmcdermott/grok-jev-router](https://github.com/colinmcdermott/grok-jev-router) | Jev decides, Grok Bot executes, humans control irreversible actions. A decision router for Grok Bot built on … | 0 | Python | 2026-09-21 |
| [community-ports/typesafeai-sdk-rust-community](https://github.com/community-ports/typesafeai-sdk-rust-community) | Community-built Rust SDK for the TypeSafe AI API (System One / Jev). A port of typesafe-sdk-python | 0 | Rust | 2026-09-21 |
| [computer-whisperer/within-reason](https://github.com/computer-whisperer/within-reason) | Within Reason (WReason): an AI opponent for Beyond All Reason — Rust AI shim for the Recoil engine, heuristic… | 0 | Rust | 2026-09-22 |
| [CondorCommodore/jev-git-graph](https://github.com/CondorCommodore/jev-git-graph) | Evidence-backed Jev relationship graph for Git branch consolidation | 0 | Python | 2026-09-22 |
| [copyleftdev/braess-router](https://github.com/copyleftdev/braess-router) | Bounded semantic routing with Jev and Poise. Rust, single-server, alpha. | 0 | Rust | 2026-09-22 |
| [corbitsdev/corbits-system-one](https://github.com/corbitsdev/corbits-system-one) | Typed-decision evaluation client for System One (Jev-class) models | 0 | TypeScript | 2026-09-22 |
| [coreywoo27/Jev-Empowered-Qwen-mlx](https://github.com/coreywoo27/Jev-Empowered-Qwen-mlx) | Jev (laya-mlx typed decisions) guided long-context compression for faster Qwen3.8 prefill on Apple Silicon MLX | 0 | Python | 2026-09-22 |
| [CorieW/JevTest](https://github.com/CorieW/JevTest) | Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence. | 0 | TypeScript | 2026-09-20 |
| [cristiancolon/jev-hft](https://github.com/cristiancolon/jev-hft) | Research pipeline testing whether TypeSafe's Jev (via Vercel AI Gateway) can judge news and market data fast … | 0 | TypeScript | 2026-09-21 |
| [crman/Jev-AI-Output-Judge](https://github.com/crman/Jev-AI-Output-Judge) | Benchmarking Jev and LLMs for RAG answer evaluation and hallucination detection | 0 | Python | 2026-09-21 |
| [CrowBe/weave](https://github.com/CrowBe/weave) | Agent Harness for System One model | 0 | TypeScript | 2026-09-22 |
| [cskwork/pi-jev-router](https://github.com/cskwork/pi-jev-router) | Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway | 0 | JavaScript | 2026-09-22 |
| [ctmx/openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp) | High-speed System One Jev AI decision gateway and MCP server powered by OpenRouter | 0 | Python | 2026-09-20 |
| [cuipengfei/agc](https://github.com/cuipengfei/agc) | — | 0 | TypeScript | 2026-09-21 |
| [CWBudde/simtgo](https://github.com/CWBudde/simtgo) | — | 0 | Go | 2026-09-19 |
| [cyberspace-cs/jev-agent-routing](https://github.com/cyberspace-cs/jev-agent-routing) | DIY Jev fast decision layer for Agent - 10x faster, 10x cheaper | 0 | HTML | 2026-09-22 |
| [cydevo202020/dsh-jev-warden](https://github.com/cydevo202020/dsh-jev-warden) | DeepSeek Harness plugin: enforces agent-constraint skills (grill-me / find-simplifications) by judging tool c… | 0 | TypeScript | 2026-09-19 |
| [cyrusasco/JevCompact](https://github.com/cyrusasco/JevCompact) | Lossless LLM session compaction for Claude Code, Codex and ZCode — Jev keep/drop decisions plus a Chinese-opt… | 0 | JavaScript | 2026-09-21 |
| [D3v0ps/jev](https://github.com/D3v0ps/jev) | — | 0 | — | 2026-09-20 |
| [dafsic/jev-xmr](https://github.com/dafsic/jev-xmr) | xmr hyperliquid trading agent | 0 | Python | 2026-09-21 |
| [dagfinndybvig/Go](https://github.com/dagfinndybvig/Go) | A Jev driven Go game | 0 | HTML | 2026-09-21 |
| [damiensmith1/semantic-pubsub-jev](https://github.com/damiensmith1/semantic-pubsub-jev) | — | 0 | Go | 2026-09-22 |
| [daneknudsen8-maker/jev-voice-control](https://github.com/daneknudsen8-maker/jev-voice-control) | Control your browser by voice. A Chrome extension that turns speech into typed commands using TypeSafe's Jev … | 0 | JavaScript | 2026-09-20 |
| [DanePete/wanigan](https://github.com/DanePete/wanigan) | Local-first Electron control surface for coding agents — starts real CLI sessions, records their operational … | 0 | TypeScript | 2026-09-21 |
| [dangquan1402/jev-extract](https://github.com/dangquan1402/jev-extract) | Paragraph information extraction using TypeSafe AI Jev — closed-set extractive spans via Choice over candidat… | 0 | Python | 2026-09-21 |
| [DanielJD1216/magic-computer-use](https://github.com/DanielJD1216/magic-computer-use) | Meet Jev, Fastest Computer Use | 0 | Swift | 2026-09-21 |
| [danielscoffee/nixos](https://github.com/danielscoffee/nixos) | — | 0 | Shell | 2026-09-19 |
| [danielwii/nestjs-libs](https://github.com/danielwii/nestjs-libs) | — | 0 | TypeScript | 2026-09-20 |
| [DanM3rcurius/po-radar](https://github.com/DanM3rcurius/po-radar) | psyop radar, powered b jev and design by roemmele | 0 | Python | 2026-09-21 |
| [DanM3rcurius/real-estate-tracker](https://github.com/DanM3rcurius/real-estate-tracker) | — | 0 | Python | 2026-09-21 |
| [DanMcInerney/robots-world](https://github.com/DanMcInerney/robots-world) | A modular multi-robot control testbed with swappable physics, sensors, AI controllers, and impaired swarm com… | 0 | TypeScript | 2026-09-21 |
| [danstoyell/jevnalysis](https://github.com/danstoyell/jevnalysis) | Playing around with Typesafe's Jev | 0 | Python | 2026-09-20 |
| [Danu28/pi-jev-harness](https://github.com/Danu28/pi-jev-harness) | Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback | 0 | TypeScript | 2026-09-20 |
| [daraskme/darask-code](https://github.com/daraskme/darask-code) | Terminal coding-agent harness: append-only session log, evidence-gated completion controller, optional Jev re… | 0 | TypeScript | 2026-09-21 |
| [datamonsterr/jev_auto_select_skills](https://github.com/datamonsterr/jev_auto_select_skills) | — | 0 | TypeScript | 2026-09-21 |
| [davafons/focus-jev](https://github.com/davafons/focus-jev) | A focused Chromium extension that uses JEV to keep browsing aligned with one session goal. | 0 | JavaScript | 2026-09-21 |
| [david-j-lustig/jev-fantasy-football-manager](https://github.com/david-j-lustig/jev-fantasy-football-manager) | Experimenting with using Jev to manage my fantasy football team | 0 | Python | 2026-09-19 |
| [davidrydberg/git-judge-jev](https://github.com/davidrydberg/git-judge-jev) | GitHub Action for agent-written PRs: one comment that says what the PR really does, which hunks need a human,… | 0 | TypeScript | 2026-09-20 |
| [DavidSnir/JevOps](https://github.com/DavidSnir/JevOps) | — | 0 | TypeScript | 2026-09-22 |
| [dazreil/jev-npc-interaction-prototype](https://github.com/dazreil/jev-npc-interaction-prototype) | Browser-based NPC interaction prototype using authored dialogue and TypeSafe Jev action selection | 0 | JavaScript | 2026-09-20 |
| [dbredesen/jev-sheets](https://github.com/dbredesen/jev-sheets) | — | 0 | JavaScript | 2026-09-19 |
| [Dcode9/D-Games](https://github.com/Dcode9/D-Games) | — | 0 | HTML | 2026-09-21 |
| [DeadPackets/SwipeRepublic](https://github.com/DeadPackets/SwipeRepublic) | Reigns-style card game with Luna and Jev. | 0 | TypeScript | 2026-09-22 |
| [DeadPackets/UnitedStatesOfJev](https://github.com/DeadPackets/UnitedStatesOfJev) | Just a silly political simulator. | 0 | TypeScript | 2026-09-22 |
| [debamitro/yc-or-not-checker](https://github.com/debamitro/yc-or-not-checker) | See if your idea can qualify for YC - powered by Jev | 0 | TypeScript | 2026-09-21 |
| [Debasishhh/jevguard](https://github.com/Debasishhh/jevguard) | — | 0 | Python | 2026-09-21 |
| [Deepusleepy/jeff](https://github.com/Deepusleepy/jeff) | A chatbot that cannot write: TypeSafe Jev ranks a checked-in bank of replies. | 0 | JavaScript | 2026-09-20 |
| [deesatzed/JevEdge0](https://github.com/deesatzed/JevEdge0) | — | 0 | Python | 2026-09-21 |
| [dej-h/jevseek](https://github.com/dej-h/jevseek) | — | 0 | TypeScript | 2026-09-20 |
| [dene-/Arcadia](https://github.com/dene-/Arcadia) | — | 0 | GDScript | 2026-09-21 |
| [derekchen14/personal_assistants](https://github.com/derekchen14/personal_assistants) | Assistant Factory that spins up peronal assistants at the click of a button | 0 | HTML | 2026-07-29 |
| [dested/alt-tv-rewind](https://github.com/dested/alt-tv-rewind) | What Usenet said the morning after: alt.tv.* reaction archives aligned to episode air dates | 0 | TypeScript | 2026-09-22 |
| [dev-willbird1936/pi-auto-model-router](https://github.com/dev-willbird1936/pi-auto-model-router) | Score-based auto router for Pi Coding Agent (experimental Jev default) | 0 | TypeScript | 2026-09-20 |
| [dev-willbird1936/pi-compact-jev](https://github.com/dev-willbird1936/pi-compact-jev) | Verbatim Jev context compaction for Pi Coding Agent | 0 | TypeScript | 2026-09-20 |
| [dev1556/jev-reranker-benchmark](https://github.com/dev1556/jev-reranker-benchmark) | — | 0 | Python | 2026-09-20 |
| [DevinRobinson1/dstack](https://github.com/DevinRobinson1/dstack) | Dstack: nine stages, one command, and readable evidence at every gate. A delivery process built for an owner … | 0 | JavaScript | 2026-09-21 |
| [deviprasadshetty-dev/jev-independent-test-report](https://github.com/deviprasadshetty-dev/jev-independent-test-report) | — | 0 | HTML | 2026-09-21 |
| [devjtv/jev-router](https://github.com/devjtv/jev-router) | — | 0 | TypeScript | 2026-09-21 |
| [devos-ing/jevbrain](https://github.com/devos-ing/jevbrain) | — | 0 | TypeScript | 2026-09-20 |
| [devsoftx/nerjev](https://github.com/devsoftx/nerjev) | — | 0 | TypeScript | 2026-09-20 |
| [DevvGwardo/ghost-route](https://github.com/DevvGwardo/ghost-route) | Flock-camera-aware privacy navigation: see ALPR cameras near you and get driving routes ranked by camera expo… | 0 | TypeScript | 2026-09-21 |
| [df-yamashitamasashi/jev_blog](https://github.com/df-yamashitamasashi/jev_blog) | TypeSafe AI Jev 実践ユースケース・サンプルコード集 | 0 | TypeScript | 2026-09-22 |
| [dfa1/typesafe-java](https://github.com/dfa1/typesafe-java) | Java client and CLI for the TypeSafe AI API | 0 | Java | 2026-09-22 |
| [dglazkov/gev](https://github.com/dglazkov/gev) | Jev from DiffusionGemma | 0 | TypeScript | 2026-09-21 |
| [dholzric/jevmarket](https://github.com/dholzric/jevmarket) | — | 0 | Python | 2026-09-21 |
| [digitalfoudnry-vb/JevBrowser](https://github.com/digitalfoudnry-vb/JevBrowser) | JEV Browser | 0 | TypeScript | 2026-09-21 |
| [DihRJ/claude-code-jev-compaction](https://github.com/DihRJ/claude-code-jev-compaction) | Reduza tokens de entrada no Claude Code com compactação de contexto por relevância (LiteLLM + TypeSafe Jev). … | 0 | Shell | 2026-09-21 |
| [discover-legal/affidavit-maker](https://github.com/discover-legal/affidavit-maker) | A affidavit generation tool | 0 | JavaScript | 2026-09-21 |
| [distil-labs/invoice-processing-pipeline](https://github.com/distil-labs/invoice-processing-pipeline) | Accounts payable pipeline: Jev for inbox triage, fine-tuned small models (distil labs) for invoice decisions.… | 0 | Python | 2026-09-22 |
| [divyekant/jev-qa](https://github.com/divyekant/jev-qa) | Jev-only browser UAT and measured design QA with a Luna wrapper and frozen evaluation evidence. | 0 | Python | 2026-09-19 |
| [dizk/jev-lens](https://github.com/dizk/jev-lens) | jev picks what a coding agent gets to see of large tool results: core library, pi extension and Claude Code p… | 0 | TypeScript | 2026-09-19 |
| [dje96/demo-grocery-web](https://github.com/dje96/demo-grocery-web) | Basket — Snowplow grocery ecommerce demo with TypeSafe Jev purchase-intent classification | 0 | TypeScript | 2026-09-21 |
| [DKeAlvaro/batallas-gallos](https://github.com/DKeAlvaro/batallas-gallos) | Corpus de batallas de gallos en español: transcripciones de YouTube y visor web | 0 | Python | 2026-09-21 |
| [dnakhoa/jev-deferred-crispification](https://github.com/dnakhoa/jev-deferred-crispification) | Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision… | 0 | TeX | 2026-09-17 |
| [dngames/JevChess](https://github.com/dngames/JevChess) | — | 0 | JavaScript | 2026-09-21 |
| [doctor-ew/nightshift-community](https://github.com/doctor-ew/nightshift-community) | Nightshift community pilot for the GSU Girls Who Code Hack-her-thon; publication audit in progress | 0 | Python | 2026-09-21 |
| [DoGMaTiiC/hermes-jev](https://github.com/DoGMaTiiC/hermes-jev) | Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. F… | 0 | Python | 2026-09-21 |
| [dominusDeus/jev-trader-fork](https://github.com/dominusDeus/jev-trader-fork) | — | 0 | TypeScript | 2026-09-19 |
| [DomMonte/n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai) | n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibra… | 0 | TypeScript | 2026-09-21 |
| [dooreelko/jeb](https://github.com/dooreelko/jeb) | The adopted but dear brother of jev | 0 | Python | 2026-09-21 |
| [doublerobust/rjif](https://github.com/doublerobust/rjif) | jif: calibrated if-statements in R via TypeSafe Jev — judgment-based control flow with reliability curves for… | 0 | R | 2026-09-22 |
| [DowLucas/browser-jev](https://github.com/DowLucas/browser-jev) | Adversarial browser testing: personas explore your web app while Jev judges every page state | 0 | TypeScript | 2026-09-21 |
| [dpaluy/pi-jev-compact](https://github.com/dpaluy/pi-jev-compact) | Smart Compact for Harnesses using Jev model | 0 | TypeScript | 2026-09-20 |
| [dpshde/berean](https://github.com/dpshde/berean) | Yes or no, then the Berean Standard Bible verses that best support the verdict. | 0 | TypeScript | 2026-09-17 |
| [drgg/ai-trending-radar](https://github.com/drgg/ai-trending-radar) | 每周自动更新的 GitHub AI 热门项目周报（近 90 天新建、Stars > 5000） | 0 | HTML | 2026-09-21 |
| [drillan/jevapan](https://github.com/drillan/jevapan) | — | 0 | Python | 2026-09-19 |
| [dsandrade/jevra](https://github.com/dsandrade/jevra) | An open-source decision layer connecting coding agents with TypeSafe Jev. | 0 | TypeScript | 2026-09-18 |
| [dtduc-git/jev-packs](https://github.com/dtduc-git/jev-packs) | Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev… | 0 | Python | 2026-09-20 |
| [dtduc-git/jev-table](https://github.com/dtduc-git/jev-table) | AI columns for CSV/JSONL files with TypeSafe's Jev — typed answers, confidence, review queue, resume and cost… | 0 | Python | 2026-09-20 |
| [dtduc-git/jevassert](https://github.com/dtduc-git/jevassert) | Record/replay regression tests for Jev (TypeSafe System One) question packs — accuracy, calibration and cost … | 0 | Python | 2026-09-20 |
| [dtsuka/jev-review](https://github.com/dtsuka/jev-review) | — | 0 | TypeScript | 2026-09-20 |
| [dugufeng666/jev-ai-guide](https://github.com/dugufeng666/jev-ai-guide) | jev-ai-guide | 0 | MDX | 2026-09-22 |
| [Dujaydis/JevSysUno](https://github.com/Dujaydis/JevSysUno) | — | 0 | TypeScript | 2026-09-19 |
| [duketopceo/dim-agent](https://github.com/duketopceo/dim-agent) | Jev-powered voice computer-use agent for Omarchy (Hyprland/Asahi): push-to-talk → whisper.cpp → Jev decision … | 0 | Python | 2026-09-20 |
| [duketopceo/jev-compact](https://github.com/duketopceo/jev-compact) | Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP | 0 | Python | 2026-09-19 |
| [DumoeDss/jev-demos](https://github.com/DumoeDss/jev-demos) | — | 0 | HTML | 2026-09-22 |
| [dxd-dechao/jev-playground](https://github.com/dxd-dechao/jev-playground) | — | 0 | TypeScript | 2026-09-22 |
| [dy-ma/jev-world](https://github.com/dy-ma/jev-world) | — | 0 | TypeScript | 2026-09-18 |
| [dymzz/lgtm-dsh](https://github.com/dymzz/lgtm-dsh) | lgtm-dsh is a DSH plugin that automatically installs lgtm, reuses the Jev already configured in DSH, and lets… | 0 | JavaScript | 2026-09-22 |
| [dyusuf/BinfoCheck](https://github.com/dyusuf/BinfoCheck) | — | 0 | Python | 2026-09-21 |
| [eachann1024/pi-jev-route](https://github.com/eachann1024/pi-jev-route) | Pi extension: Jev model selection before subagent dispatch | 0 | TypeScript | 2026-09-20 |
| [earayu/jevnews](https://github.com/earayu/jevnews) | — | 0 | TypeScript | 2026-09-20 |
| [edgelabs-ai/jev48](https://github.com/edgelabs-ai/jev48) | Open, auditable reproduction of TypeSafe Jev: a 2B probabilistic decision model benchmarked across six public… | 0 | Python | 2026-09-21 |
| [EdwardHong0627/jev-poc](https://github.com/EdwardHong0627/jev-poc) | — | 0 | Python | 2026-09-20 |
| [EdytaKucharska/ticket-quest](https://github.com/EdytaKucharska/ticket-quest) | Playful ticket triage that shows how TypeSafe Jev's typed, probability-backed decisions compare with promptin… | 0 | TypeScript | 2026-09-18 |
| [Ege-BULUT/jevcraft](https://github.com/Ege-BULUT/jevcraft) | TypeSafe's Jev plays VoxeLibre, a free block-world game, around the clock; recordings on Hugging Face. | 0 | Lua | 2026-09-22 |
| [Eggwardhan/open-jev](https://github.com/Eggwardhan/open-jev) | An open-source decision layer for AI agents: typed choices, calibrated probabilities, benchmarks, replay, and… | 0 | Python | 2026-09-22 |
| [ehab-ayman-gharib/border-protocol](https://github.com/ehab-ayman-gharib/border-protocol) | Atmospheric border inspection game with Next.js, generated pixel art, and live Jev semantic assessments throu… | 0 | TypeScript | 2026-09-22 |
| [ella0333/jev-slot-machine](https://github.com/ella0333/jev-slot-machine) | Jev plays a slot machine until the money runs out. The local version of jevslots.live. | 0 | JavaScript | 2026-09-22 |
| [Elmata2/LaVega](https://github.com/Elmata2/LaVega) | Building of the personal Finance Agent | 0 | TypeScript | 2026-09-22 |
| [elsejj/mtools](https://github.com/elsejj/mtools) | Intelligently process the content you copy. | 0 | Rust | 2026-09-21 |
| [elyashium/atlas-replay-lab](https://github.com/elyashium/atlas-replay-lab) | capability-aware quality ladder, a privacy-safe trace recorder, deterministic replay, and with an all new Jev… | 0 | JavaScript | 2026-09-22 |
| [Emanon4/tonight-cinema](https://github.com/Emanon4/tonight-cinema) | 今夜放映：用一句观影心情找到下一部电影，Jev 辅助筛选。 | 0 | JavaScript | 2026-09-22 |
| [emergency-lee/decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills) | Agent Skills for decision-native RAG: retrieve wide, decide explicitly, build evidence sets. Site: https://je… | 0 | HTML | 2026-09-19 |
| [emretheus/jev-rag-benchmark](https://github.com/emretheus/jev-rag-benchmark) | Free English RAG benchmark for TypeSafe Jev 1.13 — frozen candidate pools, calibration, paired bootstrap CIs,… | 0 | Python | 2026-09-21 |
| [enriquejuncorichi-create/pi-jev-assist](https://github.com/enriquejuncorichi-create/pi-jev-assist) | Pi extension: checks an agent's work against observation, not against its own account of itself | 0 | TypeScript | 2026-09-19 |
| [Eric-Zhou-0302/jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader) | A Jev-powered technical analysis workspace for China A-shares, supporting AKShare/Tushare, market scans, and … | 0 | Python | 2026-09-21 |
| [ericboehs/wrangle](https://github.com/ericboehs/wrangle) | Hand one Safari window to a program, and no more than that. | 0 | Ruby | 2026-09-20 |
| [EricCheng2222/vox-ambient-assistant](https://github.com/EricCheng2222/vox-ambient-assistant) | Privacy-first ambient voice assistant with OpenAI Realtime and JEV routing | 0 | TypeScript | 2026-09-22 |
| [erickardus/jev-lab](https://github.com/erickardus/jev-lab) | — | 0 | Python | 2026-09-20 |
| [ericmartinezr/are-you-smarter-than-jev](https://github.com/ericmartinezr/are-you-smarter-than-jev) | A small app to test Jev | 0 | Python | 2026-09-19 |
| [EricsenSemedo/t3code-jev](https://github.com/EricsenSemedo/t3code-jev) | Personal T3 Code fork with an opt-in Jev model-routing trial. Based on pingdotgg/t3code. | 0 | TypeScript | 2026-09-22 |
| [eriestra/blockly-jev](https://github.com/eriestra/blockly-jev) | Blockly extension: TypeSafe Jev judgments (Noul, Choice, Score) as first-class blocks | 0 | TypeScript | 2026-09-22 |
| [Eronmmer/jev-cua](https://github.com/Eronmmer/jev-cua) | Production local Cua + TypeSafe Jev fast-path runtime for Codex and Waku | 0 | TypeScript | 2026-09-21 |
| [ethereumdegen/jev-discord-bot](https://github.com/ethereumdegen/jev-discord-bot) | — | 0 | Rust | 2026-09-21 |
| [ethereumdegen/starkbot-neo](https://github.com/ethereumdegen/starkbot-neo) | Fast, local-first macOS agent with Jev navigation and Hypercanvas | 0 | Rust | 2026-09-22 |
| [Evgen-rus/JEV_voice_browser](https://github.com/Evgen-rus/JEV_voice_browser) | — | 0 | JavaScript | 2026-09-21 |
| [expanso-io/demo-expanso-jev](https://github.com/expanso-io/demo-expanso-jev) | Expanso x Jev demos: live edge-pipeline dashboard, pipeline configs, and flow UI. | 0 | HTML | 2026-09-20 |
| [Explorer1092/openclaw-zh](https://github.com/Explorer1092/openclaw-zh) | — | 0 | TypeScript | 2026-09-21 |
| [Extirpater/tasbot](https://github.com/Extirpater/tasbot) | — | 0 | JavaScript | 2026-09-22 |
| [eyenpi/actionreflex](https://github.com/eyenpi/actionreflex) | A pre-execution gate for AI agent actions, powered by TypeSafe's Jev (System One) model. | 0 | Python | 2026-09-21 |
| [fagnersouza666/Jev-plugin-for-hermes](https://github.com/fagnersouza666/Jev-plugin-for-hermes) | — | 0 | Python | 2026-09-21 |
| [falabellamichael/SignalR.E.A.C.H](https://github.com/falabellamichael/SignalR.E.A.C.H) | REACH — RAG Endpoint & AI Chat Host. A SimpleRAG plugin (installable via GitHub URL) + hosted OpenAI-compatib… | 0 | JavaScript | 2026-09-22 |
| [fangligamedev/deskfront-jevlab](https://github.com/fangligamedev/deskfront-jevlab) | 桌面前线：Godot + Blender 开源桌面战术游戏，三阵营玩具兵、掩体 AI、RTS 操作与 Agent 接口 | 0 | GDScript | 2026-09-21 |
| [Faresabdelghany/jev-browser-test](https://github.com/Faresabdelghany/jev-browser-test) | — | 0 | Python | 2026-09-22 |
| [farukkavlak/vocabboost](https://github.com/farukkavlak/vocabboost) | Look up a word from the subtitles and see what it means in that line, without leaving the video. | 0 | TypeScript | 2026-09-18 |
| [fast-facts/jev-mcp](https://github.com/fast-facts/jev-mcp) | — | 0 | Go | 2026-09-19 |
| [favoyang/jevfast-public](https://github.com/favoyang/jevfast-public) | Public project submissions for jevfast.com. Issues only; website source is maintained separately. | 0 | — | 2026-09-20 |
| [fblissjr/jev-experiments](https://github.com/fblissjr/jev-experiments) | tinkering and experiments with jev and typesafe ai | 0 | TypeScript | 2026-09-21 |
| [feikukuai/qwen3.8_jev](https://github.com/feikukuai/qwen3.8_jev) | logit_biaslogprobqwen3.8 | 0 | Python | 2026-09-22 |
| [fengyiqicoder/jevfeed](https://github.com/fengyiqicoder/jevfeed) | An infinite feed built from your own browser history, ranked in real time by TypeSafe's Jev. No likes, no fol… | 0 | JavaScript | 2026-09-21 |
| [FibonacciAi/sam-presence](https://github.com/FibonacciAi/sam-presence) | Sam — intelligence, in the moment. Realtime presence, live voice, and Jev-powered understanding. | 0 | HTML | 2026-09-21 |
| [FieldmouseWorks/redshirt](https://github.com/FieldmouseWorks/redshirt) | A shared, observable experiment runner with interchangeable environments, evaluators, and decision providers. | 0 | Rust | 2026-09-22 |
| [flaviomartil/herdr-jev](https://github.com/flaviomartil/herdr-jev) | Jev-driven multi-model triage and Triad orchestration plugin for Herdr and AI-Harness | 0 | TypeScript | 2026-09-20 |
| [flxbl-io/sf-audit-ask](https://github.com/flxbl-io/sf-audit-ask) | Experimental: ask yes/no questions of a Salesforce Setup Audit Trail CSV. No login. | 0 | JavaScript | 2026-09-21 |
| [fly88oj/jebii](https://github.com/fly88oj/jebii) | Live2D character chat — Jev decides the emotion, SoulLink performs it. | 0 | JavaScript | 2026-09-22 |
| [fol2/jev-playground](https://github.com/fol2/jev-playground) | — | 0 | Swift | 2026-09-21 |
| [fooSynaptic/jev-any-llm](https://github.com/fooSynaptic/jev-any-llm) | — | 0 | Python | 2026-09-22 |
| [formigacamuflada/jev-computer-use](https://github.com/formigacamuflada/jev-computer-use) | — | 0 | Python | 2026-09-19 |
| [FOwen123/FlowState](https://github.com/FOwen123/FlowState) | — | 0 | Swift | 2026-09-21 |
| [FranprzDev/Jev-To-Hackathon](https://github.com/FranprzDev/Jev-To-Hackathon) | — | 0 | JavaScript | 2026-09-20 |
| [frederickrohn/jev-harness](https://github.com/frederickrohn/jev-harness) | experimenting with Jev | 0 | TypeScript | 2026-09-21 |
| [frinfo702/cowork](https://github.com/frinfo702/cowork) | — | 0 | HTML | 2026-09-21 |
| [FrontTribe/grain](https://github.com/FrontTribe/grain) | — | 0 | TypeScript | 2026-09-21 |
| [fruitflyworld/fruit-fly-world](https://github.com/fruitflyworld/fruit-fly-world) | Don't exam the model. Starve it. A fruit-fly survival game with a slot for a brain — hands, genes, 24 neurons… | 0 | TypeScript | 2026-09-22 |
| [fsmiamoto/pi-jev-prune](https://github.com/fsmiamoto/pi-jev-prune) | Experimental pi extension: Jev-driven, cache-aware, recoverable pruning of stale tool results | 0 | TypeScript | 2026-09-21 |
| [fstandhartinger/who-is-right](https://github.com/fstandhartinger/who-is-right) | Comic realtime argument fact-check party demo using Gemini Live and Jev | 0 | Python | 2026-09-22 |
| [furedea/reflex-state](https://github.com/furedea/reflex-state) | Jev-powered execution state for Pi coding agents. Track changes, checks, and blockers outside the main LLM, w… | 0 | TypeScript | 2026-09-22 |
| [furuCRM-Inc/400ms-agentic-sf](https://github.com/furuCRM-Inc/400ms-agentic-sf) | 400ms Agentic Salesforce demo — Jev System 1 AI + WebMCP Direct UI Control. No screen-scraping. No token stre… | 0 | Apex | 2026-09-20 |
| [futex-ai/ai](https://github.com/futex-ai/ai) | — | 0 | Rust | 2026-09-21 |
| [Gabrielgvl/herdr-tools](https://github.com/Gabrielgvl/herdr-tools) | — | 0 | TypeScript | 2026-09-21 |
| [garygentry/jev-poc](https://github.com/garygentry/jev-poc) | POC implementing range of decision-focused use cases for jev | 0 | TypeScript | 2026-09-22 |
| [Gaurav047/job-applications-tracker](https://github.com/Gaurav047/job-applications-tracker) | This app is aimed to track individual jobs applied automatically by a master resume. | 0 | Python | 2026-09-22 |
| [gbesse/decision-hub](https://github.com/gbesse/decision-hub) | Hosted Jev policy workspaces with tenant isolation, finite evaluations and revocable aggregate reports | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-brandsafety](https://github.com/gbesse/jev-brandsafety) | Classify page context, score configurable risks and apply advertiser-owned brand-safety policy. | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-codebook](https://github.com/gbesse/jev-codebook) | Qualitative coding at scale with Jev: apply a codebook to open-ended text, review uncertain items, measure ag… | 0 | Python | 2026-09-22 |
| [gbesse/jev-columns](https://github.com/gbesse/jev-columns) | Maintain versioned semantic decisions as indexed PostgreSQL columns with a reclaimable work queue. | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-extract](https://github.com/gbesse/jev-extract) | Turn documents into typed records with bounded, auditable Jev questions and deterministic aggregation. | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-fingerprint](https://github.com/gbesse/jev-fingerprint) | Group errors by underlying cause after normalization and exact grouping, with representative comparisons. | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-label](https://github.com/gbesse/jev-label) | Prioritize human labels with active-learning strategies, durable review history and clean holdout evaluation. | 0 | Python | 2026-09-22 |
| [gbesse/jev-pii](https://github.com/gbesse/jev-pii) | Inventory personal data with local checks first and optional column-level semantic classification. | 0 | Python | 2026-09-22 |
| [gbesse/jev-proxy](https://github.com/gbesse/jev-proxy) | Policy firewall for MCP tool calls with one-time human approvals and JSONL audit. | 0 | TypeScript | 2026-09-22 |
| [gbesse/jev-regwatch](https://github.com/gbesse/jev-regwatch) | Monitor official texts, relate changes to owned artifacts and preserve critical regulatory alerts. | 0 | JavaScript | 2026-09-22 |
| [gbesse/jev-screen](https://github.com/gbesse/jev-screen) | Title and abstract screening for systematic reviews with Jev: explicit criteria, include/exclude/maybe with r… | 0 | Python | 2026-09-22 |
| [gbesse/jev-trace](https://github.com/gbesse/jev-trace) | Generate a reviewable requirements-to-code-and-tests matrix with coverage and change impact. | 0 | JavaScript | 2026-09-22 |
| [geckguy/job-posting-triage](https://github.com/geckguy/job-posting-triage) | Four engines answer the same four questions about the same job postings, on one labelled test split, with the… | 0 | Python | 2026-09-20 |
| [GeekLinkDev/jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator) | Translate SRT subtitles with structured LLM output and check every translation with Jev. | 0 | Python | 2026-09-22 |
| [Georgakopoulos-Soares-lab/biosafety_knowledge_jev](https://github.com/Georgakopoulos-Soares-lab/biosafety_knowledge_jev) | — | 0 | TeX | 2026-09-20 |
| [ghiffarsabda/easynest_v2](https://github.com/ghiffarsabda/easynest_v2) | Industrial 2D irregular nesting engine with Superposition concurrency and TypeSafe Jev System One AI intellig… | 0 | Python | 2026-09-20 |
| [ghubnab99/jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric) | Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchma… | 0 | C# | 2026-09-20 |
| [giangeralcus/gee-fundriving](https://github.com/giangeralcus/gee-fundriving) | Gee-FunDriving — 2D top-down autonomous driving sim (System-One decision loop demo) | 0 | JavaScript | 2026-09-21 |
| [Gilbert09/jev-cli](https://github.com/Gilbert09/jev-cli) | A Jev-powered judgement layer for Claude Code: semantic permission gating, prompt-injection screening, comple… | 0 | TypeScript | 2026-09-20 |
| [glebmish/jev-watchdog](https://github.com/glebmish/jev-watchdog) | Event-driven trajectory watchdog for coding agents: per-event LLM judgments (Jev, Claude, GPT) accumulated in… | 0 | Python | 2026-09-21 |
| [gnkm/jev-prompts](https://github.com/gnkm/jev-prompts) | — | 0 | Python | 2026-09-21 |
| [GodModeAI2025/JevCoreML](https://github.com/GodModeAI2025/JevCoreML) | Native Entscheidungsmaschine für macOS: kev-0.6b und laya als Core ML in Swift, ohne Python zur Laufzeit, ohn… | 0 | Swift | 2026-09-22 |
| [godspede/jev-auto-classifier](https://github.com/godspede/jev-auto-classifier) | Retired: Jev support lives in godspede/construct-auto-classifier. | 0 | — | 2026-09-19 |
| [gopalanj/jevons](https://github.com/gopalanj/jevons) | Local System One for typed decisions. Scores noul, choice, and score from option logits — never free JSON. Ty… | 0 | Python | 2026-09-20 |
| [gopaljigaur/decide](https://github.com/gopaljigaur/decide) | One client for every decision model: Choice, Score and Noul over Jev, OpenRouter, laya, MLX, CrossEncoders an… | 0 | Python | 2026-09-22 |
| [gorock007/jev-atlas](https://github.com/gorock007/jev-atlas) | An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for codin… | 0 | TypeScript | 2026-09-19 |
| [gowthamgts/pi-stuff](https://github.com/gowthamgts/pi-stuff) | pi extensions used by yours truly. | 0 | TypeScript | 2026-09-20 |
| [gpazo/jev-vphone-cli](https://github.com/gpazo/jev-vphone-cli) | Jev from Typesafe.ai + vphone-cli | 0 | Swift | 2026-09-20 |
| [gradient30/typesafe-handbook](https://github.com/gradient30/typesafe-handbook) | TypeSafe AI 官方文档中文手册（明/暗/彩三套风格，官网同步日志，GitHub Pages） | 0 | TypeScript | 2026-09-22 |
| [grapefruit0205/jev-save](https://github.com/grapefruit0205/jev-save) | Runtime efficiency guard for coding agents (Claude Code, Codex): Jev judges each tool call for necessity, red… | 0 | JavaScript | 2026-09-22 |
| [grayslawson/ha-switchboard](https://github.com/grayslawson/ha-switchboard) | Portable Jev-backed decision and control layer for Home Assistant | 0 | Python | 2026-09-22 |
| [gregjonesio/jev-nfl](https://github.com/gregjonesio/jev-nfl) | Before every NFL snap, a decision-only AI model (TypeSafe Jev) calls run or pass and go/punt/kick on fourth d… | 0 | JavaScript | 2026-09-21 |
| [GreyssonEnterprises/s1-graphify-indexer](https://github.com/GreyssonEnterprises/s1-graphify-indexer) | System-1 codebase indexer: semantic code graphs from small zero-shot models (GLiNER default; Jev/Needle-compa… | 0 | — | 2026-09-19 |
| [GrinZero/live-mira](https://github.com/GrinZero/live-mira) | — | 0 | JavaScript | 2026-09-20 |
| [guanxuyu-sv/Visual-Jev](https://github.com/guanxuyu-sv/Visual-Jev) | — | 0 | HTML | 2026-09-22 |
| [guilhermesalviano/koris-hub](https://github.com/guilhermesalviano/koris-hub) | Koris hub website. | 0 | TypeScript | 2026-09-21 |
| [guozhiwei01/langgraph-agent-practice](https://github.com/guozhiwei01/langgraph-agent-practice) | — | 0 | Python | 2026-09-22 |
| [gytkk/nix-flakes](https://github.com/gytkk/nix-flakes) | Nix flakes | 0 | Python | 2026-09-22 |
| [gzawadzki/jev-usecases](https://github.com/gzawadzki/jev-usecases) | TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage | 0 | Python | 2026-09-18 |
| [h1code2/mobile-jev-local](https://github.com/h1code2/mobile-jev-local) | — | 0 | JavaScript | 2026-09-21 |
| [hamakyo/jev-mahjong-bench](https://github.com/hamakyo/jev-mahjong-bench) | Reproducible riichi mahjong benchmark for Jev, GPT, Mortal, and hybrid agents using MJAI and RiichiEnv. | 0 | TypeScript | 2026-09-22 |
| [Hangzhi/diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang) | A Jev-like decision engine powered by DiffusionGemma and SGLang, with text/image classification, interactive … | 0 | Python | 2026-09-22 |
| [hanzpo/dogfight-bench](https://github.com/hanzpo/dogfight-bench) | — | 0 | TypeScript | 2026-09-19 |
| [harlanljones/jev-roster-shapes](https://github.com/harlanljones/jev-roster-shapes) | Interactive workspace for comparing baseball roster acquisitions — positional coverage, playing-time transfer… | 0 | TypeScript | 2026-09-21 |
| [harlanljones/sabr-jev](https://github.com/harlanljones/sabr-jev) | Season stats lie by omission. Sabr-Jev grades Batter\|Pitcher seasons with typed AI judgments behind a confid… | 0 | Elixir | 2026-09-22 |
| [harshsinha-12/library-estimate](https://github.com/harshsinha-12/library-estimate) | — | 0 | Python | 2026-09-22 |
| [havietkok-sys/BizzJev](https://github.com/havietkok-sys/BizzJev) | Experiments with TypeSafe/Jev semantic gates and a Semantic Operations Lab demo. | 0 | C# | 2026-09-21 |
| [haydarsahin0/Jev](https://github.com/haydarsahin0/Jev) | — | 0 | Python | 2026-09-21 |
| [haystackeditor/stop-rules](https://github.com/haystackeditor/stop-rules) | Holds your coding agent to your team's written coding rules. A stop hook for Claude Code, Codex, Cursor and t… | 0 | JavaScript | 2026-09-21 |
| [hectorlcastro09/jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales) | Winner-stays-on animal tournament refereed by Jev (TypeSafe System One): a local game to feel how fast typed … | 0 | HTML | 2026-09-21 |
| [heiko-hotz/jev-evaluation](https://github.com/heiko-hotz/jev-evaluation) | — | 0 | Python | 2026-09-21 |
| [heliowap/delegador](https://github.com/heliowap/delegador) | Delega tarefa de codigo ao modelo escolhido pela tarefa, com permissao deterministica, verificacao por teste … | 0 | Go | 2026-09-22 |
| [heliowap/diff-risk-sentinel](https://github.com/heliowap/diff-risk-sentinel) | Risk triage for large git diffs (CRAP + TypeSafe Jev) and a repository-wide dead-code scan for Python and JS/… | 0 | Python | 2026-09-20 |
| [hemloeth/jev-todo](https://github.com/hemloeth/jev-todo) | — | 0 | JavaScript | 2026-09-21 |
| [HenkDz/butterfly-jev](https://github.com/HenkDz/butterfly-jev) | — | 0 | TypeScript | 2026-09-20 |
| [HerbertGao/pi-extensions](https://github.com/HerbertGao/pi-extensions) | HerbertGao maintained extensions for the Pi coding agent | 0 | TypeScript | 2026-09-22 |
| [hewenyu/jev-card-agent](https://github.com/hewenyu/jev-card-agent) | auto paly with jev | 0 | TypeScript | 2026-09-22 |
| [heyitsR1/killslop](https://github.com/heyitsR1/killslop) | Block AI slop videos on YouTube. A Chrome extension and an open, reviewed list of AI slop channels (CC BY-SA … | 0 | JavaScript | 2026-09-21 |
| [hfiguera/typesafe_ai](https://github.com/hfiguera/typesafe_ai) | An Elixir client for TypeSafe AI with typed responses and bounded concurrency | 0 | Elixir | 2026-09-18 |
| [HikaruEgashira/jev-algorithms](https://github.com/HikaruEgashira/jev-algorithms) | Runtime-agnostic algorithms built on TypeSafe's Jev structured-evaluation model | 0 | JavaScript | 2026-09-21 |
| [HikaruEgashira/jev-kitchen](https://github.com/HikaruEgashira/jev-kitchen) | — | 0 | TypeScript | 2026-09-21 |
| [Hinstein/jev-vip](https://github.com/Hinstein/jev-vip) | — | 0 | TypeScript | 2026-09-22 |
| [Hinstein/jevhub](https://github.com/Hinstein/jevhub) | — | 0 | TypeScript | 2026-09-21 |
| [HiQS-Labs/Jev-unofficial-toolkit](https://github.com/HiQS-Labs/Jev-unofficial-toolkit) | HiQS' unofficial starter code for Jev model with examples and toolkit based on our testing | 0 | Python | 2026-09-21 |
| [hiro1202/jev-review-gate-poc](https://github.com/hiro1202/jev-review-gate-poc) | — | 0 | — | 2026-09-22 |
| [hiroki-abe-58/sokudan](https://github.com/hiroki-abe-58/sokudan) | Japanese System One decision model (Jev-style): typed answers and probabilities in one forward pass, no text … | 0 | Python | 2026-09-22 |
| [hiroyannnn/yuru-poll](https://github.com/hiroyannnn/yuru-poll) | Loose polling: free-text comments become fractional votes via TypeSafe Jev (System One) | 0 | MoonBit | 2026-09-19 |
| [hnegishi/typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby) | Ruby client for the TypeSafe AI(Jev) System One API | 0 | Ruby | 2026-09-20 |
| [hoaphm/jev-decision-maker](https://github.com/hoaphm/jev-decision-maker) | omp plugin: JEV (TypeSafe System One) picks the next coding step from agent-supplied candidates | 0 | TypeScript | 2026-09-21 |
| [hobbs/jev-turn-analysis](https://github.com/hobbs/jev-turn-analysis) | Jev Turn Analysis is a Rust CLI for analyzing completed Claude Code and Codex sessions. | 0 | Rust | 2026-09-21 |
| [Hol1kgmg/jev-trpg](https://github.com/Hol1kgmg/jev-trpg) | jev aiを使ったショートTRPG | 0 | TypeScript | 2026-09-21 |
| [HorusJiang/dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) | Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gat… | 0 | TypeScript | 2026-09-22 |
| [hosseintoussi/jev-flappy-bird](https://github.com/hosseintoussi/jev-flappy-bird) | A live demo of TypeSafe's Jev model playing Flappy Bird, one flap-or-wait decision at a time. | 0 | TypeScript | 2026-09-20 |
| [hraness/sys1](https://github.com/hraness/sys1) | Typed decisions for agents: a local model router, Jev-compatible gateway, and Node/Bun client. | 0 | TypeScript | 2026-09-21 |
| [hraness/system-one-skills](https://github.com/hraness/system-one-skills) | System One skills for Devin, Claude Code and Codex. Cut noisy validation-log tokens with one deterministic sk… | 0 | Python | 2026-09-20 |
| [huaizuo2022/jev-ultrafast](https://github.com/huaizuo2022/jev-ultrafast) | — | 0 | Python | 2026-09-22 |
| [hulryung/jev-testbed](https://github.com/hulryung/jev-testbed) | Jev (TypeSafe System One) 테스트베드 — 클라우드 API와 로컬 셀프호스팅(jeff/GLiFormer) 양쪽 실행 예제 및 실측 결과 | 0 | Python | 2026-09-21 |
| [hxutixnnn/ui-jev](https://github.com/hxutixnnn/ui-jev) | — | 0 | TypeScript | 2026-09-19 |
| [HyeranPark99/tiny-rag-jev](https://github.com/HyeranPark99/tiny-rag-jev) | A small RAG web app that visualizes every step of the retrieval-augmented generation pipeline | 0 | HTML | 2026-09-22 |
| [hyper186/jev-pirate-sorter](https://github.com/hyper186/jev-pirate-sorter) | A hands-on Jev demo: sorting Pirate Nation PFPs into trait-aware piles with Venice AI. | 0 | TypeScript | 2026-09-21 |
| [hyspacex/jev-router](https://github.com/hyspacex/jev-router) | Route OpenAI-style chat requests to a model and reasoning effort, using TypeSafe's Jev decision model as the … | 0 | Python | 2026-09-21 |
| [i-priyanshuverma/laravel-jev-demo](https://github.com/i-priyanshuverma/laravel-jev-demo) | — | 0 | PHP | 2026-09-21 |
| [i3u8/jev-skill-selection](https://github.com/i3u8/jev-skill-selection) | Pre-message hook: use TypeSafe Jev to keep/drop skills and shrink agent context | 0 | Python | 2026-09-22 |
| [iamdin/pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench) | Benchmark for Pi skill routing: BM25 vs TypeSafe Jev across roster sizes 50–500 | 0 | TypeScript | 2026-09-20 |
| [ianlintner/jev-router](https://github.com/ianlintner/jev-router) | Shadow-mode Jev decision adapter for model-routing comparisons, with Prometheus metrics and Grafana dashboards | 0 | Python | 2026-09-20 |
| [ianwijma/skill-library-skill](https://github.com/ianwijma/skill-library-skill) | — | 0 | TypeScript | 2026-09-21 |
| [icecold009/hacksocial-policylens](https://github.com/icecold009/hacksocial-policylens) | PolicyLens: a privacy-conscious AI tool for understanding public school policies. | 0 | JavaScript | 2026-09-20 |
| [iDiagoValeta/jev-decision-gate](https://github.com/iDiagoValeta/jev-decision-gate) | LLM-based permission gate for OpenCode agents: Jev auto-approves routine tool calls and fails open to a human… | 0 | TypeScript | 2026-09-22 |
| [igormorais123/JEV](https://github.com/igormorais123/JEV) | Testes experimentais com o modelo de classificação JEV | 0 | HTML | 2026-09-22 |
| [ihs7/darkops](https://github.com/ihs7/darkops) | — | 0 | TypeScript | 2026-09-21 |
| [iluoxw/jev-vs-llm-snake](https://github.com/iluoxw/jev-vs-llm-snake) | Jev 与 LLM 同页对照的贪吃蛇 | 0 | TypeScript | 2026-09-22 |
| [imandreaugusto/quaseoficial](https://github.com/imandreaugusto/quaseoficial) | O melhor conteúdo de inglês do mundo! | 0 | TypeScript | 2026-09-21 |
| [ImFeH2/jev-arcade](https://github.com/ImFeH2/jev-arcade) | — | 0 | TypeScript | 2026-09-20 |
| [imprfct-code/jevdokku](https://github.com/imprfct-code/jevdokku) | — | 0 | TypeScript | 2026-09-19 |
| [inematds/jev-curso](https://github.com/inematds/jev-curso) | Plano pedagógico do curso Jev: três trilhas, doze módulos e trinta e seis aulas | 0 | HTML | 2026-09-21 |
| [inkwell-finance/jev-switchyard](https://github.com/inkwell-finance/jev-switchyard) | — | 0 | Python | 2026-09-17 |
| [Ioluca/fili_Jev](https://github.com/Ioluca/fili_Jev) | Plugin WordPress: trova i link interni che mancano e gli articoli doppi. Propone, non scrive. Giudizi di Jev … | 0 | PHP | 2026-09-21 |
| [ioOvOoi/Pi-Jev](https://github.com/ioOvOoi/Pi-Jev) | — | 0 | TypeScript | 2026-09-18 |
| [Isaac-Flath/agentkb](https://github.com/Isaac-Flath/agentkb) | — | 0 | Python | 2026-09-17 |
| [isHeSatoshi/smalljev](https://github.com/isHeSatoshi/smalljev) | the open TypeSafe Jev that runs on your mama's phone. 2.5B params, one forward pass, zero generated tokens. | 0 | Python | 2026-09-21 |
| [isiomaC/jevkit](https://github.com/isiomaC/jevkit) | Native Swift SDK for TypeSafe Jev System One decisions. | 0 | Swift | 2026-09-20 |
| [IslamBaraka90/jev-typesafe-real-financial-use-cases](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases) | Fifty real-world financial use cases for TypeSafe's Jev model: typed, structured LLM answers over ledgers, fr… | 0 | JavaScript | 2026-09-20 |
| [ismailakdag/typesafe-jev](https://github.com/ismailakdag/typesafe-jev) | sahibinden ilanlarini tarayicida yakalayip TypeSafe (Jev) ile eleyen yerel arac — emlak ve vasita icin ayri s… | 0 | Python | 2026-09-20 |
| [ItIsCuthNotCup/SameThing](https://github.com/ItIsCuthNotCup/SameThing) | SameThing test with Jev | 0 | Python | 2026-09-21 |
| [ItisNoMatter/kojev](https://github.com/ItisNoMatter/kojev) | Kotlin Multiplatform client for Jev that returns your own enum/sealed types instead of string keys. | 0 | Kotlin | 2026-09-22 |
| [its-panzer/skilltree](https://github.com/its-panzer/skilltree) | A local-first skill library and visual skill tree, with Jev routing and MCP access. | 0 | JavaScript | 2026-09-18 |
| [itsaam/slop-detector](https://github.com/itsaam/slop-detector) | A Chrome extension that flags low-substance engagement bait on X using Jev. | 0 | JavaScript | 2026-09-20 |
| [itsflownium/Kestrel-Agent](https://github.com/itsflownium/Kestrel-Agent) | A multi-provider terminal AI agent for coding, research, and browser automation, with discoverable skills, re… | 0 | Python | 2026-09-22 |
| [itsKarad/jev-poker](https://github.com/itsKarad/jev-poker) | — | 0 | TypeScript | 2026-09-20 |
| [iurysza/logview](https://github.com/iurysza/logview) | Keyboard-driven Android log viewer with live capture, recording, and replay | 0 | TypeScript | 2026-09-20 |
| [J12003LPZ/davinci](https://github.com/J12003LPZ/davinci) | — | 0 | Rust | 2026-09-22 |
| [j7708git/jev-tradingview-signal](https://github.com/j7708git/jev-tradingview-signal) | Chrome MV3 擴充：在 TradingView 圖表上按一次，把當前 300 根 K 棒送給 TypeSafe Jev 模型判斷多空，結果顯示於側邊面板（不自動下單、零依賴） | 0 | JavaScript | 2026-09-22 |
| [Jacarte/pepi](https://github.com/Jacarte/pepi) | My Personal Pi config | 0 | TypeScript | 2026-09-21 |
| [jackma5477001/dsh-jev-auto](https://github.com/jackma5477001/dsh-jev-auto) | — | 0 | JavaScript | 2026-09-22 |
| [jackojacko05/jev-keiba-calling](https://github.com/jackojacko05/jev-keiba-calling) | Compare direct LLM horse-race commentary with Jev-assisted structured decisions. | 0 | TypeScript | 2026-09-20 |
| [JackZH26/Jev-Live](https://github.com/JackZH26/Jev-Live) | Open-source Windows studio for Steam games: local AI host, editable avatars/chat, manual or JEV-assisted play… | 0 | TypeScript | 2026-09-21 |
| [JacobLinCool/lookline](https://github.com/JacobLinCool/lookline) | LookLine, a complete fashion experience that connects acquisition and creation in one continuous loop. Find t… | 0 | TypeScript | 2026-09-20 |
| [jagenaujagenau/ground-truth](https://github.com/jagenaujagenau/ground-truth) | Ground News style bias check for the article in your current tab. | 0 | TypeScript | 2026-09-21 |
| [Jaimejourney/mbti-jev-explorer](https://github.com/Jaimejourney/mbti-jev-explorer) | mbti html | 0 | HTML | 2026-09-22 |
| [jakenbear/the-jev-enator](https://github.com/jakenbear/the-jev-enator) | The Jev-enator: three Jev-backed Claude Code hooks - a danger gate, a failure notice, and a completion check. | 0 | Python | 2026-09-21 |
| [james947/codex-jev](https://github.com/james947/codex-jev) | Route each Codex prompt to the right effort with TypeSafe's Jev | 0 | Python | 2026-09-22 |
| [JamesANZ/jev-chrome-blocker-extension](https://github.com/JamesANZ/jev-chrome-blocker-extension) | A chrome extension that uses JEV to dynamically block content per user request | 0 | TypeScript | 2026-09-22 |
| [jamilxt/typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java) | Community-maintained Java SDK for the TypeSafe AI System One (Jev) API. Not an official TypeSafe product. | 0 | Java | 2026-09-21 |
| [jan-barg/jev-traffic-control](https://github.com/jan-barg/jev-traffic-control) | Can Jev beat conventional traffic control? NYC-informed SUMO benchmarks and interactive side-by-side replays. | 0 | Python | 2026-09-21 |
| [jangya/jev-webmcp](https://github.com/jangya/jev-webmcp) | — | 0 | TypeScript | 2026-09-18 |
| [jaredwerba/xword](https://github.com/jaredwerba/xword) | Crossword agent: Tavily grounds, Jev ranks, Token Factory writes leftovers | 0 | Python | 2026-09-20 |
| [jasondotsetHacked/jev-discord-gate-v1](https://github.com/jasondotsetHacked/jev-discord-gate-v1) | — | 0 | JavaScript | 2026-09-21 |
| [jaswanthsanjay88/rev](https://github.com/jaswanthsanjay88/rev) | Fast, prefill-only decision model. Typed questions in, calibrated probabilities out, single forward pass with… | 0 | Python | 2026-09-22 |
| [jawauntb/mapvest](https://github.com/jawauntb/mapvest) | Mapvest — Google-Maps/Zillow-style investable-brand explorer. Photo scanning identifies public companies + ET… | 0 | TypeScript | 2026-09-20 |
| [jaysonsantos/sudoku-jev](https://github.com/jaysonsantos/sudoku-jev) | Sudoku game played by the TypeSafe Jev decision model through OpenRouter | 0 | TypeScript | 2026-09-21 |
| [jcardama/bird-jev](https://github.com/jcardama/bird-jev) | Private maintenance fork of Bird for reading and searching X; JEV integration planned | 0 | TypeScript | 2026-09-21 |
| [jdhornsby/typesafe-jev](https://github.com/jdhornsby/typesafe-jev) | — | 0 | Python | 2026-09-20 |
| [jdorado/ez-fast-browser](https://github.com/jdorado/ez-fast-browser) | Bounded Jev-powered browser sessions for Ez agents | 0 | Python | 2026-09-19 |
| [jdubpark/jevcode](https://github.com/jdubpark/jevcode) | — | 0 | TypeScript | 2026-09-20 |
| [Je1zzz/Jev-Codex-accelerator](https://github.com/Je1zzz/Jev-Codex-accelerator) | — | 0 | Python | 2026-09-21 |
| [JeffNa1/social-anti-ragebait](https://github.com/JeffNa1/social-anti-ragebait) | Automatically detect, classify, and blur outrage-inducing posts and drama on X (Twitter), Threads, and Facebo… | 0 | JavaScript | 2026-09-21 |
| [jekozyra/pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) | — | 0 | TypeScript | 2026-09-20 |
| [Jevals/jevals-data](https://github.com/Jevals/jevals-data) | Independent benchmark data for TypeSafe's Jev (System One model) vs LLMs: accuracy, calibration, cost. Boards… | 0 | — | 2026-09-21 |
| [jevbook/jevbook](https://github.com/jevbook/jevbook) | The typed social network. Agents post. Jev decides. | 0 | — | 2026-09-19 |
| [jevido/omarchy-jevido](https://github.com/jevido/omarchy-jevido) | My Omarchy 4 shell plugins: a daily wiki digest, a calendar clock, and media controls | 0 | QML | 2026-09-17 |
| [JevolUkraine/jevol-website](https://github.com/JevolUkraine/jevol-website) | — | 0 | TypeScript | 2026-09-22 |
| [jevrl/jevrl.github.io](https://github.com/jevrl/jevrl.github.io) | — | 0 | HTML | 2026-09-21 |
| [jevtail/jevtail](https://github.com/jevtail/jevtail) | Nothing to read: a message only when your app is actually broken, with what kind of problem it is. Log and al… | 0 | TypeScript | 2026-09-20 |
| [jfrader/jev-mcp](https://github.com/jfrader/jev-mcp) | Unofficial stdio MCP client for TypeSafe Jev. Bring your own API key. | 0 | Go | 2026-09-22 |
| [jgodmere808/tetris-with-jev](https://github.com/jgodmere808/tetris-with-jev) | A tetris game written in C and automated with JEV | 0 | C | 2026-09-20 |
| [jh1373/jev-search](https://github.com/jh1373/jev-search) | Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only aft… | 0 | JavaScript | 2026-09-20 |
| [Jhounx/ai-pentest-workbench](https://github.com/Jhounx/ai-pentest-workbench) | Electron and CDP workbench for LLM-assisted, authorized web security testing | 0 | TypeScript | 2026-09-18 |
| [JiangZehua/Game-Jev](https://github.com/JiangZehua/Game-Jev) | — | 0 | Python | 2026-09-22 |
| [jianrong7/jev-codex-model-router](https://github.com/jianrong7/jev-codex-model-router) | — | 0 | JavaScript | 2026-09-20 |
| [JiaWeiXie/jev-enhanced-plugin](https://github.com/JiaWeiXie/jev-enhanced-plugin) | A Claude Code plugin that takes skills already in use and adds one thing to each: a typed judgment from \[Typ… | 0 | JavaScript | 2026-09-22 |
| [jinwon-int/ccc-node](https://github.com/jinwon-int/ccc-node) | Reusable template to bootstrap a Seoyoon/Hermes node into a Claude Code/Codex node (클코·코덱스 노드). Sanitized fro… | 0 | Python | 2026-09-22 |
| [jiwenbo0803-hub/btc-jev-radar](https://github.com/jiwenbo0803-hub/btc-jev-radar) | BTC Jev + GPT market radar | 0 | JavaScript | 2026-09-21 |
| [jjjjuuudde/jev-ad-blocker](https://github.com/jjjjuuudde/jev-ad-blocker) | — | 0 | JavaScript | 2026-09-18 |
| [jkup/jevprint](https://github.com/jkup/jevprint) | — | 0 | TypeScript | 2026-09-21 |
| [jlov7/jev-decision-lab](https://github.com/jlov7/jev-decision-lab) | A local lab for seeing what TypeSafe's Jev judgment model does on realistic business cases: typed answers, pr… | 0 | Python | 2026-09-21 |
| [joaoh82/coffee-under-fire](https://github.com/joaoh82/coffee-under-fire) | Coffee Under Fire: a free browser shooter with NPC tactics powered by TypeSafe AI’s Jev model. Play at https:… | 0 | TypeScript | 2026-09-21 |
| [JoelLewis/game-coach](https://github.com/JoelLewis/game-coach) | Browser chess coach on Cloudflare: Stockfish owns truth, Jev owns judgment | 0 | TypeScript | 2026-09-20 |
| [JohnCari/rossrecall](https://github.com/JohnCari/rossrecall) | RossRecall: an AI litigation associate that quotes a real case file, checks every sentence against its source… | 0 | TypeScript | 2026-09-22 |
| [johnny-ggao/trading-agent](https://github.com/johnny-ggao/trading-agent) | trading agent for dsh | 0 | TypeScript | 2026-09-22 |
| [johnpozy/codriver](https://github.com/johnpozy/codriver) | Instead of locking a whole session to one model, you pick Auto in the model picker — and for every turn, Codr… | 0 | TypeScript | 2026-09-20 |
| [JohnsonRan/pi-jev](https://github.com/JohnsonRan/pi-jev) | Claude-style auto-mode classifier for Pi, powered by TypeSafe Jev | 0 | TypeScript | 2026-09-21 |
| [jolehuit/jev-downloads-sorter](https://github.com/jolehuit/jev-downloads-sorter) | A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon | 0 | Python | 2026-09-21 |
| [jon-devlapaz/jev-decisions](https://github.com/jon-devlapaz/jev-decisions) | — | 0 | — | 2026-09-17 |
| [jongyunhur/jev-webagent-bench](https://github.com/jongyunhur/jev-webagent-bench) | Evaluating System-One Action Selection in Long-Horizon Web Agents | 0 | Python | 2026-09-22 |
| [JonusNattapong/jev-my-bro](https://github.com/JonusNattapong/jev-my-bro) | — | 0 | Python | 2026-09-22 |
| [jose-troche/live-rubric](https://github.com/jose-troche/live-rubric) | A writing editor that re-scores 15 typed rubric dimensions on every typing pause — one Jev System One call pe… | 0 | TypeScript | 2026-09-20 |
| [joseluissaorin/prosper-jev](https://github.com/joseluissaorin/prosper-jev) | Recepcionista de voz con Jev (Sistema 1) y Gemini (Sistema 2) para el reto Prosper de HackSpain | 0 | Python | 2026-09-20 |
| [jostoz/sweetlips](https://github.com/jostoz/sweetlips) | Edge voice pipeline: mic -> FireRedVAD -> Confucius4-R2T2 (streaming ASR) -> Jev System1 -> Kokoro TTS -> alt… | 0 | Python | 2026-09-22 |
| [jourdanlabs/assay-001](https://github.com/jourdanlabs/assay-001) | ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Spl… | 0 | Python | 2026-09-21 |
| [jpanasuk-netizen/jaspers-trade-bot](https://github.com/jpanasuk-netizen/jaspers-trade-bot) | Jasper's Trade Bot — Kalshi 15-minute BTC YES/NO desk (no secrets) | 0 | Python | 2026-09-22 |
| [jpollard-cs/jev-observatory](https://github.com/jpollard-cs/jev-observatory) | — | 0 | JavaScript | 2026-09-21 |
| [jpowersdev/neuralint](https://github.com/jpowersdev/neuralint) | AI code review against your repository's rules, powered by TypeSafe AI's Jev. | 0 | HTML | 2026-09-22 |
| [jrmello4/devorbit](https://github.com/jrmello4/devorbit) | — | 0 | TypeScript | 2026-09-21 |
| [jsherman999/engineer-assistant](https://github.com/jsherman999/engineer-assistant) | — | 0 | Swift | 2026-09-17 |
| [jsherman999/jev_local_web_seatch-](https://github.com/jsherman999/jev_local_web_seatch-) | — | 0 | Python | 2026-09-19 |
| [juan294/sutura](https://github.com/juan294/sutura) | AI agents make CI pass. Sutura verifies the fix, filters flaky failures, rejects unsafe shortcuts, and opens … | 0 | TypeScript | 2026-09-21 |
| [juanlentino/jev-comment-analysis](https://github.com/juanlentino/jev-comment-analysis) | Backs the WordPress AI plugin's Comment Moderation with TypeSafe Jev, through Connector for TypeSafe Jev | 0 | PHP | 2026-09-20 |
| [judoaseeta/duckdb-jev](https://github.com/judoaseeta/duckdb-jev) | Ask your DuckDB tables questions in plain language. A DuckDB port of pg-jev, powered by TypeSafe's Jev. | 0 | C++ | 2026-09-21 |
| [Jul0t/jevent-bot](https://github.com/Jul0t/jevent-bot) | JEvent Bot | 0 | JavaScript | 2026-09-21 |
| [julianarchila/jev-experiments](https://github.com/julianarchila/jev-experiments) | — | 0 | TypeScript | 2026-09-19 |
| [JulianLee1117/jev-moneyprinter](https://github.com/JulianLee1117/jev-moneyprinter) | — | 0 | Python | 2026-09-19 |
| [junyeong-nero/jev-doom](https://github.com/junyeong-nero/jev-doom) | Play DOOM with Jev | 0 | Python | 2026-09-20 |
| [just-be-dev/jev-sat](https://github.com/just-be-dev/jev-sat) | — | 0 | TypeScript | 2026-09-20 |
| [justinfrevert/jev-agent-safety](https://github.com/justinfrevert/jev-agent-safety) | — | 0 | Python | 2026-09-22 |
| [JustinRoderick/jev-test](https://github.com/JustinRoderick/jev-test) | Testing typesafe.ai new model Jev | 0 | TypeScript | 2026-09-21 |
| [JustRelaXD/context-pack](https://github.com/JustRelaXD/context-pack) | — | 0 | TypeScript | 2026-09-20 |
| [JustSebNL/timekeeper](https://github.com/JustSebNL/timekeeper) | Local-first project execution memory system for humans and agents. | 0 | Go | 2026-09-21 |
| [JxWayne890/jev-control-plane](https://github.com/JxWayne890/jev-control-plane) | JEV powered model and reasoning routing for delegated Codex work | 0 | Python | 2026-09-22 |
| [jxzxl07/JevDesk](https://github.com/jxzxl07/JevDesk) | Local-first push-to-talk desktop agent that completes work visibly, verifies outcomes, and compiles successfu… | 0 | TypeScript | 2026-09-21 |
| [JYbill/xqv-skills](https://github.com/JYbill/xqv-skills) | 个人认为非常适合opencode、codecode的skills | 0 | JavaScript | 2026-09-21 |
| [jyje/pilot-typesafeai-jev](https://github.com/jyje/pilot-typesafeai-jev) | 👩‍🔬 Pilot of the decision model 'jev' from TypeSafe AI | 0 | Jupyter Notebook | 2026-09-21 |
| [jyothepro/jev-games](https://github.com/jyothepro/jev-games) | — | 0 | — | 2026-09-21 |
| [ka10ryu1/smart-leger](https://github.com/ka10ryu1/smart-leger) | クレジットカード利用履歴をAIで自動分類し、家計の支出を管理・分析する家計簿アプリ。初期検証ではJevを利用。 | 0 | Python | 2026-09-21 |
| [kabeza/JEV_ebaysearch](https://github.com/kabeza/JEV_ebaysearch) | — | 0 | TypeScript | 2026-09-21 |
| [kabishou-lab/keepdrop](https://github.com/kabishou-lab/keepdrop) | Jev-compatible System One on the LLM you already pay for. Verbatim keep/drop compaction. No waitlist. | 0 | TypeScript | 2026-09-22 |
| [kablewithak/auragateway](https://github.com/kablewithak/auragateway) | Cache-aware agent runtime and evaluation harness for controlled AI reliability benchmarking. | 0 | Python | 2026-09-21 |
| [kabukisensei/coop-agent](https://github.com/kabukisensei/coop-agent) | — | 0 | JavaScript | 2026-09-22 |
| [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) | TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness | 0 | JavaScript | 2026-09-20 |
| [kairin/stay-up](https://github.com/kairin/stay-up) | Lightweight Windows keep-awake helper and consolidated PowerToys research | 0 | Python | 2026-09-22 |
| [kanaharu20/jev-learn](https://github.com/kanaharu20/jev-learn) | — | 0 | HTML | 2026-09-19 |
| [kang9307/lotto-generator](https://github.com/kang9307/lotto-generator) | BrainDetox Utility Box | 0 | HTML | 2026-09-21 |
| [kangshifu1/jev-skills-market](https://github.com/kangshifu1/jev-skills-market) | Community Jev skill market and assistant for automation testing, finance research and voice workflows. Comput… | 0 | JavaScript | 2026-09-22 |
| [karanb192/jev-skill-scout](https://github.com/karanb192/jev-skill-scout) | Finds the turns where Claude Code should have loaded one of your skills and did not, judged by TypeSafe's Jev… | 0 | JavaScript | 2026-09-21 |
| [kaustav1996/reflex](https://github.com/kaustav1996/reflex) | A coding agent and personal assistant with System One reflexes (TypeSafe Jev) on top of the Pi coding agent | 0 | TypeScript | 2026-09-21 |
| [ke-suke0215/contract-review-demo](https://github.com/ke-suke0215/contract-review-demo) | Bun + Hono + TypeScript contract review demo with GPT-5.6 Luna and Jev | 0 | HTML | 2026-09-20 |
| [keepwonder/jev-hub](https://github.com/keepwonder/jev-hub) | Jev / TypeSafe AI 中文跟踪与文档聚合站 | 0 | Astro | 2026-09-22 |
| [kelinbruce/jev-aico](https://github.com/kelinbruce/jev-aico) | AICO skill selection benchmarks, JEV comparisons, and local KEV testing | 0 | Python | 2026-09-22 |
| [kentaro/jev-shogi](https://github.com/kentaro/jev-shogi) | 判定特化モデル Jev に将棋を指させる実験（ロリポップ！AIゲートウェイ経由） | 0 | Python | 2026-09-19 |
| [kevin9327/jev-master](https://github.com/kevin9327/jev-master) | Typed System One decisions with Jev: Choice + Score + Noul composed in code. | 0 | Python | 2026-09-20 |
| [KeWang0622/jev-board-game](https://github.com/KeWang0622/jev-board-game) | Belief as a primitive: instrumenting social-deduction games (Undercover, Werewolf, Avalon) with TypeSafe's ca… | 0 | Python | 2026-09-21 |
| [KhaiStimpson/JevGen](https://github.com/KhaiStimpson/JevGen) | — | 0 | C# | 2026-09-19 |
| [kidow/lingo](https://github.com/kidow/lingo) | — | 0 | TypeScript | 2026-09-22 |
| [kierandotai/jev-scout](https://github.com/kierandotai/jev-scout) | Jev-scored observable web research for MCP agents — every query, result, and fetched page judged for relevanc… | 0 | TypeScript | 2026-09-21 |
| [kijung4290/maeum-on-attendance-care](https://github.com/kijung4290/maeum-on-attendance-care) | 어르신 프로그램 출석 위험 모니터링 대시보드 · TypeSafe AI JEV 연동 | 0 | JavaScript | 2026-09-21 |
| [kingdsa/jev-chinese-grader](https://github.com/kingdsa/jev-chinese-grader) | — | 0 | TypeScript | 2026-09-22 |
| [kinoko34077/jev-audit](https://github.com/kinoko34077/jev-audit) | — | 0 | Python | 2026-09-22 |
| [kirin765/jev-email-filter](https://github.com/kirin765/jev-email-filter) | — | 0 | Python | 2026-09-22 |
| [kirkchen/devbox](https://github.com/kirkchen/devbox) | — | 0 | Python | 2026-09-22 |
| [kkwelfare/jev-route-screening-public](https://github.com/kkwelfare/jev-route-screening-public) | — | 0 | Python | 2026-09-22 |
| [kleosr/jevsor](https://github.com/kleosr/jevsor) | Jev-compatible decision engine over caller-provided models | 0 | Python | 2026-09-19 |
| [klren0312/jev-trade](https://github.com/klren0312/jev-trade) | — | 0 | JavaScript | 2026-09-22 |
| [Kmassidik/Everything-with-jev-ai](https://github.com/Kmassidik/Everything-with-jev-ai) | a single project for all product using jev ai | 0 | Go | 2026-09-21 |
| [knowlet/JevGuard-NSFA](https://github.com/knowlet/JevGuard-NSFA) | Experimental System One implementation of the SingGuard-NSFA agent-security taxonom. | 0 | Python | 2026-09-21 |
| [KO6BXL/jev-bot](https://github.com/KO6BXL/jev-bot) | A discord chatbot that respones when jev decides it should. | 0 | TypeScript | 2026-09-22 |
| [koderhack/readproof](https://github.com/koderhack/readproof) | — | 0 | HTML | 2026-09-21 |
| [koh11235813/skills](https://github.com/koh11235813/skills) | — | 0 | TeX | 2026-09-20 |
| [kokuren333/jev-jmle-benchmark](https://github.com/kokuren333/jev-jmle-benchmark) | Benchmarking Jev on Japanese Medical Licensing Examination questions: accuracy, calibration, latency, image d… | 0 | Python | 2026-09-21 |
| [kong75/jev-directory](https://github.com/kong75/jev-directory) | Copyable prompts, typed decision patterns, and practical guides for Jev by TypeSafe. Free, independent, and s… | 0 | Astro | 2026-09-20 |
| [Korbeil/opencode-jev-plugin](https://github.com/Korbeil/opencode-jev-plugin) | — | 0 | TypeScript | 2026-09-21 |
| [kostysh/goblin-hr](https://github.com/kostysh/goblin-hr) | Simple Jev usage demo | 0 | TypeScript | 2026-09-17 |
| [kp84-hub/kyrex](https://github.com/kp84-hub/kyrex) | "Terminal AI agent — Go TUI + Python engine with agentic coding tools" | 0 | Python | 2026-09-21 |
| [krushideep/Worldtour](https://github.com/krushideep/Worldtour) | An interesting idea to test Jev's capabilities to travers to all the capitals of the world in a shortest dist… | 0 | TypeScript | 2026-09-21 |
| [KsanaDock/jev-go](https://github.com/KsanaDock/jev-go) | — | 0 | JavaScript | 2026-09-21 |
| [kspviswa/chakravyuha-oss](https://github.com/kspviswa/chakravyuha-oss) | Chakravyuha (OSS) — the polar ring-maze where every move is a Laya decision. Same experiment as chakravyuha-j… | 0 | JavaScript | 2026-09-20 |
| [Kstudy101/Gyosei-navi](https://github.com/Kstudy101/Gyosei-navi) | 行政書士ナビ・ジャーナル — 行政書士業務の総合情報メディア（Next.js 静的サイト + 一次情報収集パイプライン） | 0 | MDX | 2026-09-22 |
| [kt3k/jevmaze](https://github.com/kt3k/jevmaze) | — | 0 | TypeScript | 2026-09-19 |
| [ktsu2i/jevgate](https://github.com/ktsu2i/jevgate) | — | 0 | Go | 2026-09-20 |
| [ktsu2i/jevgate-action](https://github.com/ktsu2i/jevgate-action) | — | 0 | Shell | 2026-09-21 |
| [kunobi-ninja/kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev) | Rust client for the TypeSafe System One API (Jev) | 0 | Rust | 2026-09-18 |
| [kuri-leo/yet-another-jev](https://github.com/kuri-leo/yet-another-jev) | — | 0 | Python | 2026-09-22 |
| [kurihada/pi-jev-permit](https://github.com/kurihada/pi-jev-permit) | A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call be… | 0 | TypeScript | 2026-09-21 |
| [kurousa/jev](https://github.com/kurousa/jev) | — | 0 | Python | 2026-09-22 |
| [kushalpatil07/jevify](https://github.com/kushalpatil07/jevify) | A repository for jevify | 0 | Python | 2026-09-20 |
| [Kylejeong2/jev-judge](https://github.com/Kylejeong2/jev-judge) | — | 0 | TypeScript | 2026-09-21 |
| [LachlanLindsay/is-jev-calibrated](https://github.com/LachlanLindsay/is-jev-calibrated) | — | 0 | — | 2026-09-21 |
| [Lagnajit09/sgrep](https://github.com/Lagnajit09/sgrep) | sgrep - semantic grep, powered by Jev | 0 | Python | 2026-09-21 |
| [laihenyi/pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser) | Browser and macOS desktop agent for pi: Jev (TypeSafe System One) chooses each action from a structured obser… | 0 | TypeScript | 2026-09-20 |
| [lalitsonawane/jev-one-system](https://github.com/lalitsonawane/jev-one-system) | — | 0 | TypeScript | 2026-09-20 |
| [lastlad/jev-model-router](https://github.com/lastlad/jev-model-router) | — | 0 | Python | 2026-09-21 |
| [latere-ai/typesafe-ai-go-sdk](https://github.com/latere-ai/typesafe-ai-go-sdk) | Archived: Go client for the TypeSafe API. Use latere.ai/x/pkg/typesafeai. | 0 | Go | 2026-09-19 |
| [laurentfabre/databricks-jev-pdf-lab](https://github.com/laurentfabre/databricks-jev-pdf-lab) | Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs a… | 0 | Python | 2026-09-20 |
| [LauricellaAndrea/Jev-browser-remote](https://github.com/LauricellaAndrea/Jev-browser-remote) | beta project di use-computer su google chrome mediante l'uso di Jerv, riducendo notevolmente la latenza e i c… | 0 | TypeScript | 2026-09-21 |
| [lawzhougc/jev-openclash](https://github.com/lawzhougc/jev-openclash) | jev-openclash | 0 | Python | 2026-09-21 |
| [lazniak/Jev-UltraCuse](https://github.com/lazniak/Jev-UltraCuse) | Najszybszy Computer Use na Jev 1.13: Rust, portable exe, UIA + SendInput + PowerShell, realtime STT (PL) | 0 | Rust | 2026-09-21 |
| [lazyoft/jev-explorer](https://github.com/lazyoft/jev-explorer) | Goal-driven browser exploration with Jev, compact evidence, and persistent supervisor handoff over MCP. | 0 | TypeScript | 2026-09-20 |
| [lbbbboom/jev-chat](https://github.com/lbbbboom/jev-chat) | — | 0 | Python | 2026-09-22 |
| [LeandroSantosP/email-classifier](https://github.com/LeandroSantosP/email-classifier) | — | 0 | TypeScript | 2026-09-22 |
| [ledgerwerk/pyjev](https://github.com/ledgerwerk/pyjev) | Reusable, inspectable Jev decision contracts for Python applications and automation. | 0 | Python | 2026-09-21 |
| [lee-lou2/jev-tree](https://github.com/lee-lou2/jev-tree) | Hierarchical knowledge service: a model carries context down a taxonomy tree to search and ingest Q&A. One Ru… | 0 | Rust | 2026-09-22 |
| [lenML/deep-jev-seek](https://github.com/lenML/deep-jev-seek) | Use DeepSeek/llamacpp like Jev. (just api router) | 0 | TypeScript | 2026-09-21 |
| [lennon-li/HMA](https://github.com/lennon-li/HMA) | — | 0 | Go | 2026-09-18 |
| [leofurio/AutoTestJev](https://github.com/leofurio/AutoTestJev) | AUTONOMOUS TESTING with JEV | 0 | Python | 2026-09-22 |
| [Leonezz/quire](https://github.com/Leonezz/quire) | Quire — a calm reading surface for everything you subscribe to: blogs, newsletters, papers and PDFs, with hig… | 0 | TypeScript | 2026-09-21 |
| [leonininder/remember-me](https://github.com/leonininder/remember-me) | Agent memory that decides what to hydrate — local topology recall + TypeSafe Jev gates (not another dump-ever… | 0 | Python | 2026-09-21 |
| [lhotwll217/jev-cli](https://github.com/lhotwll217/jev-cli) | JSON-in, typed-decisions-out CLI for the TypeSafe System One API | 0 | TypeScript | 2026-09-21 |
| [LiamCarlin/Navi](https://github.com/LiamCarlin/Navi) | Jev-powered Spotlight replacement for macOS — typed fast decisions, Claude for answers and computer use, loca… | 0 | Swift | 2026-09-22 |
| [liatrio/jev-demo-jburns24](https://github.com/liatrio/jev-demo-jburns24) | — | 0 | Python | 2026-09-22 |
| [lifefesta/jev-mail-router](https://github.com/lifefesta/jev-mail-router) | — | 0 | TypeScript | 2026-09-20 |
| [LightningK0ala/jev-marshal](https://github.com/LightningK0ala/jev-marshal) | Semantic PR policy checks powered by Jev. | 0 | TypeScript | 2026-09-20 |
| [LilDojd/jevons](https://github.com/LilDojd/jevons) | A bounded Pi execution supervisor powered by TypeSafe Jev: decisions, recovery, review and verification. | 0 | TypeScript | 2026-09-21 |
| [Lindagr78/openeval](https://github.com/Lindagr78/openeval) | Evaluate AI agents and LLMs with plain functions, isolated runs, and inspectable scores. | 0 | TypeScript | 2026-09-22 |
| [linksawakening/jev-harness](https://github.com/linksawakening/jev-harness) | Self-hosted project harness: code owns the loop, TypeSafe Jev owns the judgments, the LLM owns the content. | 0 | Python | 2026-09-21 |
| [liou666/senseek](https://github.com/liou666/senseek) | Senseek — Semantic Page Search browser extension. Find what you mean. Powerd by Jev | 0 | JavaScript | 2026-09-21 |
| [lirantal/discoprint](https://github.com/lirantal/discoprint) | Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it a… | 0 | JavaScript | 2026-09-22 |
| [listepo/cox](https://github.com/listepo/cox) | A modular terminal coding agent in Rust with a safe, event-driven core. | 0 | Rust | 2026-09-20 |
| [liuup/jev-research](https://github.com/liuup/jev-research) | 📊 The third-party research implementation of jev. | 0 | Python | 2026-09-20 |
| [liuyejinghong/ai-mud](https://github.com/liuyejinghong/ai-mud) | Server-authoritative dark-fantasy Web MUD with governed AI narrative systems. | 0 | TypeScript | 2026-09-21 |
| [liyumini/Jev-driven-agent-loop](https://github.com/liyumini/Jev-driven-agent-loop) | — | 0 | TypeScript | 2026-09-20 |
| [ljbuturovic/jevgram](https://github.com/ljbuturovic/jevgram) | — | 0 | Python | 2026-09-22 |
| [llaplace-dev/jev-overcome-cartpole](https://github.com/llaplace-dev/jev-overcome-cartpole) | — | 0 | Python | 2026-09-22 |
| [lldois/dsh-jev](https://github.com/lldois/dsh-jev) | TypeSafe Jev System One semantic tool routing and typed decisions for DeepSeek Harness (DSH) | 0 | JavaScript | 2026-09-21 |
| [logan-han/hearth](https://github.com/logan-han/hearth) | Self-hosted family assistant in a Telegram chat: shared calendar, lists, reminders, email and money answers. … | 0 | TypeScript | 2026-09-21 |
| [loongWoong/jev-zen](https://github.com/loongWoong/jev-zen) | Jev-inspired validation and local reimplementation of Laya, an open-weight System-1 typed decision model. | 0 | HTML | 2026-09-22 |
| [lorensation/llm-cost-optimizer-jev](https://github.com/lorensation/llm-cost-optimizer-jev) | An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM… | 0 | Python | 2026-09-20 |
| [LoTwT/uno-jev](https://github.com/LoTwT/uno-jev) | — | 0 | TypeScript | 2026-09-21 |
| [louispaulet/jev-playground](https://github.com/louispaulet/jev-playground) | Testing the brand new JEV model | 0 | Python | 2026-09-22 |
| [Loule95450/jev-free-router](https://github.com/Loule95450/jev-free-router) | Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router) | 0 | JavaScript | 2026-09-21 |
| [luanewb/jevai](https://github.com/luanewb/jevai) | — | 0 | Python | 2026-09-19 |
| [lucasfth/config](https://github.com/lucasfth/config) | Relevant config files for meee | 0 | Nix | 2026-09-18 |
| [lucianoon/backoffice-agents](https://github.com/lucianoon/backoffice-agents) | Piloto de agentes de backoffice: LLM gera e raciocina, Jev (TypeSafe AI) decide, roteia e verifica | 0 | Python | 2026-09-21 |
| [luisrapalino/jev-smart-bets](https://github.com/luisrapalino/jev-smart-bets) | Asistente y framework de apuestas deportivas open-source con Next.js e IA (Jev) | 0 | TypeScript | 2026-09-21 |
| [luizribeiro/jevrs](https://github.com/luizribeiro/jevrs) | Rust client for TypeSafe AI's Jev (System One) model: sans-IO core, typed questions, WASI transports | 0 | Rust | 2026-09-21 |
| [lukasikgrzegorz/jev-ai-test](https://github.com/lukasikgrzegorz/jev-ai-test) | — | 0 | JavaScript | 2026-09-21 |
| [Lushangtu123/CS-166-Final-Project](https://github.com/Lushangtu123/CS-166-Final-Project) | — | 0 | Python | 2026-09-22 |
| [luw2007/omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions) | OMP / pi-coding-agent extensions that delegate acceptance gating and subagent routing to the Typesafe Jev dec… | 0 | TypeScript | 2026-09-22 |
| [LVTD-LLC/games](https://github.com/LVTD-LLC/games) | Small web games, independently built. Astro catalogue at games.lvtd.dev. | 0 | JavaScript | 2026-09-18 |
| [LYJW131/lyjwpage](https://github.com/LYJW131/lyjwpage) | 个人主页：信息展示 + 实时状态（Emby / Apple Music / 充电头 / Vibe Coding） | 0 | TypeScript | 2026-09-22 |
| [m-mizutani/semgate](https://github.com/m-mizutani/semgate) | Semantic request filtering and routing for Go HTTP, powered by TypeSafe AI. | 0 | Go | 2026-09-21 |
| [m-naw/ux-explore](https://github.com/m-naw/ux-explore) | Goal-driven synthetic persona testing for websites: Jev decides, Playwright acts, one Sonnet report per journ… | 0 | TypeScript | 2026-09-21 |
| [maci0/rebrew](https://github.com/maci0/rebrew) | Compiler-in-the-loop decompilation workbench for binary-matching game reversing. | 0 | Python | 2026-09-21 |
| [madousho-ai/decidophobia](https://github.com/madousho-ai/decidophobia) | — | 0 | Python | 2026-09-22 |
| [maguro777R/jev-test](https://github.com/maguro777R/jev-test) | jevのテストをします | 0 | JavaScript | 2026-09-21 |
| [mahavirn/mnjev-cli](https://github.com/mahavirn/mnjev-cli) | CLI for JEV Model | 0 | TypeScript | 2026-09-21 |
| [mahirmlk/mahirmalik](https://github.com/mahirmlk/mahirmalik) | sharing about myself, and my work through this personal website. | 0 | TypeScript | 2026-09-21 |
| [mahynotch/newsscore](https://github.com/mahynotch/newsscore) | One number per ticker from the week's news. Async Python library + CLI, pluggable scorer, Jev by default. | 0 | Python | 2026-09-19 |
| [maito1201/jev-harness](https://github.com/maito1201/jev-harness) | TypeSafe jev でエージェントの応答を審査し、形式的な完了を Stop hook で差し戻す Claude Code / Codex plugin | 0 | JavaScript | 2026-09-22 |
| [makefunstuff/clank](https://github.com/makefunstuff/clank) | minimal unix-style local-inference cli | 0 | Rust | 2026-09-20 |
| [makefunstuff/jev-lsp](https://github.com/makefunstuff/jev-lsp) | An LSP server whose ambient pass runs the rules a repository states in `.jev/rules/*.json`: each candidate li… | 0 | Rust | 2026-09-21 |
| [makeorbreakshop/djr3x_voice](https://github.com/makeorbreakshop/djr3x_voice) | — | 0 | Python | 2026-09-17 |
| [makiisthenes/JevAIExperimentation](https://github.com/makiisthenes/JevAIExperimentation) | Learning about Jev, Typesafes flagship structured decision model. | 0 | Python | 2026-09-21 |
| [MalinrRuwan/experiments](https://github.com/MalinrRuwan/experiments) | Polyglot experiments sandbox | 0 | TypeScript | 2026-09-17 |
| [manali-co/yapp](https://github.com/manali-co/yapp) | Hold a key, talk, and your Mac acts while you're still talking. Local Whisper + TypeSafe Jev, by Manali. | 0 | Python | 2026-09-22 |
| [ManatoYamashita/tcu-setagayafes97-web](https://github.com/ManatoYamashita/tcu-setagayafes97-web) | 東京都市大学 第97回世田谷祭（2026）のwebサイト | 0 | TypeScript | 2026-09-22 |
| [mandarkashikar/linkedin-slop-filter](https://github.com/mandarkashikar/linkedin-slop-filter) | Chrome extension prototype that filters low-value AI slop from LinkedIn using Jev classification | 0 | JavaScript | 2026-09-22 |
| [mandubian/quiet-space](https://github.com/mandubian/quiet-space) | — | 0 | TypeScript | 2026-09-19 |
| [MANI8148/the-daily-byte](https://github.com/MANI8148/the-daily-byte) | — | 0 | TypeScript | 2026-09-21 |
| [manifoldfrs/dotfiles](https://github.com/manifoldfrs/dotfiles) | config files | 0 | Python | 2026-09-21 |
| [manjunathshiva/jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench) | TypeSafe Jev 1.13 vs Claude Fable 5.1, GPT-6 Astra, Kimi K3, MiniMax M3 and DeepSeek V4.1 Flash on 200 typed … | 0 | Python | 2026-09-20 |
| [manutej/jev](https://github.com/manutej/jev) | JEV — applied double operadic type system (Libkind–Myers, arXiv:2505.18329). Colored operads, masked-language… | 0 | TypeScript | 2026-09-22 |
| [maraichr/jev-triage](https://github.com/maraichr/jev-triage) | Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter | 0 | JavaScript | 2026-09-20 |
| [marcelormendes/diffninja](https://github.com/marcelormendes/diffninja) | Focused local PR reviews with calldiff and Jev | 0 | TypeScript | 2026-09-21 |
| [MarcoLoDico/pi-jev-router](https://github.com/MarcoLoDico/pi-jev-router) | — | 0 | JavaScript | 2026-09-21 |
| [marcosmartinez/jev-acento](https://github.com/marcosmartinez/jev-acento) | ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and tok… | 0 | Python | 2026-09-21 |
| [marianimatteo-lexroom/poly-jev](https://github.com/marianimatteo-lexroom/poly-jev) | — | 0 | Python | 2026-09-21 |
| [MarkChu-git/typesafe-mcp](https://github.com/MarkChu-git/typesafe-mcp) | Research and scaffolding for a TypeSafe Jev MCP server | 0 | TypeScript | 2026-09-22 |
| [mas2194/maybe-jev-bySol](https://github.com/mas2194/maybe-jev-bySol) | — | 0 | HTML | 2026-09-21 |
| [mashmalol/Vis-Jev-vibe](https://github.com/mashmalol/Vis-Jev-vibe) | — | 0 | HTML | 2026-09-19 |
| [maskjelly/TiVM](https://github.com/maskjelly/TiVM) | Computer-use agent for a throwaway Linux desktop: AT-SPI accessibility-tree perception, TypeSafe Jev / GPT-5.… | 0 | Python | 2026-09-20 |
| [matchstick-trading/jev-regime-gate](https://github.com/matchstick-trading/jev-regime-gate) | Jev-powered regime gate for trading strategy backtests. Research experiment, not investment advice. | 0 | TypeScript | 2026-09-21 |
| [matt-riley/pi-extensions](https://github.com/matt-riley/pi-extensions) | Personal pi extension collection: /exit alias, read-only /plan mode | 0 | JavaScript | 2026-09-21 |
| [mattneel/typesafe.zig](https://github.com/mattneel/typesafe.zig) | An idiomatic Zig client for the TypeSafe AI API | 0 | Zig | 2026-09-18 |
| [matu79go/jev-hanko](https://github.com/matu79go/jev-hanko) | Measuring TypeSafe AI's Jev on 41-clause contract review (CUAD, 20,500 decisions) against fast, cheap LLMs — … | 0 | Python | 2026-09-21 |
| [mausalas99/r-mas](https://github.com/mausalas99/r-mas) | R+ 8.0 — Laboratorio clínico, notas de evolución e indicaciones; modos Sala e Interconsulta; listado de probl… | 0 | JavaScript | 2026-09-21 |
| [mavericksxx/typesafe-jev-history-globe](https://github.com/mavericksxx/typesafe-jev-history-globe) | — | 0 | TypeScript | 2026-09-21 |
| [max1874/open-computer-use](https://github.com/max1874/open-computer-use) | A macOS computer-use agent with a dynamic, indexed action space. No screenshots, no coordinates. A macOS port… | 0 | Python | 2026-09-20 |
| [maybern-tripp-smith/fedjev-bench](https://github.com/maybern-tripp-smith/fedjev-bench) | FOMC hawkishness: TypeSafe Jev pairwise Choice vs rate actions (+ Haiku 4.5 comparison). Pages in /docs. | 0 | Python | 2026-09-21 |
| [mayonaka-ratori/60s-magic](https://github.com/mayonaka-ratori/60s-magic) | — | 0 | TypeScript | 2026-09-22 |
| [mcgalleg/grokbot-jev-jobs](https://github.com/mcgalleg/grokbot-jev-jobs) | Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cro… | 0 | TypeScript | 2026-09-19 |
| [mcread29/gizmo](https://github.com/mcread29/gizmo) | — | 0 | TypeScript | 2026-09-22 |
| [meaningfree/jev-work](https://github.com/meaningfree/jev-work) | — | 0 | JavaScript | 2026-09-22 |
| [mednabouli/jev-ai-polymarket-copy-trading](https://github.com/mednabouli/jev-ai-polymarket-copy-trading) | Automated Polymarket copy trading bot with MCP servers, Telegram alerts, and profitable wallet tracking. Zero… | 0 | Python | 2026-09-21 |
| [meijustory123/OpenJev-Kit](https://github.com/meijustory123/OpenJev-Kit) | 参考jev实现的开源决策模型，并公开全部训练过程 | 0 | Python | 2026-09-22 |
| [meimingqi222/pi-plugins](https://github.com/meimingqi222/pi-plugins) | A bun workspace of independently published pi extensions: secret redaction (pi-redact) and Jev-based verbatim… | 0 | TypeScript | 2026-09-21 |
| [memeshee/nansen-league](https://github.com/memeshee/nansen-league) | A Telegram game where you draft proven smart-money wallets into weekly rounds settled on live Nansen PnL — pl… | 0 | Python | 2026-09-21 |
| [memorysaver/jev-atari-lab](https://github.com/memorysaver/jev-atari-lab) | Challenge Atari with Jev: structured decisions, value questions, and replayable experiments | 0 | Python | 2026-09-21 |
| [metrox-eth/moss-jev](https://github.com/metrox-eth/moss-jev) | MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision … | 0 | JavaScript | 2026-09-20 |
| [mfreeze77/oil](https://github.com/mfreeze77/oil) | — | 0 | Python | 2026-09-22 |
| [mheers/typesafeai-systemone-jev-go](https://github.com/mheers/typesafeai-systemone-jev-go) | Typed Go client for the TypeSafe System One API (Jev): structured questions and answers your code can act on.… | 0 | Go | 2026-09-21 |
| [mhingston/jev-agent-browser](https://github.com/mhingston/jev-agent-browser) | Confidence-gated browser action routing with TypeSafe Jev and agent-browser | 0 | TypeScript | 2026-09-21 |
| [mhingston/jev-cli](https://github.com/mhingston/jev-cli) | A small, provider-agnostic CLI for Jev. | 0 | TypeScript | 2026-09-21 |
| [mhmdkzr/jev](https://github.com/mhmdkzr/jev) | An unofficial Go client for TypeSafe's System One Jev model | 0 | Go | 2026-09-18 |
| [michaeljabbour/amplifier-bundle-fast-decisions](https://github.com/michaeljabbour/amplifier-bundle-fast-decisions) | Fast-decision layer for Amplifier: telemetry hook, read-only workspace tool, and an opt-in shadow/active deci… | 0 | Python | 2026-09-22 |
| [michaelpersonal/jev-trade-cc](https://github.com/michaelpersonal/jev-trade-cc) | Jev Can Trade Stocks — a point-in-time O'Neil momentum backtest where TypeSafe's System One model picks the e… | 0 | Python | 2026-09-22 |
| [MidasMulli/kev-ane](https://github.com/MidasMulli/kev-ane) | Kev-0.6B, a Jev-class decision model, running on the Apple Neural Engine — with the gates and instruments use… | 0 | Python | 2026-09-22 |
| [midorisawa/Shirakawa](https://github.com/midorisawa/Shirakawa) | タイムラインをAI（Jev）で浄化する | 0 | JavaScript | 2026-09-22 |
| [mihir-s-05/jev-reward-model](https://github.com/mihir-s-05/jev-reward-model) | — | 0 | Python | 2026-09-18 |
| [mikekelly/ex_jev](https://github.com/mikekelly/ex_jev) | — | 0 | Elixir | 2026-09-21 |
| [Milluna/jev-cloth](https://github.com/Milluna/jev-cloth) | — | 0 | HTML | 2026-09-21 |
| [Milo318/mailordinal](https://github.com/Milo318/mailordinal) | Decision-native enterprise inbox: typed AI signals, deterministic priority policy, confidence-aware routing. | 0 | TypeScript | 2026-09-20 |
| [minhgv/jev-mcp](https://github.com/minhgv/jev-mcp) | TypeSafe Jev MCP decision layer for coding agents and CI | 0 | TypeScript | 2026-09-18 |
| [Mishkun/judge-jev](https://github.com/Mishkun/judge-jev) | — | 0 | TypeScript | 2026-09-21 |
| [Mitravasu/jevu](https://github.com/Mitravasu/jevu) | JevU | 0 | Python | 2026-09-21 |
| [mittal-parth/jev-experiments](https://github.com/mittal-parth/jev-experiments) | — | 0 | Python | 2026-09-18 |
| [Miyamura80/among-us-jev](https://github.com/Miyamura80/among-us-jev) | 🔪🩸 Among Us played by Jev | 0 | TypeScript | 2026-09-21 |
| [mizchi/jev-gomoku](https://github.com/mizchi/jev-gomoku) | — | 0 | MoonBit | 2026-09-18 |
| [mjj2332/Quincy_Portal](https://github.com/mjj2332/Quincy_Portal) | Photos review and delivery web app | 0 | TypeScript | 2026-09-21 |
| [mjyoke1111/jev-lab](https://github.com/mjyoke1111/jev-lab) | Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks | 0 | TypeScript | 2026-09-22 |
| [mkruglikov/droidjev](https://github.com/mkruglikov/droidjev) | A fast, screenshot-free Android emulator clicker powered by TypeSafe's jev | 0 | JavaScript | 2026-09-20 |
| [mleyvaz/jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse) | Jev (TypeSafe AI) y el colapso entre conflicto e ignorancia. 3 experimentos via Vercel AI Gateway. Nota de ca… | 0 | Python | 2026-09-20 |
| [moamenFathy/Jev_voice_computer_use](https://github.com/moamenFathy/Jev_voice_computer_use) | — | 0 | Python | 2026-09-22 |
| [modal-projects/goodhart](https://github.com/modal-projects/goodhart) | Jev for preventing reward hacking. | 0 | Python | 2026-09-20 |
| [mohammedwessam2007/uberbondd](https://github.com/mohammedwessam2007/uberbondd) | — | 0 | JavaScript | 2026-09-22 |
| [mohannadize/jev-ielts-test](https://github.com/mohannadize/jev-ielts-test) | — | 0 | TypeScript | 2026-09-19 |
| [MohtashamMurshid/jev-speed-test](https://github.com/MohtashamMurshid/jev-speed-test) | Reproducible Jev vs fast LLM experiment: BANKING77 data, raw responses, confidence evaluation, and analysis | 0 | Python | 2026-09-22 |
| [MokiMeow/jev-fabric](https://github.com/MokiMeow/jev-fabric) | A typed decision control plane for bounded semantic choices with Jev and AI agents. | 0 | TypeScript | 2026-09-21 |
| [monet88/chang-store](https://github.com/monet88/chang-store) | — | 0 | TypeScript | 2026-09-21 |
| [MoonTory/pi-jev-harness](https://github.com/MoonTory/pi-jev-harness) | Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards to… | 0 | TypeScript | 2026-09-18 |
| [MoRohn/meridian-demo](https://github.com/MoRohn/meridian-demo) | Meridian \| AI context-intake and contraction risk & compliance micro-app with live TypeSafe AI vs OpenAI eva… | 0 | TypeScript | 2026-09-21 |
| [moto-taka/jev-orchestrator](https://github.com/moto-taka/jev-orchestrator) | — | 0 | TypeScript | 2026-09-19 |
| [mouadse/jev-vs-laya](https://github.com/mouadse/jev-vs-laya) | Can an at-home model match Jev? TypeSafe Jev vs self-hosted Laya on Moroccan Darija sentiment, with reproduci… | 0 | Python | 2026-09-22 |
| [mozhuanzuojing/dsh-shadow](https://github.com/mozhuanzuojing/dsh-shadow) | dsh-shadow: agent 思维/上下文/灵魂的投影记忆树(一切皆文件,一记忆一文件,read_shadow 可穿透) | 0 | TypeScript | 2026-09-21 |
| [mpiv-ai/bb-plugin-typesafe-router](https://github.com/mpiv-ai/bb-plugin-typesafe-router) | Routes a thread's first message to the right harness and model with TypeSafe (Jev), then asks you to confirm. | 0 | TypeScript | 2026-09-18 |
| [MrDesjardins/jev-send-guard](https://github.com/MrDesjardins/jev-send-guard) | — | 0 | Python | 2026-09-21 |
| [Mrmimee/hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev) | Jev (TypeSafe AI) System One decision engine plugin for Hermes Agent, backed by Agnes AI Flash. | 0 | Python | 2026-09-22 |
| [MrTrigger/yardmaster](https://github.com/MrTrigger/yardmaster) | Routing layer for AI coding agents: model, effort and account selection with quota pacing | 0 | Rust | 2026-09-21 |
| [msilvalcs/alinha-curriculo](https://github.com/msilvalcs/alinha-curriculo) | — | 0 | TypeScript | 2026-09-21 |
| [mtane0412/hanatane](https://github.com/mtane0412/hanatane) | hanatane.net (Ghost) monorepo: theme, OGP image generation, VPS infrastructure | 0 | JavaScript | 2026-09-20 |
| [mudassirnizamani/Bindery](https://github.com/mudassirnizamani/Bindery) | — | 0 | Python | 2026-09-21 |
| [mugenkyou/JEV-VS-ML](https://github.com/mugenkyou/JEV-VS-ML) | An independent, reproducible empirical benchmark comparing Jev 1.13.0 (a semantic classification LLM API) aga… | 0 | Jupyter Notebook | 2026-09-21 |
| [Muhammad-Zain01/jev-real-usecases](https://github.com/Muhammad-Zain01/jev-real-usecases) | — | 0 | Python | 2026-09-20 |
| [muratcanberber/JEV-TheFishGame](https://github.com/muratcanberber/JEV-TheFishGame) | 🐠 A multiplayer fish game where every AI decision is a TypeSafe Jev (System One) call — flee, hunt, roam, wit… | 0 | HTML | 2026-09-21 |
| [mushfiqk47/lms-jev](https://github.com/mushfiqk47/lms-jev) | Semantic ifs from open models, on a 3090 at home — or through LM Studio | 0 | Python | 2026-09-20 |
| [muthuishere/jevd](https://github.com/muthuishere/jevd) | Inference server for the openjev NLI cross-encoder. One command, downloads on first run, CPU and GPU. | 0 | Rust | 2026-09-20 |
| [Muzych/jev-x-tags](https://github.com/Muzych/jev-x-tags) | Tag X/Twitter accounts with TypeSafe Jev and hide posts by tag (Chrome MV3 / WXT). | 0 | TypeScript | 2026-09-21 |
| [myokoym/misereru-slide-jev](https://github.com/myokoym/misereru-slide-jev) | — | 0 | JavaScript | 2026-09-20 |
| [n-yokomachi/jev-dev](https://github.com/n-yokomachi/jev-dev) | 同じ発言を jev と LLM の両方に判定させ、感情の変動値のズレと応答速度を1画面で見比べるデモ（affectus + Vercel AI Gateway） | 0 | TypeScript | 2026-09-18 |
| [n0nuser/battlesnake-jev](https://github.com/n0nuser/battlesnake-jev) | A Battlesnake in Go where deterministic code owns tactics and a TypeSafe Jev classifier gets the judgment cal… | 0 | Go | 2026-09-20 |
| [nadeemcite/jev-crash-course](https://github.com/nadeemcite/jev-crash-course) | An 11-level crash course on Jev, TypeSafe AI's System One decision model — runnable examples against the real… | 0 | Python | 2026-09-22 |
| [nadyth/jev-crash-course](https://github.com/nadyth/jev-crash-course) | An 11-level crash course on Jev, TypeSafe AI's System One decision model — runnable examples against the real… | 0 | Python | 2026-09-22 |
| [nak1b/jev-experiments](https://github.com/nak1b/jev-experiments) | Small experiments with Jev by TypeSafe | 0 | TypeScript | 2026-09-21 |
| [NakliTechie/llamacpp-jev](https://github.com/NakliTechie/llamacpp-jev) | — | 0 | Python | 2026-09-22 |
| [NakliTechie/verdict](https://github.com/NakliTechie/verdict) | Sovereign typed decisions on your Mac — zero install. On-device Apple Foundation Models + Laya, Jev-compatibl… | 0 | Swift | 2026-09-22 |
| [NaluKicks-808/jev-field-guide-skill](https://github.com/NaluKicks-808/jev-field-guide-skill) | A Claude Code skill of field notes on Jev: which question shape fits which job, how to test a use before trus… | 0 | — | 2026-09-21 |
| [NaluKicks-808/jev-field-trial](https://github.com/NaluKicks-808/jev-field-trial) | A pre-registered field trial of Jev (TypeSafe's judgment model) on a second brain and Claude Code history: 20… | 0 | Python | 2026-09-21 |
| [NaluKicks-808/vault-search-bench](https://github.com/NaluKicks-808/vault-search-bench) | Test search over any Obsidian vault with zero labelling: the vault's own links are the answer key. Plain rank… | 0 | Python | 2026-09-21 |
| [namayasai/backstage-jev-operations-support](https://github.com/namayasai/backstage-jev-operations-support) | Jev-powered operations decision support for Backstage: readiness checks, incident triage, change review, temp… | 0 | TypeScript | 2026-09-21 |
| [nanami-0713/jev-resume-screening](https://github.com/nanami-0713/jev-resume-screening) | TypeSafe Jev (System One) 简历-JD 匹配度初筛：判据模板 + 正/负/陷阱三类样本测试档案，判据 v1→v3 迭代全程可复现 / Resume-JD screening with TypeS… | 0 | JavaScript | 2026-09-20 |
| [nardinmarcus/pi-jev-typesafe](https://github.com/nardinmarcus/pi-jev-typesafe) | TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discove… | 0 | TypeScript | 2026-09-19 |
| [narulaskaran/jev-data-questions](https://github.com/narulaskaran/jev-data-questions) | — | 0 | TypeScript | 2026-09-22 |
| [Nasrallah-AL/sessionwise](https://github.com/Nasrallah-AL/sessionwise) | Analyze, understand, and optimize AI sessions. Claude Code adapter, model-fit/cache/context/health metrics, o… | 0 | TypeScript | 2026-09-20 |
| [navidkashani/jev-guard](https://github.com/navidkashani/jev-guard) | Spam protection for WordPress comments, reviews and Contact Form 7 using the Jev decision model (independent,… | 0 | PHP | 2026-09-22 |
| [nawwwal/seriph](https://github.com/nawwwal/seriph) | — | 0 | TypeScript | 2026-09-18 |
| [naz3eh/raycast-jev](https://github.com/naz3eh/raycast-jev) | — | 0 | TypeScript | 2026-09-21 |
| [nekowasabi/jev-routing-mcp](https://github.com/nekowasabi/jev-routing-mcp) | — | 0 | TypeScript | 2026-09-18 |
| [NeOMakinG/kev-model-router](https://github.com/NeOMakinG/kev-model-router) | Jev-style model routing powered by kev — a tiny local System One model classifies every request and picks the… | 0 | Python | 2026-09-21 |
| [neostryder/mercury](https://github.com/neostryder/mercury) | Semantic email filtering for rpgm.tools - Loremaster-reviewed spam/phishing triage via ForwardEmail webhooks | 0 | Python | 2026-09-21 |
| [nevzataksoy/jev-trader-bybit](https://github.com/nevzataksoy/jev-trader-bybit) | — | 0 | TypeScript | 2026-09-21 |
| [NexTechnologies-MY/Mortar](https://github.com/NexTechnologies-MY/Mortar) | Booking-to-SPA conversion intelligence for property developers (YEI 3.0, Chin Hin Group) | 0 | JavaScript | 2026-09-20 |
| [ngouard5/jeveuxaider-design](https://github.com/ngouard5/jeveuxaider-design) | — | 0 | HTML | 2026-09-21 |
| [ngpestelos-mirrors/hermes-agent](https://github.com/ngpestelos-mirrors/hermes-agent) | Mirror of NousResearch/hermes-agent (full history) | 0 | Python | 2026-09-21 |
| [ngpestelos-mirrors/openclaw](https://github.com/ngpestelos-mirrors/openclaw) | Public full-history mirror of openclaw/openclaw (not a fork) | 0 | TypeScript | 2026-09-21 |
| [Nibir1/typesafe-go](https://github.com/Nibir1/typesafe-go) | Zero-dependency Go SDK for TypeSafe's System One API (Jev). Typed questions in, calibrated probabilities out … | 0 | Go | 2026-09-19 |
| [nickwinder/jev-judge](https://github.com/nickwinder/jev-judge) | Jev CLI for the jev-judge Claude/Codex skill. Wraps the official @typesafe-ai/sdk. | 0 | JavaScript | 2026-09-22 |
| [nickylin/jev-harness](https://github.com/nickylin/jev-harness) | Typed decision control plane for agents, powered by TypeSafe Jev | 0 | TypeScript | 2026-09-20 |
| [nicolasalveshenrique-spec/medical-knowledge-triage](https://github.com/nicolasalveshenrique-spec/medical-knowledge-triage) | A typed decision-routing prototype for turning medical learning material into deterministic study actions, de… | 0 | — | 2026-09-21 |
| [nighthawk6389/Jev-credit-agreement-parser](https://github.com/nighthawk6389/Jev-credit-agreement-parser) | — | 0 | Python | 2026-09-22 |
| [nik1tsyganov/conclave](https://github.com/nik1tsyganov/conclave) | A tri-vendor review panel: one seat builds, two check it in sessions of their own, and the votes are counted … | 0 | JavaScript | 2026-09-22 |
| [nikotaronosuke/jev-voice-decision](https://github.com/nikotaronosuke/jev-voice-decision) | Japanese speech → local STT → Jev typed decisions → deterministic actions. | 0 | Python | 2026-09-20 |
| [nirgal-soft/typesafe-rs](https://github.com/nirgal-soft/typesafe-rs) | A rust client for the TypeSafe AI API | 0 | Rust | 2026-09-21 |
| [nishimotz/hello-jev](https://github.com/nishimotz/hello-jev) | — | 0 | Python | 2026-09-19 |
| [NitayRabi/hunch](https://github.com/NitayRabi/hunch) | — | 0 | TypeScript | 2026-09-19 |
| [nitro527/jev_project](https://github.com/nitro527/jev_project) | — | 0 | Python | 2026-09-19 |
| [Nixz0824/rag-jev](https://github.com/Nixz0824/rag-jev) | 国服《英雄联盟》版本更新公告的本地 RAG 问答：数字只来自公告，Jev（TypeSafe System One）负责候选重排与回答自检 | 0 | Python | 2026-09-21 |
| [nmfisher/tina](https://github.com/nmfisher/tina) | Tina — a terminal multi-agent coding TUI (Tina Is No Agent) | 0 | Dart | 2026-09-22 |
| [noahbclarkson/typesafe-api-rs](https://github.com/noahbclarkson/typesafe-api-rs) | Ergonomic, strongly typed Rust client for the TypeSafe System One API (Jev) | 0 | Rust | 2026-09-21 |
| [Nofuture123/qonnwolfbuddy](https://github.com/Nofuture123/qonnwolfbuddy) | qonnwolf-buddy（简称 QW buddy）— 单项目轻量 AI 主控 | 0 | Shell | 2026-09-22 |
| [Nomarcus/FoodSim](https://github.com/Nomarcus/FoodSim) | — | 0 | HTML | 2026-09-21 |
| [NomekoGenkah/liticia](https://github.com/NomekoGenkah/liticia) | — | 0 | TypeScript | 2026-09-21 |
| [Non-Plus/fast-jev-llm](https://github.com/Non-Plus/fast-jev-llm) | Context optimization for Claude Code, Codex, and Cursor. | 0 | TypeScript | 2026-09-22 |
| [NoRaincheck/gliger](https://github.com/NoRaincheck/gliger) | Jev Adapter for GLiClass (GLiNER) Models | 0 | Python | 2026-09-20 |
| [notCorwin/SurfWax](https://github.com/notCorwin/SurfWax) | Chrome 侧边栏智能体插件 | 0 | TypeScript | 2026-09-21 |
| [notdogus/ai-adblocker](https://github.com/notdogus/ai-adblocker) | — | 0 | TypeScript | 2026-09-21 |
| [notfresh/big-news-at-2026](https://github.com/notfresh/big-news-at-2026) | — | 0 | — | 2026-09-21 |
| [ns2250225/voice-magic](https://github.com/ns2250225/voice-magic) | 基于jev模型的语音释放魔法技能网站 | 0 | JavaScript | 2026-09-21 |
| [nsillik/jevvin-off](https://github.com/nsillik/jevvin-off) | Prototyping against TypeSafe's Jev System One API: a one-ticket quickstart and a Bluesky Jetstream firehose d… | 0 | — | 2026-09-21 |
| [Nsilswal/opencode-toolrouter](https://github.com/Nsilswal/opencode-toolrouter) | opencode plugin: send the model only the MCP tools each request needs, picked by TypeSafe's Jev | 0 | TypeScript | 2026-09-19 |
| [nvkudva/laya-server](https://github.com/nvkudva/laya-server) | Run the Laya System One decision model locally behind TypeSafe's Jev wire API, with a demo page | 0 | Python | 2026-09-22 |
| [oat431/oralita_md](https://github.com/oat431/oralita_md) | — | 0 | HTML | 2026-09-21 |
| [obekt/jev-agentic-ops](https://github.com/obekt/jev-agentic-ops) | — | 0 | Python | 2026-09-19 |
| [Obrais-cloud/ticket-rerank](https://github.com/Obrais-cloud/ticket-rerank) | FastAPI service that reranks support tickets by urgency using TypeSafe (Jev / System One) | 0 | Python | 2026-09-21 |
| [Obrais-cloud/typesafe-translate](https://github.com/Obrais-cloud/typesafe-translate) | Escribe lenguaje natural y un LLM local lo compila a variables de TypeSafe (state + questions) y las ejecuta … | 0 | Python | 2026-09-21 |
| [oceanByte/tsai-cli](https://github.com/oceanByte/tsai-cli) | Unofficial CLI for the TypeSafe AI System One API. | 0 | TypeScript | 2026-09-21 |
| [Octalab-Inc/jqv](https://github.com/Octalab-Inc/jqv) | Decision API on stock Qwen3: shared-state prefill, isolated question branches, direct choice-token readout, t… | 0 | Python | 2026-09-22 |
| [octanevz/jev-playground-openrouter](https://github.com/octanevz/jev-playground-openrouter) | Local browser playground for TypeSafe's Jev decision model via OpenRouter. Python stdlib only. | 0 | JavaScript | 2026-09-20 |
| [octkmr/jev-demo](https://github.com/octkmr/jev-demo) | — | 0 | HTML | 2026-09-20 |
| [oguressive/sample-jev](https://github.com/oguressive/sample-jev) | — | 0 | TypeScript | 2026-09-22 |
| [oh-ashen-one/jev-lab](https://github.com/oh-ashen-one/jev-lab) | — | 0 | JavaScript | 2026-09-20 |
| [ohernandezdev/jevmod](https://github.com/ohernandezdev/jevmod) | Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you ow… | 0 | Python | 2026-09-21 |
| [ojusave/beat-jev](https://github.com/ojusave/beat-jev) | A penalty shootout powered by Render Workflows, TypeSafe Jev, and Render Postgres. Python and TypeScript exam… | 0 | TypeScript | 2026-09-21 |
| [Okura66/kahn1](https://github.com/Okura66/kahn1) | High-throughput, sub-20ms System 1 decision engine on LLM logits. Zero text generation, calibrated probabilit… | 0 | Python | 2026-09-22 |
| [OliverMao/TeleJev](https://github.com/OliverMao/TeleJev) | — | 0 | Python | 2026-09-22 |
| [oluwadunni1/Instagram](https://github.com/oluwadunni1/Instagram) | — | 0 | Python | 2026-09-21 |
| [OmarAlaaeldein/jev-verifier-skill](https://github.com/OmarAlaaeldein/jev-verifier-skill) | Fast 'System One' reflex for reasoning LLMs: typed probabilistic second opinions from Jev via OpenCode Zen, w… | 0 | — | 2026-09-21 |
| [omerfeyzioglu/JevOps](https://github.com/omerfeyzioglu/JevOps) | — | 0 | Python | 2026-09-21 |
| [omribenami/jev-operated-drone](https://github.com/omribenami/jev-operated-drone) | Autonomous Tello search drone: jev decides where and when to navigate | 0 | Python | 2026-09-22 |
| [OpenNekoPaw/JevFlow](https://github.com/OpenNekoPaw/JevFlow) | — | 0 | Python | 2026-09-22 |
| [openprose/prose-cli](https://github.com/openprose/prose-cli) | — | 0 | Python | 2026-09-21 |
| [oqzl/JevSamples](https://github.com/oqzl/JevSamples) | — | 0 | JavaScript | 2026-09-21 |
| [Oracle0703/xyai](https://github.com/Oracle0703/xyai) | 这是我们新项目的第一步 | 0 | Go | 2026-09-21 |
| [orlenko/aiq](https://github.com/orlenko/aiq) | Quota-aware router for pooled Claude Code and Codex subscriptions: PATH shims, rollover scoring, long-session… | 0 | Go | 2026-09-20 |
| [orlenko/skills](https://github.com/orlenko/skills) | — | 0 | Python | 2026-09-21 |
| [OrMizL/jev-compaction-bench](https://github.com/OrMizL/jev-compaction-bench) | Measure what context compaction deletes, how confident the model was, and whether the agent can still finish … | 0 | JavaScript | 2026-09-21 |
| [orvn/typesafe-tidbits](https://github.com/orvn/typesafe-tidbits) | — | 0 | TypeScript | 2026-09-20 |
| [OsirianLegacy/JevSimulation](https://github.com/OsirianLegacy/JevSimulation) | Building a Simulated world using Typesafe Ai's Jev to run entity choices, C++ 20, JSON for Jev Interactions, … | 0 | — | 2026-09-21 |
| [OsirianLegacy/JevTactics](https://github.com/OsirianLegacy/JevTactics) | — | 0 | JavaScript | 2026-09-19 |
| [OVRLab/jev-guided-decoding](https://github.com/OVRLab/jev-guided-decoding) | — | 0 | — | 2026-09-22 |
| [owainlewis/jev-examples](https://github.com/owainlewis/jev-examples) | Examples on how to use the AI model Jev. | 0 | Python | 2026-09-22 |
| [OxFrancesco/BeeGreat](https://github.com/OxFrancesco/BeeGreat) | — | 0 | TypeScript | 2026-09-21 |
| [ozzy2438/apply-os](https://github.com/ozzy2438/apply-os) | Apply OS — Personal career decision engine powered by TypeSafe AI (Jev). Ranks job postings, drafts applicati… | 0 | — | 2026-09-20 |
| [ozzy2438/flow-desk](https://github.com/ozzy2438/flow-desk) | Evidence-backed job discovery workspace with parallel browser flows, Jev-based typed decisions, and human-app… | 0 | — | 2026-09-21 |
| [pablozr/JevGuard](https://github.com/pablozr/JevGuard) | — | 0 | TypeScript | 2026-09-20 |
| [pakkio/nexus](https://github.com/pakkio/nexus) | — | 0 | Python | 2026-09-18 |
| [pangpond/herdr-theme-cobalt2](https://github.com/pangpond/herdr-theme-cobalt2) | Cobalt2 theme for Herdr (adapted from wesbos/cobalt2-iterm) | 0 | Python | 2026-09-18 |
| [patelvishwa112/jev-system-one-rlcd](https://github.com/patelvishwa112/jev-system-one-rlcd) | Jev System One AI & RLCD Reproduction Engine: Sub-70ms Calibrated Decisions with SmolLM-135M and 0 Output Tok… | 0 | HTML | 2026-09-21 |
| [pathak-r/how-good-is-jev](https://github.com/pathak-r/how-good-is-jev) | How good is Jev? TypeSafe Jev vs an LLM on the same intent-routing task. | 0 | TypeScript | 2026-09-21 |
| [PatrickLaflamme/typesafe-llm-router](https://github.com/PatrickLaflamme/typesafe-llm-router) | Experimental Typesafe.ai smart router: route prompts to LLMs with caching and cost awareness | 0 | Rust | 2026-09-21 |
| [Paul-Sizon/tab-organizer](https://github.com/Paul-Sizon/tab-organizer) | Chrome extension that groups your open tabs by category using TypeSafe AI | 0 | TypeScript | 2026-09-19 |
| [pav-bio-gh/spec-ptc-jev](https://github.com/pav-bio-gh/spec-ptc-jev) | Natural-language speculation gates for speculative programmatic tool calling (spec-ptc), judged by TypeSafe J… | 0 | Python | 2026-09-21 |
| [pavan142/jev-experiments](https://github.com/pavan142/jev-experiments) | — | 0 | TypeScript | 2026-09-21 |
| [PavelLizunov/jev-sentinel](https://github.com/PavelLizunov/jev-sentinel) | — | 0 | Rust | 2026-09-21 |
| [pawelmamcarz/procuracost](https://github.com/pawelmamcarz/procuracost) | Procurement cost calculator & path optimizer — academic research tool. Pipe vs. Field model, Random Forest pa… | 0 | TypeScript | 2026-09-22 |
| [pb-crackers/Jev-Cognigy-QA-Suite](https://github.com/pb-crackers/Jev-Cognigy-QA-Suite) | Score every Cognigy conversation against rubrics you write, using TypeSafe Jev instead of an LLM. CLI, local … | 0 | TypeScript | 2026-09-21 |
| [peach-zhang/typesafe-go](https://github.com/peach-zhang/typesafe-go) | TypeSafe System One (Jev) 的 Go SDK — 类型化判断与概率,代码掌控工作流 | 0 | Go | 2026-09-22 |
| [pedro-pscunha/guideme-python](https://github.com/pedro-pscunha/guideme-python) | Type-safe inline judgments from TypeSafe Jev, for Python | 0 | Python | 2026-09-22 |
| [pedro-pscunha/guideme-rust](https://github.com/pedro-pscunha/guideme-rust) | Judgments from TypeSafe Jev that read like Rust control flow: a yes/no is an if, a choice is an exhaustive ma… | 0 | Rust | 2026-09-22 |
| [pedroknigge/mcp_jev](https://github.com/pedroknigge/mcp_jev) | Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor & agents | 0 | TypeScript | 2026-09-20 |
| [pedrorau/feedback-radar-jev](https://github.com/pedrorau/feedback-radar-jev) | — | 0 | Astro | 2026-09-21 |
| [peekuh/jev-vs-rerankers](https://github.com/peekuh/jev-vs-rerankers) | — | 0 | Python | 2026-09-20 |
| [perrydunnit/strudel-jev-jam](https://github.com/perrydunnit/strudel-jev-jam) | — | 0 | TypeScript | 2026-09-22 |
| [PerryLink/laya-mcp](https://github.com/PerryLink/laya-mcp) | MCP server for Laya typed decisions (noul / choice / score): warm model sidecar, token-budget preflight, pers… | 0 | Python | 2026-09-22 |
| [pertrai1/my-opencode](https://github.com/pertrai1/my-opencode) | — | 0 | JavaScript | 2026-09-22 |
| [peskycipher/jevBMAD](https://github.com/peskycipher/jevBMAD) | — | 0 | Python | 2026-09-20 |
| [petercr/jev-orchestrator](https://github.com/petercr/jev-orchestrator) | An mini node orchestrator that uses Jev to handle routing to different LLMs based on difficulty. | 0 | TypeScript | 2026-09-21 |
| [peterrauscher/x-bookmark-sorter](https://github.com/peterrauscher/x-bookmark-sorter) | Chrome extension that auto-sorts your X bookmarks into folders using Jev. | 0 | JavaScript | 2026-09-21 |
| [pfoundation/ocAdvisorTool](https://github.com/pfoundation/ocAdvisorTool) | OpenCode Advanced Model Advisor Tool | 0 | TypeScript | 2026-09-20 |
| [phanngoc/browser-ai](https://github.com/phanngoc/browser-ai) | Jev-driven browser agent in pure Go — CDP over pipe/WebSocket, attach to real Chrome, built to measure real s… | 0 | Go | 2026-09-20 |
| [phareim/sfl](https://github.com/phareim/sfl) | Save For Later | 0 | JavaScript | 2026-09-19 |
| [philosophyAIEDU/260921jev](https://github.com/philosophyAIEDU/260921jev) | — | 0 | TypeScript | 2026-09-22 |
| [phin-tech/pi-jev-approver](https://github.com/phin-tech/pi-jev-approver) | Shell command safety gate for the Pi coding agent, backed by TypeSafe's Jev judgment model | 0 | TypeScript | 2026-09-19 |
| [phureewat29/jev-moviebox](https://github.com/phureewat29/jev-moviebox) | Movies Recommendation Engine with Jev | 0 | TypeScript | 2026-09-21 |
| [phurley/daily-brief](https://github.com/phurley/daily-brief) | A sourced southeast Michigan daily brief generated by AI Overwatch | 0 | Python | 2026-09-22 |
| [pianistprogrammer/Jev-Browser](https://github.com/pianistprogrammer/Jev-Browser) | — | 0 | TypeScript | 2026-09-21 |
| [Pimmetjeoss/tribe-crm-jev](https://github.com/Pimmetjeoss/tribe-crm-jev) | TypeSafe Jev-powered lead intake and live CRM judgment demo for Tribe CRM | 0 | TypeScript | 2026-09-19 |
| [Pinutss/jev-agent-router](https://github.com/Pinutss/jev-agent-router) | Explainable AI agent selection with abstention, bounded fallback, and a multi-LLM catalog. | 0 | Python | 2026-09-18 |
| [Pinutss/jev-memory-selector](https://github.com/Pinutss/jev-memory-selector) | Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker. | 0 | Python | 2026-09-18 |
| [Pioneer113/cursor-jev-mcp](https://github.com/Pioneer113/cursor-jev-mcp) | Cursor MCP that runs the jev-browser-use click loop in Google Chrome. Russian: README.ru.md | 0 | JavaScript | 2026-09-22 |
| [Pizzawookiee/jev-tree-memory](https://github.com/Pizzawookiee/jev-tree-memory) | TypeSafe’s Jev AI + an n-ary memory tree = efficient agentic memory routing and retrieval. | 0 | Python | 2026-09-21 |
| [pjrpjr/qingliu](https://github.com/pjrpjr/qingliu) | X 时间线清洁工 · FeedSieve(MIT) 衍生 · 带实测标定的 AI 判定层：误杀 0.7%，还能抓词库认不出的 47% | 0 | TypeScript | 2026-09-19 |
| [pksorensen/alp-pr-review](https://github.com/pksorensen/alp-pr-review) | ALP-linje: PR-review med Jev-routing (TypeSafe System One) og automerge bag port | 0 | JavaScript | 2026-09-20 |
| [plm66/hermes-delegate](https://github.com/plm66/hermes-delegate) | Route subagents to the right Hermes profile — model, provider, credentials, and personality per delegate_task… | 0 | Python | 2026-09-21 |
| [ponyo877/jev-realtime-brain-scanner](https://github.com/ponyo877/jev-realtime-brain-scanner) | — | 0 | JavaScript | 2026-09-19 |
| [pozapas/jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding) | Calibrated conversion of police crash narratives into probabilistic crash variables with a System One model. … | 0 | Python | 2026-09-21 |
| [pozapas/jev-gold-labeling](https://github.com/pozapas/jev-gold-labeling) | Blind human labelling app for the Jev crash-narrative calibration reference set (private: contains redacted C… | 0 | TypeScript | 2026-09-21 |
| [Pragyan330/WHAT-s-Up-jev](https://github.com/Pragyan330/WHAT-s-Up-jev) | — | 0 | Python | 2026-09-21 |
| [prarolab/jev-migration-harness](https://github.com/prarolab/jev-migration-harness) | — | 0 | Python | 2026-09-22 |
| [pravinl23/htn2026](https://github.com/pravinl23/htn2026) | — | 0 | TypeScript | 2026-09-21 |
| [priyankark/jev-state](https://github.com/priyankark/jev-state) | Build and regression-test conversational state machines powered by Jev. Inspect decisions, capture failing co… | 0 | TypeScript | 2026-09-21 |
| [proshano/KCRU-website](https://github.com/proshano/KCRU-website) | — | 0 | JavaScript | 2026-09-20 |
| [PsyChaos/ai-team-harness](https://github.com/PsyChaos/ai-team-harness) | — | 0 | Python | 2026-09-21 |
| [pulseforgeatmns-ops/pulseforge-leadgen](https://github.com/pulseforgeatmns-ops/pulseforge-leadgen) | Modular AI platform for workflow automation, multi-agent orchestration, knowledge management, and human-gover… | 0 | JavaScript | 2026-09-21 |
| [punitarani/jeve](https://github.com/punitarani/jeve) | — | 0 | Python | 2026-09-22 |
| [qiaohaojie/Jev-MongoDB](https://github.com/qiaohaojie/Jev-MongoDB) | Real-time FMCG customer care triage: MongoDB Change Streams + TypeSafe Jev | 0 | JavaScript | 2026-09-21 |
| [qiudingkai-crypto/jevai](https://github.com/qiudingkai-crypto/jevai) | — | 0 | HTML | 2026-09-22 |
| [qpdbcoocdbqp/Geki-teikokukagekidan-kai](https://github.com/qpdbcoocdbqp/Geki-teikokukagekidan-kai) | Explore Jev in browser used. Playing with 檄! 帝国華撃団（改）. | 0 | Python | 2026-09-21 |
| [qte77/2026-09-12-WandB-AGIH-CoreWeave-Hack](https://github.com/qte77/2026-09-12-WandB-AGIH-CoreWeave-Hack) | A small, real critique-refine agent loop fixing Elixir bugs: a cheap draft model attempts a fix, the fix is g… | 0 | Python | 2026-09-13 |
| [quinnjr/opencode-jev-compaction](https://github.com/quinnjr/opencode-jev-compaction) | Jev-powered context compaction plugin for opencode: prune stale tool calls and results before every request, … | 0 | TypeScript | 2026-09-21 |
| [Quintonhogshead/docproof](https://github.com/Quintonhogshead/docproof) | LLM-assisted grammar review and InDesign layout prep for Word and InDesign documents | 0 | Python | 2026-09-21 |
| [r1z4x/tezgah](https://github.com/r1z4x/tezgah) | One shared working contract for every AI coding assistant you run: Claude Code, Codex, Cursor, opencode, dsh … | 0 | Python | 2026-09-21 |
| [rachit-srivastava-devx/jev-classification-benchmark](https://github.com/rachit-srivastava-devx/jev-classification-benchmark) | Benchmarking TypeSafe Jev against 15 chat-model configurations on support-ticket classification: latency, tok… | 0 | HTML | 2026-09-20 |
| [RadRebelSam/ai4all-20c-darkpatterns](https://github.com/RadRebelSam/ai4all-20c-darkpatterns) | Detecting manipulative e-commerce website language using supervised machine learning - deployed as a Streamli… | 0 | Python | 2026-09-20 |
| [RadRebelSam/jev-decision-lab](https://github.com/RadRebelSam/jev-decision-lab) | A transparent Next.js benchmark comparing function-only personalization with a function + Jev hybrid. | 0 | Python | 2026-09-21 |
| [RadRebelSam/whichjudge.dev](https://github.com/RadRebelSam/whichjudge.dev) | Replacement matrix for cheap judge / decision models. | 0 | Python | 2026-09-21 |
| [rahiseko-alt/jev-test1](https://github.com/rahiseko-alt/jev-test1) | — | 0 | TypeScript | 2026-09-21 |
| [rahiseko-alt/Jev-write](https://github.com/rahiseko-alt/Jev-write) | — | 0 | TypeScript | 2026-09-22 |
| [raitoxlol/hermes-slash-router](https://github.com/raitoxlol/hermes-slash-router) | Unified Hermes Agent + Desktop plugin: TypeSafe Jev routes misspelled, shortened, and meaning-based slash com… | 0 | Python | 2026-09-21 |
| [raj8525/universal-jev](https://github.com/raj8525/universal-jev) | Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents | 0 | JavaScript | 2026-09-19 |
| [rajarshidattapy/Jev_harness](https://github.com/rajarshidattapy/Jev_harness) | building an agent harness with Jev | 0 | — | 2026-09-22 |
| [Rajeev-SG/jev-tests](https://github.com/Rajeev-SG/jev-tests) | — | 0 | Python | 2026-09-20 |
| [Ramprasad4121/varanasi](https://github.com/Ramprasad4121/varanasi) | varanasi — the enforcement rail for agentic commerce: mandates verified at settlement, reputation grounded in… | 0 | TypeScript | 2026-09-21 |
| [rapidstartup/jevbench](https://github.com/rapidstartup/jevbench) | JevBench public leaderboard site (jevbench.dev) | 0 | JavaScript | 2026-09-21 |
| [rashedInt32/jev-gates](https://github.com/rashedInt32/jev-gates) | Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit … | 0 | JavaScript | 2026-09-20 |
| [rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens) | Do I need to look at what Claude Code just did? A calibrated verdict per stop, judged by TypeSafe Jev. Pairs … | 0 | JavaScript | 2026-09-20 |
| [RaulLazaro/dsh-jev](https://github.com/RaulLazaro/dsh-jev) | Ask Jev (TypeSafe System One) typed questions from DeepSeek Harness: batch judgements with probabilities, con… | 0 | JavaScript | 2026-09-22 |
| [ravi3594444/jev-agent1](https://github.com/ravi3594444/jev-agent1) | — | 0 | Python | 2026-09-20 |
| [Ravicha2/jev-browser](https://github.com/Ravicha2/jev-browser) | Deterministic browser loop: Jev supplies judgments, code owns control flow | 0 | JavaScript | 2026-09-22 |
| [RazanKai/pi-delegateau](https://github.com/RazanKai/pi-delegateau) | A Pi extension for bounded, model-routed delegation to trusted child agents | 0 | TypeScript | 2026-09-21 |
| [rbalch/typesafeai-review](https://github.com/rbalch/typesafeai-review) | Using Typesafe.AI to generate diff reviews. | 0 | Python | 2026-09-21 |
| [rchovatiya88/cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev) | Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One… | 0 | JavaScript | 2026-09-18 |
| [Reactive-Skills/reactive-skills](https://github.com/Reactive-Skills/reactive-skills) | HSM runtime and AXI for deterministic AI workflows | 0 | TypeScript | 2026-09-22 |
| [RealDevRay/Sauti-Mtaani-Nairobi](https://github.com/RealDevRay/Sauti-Mtaani-Nairobi) | — | 0 | TypeScript | 2026-09-22 |
| [ReallyArtificial/jev-by-example](https://github.com/ReallyArtificial/jev-by-example) | Ten runnable Jev examples for agent decisions: memory conflicts, tool-result checks, recovery, context select… | 0 | JavaScript | 2026-09-22 |
| [RefoundAI/jev-editor-skill](https://github.com/RefoundAI/jev-editor-skill) | Editorial gate skill for Claude Code and other agents. Scores a draft on AI tells, your own voice, editorial … | 0 | Python | 2026-09-21 |
| [rei0623/AFNJP](https://github.com/rei0623/AFNJP) | 海外のAIニュースを一次情報から確認し、出典リンク付きの日本語記事として毎日届けるDiscordコミュニティ「AI Frontier News JP」の公式サイト | 0 | HTML | 2026-09-22 |
| [RemiCarbonne/jev-code-context-router](https://github.com/RemiCarbonne/jev-code-context-router) | — | 0 | Python | 2026-09-19 |
| [renatobardi/jev-o-matic](https://github.com/renatobardi/jev-o-matic) | Lab of Jev | 0 | Python | 2026-09-20 |
| [renatosousa/jev-trader](https://github.com/renatosousa/jev-trader) | — | 0 | Python | 2026-09-18 |
| [Renwang-Huang/arbitype](https://github.com/Renwang-Huang/arbitype) | Typed decision tools for AI agents, powered by TypeSafe Jev | 0 | Python | 2026-09-22 |
| [resumocast/jev-mcp](https://github.com/resumocast/jev-mcp) | Community experimental MCP server and Pi adapter for bounded TypeSafe Jev judgments | 0 | Go | 2026-09-21 |
| [rexmcintosh/ai-harness](https://github.com/rexmcintosh/ai-harness) | — | 0 | Python | 2026-09-21 |
| [rhelmer/filelathe](https://github.com/rhelmer/filelathe) | — | 0 | TypeScript | 2026-09-22 |
| [rheono/html-jev](https://github.com/rheono/html-jev) | SO-meme HTML judge on TypeSafe Jev | 0 | HTML | 2026-09-21 |
| [RichardoMrMu/jev-mini](https://github.com/RichardoMrMu/jev-mini) | Put Jev's three headline claims on trial on your own GPU. One command, a 0.5B local model: measures constrain… | 0 | Python | 2026-09-21 |
| [riclib/llm-wires](https://github.com/riclib/llm-wires) | One Provider trait over the Anthropic and OpenAI HTTP shapes: tools, streaming, and a key that cannot print i… | 0 | Rust | 2026-09-20 |
| [rikhoffbauer/soggfy-cli](https://github.com/rikhoffbauer/soggfy-cli) | — | 0 | TypeScript | 2026-09-19 |
| [rinti/wagtail-jev](https://github.com/rinti/wagtail-jev) | Use jev to classify tags for pages | 0 | Python | 2026-09-21 |
| [rioriost/rspamd-jev](https://github.com/rioriost/rspamd-jev) | TypeSafe Jev shadow-evaluation plugin for Rspamd with optional GPT provider comparison | 0 | Python | 2026-09-21 |
| [riposta/pi-jev](https://github.com/riposta/pi-jev) | a Jev classification layer for the Pi coding agent | 0 | TypeScript | 2026-09-19 |
| [rishi-raj-jain/ping-pong-jev](https://github.com/rishi-raj-jain/ping-pong-jev) | — | 0 | TypeScript | 2026-09-22 |
| [rivianpratama/JeVJ](https://github.com/rivianpratama/JeVJ) | — | 0 | TypeScript | 2026-09-18 |
| [rmakiyama/raincheck](https://github.com/rmakiyama/raincheck) | Every bookmark is a rain check. Find the ones worth redeeming today. | 0 | TypeScript | 2026-09-21 |
| [rnjsxodyd90/jev-relay](https://github.com/rnjsxodyd90/jev-relay) | A typed Jev decision gate, local-voice interpreter workbench, and reproducible Jev vs Qwen research. | 0 | JavaScript | 2026-09-20 |
| [rnldsalili/email-triage-badi](https://github.com/rnldsalili/email-triage-badi) | Personal Gmail triage on Cloudflare Workers with Hono, Jev, Drizzle, and Bun | 0 | JavaScript | 2026-09-20 |
| [Robot-Friends-Community/customs-authority](https://github.com/Robot-Friends-Community/customs-authority) | Customs Authority · Department of Snap Judgments — the decision-layer toolkit for Claude Code. Find where Typ… | 0 | Python | 2026-09-22 |
| [rockjoel/local-skill-router](https://github.com/rockjoel/local-skill-router) | Local-first skill router for coding agents. Inspired by TypeSafe Jev; optional swappable judge (not an offici… | 0 | Python | 2026-09-19 |
| [roguefort-dev/TrashCompact](https://github.com/roguefort-dev/TrashCompact) | Deterministic transcript cleanup and compaction support using TypeSafe's Jev. | 0 | JavaScript | 2026-09-21 |
| [rolln-ai/axel](https://github.com/rolln-ai/axel) | Open-source webhook ingestion and event delivery platform. The source for Axel Cloud. | 0 | TypeScript | 2026-09-22 |
| [rolznz/infinite-dashboard](https://github.com/rolznz/infinite-dashboard) | Add fun widgets to an infinite dashboard. Powered by Cerebras, Jev, and TaskFuel | 0 | TypeScript | 2026-09-22 |
| [RomainFranceschini/typesafe_ai_sdk](https://github.com/RomainFranceschini/typesafe_ai_sdk) | An unofficial Dart SDK for the TypeSafe AI API | 0 | Dart | 2026-09-21 |
| [romanmeclazcke/codex-sift](https://github.com/romanmeclazcke/codex-sift) | Route each Codex turn to the cheapest model that can handle it, judged by TypeSafe Jev. | 0 | TypeScript | 2026-09-22 |
| [romiluz13/jevmory](https://github.com/romiluz13/jevmory) | Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Loca… | 0 | Python | 2026-09-21 |
| [Rorogogogo/jev-browser-relay](https://github.com/Rorogogogo/jev-browser-relay) | A high-speed browser runtime for AI coding agents: Jev drives the browser loop, the host model intervenes onl… | 0 | Rust | 2026-09-21 |
| [ross-jill-ws/pi-fast-jev-compaction](https://github.com/ross-jill-ws/pi-fast-jev-compaction) | Fast, verbatim, jev-guided compaction for pi | 0 | TypeScript | 2026-09-20 |
| [royosherove/graphlin](https://github.com/royosherove/graphlin) | Live architecture and activity diagrams for coding agents using JEV. | 0 | JavaScript | 2026-09-21 |
| [RubenVroman/Hearth](https://github.com/RubenVroman/Hearth) | — | 0 | Python | 2026-09-20 |
| [rudrasingh500/jev_minecraft](https://github.com/rudrasingh500/jev_minecraft) | An agent to beat minecraft | 0 | JavaScript | 2026-09-21 |
| [rurasua/dashboard-jev](https://github.com/rurasua/dashboard-jev) | dashboard especial para mejorar probabilidad de eventos geologicos con certeza | 0 | HTML | 2026-09-20 |
| [russleyshaw/typesafe-jev-gate](https://github.com/russleyshaw/typesafe-jev-gate) | Fail-closed Jev policy gate for Hermes Agent tool calls | 0 | Python | 2026-09-20 |
| [rustfuture/reflex-control](https://github.com/rustfuture/reflex-control) | Rust policy engine using TypeSafe Jev and deterministic checks to route AI agent decisions. | 0 | Rust | 2026-09-19 |
| [rvben/werkt](https://github.com/rvben/werkt) | An agent-first, Git-native control plane for code automations. | 0 | Go | 2026-09-21 |
| [rxova/jev-planner](https://github.com/rxova/jev-planner) | — | 0 | TypeScript | 2026-09-22 |
| [ryan-sunny/dbt-assay](https://github.com/ryan-sunny/dbt-assay) | Your dbt project has types nobody declared. assay infers them and finds where they contradict each other. sql… | 0 | Python | 2026-09-22 |
| [RyanNg1403/jev-cli](https://github.com/RyanNg1403/jev-cli) | High-performance Unix semantic reflex CLI powered by TypeSafe Jev for agent progressive discovery & pipelines | 0 | TypeScript | 2026-09-22 |
| [RyoyaYahagi/Trader-Jev](https://github.com/RyoyaYahagi/Trader-Jev) | — | 0 | — | 2026-09-21 |
| [ryuchan00/jev_practice](https://github.com/ryuchan00/jev_practice) | Jev (TypeSafe System One) と LLM に同じゲームを打たせて、レイテンシ・コスト・判断の質を比べる練習台 | 0 | Python | 2026-09-21 |
| [s-hiraoku/jev-checkkit](https://github.com/s-hiraoku/jev-checkkit) | — | 0 | TypeScript | 2026-09-21 |
| [s-hiraoku/jev-page-checker](https://github.com/s-hiraoku/jev-page-checker) | — | 0 | TypeScript | 2026-09-22 |
| [S1LV3RJ1NX/openjev](https://github.com/S1LV3RJ1NX/openjev) | Open System One models: typed decisions with calibrated probabilities, trainable on your own data. No text ge… | 0 | Python | 2026-09-22 |
| [s2422114/jev_app](https://github.com/s2422114/jev_app) | — | 0 | — | 2026-09-21 |
| [Sachin-chaurasiya/scam-checker-with-jev](https://github.com/Sachin-chaurasiya/scam-checker-with-jev) | Paste a suspicious text message. Get a straight answer and the reasons behind it. | 0 | TypeScript | 2026-09-21 |
| [sahajamit/jev-lens](https://github.com/sahajamit/jev-lens) | Personal Chrome extension: Jev (TypeSafe) badges X and LinkedIn posts READ / MAYBE / SKIP against my own inte… | 0 | JavaScript | 2026-09-21 |
| [sambawy01/jevistication](https://github.com/sambawy01/jevistication) | A calibrated decision engine for developer workflows, built on fast structured-decision models. | 0 | Kotlin | 2026-09-22 |
| [sambhav/jev-explained](https://github.com/sambhav/jev-explained) | — | 0 | HTML | 2026-09-18 |
| [Samge0/jev-arena](https://github.com/Samge0/jev-arena) | Jev模型跟开源方案NanoJev / Laya的对比测试 | 0 | Python | 2026-09-21 |
| [samimcloud2020/jevai](https://github.com/samimcloud2020/jevai) | — | 0 | Python | 2026-09-22 |
| [sammyjoyce/prime-browser-skills](https://github.com/sammyjoyce/prime-browser-skills) | Native Prime Agent browser skills: Astra, Jev, and evidence-based web QA | 0 | Python | 2026-09-22 |
| [samyung0/capy-notebook](https://github.com/samyung0/capy-notebook) | — | 0 | Python | 2026-09-21 |
| [sandrotaje/pi-jev-concise](https://github.com/sandrotaje/pi-jev-concise) | — | 0 | TypeScript | 2026-09-20 |
| [sanmai/typesafe-ai-php](https://github.com/sanmai/typesafe-ai-php) | Jev for PHP, TypeSafe AI PHP SDK | 0 | PHP | 2026-09-22 |
| [Sannrox/sekai-chisei](https://github.com/Sannrox/sekai-chisei) | Local-first Rust control plane for ontology-driven, governed agent operations: policy, budgets, audit, evalua… | 0 | Rust | 2026-09-22 |
| [santmun/radar](https://github.com/santmun/radar) | Escribe un tema y mira cómo Jev (TypeSafe) juzga 100 videos de YouTube en segundos. Corre en tu propia cuenta… | 0 | TypeScript | 2026-09-22 |
| [SApplefeld/agent_persona](https://github.com/SApplefeld/agent_persona) | Claude based Function Hooks implementation of PIANO style loops for goal management, memory curation, redirec… | 0 | JavaScript | 2026-09-22 |
| [sarang-pratham/jev-computer-use](https://github.com/sarang-pratham/jev-computer-use) | computer use (mac for now) | 0 | Python | 2026-09-21 |
| [SarathChandraBellam/jev-vs-llm-ticket-router](https://github.com/SarathChandraBellam/jev-vs-llm-ticket-router) | Benchmark: TypeSafe Jev vs traditional LLM on support-ticket routing accuracy, latency, and cost | 0 | Python | 2026-09-21 |
| [SashaSkind/beyondgreen](https://github.com/SashaSkind/beyondgreen) | Your tests passed. We check what they missed. | 0 | TypeScript | 2026-09-15 |
| [satvik314/jev-experiments](https://github.com/satvik314/jev-experiments) | — | 0 | Jupyter Notebook | 2026-09-22 |
| [sava-software/typesafe-client](https://github.com/sava-software/typesafe-client) | Java client for the TypeSafe System One API (Jev): typed questions in, calibrated probabilities out | 0 | Java | 2026-09-18 |
| [scbrown/camayoc](https://github.com/scbrown/camayoc) | 🪢 The knot-keeper — bootstrap ontology, knowledge ingress, and knowledge packs for the quipu stack | 0 | Python | 2026-09-21 |
| [SCBuergel/jev-netprofiler](https://github.com/SCBuergel/jev-netprofiler) | A network profiler usign Jev, educational proof of concept only! | 0 | Python | 2026-09-21 |
| [schalkneethling/jev-lint](https://github.com/schalkneethling/jev-lint) | An experiment with semantic code linting using Jev from TypeSafe AI | 0 | TypeScript | 2026-09-21 |
| [schuettc/pi-extensions](https://github.com/schuettc/pi-extensions) | Extensions for the pi coding agent: pi-quiet (calm tool rendering) and Channels / channels.tools (wake sessio… | 0 | TypeScript | 2026-09-22 |
| [schulxf/browser-qa](https://github.com/schulxf/browser-qa) | Skill de QA visual e funcional para aplicações web. Combina agent-browser, Jev e verificação independente com… | 0 | JavaScript | 2026-09-18 |
| [Schweik7/jev-pacman](https://github.com/Schweik7/jev-pacman) | Pac-Man decision environment for TypeSafe's Jev (System One) model | 0 | Python | 2026-09-20 |
| [scottjoyner/my-jev](https://github.com/scottjoyner/my-jev) | — | 0 | — | 2026-09-22 |
| [scursel/hermes-jev-fastpath](https://github.com/scursel/hermes-jev-fastpath) | Hermes Agent middleware using TypeSafe Jev for fail-open deterministic fast paths before LLM execution | 0 | Python | 2026-09-20 |
| [sean-lai-sh/talent-graph](https://github.com/sean-lai-sh/talent-graph) | Talent Graph algorithm core: Referral Signal (V0) + Bradley-Terry relative capability (V1). Bun + TypeScript. | 0 | TypeScript | 2026-09-21 |
| [SeanPlusPlus/hellojev](https://github.com/SeanPlusPlus/hellojev) | 👋 jev | 0 | TypeScript | 2026-09-21 |
| [seb4ez/jevguard](https://github.com/seb4ez/jevguard) | Deterministic decision runtime, zero-token caching, and certainty calibrator for TypeSafe AI (Jev). | 0 | Python | 2026-09-21 |
| [seb4ez/jevguard-mcp](https://github.com/seb4ez/jevguard-mcp) | Official Model Context Protocol (MCP) server for JevGuard and TypeSafe AI | 0 | Python | 2026-09-21 |
| [secondfret/mailjay](https://github.com/secondfret/mailjay) | Personal macOS inbox triage app powered by Gmail API and TypeSafe Jev | 0 | Swift | 2026-09-20 |
| [seethinajayadileep/jev-desk](https://github.com/seethinajayadileep/jev-desk) | — | 0 | Python | 2026-09-22 |
| [Selmar/typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review) | About calibrating Jev for code reviews | 0 | Python | 2026-09-22 |
| [seoheejung/spendguard-agent](https://github.com/seoheejung/spendguard-agent) | Jev, OpenAI Agent, MCP를 활용해 구매·구독·비용 의사결정을 계산·비교·검증하는 프로젝트 | 0 | Python | 2026-09-19 |
| [SergeiGolos/ask-jev](https://github.com/SergeiGolos/ask-jev) | — | 0 | TypeScript | 2026-09-20 |
| [SerovaAI/ficta](https://github.com/SerovaAI/ficta) | — | 0 | TypeScript | 2026-09-21 |
| [sfriedowitz/toy-jev](https://github.com/sfriedowitz/toy-jev) | Toy implementation of a Jev-like model. | 0 | Python | 2026-09-20 |
| [sglenon/jev-semantic-reviewer](https://github.com/sglenon/jev-semantic-reviewer) | — | 0 | TypeScript | 2026-09-21 |
| [shaduf-labs/jev-catalog](https://github.com/shaduf-labs/jev-catalog) | Jev use cases, open-source alternatives, real products and current access prices. | 0 | HTML | 2026-09-22 |
| [shailesh-svg/Jev-POC-Lead-Gen](https://github.com/shailesh-svg/Jev-POC-Lead-Gen) | — | 0 | TypeScript | 2026-09-21 |
| [Shalimov04/open-jev](https://github.com/Shalimov04/open-jev) | Distil a prompt into a small, fast, calibrated classifier. Typed decisions (choice/score/noul) with calibrate… | 0 | Python | 2026-09-21 |
| [shank4804/shank4804.github.io](https://github.com/shank4804/shank4804.github.io) | The actual website HTML/CSS files | 0 | HTML | 2026-09-19 |
| [shantanugoel/tetris-ai](https://github.com/shantanugoel/tetris-ai) | Browser Tetris with a first-class AI API: play it with a built-in planning agent, TypeSafe's Jev decision mod… | 0 | JavaScript | 2026-09-18 |
| [Sharkelot/jev-laya-free](https://github.com/Sharkelot/jev-laya-free) | Free local Jev-compatible typed decisions backed by rules or Laya, with a TypeSafe SDK-compatible Python surf… | 0 | Python | 2026-09-21 |
| [sharpninja/jev-codex-blazor](https://github.com/sharpninja/jev-codex-blazor) | Jev emulation layer over Codex CLI using Microsoft Agent Framework and a Blazor chat harness | 0 | C# | 2026-09-21 |
| [shashwatc12/watermelon](https://github.com/shashwatc12/watermelon) | Green on the outside, red on the inside. Jev checks whether a weekly program status update's claimed status m… | 0 | JavaScript | 2026-09-22 |
| [SherlockGy/play-jev](https://github.com/SherlockGy/play-jev) | — | 0 | JavaScript | 2026-09-21 |
| [Sheshiyer/urania-137](https://github.com/Sheshiyer/urania-137) | Graph-first stellar console over the Selemene engine — chat is the threshold, the Folio is the durable readin… | 0 | TypeScript | 2026-09-21 |
| [shimayuz/cath-lab-open](https://github.com/shimayuz/cath-lab-open) | Open-source coronary catheter learning prototype. English/Japanese. Research data under separate terms; Jev P… | 0 | TypeScript | 2026-09-20 |
| [ShingoHiroki/jev-test](https://github.com/ShingoHiroki/jev-test) | — | 0 | TypeScript | 2026-09-20 |
| [ShiqinGuo/jev4jobhunter](https://github.com/ShiqinGuo/jev4jobhunter) | Jev4JobHunter — AI job application plugin with TypeSafe Jev for job matching. Screen BOSS Zhipin jobs, apply … | 0 | Python | 2026-09-21 |
| [shivam-raval96/multiagent-jev-monitor](https://github.com/shivam-raval96/multiagent-jev-monitor) | — | 0 | JavaScript | 2026-09-18 |
| [shivamnarkar47/Jev-testcase](https://github.com/shivamnarkar47/Jev-testcase) | Validate execution plans with TypeSafe Jev (raw curl, tunable thresholds, JSON mode) | 0 | Python | 2026-09-20 |
| [shm11C3/jev-checkup](https://github.com/shm11C3/jev-checkup) | — | 0 | TypeScript | 2026-09-21 |
| [Shuhan-Zhang/simtra](https://github.com/Shuhan-Zhang/simtra) | — | 0 | Rust | 2026-09-19 |
| [shumizu418128/gbbinfo4.0](https://github.com/shumizu418128/gbbinfo4.0) | リファクタリング版 GBB非公式サイト (astro) | 0 | TypeScript | 2026-09-22 |
| [shunta-furukawa/jev-tick-lab](https://github.com/shunta-furukawa/jev-tick-lab) | A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged f… | 0 | — | 2026-09-19 |
| [shuymn/hermes-agent](https://github.com/shuymn/hermes-agent) | The agent that grows with you | 0 | Python | 2026-09-22 |
| [si618/explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai) | TypeSafe System One (Jev) evaluated on synthetic FHIR clinical scenarios, with Claude as System Two | 0 | Python | 2026-09-20 |
| [sichengchen/unimeasure](https://github.com/sichengchen/unimeasure) | Imperial/Metric conversion for Chrome. Smart detection with Jev. | 0 | JavaScript | 2026-09-20 |
| [sijiaoh/jevgrep](https://github.com/sijiaoh/jevgrep) | grep lines by what they mean | 0 | Go | 2026-09-20 |
| [silvaan/nav-jev](https://github.com/silvaan/nav-jev) | — | 0 | Python | 2026-09-22 |
| [silverzzzzz/jev-binaryoption](https://github.com/silverzzzzz/jev-binaryoption) | — | 0 | JavaScript | 2026-09-19 |
| [simplosophy/jev-skill](https://github.com/simplosophy/jev-skill) | — | 0 | Python | 2026-09-21 |
| [sinfiny/jev-feed](https://github.com/sinfiny/jev-feed) | Adaptive public YouTube learning feeds built for focused audiences. | 0 | TypeScript | 2026-09-21 |
| [siren2345/jev-apple-fm](https://github.com/siren2345/jev-apple-fm) | — | 0 | JavaScript | 2026-09-22 |
| [siren2345/jev-single-decode](https://github.com/siren2345/jev-single-decode) | Jev-compatible choice inference using prefill plus exactly one decode step | 0 | Python | 2026-09-21 |
| [siroccomask/snake-jev](https://github.com/siroccomask/snake-jev) | Snake controlled by parallel Jev assessments, with one API call per game tick. | 0 | Python | 2026-09-19 |
| [sirviejo/jev-tidy-my-desktop](https://github.com/sirviejo/jev-tidy-my-desktop) | Jev Tidy my Desktop: tidies the macOS Desktop with TypeSafe's Jev: screenshots always go to their folder; fol… | 0 | Python | 2026-09-20 |
| [SivletLabs/jev-eval](https://github.com/SivletLabs/jev-eval) | Evaluation dataset and environment for Jev / System One typed decisions | 0 | Python | 2026-09-22 |
| [sk8metalme/jev-practice](https://github.com/sk8metalme/jev-practice) | — | 0 | Rust | 2026-09-22 |
| [skiingfalcon/jev-email-cascade](https://github.com/skiingfalcon/jev-email-cascade) | Proves an email-triage cascade: Jev decides via typed questions, a policy routes, gpt-oss handles the leftove… | 0 | Python | 2026-09-20 |
| [sksq96/jevgram](https://github.com/sksq96/jevgram) | Can Jev (TypeSafe System One) do what Pangram does? 7,139 texts from RAID, HC3 and MAGE, one typed question e… | 0 | Python | 2026-09-22 |
| [slatinwine/jevy](https://github.com/slatinwine/jevy) | Jev-style typed-decision model distilled from official Jev. 118M, EN+CN, trains on a 4GB GPU in 10 minutes. | 0 | Python | 2026-09-22 |
| [slavadubrov/sgr-judge-bench](https://github.com/slavadubrov/sgr-judge-bench) | Reproducible one-call comparison of Jev decisions and structured-output LLM judges on TabFact. | 0 | Python | 2026-09-21 |
| [slay22/AgentTest](https://github.com/slay22/AgentTest) | \[Flue\](https://flueframework.com) Tesrt | 0 | TypeScript | 2026-09-22 |
| [smaldd14/qavo](https://github.com/smaldd14/qavo) | A QA agent that drives a real browser with Jev choices | 0 | TypeScript | 2026-09-22 |
| [smalltownrobotics/proxima-1024](https://github.com/smalltownrobotics/proxima-1024) | Open-source generation-ship command simulation with Astra and Jev. | 0 | Python | 2026-09-19 |
| [smammadov1994/Signal98](https://github.com/smammadov1994/Signal98) | A new type of error handling for your project with JEV | 0 | JavaScript | 2026-09-20 |
| [smcronin/jev-the-band](https://github.com/smcronin/jev-the-band) | Five decision models. One improvising jam band. Jev personas, a declarative score, live audio, and a virtual … | 0 | TypeScript | 2026-09-21 |
| [Smotherer007/pi-jev](https://github.com/Smotherer007/pi-jev) | — | 0 | TypeScript | 2026-09-21 |
| [snakerzr/OpenJev](https://github.com/snakerzr/OpenJev) | Open-source self-hosted implementation of System One Decisions API (zero-generation fast classification engin… | 0 | Python | 2026-09-20 |
| [sneldao/stoppage](https://github.com/sneldao/stoppage) | stoppage.sportwarren.com | 0 | JavaScript | 2026-09-21 |
| [soloa715/Valorant-Mc](https://github.com/soloa715/Valorant-Mc) | — | 0 | Java | 2026-09-21 |
| [somarc/da-jev](https://github.com/somarc/da-jev) | — | 0 | JavaScript | 2026-09-18 |
| [someka-vrc/obsidian-note-filer](https://github.com/someka-vrc/obsidian-note-filer) | Categorize notes with Typesafe AI Jev and move them into folders that follow a standard taxonomy. | 0 | TypeScript | 2026-09-22 |
| [SongMarco/jev-jstris](https://github.com/SongMarco/jev-jstris) | Jev chooses Tetris placements; a local controller plays Jstris through keyboard input. | 0 | TypeScript | 2026-09-21 |
| [SophiaSama/Manufacturing-Assistant-Agent-Framework](https://github.com/SophiaSama/Manufacturing-Assistant-Agent-Framework) | A framework for generic RAG in enterprise environment | 0 | Python | 2026-09-21 |
| [SoundBlaster/SwiftDecision](https://github.com/SoundBlaster/SwiftDecision) | Typed decisions for Swift apps and agents by Jev and other Systems One models | 0 | Swift | 2026-09-22 |
| [SoundBlaster/SwiftDecision-Examples](https://github.com/SoundBlaster/SwiftDecision-Examples) | Showcase with Jev-driven mini-apps | 0 | Swift | 2026-09-22 |
| [SoundBlaster/SwiftJev](https://github.com/SoundBlaster/SwiftJev) | Swift framework to access Jev System One model by TypeSafe.ai | 0 | Swift | 2026-09-22 |
| [spareilleux/learn](https://github.com/spareilleux/learn) | Learning in public — bilingual (en/fr) courses written as I learn | 0 | MDX | 2026-09-21 |
| [SpecialSouth2004/AutoGPT](https://github.com/SpecialSouth2004/AutoGPT) | — | 0 | Python | 2026-09-22 |
| [spencerlepine/blog](https://github.com/spencerlepine/blog) | Personal developer blog | 0 | Markdown | 2026-09-21 |
| [sperictao/dsh-auto-review-jev](https://github.com/sperictao/dsh-auto-review-jev) | DeepSeek Harness plugin: per-tool-call Auto-permission review powered by TypeSafe Jev, with account usage and… | 0 | TypeScript | 2026-09-22 |
| [spivi/cloudforge-jev](https://github.com/spivi/cloudforge-jev) | Sidecar: grade a cloudforge student writeup with TypeSafe Jev. Not part of the OSS product. | 0 | Python | 2026-09-18 |
| [Spykoninho/trading-bot-jev](https://github.com/Spykoninho/trading-bot-jev) | Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news | 0 | TypeScript | 2026-09-19 |
| [SqaaSSL/aeat-doc-classifier](https://github.com/SqaaSSL/aeat-doc-classifier) | Spanish AEAT document classification and reviewable PGC account suggestions powered by Jev. MIT. | 0 | TypeScript | 2026-09-21 |
| [Sqhh99/personal-site](https://github.com/Sqhh99/personal-site) | this is my personal website. | 0 | TypeScript | 2026-09-22 |
| [srbryers/model-routing-cards](https://github.com/srbryers/model-routing-cards) | Which model for this task, and whether to believe it. Routing cards with a trust gate that refuses to name a … | 0 | JavaScript | 2026-09-20 |
| [sriannamalai/Jev.UI](https://github.com/sriannamalai/Jev.UI) | Easy to use User Interface for System One's Jev Model interaction. | 0 | TypeScript | 2026-09-21 |
| [Sskift/jev-sts2-agent](https://github.com/Sskift/jev-sts2-agent) | — | 0 | JavaScript | 2026-09-21 |
| [stakwork/aws-advisor](https://github.com/stakwork/aws-advisor) | — | 0 | TypeScript | 2026-09-21 |
| [steelwalrus/jev-needs-review](https://github.com/steelwalrus/jev-needs-review) | Classifies PRs as "merge candidate" or "human review" required using Jev's typed decision making. | 0 | TypeScript | 2026-09-20 |
| [STEERIX-home/robo-jev](https://github.com/STEERIX-home/robo-jev) | — | 0 | Python | 2026-09-21 |
| [StefH/typesafe-ai.sdk](https://github.com/StefH/typesafe-ai.sdk) | .NET SDK for TypeSafe AI | 0 | C# | 2026-09-21 |
| [Stephonomon/scribe-verify](https://github.com/Stephonomon/scribe-verify) | Can a non-generative model (Jev) double-check an AI scribe's note against the encounter transcript? Working m… | 0 | HTML | 2026-09-22 |
| [sterlingdigitalp/jevtweet](https://github.com/sterlingdigitalp/jevtweet) | — | 0 | Python | 2026-09-19 |
| [stevenke1981/jev-codex-harness](https://github.com/stevenke1981/jev-codex-harness) | — | 0 | Go | 2026-09-21 |
| [STiFLeR7/Jev-LLM-Playground](https://github.com/STiFLeR7/Jev-LLM-Playground) | Independent playground for TypeSafe AI Jev decision models: typed decisions, support-ticket routing, reproduc… | 0 | JavaScript | 2026-09-22 |
| [STRML/omp-classifier](https://github.com/STRML/omp-classifier) | Model-judged permission gate for OMP: classifies bash commands and spawn-bearing eval payloads before they ru… | 0 | TypeScript | 2026-09-21 |
| [STRML/omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier) | Jev-powered model-judged permission gate for OMP (TypeSafe System One) | 0 | TypeScript | 2026-09-17 |
| [Studio-Sasquatch/typesafe-sdk-elixir](https://github.com/Studio-Sasquatch/typesafe-sdk-elixir) | An unofficial SDK for TypeSafe AI | 0 | Elixir | 2026-09-21 |
| [sub-surface/jev](https://github.com/sub-surface/jev) | — | 0 | Python | 2026-09-19 |
| [sudeshkar/jev-corrective-rag](https://github.com/sudeshkar/jev-corrective-rag) | Corrective RAG where every decision gate is a typed System One model call instead of an LLM judge. 7x fewer L… | 0 | Python | 2026-09-21 |
| [sueszli/qwen27b-jev](https://github.com/sueszli/qwen27b-jev) | logits to multiple-choice questions for Qwen3.8-27B | 0 | Python | 2026-09-19 |
| [suiramdev/freenary](https://github.com/suiramdev/freenary) | Open-source, AI-powered personal finance and wealth-management platform: aggregates banking, investments, ass… | 0 | TypeScript | 2026-09-21 |
| [SunnyKikiHK/jev-replacement](https://github.com/SunnyKikiHK/jev-replacement) | — | 0 | Python | 2026-09-20 |
| [Sunwood-ai-labs/jev-colab-lab](https://github.com/Sunwood-ai-labs/jev-colab-lab) | Reproducible Google Colab GPU experiments for decision-model inference | 0 | Python | 2026-09-21 |
| [SuperInstance/jev-quilt](https://github.com/SuperInstance/jev-quilt) | JEV for quilt as understood output: cellular-first decision substrate — typed cells, hook-and-drop deltas, bo… | 0 | Python | 2026-09-22 |
| [SuperInstance/jeviter](https://github.com/SuperInstance/jeviter) | — | 0 | JavaScript | 2026-09-22 |
| [SuperInstance/substrate-gan](https://github.com/SuperInstance/substrate-gan) | JEV-as-judge GAN harness | 0 | TypeScript | 2026-09-22 |
| [SupremeDreamZ/jev-fastloop](https://github.com/SupremeDreamZ/jev-fastloop) | Cheap fail-open semantic edge layer for Jev (TypeSafe System One): decision service + confidence policy + dec… | 0 | Python | 2026-09-21 |
| [suraj-phanindra/wellposed](https://github.com/suraj-phanindra/wellposed) | Lint your jev requests before they come back confidently wrong. | 0 | JavaScript | 2026-09-21 |
| [surajkushvaha/tic-tac-toe-with-jev](https://github.com/surajkushvaha/tic-tac-toe-with-jev) | — | 0 | TypeScript | 2026-09-20 |
| [surreptakos/claude-dotfiles](https://github.com/surreptakos/claude-dotfiles) | Machine-local half of a Claude Code setup: global rules, skills, hooks, plugin manifests, per-project memory.… | 0 | JavaScript | 2026-09-22 |
| [suwa-sh/zenn-contents](https://github.com/suwa-sh/zenn-contents) | https://zenn.dev/suwash | 0 | Astro | 2026-09-21 |
| [suyash-lyzr/jev-typesafe](https://github.com/suyash-lyzr/jev-typesafe) | — | 0 | TypeScript | 2026-09-22 |
| [svilupp/agent-hotwash](https://github.com/svilupp/agent-hotwash) | — | 0 | Python | 2026-09-20 |
| [svsaraf/tswitch](https://github.com/svsaraf/tswitch) | Typesafe switch, score, and bool primitives for Python, powered by TypeSafe AI | 0 | Python | 2026-09-19 |
| [sw-ml-study/demo-decision-model](https://github.com/sw-ml-study/demo-decision-model) | A Jev-or-System-1 inspired typed decision model demo in sw-mlpl | 0 | Rust | 2026-09-22 |
| [swang666/polymarket-jev](https://github.com/swang666/polymarket-jev) | Polymarket resolution-lag scanner built on TypeSafe's Jev model. Finds markets where a published fact already… | 0 | Python | 2026-09-22 |
| [swarooppatilx/oxox](https://github.com/swarooppatilx/oxox) | Probably the least useful thing you can build with Jev | 0 | TypeScript | 2026-09-20 |
| [SwiftFaze/Jev-Studio](https://github.com/SwiftFaze/Jev-Studio) | — | 0 | JavaScript | 2026-09-21 |
| [swkim0128/PARA](https://github.com/swkim0128/PARA) | PARA Storage | 0 | HTML | 2026-09-19 |
| [sysone-help/sysone](https://github.com/sysone-help/sysone) | A tiny, zero-dependency TypeScript library for Jev by TypeSafe. Checks, classification and scoring, with a li… | 0 | TypeScript | 2026-09-20 |
| [szocpaul/jev-compaction-prime](https://github.com/szocpaul/jev-compaction-prime) | Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scor… | 0 | Python | 2026-09-20 |
| [T-Lind/accessor](https://github.com/T-Lind/accessor) | Local voice gateway around Codex, Claude Code, and Antigravity | 0 | Rust | 2026-09-22 |
| [tackaaaada/jev-langfuse-trial](https://github.com/tackaaaada/jev-langfuse-trial) | — | 0 | Python | 2026-09-21 |
| [taecontrol/manuvra](https://github.com/taecontrol/manuvra) | macOS CLI for coding agents to observe and control exact Chrome tabs and native windows | 0 | Rust | 2026-09-21 |
| [taisan11/jev-agent](https://github.com/taisan11/jev-agent) | — | 0 | TypeScript | 2026-09-19 |
| [taituo/jev](https://github.com/taituo/jev) | Audited LLM Wiki over RFCs 7519/7515/7516/6749/6750/8725 — Slice 1: reproducible sources, resolvable citation… | 0 | Python | 2026-09-19 |
| [takafumikobayashi/jev-snap-lab](https://github.com/takafumikobayashi/jev-snap-lab) | Tiny inputs. Instant decisions. A small experimental playground for exploring fast, probabilistic decisions w… | 0 | TypeScript | 2026-09-22 |
| [TakashiYoshinaga/Jev-vs-VectorSearch](https://github.com/TakashiYoshinaga/Jev-vs-VectorSearch) | — | 0 | Python | 2026-09-20 |
| [takezou621/jev-mcp](https://github.com/takezou621/jev-mcp) | — | 0 | TypeScript | 2026-09-22 |
| [TakSeBiegam/jevode](https://github.com/TakSeBiegam/jevode) | — | 0 | TypeScript | 2026-09-19 |
| [taku-me/chakuho](https://github.com/taku-me/chakuho) | Jev-compatible System One decision endpoint over a local LLM (1-token logprob decisions) | 0 | Python | 2026-09-21 |
| [Talya1412/jev-harness](https://github.com/Talya1412/jev-harness) | TypeSafe Jev (System One) integrations for OMP, MCP, Claude Code, and Pi — fail-open decision routing, gating… | 0 | TypeScript | 2026-09-20 |
| [tanayvasishtha/jev-lab](https://github.com/tanayvasishtha/jev-lab) | — | 0 | JavaScript | 2026-09-21 |
| [Tango-Tango/ex_typesafe](https://github.com/Tango-Tango/ex_typesafe) | An Elixir SDK for Typesafe's API (https://docs.typesafe.ai/sdk) | 0 | Elixir | 2026-09-21 |
| [tano2026/AI-Vibe-Toolkit](https://github.com/tano2026/AI-Vibe-Toolkit) | — | 0 | Python | 2026-09-22 |
| [tarasyarema/hackspain](https://github.com/tarasyarema/hackspain) | CINTA — Class-agnostic INline Transport Analyzer | 0 | Python | 2026-09-20 |
| [taro1985/dual-process-ai](https://github.com/taro1985/dual-process-ai) | Dual-Process AI: A design pattern combining System 1 (Jev/TypeSafe AI) with System 2 (Gemini) — inspired by K… | 0 | Python | 2026-09-20 |
| [taruo/jev-adblocker](https://github.com/taruo/jev-adblocker) | — | 0 | JavaScript | 2026-09-21 |
| [tatdt622989/blog](https://github.com/tatdt622989/blog) | — | 0 | HTML | 2026-09-18 |
| [Tatendaz/model-picker](https://github.com/Tatendaz/model-picker) | Model Picker: JEV-powered Codex model and effort recommendations as task scope grows. Manual switching, priva… | 0 | Python | 2026-09-22 |
| [taxfree-python/taxfree-python.github.io](https://github.com/taxfree-python/taxfree-python.github.io) | — | 0 | TypeScript | 2026-09-19 |
| [tayaee/typesafe-ai-jev-demo](https://github.com/tayaee/typesafe-ai-jev-demo) | — | 0 | Python | 2026-09-22 |
| [tcgarvin/bobgame](https://github.com/tcgarvin/bobgame) | Vibe coding experiment | 0 | Python | 2026-09-21 |
| [tcsenpai/jevoracle](https://github.com/tcsenpai/jevoracle) | Typed questions over your own state, not a chat. A front end for TypeSafe's System One API. | 0 | JavaScript | 2026-09-22 |
| [technomad641/play-with-jev](https://github.com/technomad641/play-with-jev) | — | 0 | — | 2026-09-22 |
| [tensorfish/jrisc](https://github.com/tensorfish/jrisc) | Jev's Reduced Instruction Set | 0 | JavaScript | 2026-09-19 |
| [TentacleCat/JevDice](https://github.com/TentacleCat/JevDice) | A Jev-powered dice and coin CLI | 0 | Rust | 2026-09-20 |
| [Tewoto1/Computer-use-and-control-with-Jev](https://github.com/Tewoto1/Computer-use-and-control-with-Jev) | Jev assisted computer use and control framework, can link to a phone or a display to showcase current use pro… | 0 | Python | 2026-09-20 |
| [teyhouse/jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) | Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets | 0 | Python | 2026-09-18 |
| [tgiridhar/claude-code-jev-smart-router](https://github.com/tgiridhar/claude-code-jev-smart-router) | HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task … | 0 | Python | 2026-09-19 |
| [the-wbs-project/aec-integrations](https://github.com/the-wbs-project/aec-integrations) | — | 0 | TypeScript | 2026-09-22 |
| [TheodoreGalanos/agent-memory](https://github.com/TheodoreGalanos/agent-memory) | Agent memory architecture: Rust host, Pi worker pool, judgement runtime with Jev shadow, formation/activation… | 0 | Rust | 2026-09-20 |
| [theosunny/jev_stock](https://github.com/theosunny/jev_stock) | — | 0 | Python | 2026-09-22 |
| [TheWayWithin/jev-bench](https://github.com/TheWayWithin/jev-bench) | Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claud… | 0 | Python | 2026-09-21 |
| [thijmenkam/jev-benchmarks](https://github.com/thijmenkam/jev-benchmarks) | — | 0 | Python | 2026-09-18 |
| [thirdlf03/swe2-orca-orchestrate](https://github.com/thirdlf03/swe2-orca-orchestrate) | Orca + Devin CLI (SWE-2) multi-agent orchestration harness | 0 | Python | 2026-09-20 |
| [thisisandreeeee/jev-benchmarks](https://github.com/thisisandreeeee/jev-benchmarks) | Benchmark suite to compare Jev vs. supervised and zero-shot baselines | 0 | Python | 2026-09-22 |
| [thisisjorge/jev-control-room](https://github.com/thisisjorge/jev-control-room) | A visual control room for typed AI evaluations, structured decision-making, and confidence-aware policy gatin… | 0 | TypeScript | 2026-09-19 |
| [thomas-chong/agy-cli-jev-auto-mode](https://github.com/thomas-chong/agy-cli-jev-auto-mode) | — | 0 | JavaScript | 2026-09-21 |
| [TimMikeladze/JevLang](https://github.com/TimMikeladze/JevLang) | A policy engine for LLM decisions: declare routes, gates and actions once in TypeScript or Python, and every … | 0 | JavaScript | 2026-09-22 |
| [timnikolov/jev-system-one-ai-engine](https://github.com/timnikolov/jev-system-one-ai-engine) | — | 0 | JavaScript | 2026-09-21 |
| [tincke10/Jevest](https://github.com/tincke10/Jevest) | Automated PR review pipeline using Jev (TypeSafe AI) as a millisecond decision layer over an LLM reviewer | 0 | TypeScript | 2026-09-22 |
| [tinyhumansai/tinyjevclient](https://github.com/tinyhumansai/tinyjevclient) | An integration with jev by typesafe.ai in Rust | 0 | Rust | 2026-09-22 |
| [tirukovelamanoj/jev-plays-doom](https://github.com/tirukovelamanoj/jev-plays-doom) | A System One model driving the game through structured state, no pixels. | 0 | Python | 2026-09-19 |
| [tkuhemiya/jeveve](https://github.com/tkuhemiya/jeveve) | — | 0 | Python | 2026-09-21 |
| [tmoody1973/parcelpilot](https://github.com/tmoody1973/parcelpilot) | Preliminary zoning screen for Milwaukee infill parcels. Not an official zoning determination. | 0 | TypeScript | 2026-09-22 |
| [Toby-Faucher/oarfish](https://github.com/Toby-Faucher/oarfish) | Log-driven alarms for homelabs, with a judgment model where the guesswork used to be. Rust + Drain + Jev + As… | 0 | Rust | 2026-09-20 |
| [Tom-R-Main/Footwork](https://github.com/Tom-R-Main/Footwork) | A dual-process browser agent: fast, calibrated System 1 decisions from TypeSafe Jev in front of the deliberat… | 0 | Python | 2026-09-22 |
| [tomcat7707/jev-tetris-player](https://github.com/tomcat7707/jev-tetris-player) | Autonomous Tetris Player powered by TypeSafe JEV System 1 AI | 0 | Python | 2026-09-22 |
| [Tomdachs/jev-replay-lab](https://github.com/Tomdachs/jev-replay-lab) | Local Jev evaluation workbench: datasets, typed questions, threshold simulation and run comparison | 0 | TypeScript | 2026-09-21 |
| [tomfrazier/slopmop](https://github.com/tomfrazier/slopmop) | Mop the slop out of your LinkedIn feed. Not an AI detector: a bad-writing detector. Chrome extension + Vercel… | 0 | TypeScript | 2026-09-22 |
| [tomharris/engineer-agent](https://github.com/tomharris/engineer-agent) | A Claude Code plugin that automates senior software engineer work — PR reviews, Slack answers, ticket impleme… | 0 | Shell | 2026-09-20 |
| [Tonours/etabli](https://github.com/Tonours/etabli) | — | 0 | Shell | 2026-09-21 |
| [TonyP-MR/jev-curation-engine](https://github.com/TonyP-MR/jev-curation-engine) | Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions… | 0 | Python | 2026-09-21 |
| [toorop/pi-jev-router](https://github.com/toorop/pi-jev-router) | — | 0 | TypeScript | 2026-09-21 |
| [toorop/veille-by-jev](https://github.com/toorop/veille-by-jev) | — | 0 | Python | 2026-09-18 |
| [totally-tim/jev-gate](https://github.com/totally-tim/jev-gate) | Calibrated PR review gates powered by TypeSafe Jev: a GitHub Action, a local CLI, and an OpenCode plugin | 0 | TypeScript | 2026-09-21 |
| [toufu-cell/jev_mine](https://github.com/toufu-cell/jev_mine) | — | 0 | JavaScript | 2026-09-20 |
| [toxicwind/sovereign-projects](https://github.com/toxicwind/sovereign-projects) | Maximal sovereign workspace layer and monorepo | 0 | Rust | 2026-09-22 |
| [tpellet/jevify](https://github.com/tpellet/jevify) | grep for meaning: find the error in a 10,000-line log, a commit by description, the command for a task. A Uni… | 0 | Rust | 2026-09-22 |
| [tr1v3r/dsh-jev](https://github.com/tr1v3r/dsh-jev) | jev × DeepSeek Harness: System One decision client, MCP server, per-turn router and effort plugins | 0 | TypeScript | 2026-09-21 |
| [TranBaVinhSon/jev-router](https://github.com/TranBaVinhSon/jev-router) | — | 0 | TypeScript | 2026-09-20 |
| [TreeCityWes/jev_x1](https://github.com/TreeCityWes/jev_x1) | x1.xyz transaction classifier | 0 | JavaScript | 2026-09-19 |
| [treycausey/semantic-find](https://github.com/treycausey/semantic-find) | Local evidence search with optional Jev semantic ranking | 0 | TypeScript | 2026-09-21 |
| [trivikrama-madhusudhana/onpurpose](https://github.com/trivikrama-madhusudhana/onpurpose) | A desktop Chrome extension that filters YouTube recommendations against your goal using Jev. | 0 | JavaScript | 2026-09-22 |
| [TS0047/jev-triage-demo](https://github.com/TS0047/jev-triage-demo) | — | 0 | Python | 2026-09-22 |
| [tsnAnh/pikachu](https://github.com/tsnAnh/pikachu) | Curated Pi coding agent configuration with Jev compaction, LSP, subagents, plan mode, safety tools, and autom… | 0 | TypeScript | 2026-09-21 |
| [ttlequals0/MinusPodJev](https://github.com/ttlequals0/MinusPodJev) | MinusPod Jev Proxy | 0 | Python | 2026-09-21 |
| [tune-77/tune_lease_55](https://github.com/tune-77/tune_lease_55) | SHION — an AI that turns on-the-ground "something feels off" into reusable judgment assets for lease-financin… | 0 | Python | 2026-09-21 |
| [twilwa/pi-typesafe](https://github.com/twilwa/pi-typesafe) | Pi coding-agent extension built on the TypeSafe AI System One API (Jev) | 0 | TypeScript | 2026-09-22 |
| [twwright/jeverything](https://github.com/twwright/jeverything) | Jev engineering skill and source-backed knowledge | 0 | — | 2026-09-19 |
| [tylerfloyd/spec-drift](https://github.com/tylerfloyd/spec-drift) | Jev-backed spec-drift review bot for Pi | 0 | TypeScript | 2026-09-20 |
| [tylervick/jevplays](https://github.com/tylervick/jevplays) | — | 0 | Python | 2026-09-22 |
| [typesend/typesafe_ai](https://github.com/typesend/typesafe_ai) | Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out… | 0 | Elixir | 2026-09-17 |
| [ufx7/jev-testbench](https://github.com/ufx7/jev-testbench) | Black-box Jev test bench + a Claude/LLM-and-Jev collaboration measurement harness | 0 | TypeScript | 2026-09-19 |
| [uh-joan/jev-warning-letter-classifier](https://github.com/uh-joan/jev-warning-letter-classifier) | — | 0 | TypeScript | 2026-09-19 |
| [uist1idrju3i/study-jev](https://github.com/uist1idrju3i/study-jev) | — | 0 | HTML | 2026-09-20 |
| [umgbhalla/jevx](https://github.com/umgbhalla/jevx) | Jev (TypeSafe System One) research: API notes, benchmarks, community experiments, agent-loop patterns | 0 | Python | 2026-09-21 |
| [UnbelievableT/topxai-docs](https://github.com/UnbelievableT/topxai-docs) | TopxAI documentation: one OpenAI- and Anthropic-compatible API for Claude, GPT, Grok, GLM, Kimi and Jev at fi… | 0 | — | 2026-09-19 |
| [uninhibited-scholar/jev-universal](https://github.com/uninhibited-scholar/jev-universal) | Jev structured decisions for Claude, ChatGPT, Kimi Code, ZCode and Codex via MCP | 0 | Python | 2026-09-21 |
| [uspraveen/Jev-Reranker](https://github.com/uspraveen/Jev-Reranker) | A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings | 0 | Python | 2026-09-20 |
| [uzak0209/AI-Research](https://github.com/uzak0209/AI-Research) | 研究トレンドの自動追跡 — 日次で論文を収集し、重複／活用可能性とテーマ候補を報告。アプリ内で参考文献を管理し、.bib / Typst へ自動書き出し。原稿のファクトチェックも行う (設計フェーズ) | 0 | TypeScript | 2026-09-22 |
| [v4fs/awesome-jev-security](https://github.com/v4fs/awesome-jev-security) | Basic triage for security issues using SSVC and Jev | 0 | Python | 2026-09-21 |
| [vafaei-ar/jev-scientific-development](https://github.com/vafaei-ar/jev-scientific-development) | — | 0 | Python | 2026-09-19 |
| [valksor/typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go) | Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not a… | 0 | Go | 2026-09-19 |
| [valksor/typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php) | Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not … | 0 | PHP | 2026-09-19 |
| [vamsikrishna2421/jev-usecases](https://github.com/vamsikrishna2421/jev-usecases) | Jev (TypeSafe AI's System One decision model) use-case catalog: real-world builds, cost math, design patterns… | 0 | — | 2026-09-21 |
| [vayungodara/jev-lint](https://github.com/vayungodara/jev-lint) | Lint a Markdown knowledge base (Obsidian vault or LLM wiki) for contradictions, stale claims, unresolved mark… | 0 | Python | 2026-09-19 |
| [VdustR/gomoku-arena](https://github.com/VdustR/gomoku-arena) | A gomoku board any player can sit at — you, a search algorithm, a model, or an agent over MCP. Free-style and… | 0 | TypeScript | 2026-09-20 |
| [vedang/pi-progress-bar](https://github.com/vedang/pi-progress-bar) | A progress bar to see if work is being done well. | 0 | TypeScript | 2026-09-21 |
| [veighnsche/can-lang](https://github.com/veighnsche/can-lang) | — | 0 | Go | 2026-09-22 |
| [venkataramareddy123-tech/Project-Dorito](https://github.com/venkataramareddy123-tech/Project-Dorito) | Earnings Call Parser & Behavioral Intelligence Pipeline powered by TypeSafe AI. | 0 | Python | 2026-09-21 |
| [VennIntelligence/jev-drive](https://github.com/VennIntelligence/jev-drive) | — | 0 | Python | 2026-09-21 |
| [Verhex/xerify](https://github.com/Verhex/xerify) | Verify before you trust. Cross-provider verification with LLMs and Jev. CLI, library & MCP. | 0 | TypeScript | 2026-09-18 |
| [victorbvieira/system-one-lab](https://github.com/victorbvieira/system-one-lab) | Benchmarking System One models against LLMs for typed decisions in Python. Jev vs. LLM on routing, urgency tr… | 0 | — | 2026-09-22 |
| [victortran0904/Jev-Browser-Use](https://github.com/victortran0904/Jev-Browser-Use) | — | 0 | TypeScript | 2026-09-19 |
| [vincentlauriat/ClaudeMenu](https://github.com/vincentlauriat/ClaudeMenu) | macOS menu bar app for Claude usage — Anthropic's own 5h/7d gauge with pace projections, exact token counts f… | 0 | Swift | 2026-09-22 |
| [vineetagarwal54/jev-mcp-middleware](https://github.com/vineetagarwal54/jev-mcp-middleware) | Semantic MCP middleware that intercepts AI-agent tool calls and combines deterministic policy with TypeSafe J… | 0 | PowerShell | 2026-09-22 |
| [vinsonws/jev-page-tester](https://github.com/vinsonws/jev-page-tester) | — | 0 | TypeScript | 2026-09-21 |
| [viraatdas/league-of-jev](https://github.com/viraatdas/league-of-jev) | play league of legends with jev | 0 | Python | 2026-09-22 |
| [VirtualMachinist/bezel](https://github.com/VirtualMachinist/bezel) | Bezel is a harness agnostic supplemental overlay. Jev integration, bend2 planned. current status prototype, w… | 0 | JavaScript | 2026-09-22 |
| [vishesh-baghel/typesafe](https://github.com/vishesh-baghel/typesafe) | — | 0 | TypeScript | 2026-09-18 |
| [vishivishvish/jev-typesafeai](https://github.com/vishivishvish/jev-typesafeai) | — | 0 | TypeScript | 2026-09-19 |
| [Visorian/TidyUp](https://github.com/Visorian/TidyUp) | Experimental Jev based Ad Blocker | 0 | TypeScript | 2026-09-20 |
| [voidrco/voidr-app](https://github.com/voidrco/voidr-app) | — | 0 | TypeScript | 2026-09-21 |
| [voyagerforge-dev/loci](https://github.com/voyagerforge-dev/loci) | FOSS dynamic slotting engine with evidence-aware optimization, rules, constraints, and optional Jev judgment | 0 | Python | 2026-09-22 |
| [vrash/jeval](https://github.com/vrash/jeval) | jeval: open-source evaluations for AI outputs and agents, judged by Jev | 0 | TypeScript | 2026-09-20 |
| [vtavakkoli/simple-jev](https://github.com/vtavakkoli/simple-jev) | Turn any open model into a classifier/jev endpoint | 0 | Jupyter Notebook | 2026-09-21 |
| [vzornjak/typesafe-decision](https://github.com/vzornjak/typesafe-decision) | Unofficial, advisory TypeSafe Jev decision layer for Minis — fail-closed routing, ranking, verification, and … | 0 | Python | 2026-09-21 |
| [waland1510/yard](https://github.com/waland1510/yard) | Web version of Scotland Yard board game | 0 | TypeScript | 2026-09-20 |
| [walidboulanouar/jev-agent-kit](https://github.com/walidboulanouar/jev-agent-kit) | jevkit: fast typed decisions for agents. CLI and MCP tools (route, triage, guard, grep, rank, compact, judge)… | 0 | JavaScript | 2026-09-21 |
| [WallerChen/jev-measured](https://github.com/WallerChen/jev-measured) | Measured cost, latency and raw output from the live Jev API (TypeSafe AI System One model) across 8 use cases… | 0 | Python | 2026-09-20 |
| [wangzhezbz/jev-pilot](https://github.com/wangzhezbz/jev-pilot) | An all-in-one Jev plugin for Codex. Bringing automatic reasoning-effort routing, context filtering, and workf… | 0 | Python | 2026-09-22 |
| [warmlukecore/warmluke](https://github.com/warmlukecore/warmluke) | — | 0 | TypeScript | 2026-09-21 |
| [waschbaerwerkstatt-tech/jev-review-vorschau](https://github.com/waschbaerwerkstatt-tech/jev-review-vorschau) | Passwortgeschützte Jev-Review-Auswertung; ausschließlich verschlüsselte HTML-Datei | 0 | HTML | 2026-09-19 |
| [waterme7on/jev-paper-trader](https://github.com/waterme7on/jev-paper-trader) | 用 typesafe-ai/jev 做决策引擎的 BTC/ETH 纸面交易台（每 5 秒评估，含买卖点与决策历史） | 0 | JavaScript | 2026-09-21 |
| [waygatetech/jev-go](https://github.com/waygatetech/jev-go) | An unofficial Go SDK for TypeSafe AI's Jev model | 0 | Go | 2026-09-21 |
| [waynegault/oilwatch](https://github.com/waynegault/oilwatch) | Domestic heating oil price tracker for Aberdeenshire, Scotland | 0 | Python | 2026-09-22 |
| [webmandman/loggerai](https://github.com/webmandman/loggerai) | — | 0 | TypeScript | 2026-09-20 |
| [webNeat/llama-jev](https://github.com/webNeat/llama-jev) | Reproducing jev classifier API on top of llama.cpp | 0 | TypeScript | 2026-09-20 |
| [webstercharly/jev-authorship-check](https://github.com/webstercharly/jev-authorship-check) | A small Jev experiment for classifying text as human, AI-generated, or uncertain | 0 | Python | 2026-09-20 |
| [WesleySmits/spark-jev-email-triage](https://github.com/WesleySmits/spark-jev-email-triage) | Email triage app built around Spark CLI and TypeSafe Jev. Early development: TanStack Start, React and TypeSc… | 0 | TypeScript | 2026-09-22 |
| [WhiteK0T/Base-of-knowledge](https://github.com/WhiteK0T/Base-of-knowledge) | — | 0 | Shell | 2026-09-20 |
| [who/naming-things](https://github.com/who/naming-things) | Use Jev combined with an LLM, and your own rules/taste to make better names for things. | 0 | TypeScript | 2026-09-22 |
| [whosydd/pi-web-toolkit](https://github.com/whosydd/pi-web-toolkit) | Single pi extension: Context7 library docs + Exa web search + Sourcegraph code search | 0 | TypeScript | 2026-09-21 |
| [wikigsroom/Jev-Wiki-Book](https://github.com/wikigsroom/Jev-Wiki-Book) | A local wikillm base on nano-jev | 0 | Python | 2026-09-22 |
| [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) | An adversarial evaluation of TypeSafe's jev decision model: nine experiments and 28 predictions fixed before … | 0 | Python | 2026-09-22 |
| [windymelt/ddskk-jev](https://github.com/windymelt/ddskk-jev) | — | 0 | Emacs Lisp | 2026-09-18 |
| [WingManJJH/continuum-core](https://github.com/WingManJJH/continuum-core) | Continuum Core — an event-sourced process-to-agent governance model: editable guardrails enforced as a real g… | 0 | Python | 2026-09-21 |
| [winter-loo/jev-voice-browser](https://github.com/winter-loo/jev-voice-browser) | Voice-controlled browser via Jev, native CDP (port 9229), Doubao Voice Bridge and Web Audio streaming | 0 | JavaScript | 2026-09-21 |
| [WiredMind2/jev](https://github.com/WiredMind2/jev) | Independent research notes toward an open Jev-like decision model: public facts, API contract, training and e… | 0 | Python | 2026-09-22 |
| [wizicer/jev_info_site](https://github.com/wizicer/jev_info_site) | Community index of tools, models, and real-world use cases built on Jev. | 0 | Astro | 2026-09-22 |
| [wjdjdakf17/jev-study](https://github.com/wjdjdakf17/jev-study) | Jev(TypeSafe AI System One Model) 스터디 — 타입화된 결정·RLCD·confidence-gated routing을 한국어 노트와 TypeScript 목업으로 정리 | 0 | TypeScript | 2026-09-21 |
| [wmsing/agent-firewall](https://github.com/wmsing/agent-firewall) | Lightweight, zero-dependency AI Agent runtime firewall (L7 HTTP Proxy + MCP Sandbox) in Go. | 0 | Go | 2026-09-22 |
| [wmtang2/jevknows](https://github.com/wmtang2/jevknows) | A malicious instruction protection skill and prehook for zcode | 0 | Python | 2026-09-21 |
| [work4life2/jev-fc-buddy](https://github.com/work4life2/jev-fc-buddy) | — | 0 | JavaScript | 2026-09-22 |
| [WXH666-bit/jev-tetris-lab](https://github.com/WXH666-bit/jev-tetris-lab) | AI-driven Tetris decision playground with a cosmic UI, provider management, and Jev integration | 0 | TypeScript | 2026-09-21 |
| [wylu1037/pi-jev-checkpoints](https://github.com/wylu1037/pi-jev-checkpoints) | — | 0 | TypeScript | 2026-09-22 |
| [xAndreiLi/pi-jev-wiki](https://github.com/xAndreiLi/pi-jev-wiki) | Agent managed wiki for a project's conceptual space, utilizing Jev to ensure legitmate, relevant, and robust … | 0 | TypeScript | 2026-09-20 |
| [xcellect/theia](https://github.com/xcellect/theia) | — | 0 | Python | 2026-09-20 |
| [xiaobai1017/ai-town](https://github.com/xiaobai1017/ai-town) | — | 0 | TypeScript | 2026-09-21 |
| [xiaohu0x/jevaimodel](https://github.com/xiaohu0x/jevaimodel) | Source for jevaimodel.app | 0 | TypeScript | 2026-09-21 |
| [xiaohu0x/jevhunt](https://github.com/xiaohu0x/jevhunt) | jevhunt project | 0 | HTML | 2026-09-22 |
| [xiaohuaxi/jev-study](https://github.com/xiaohuaxi/jev-study) | Hands-on measurements of TypeSafe's Jev via OpenRouter: integration, Chinese-language behaviour, and game loo… | 0 | Python | 2026-09-22 |
| [xinian5216/chat-signal-analyzer](https://github.com/xinian5216/chat-signal-analyzer) | Privacy-conscious Jev-powered chat signal analyzer for observable emotion, intent, engagement, and relationsh… | 0 | Python | 2026-09-22 |
| [Xio-Shark/local-search-engine](https://github.com/Xio-Shark/local-search-engine) | Local code & document retrieval layer built on Tantivy: CJK/code tokenization, query AST, symbol-aware eviden… | 0 | Python | 2026-09-21 |
| [Xopher00/jevdevice](https://github.com/Xopher00/jevdevice) | MCP server that lets an LLM agent control a real Android phone, using TypeSafe's Jev to pick real, runtime-di… | 0 | Python | 2026-09-21 |
| [xpressabhi/jev-browser](https://github.com/xpressabhi/jev-browser) | Jev decides. The harness acts. | 0 | TypeScript | 2026-09-20 |
| [xuan7zhang/jev-toolspace](https://github.com/xuan7zhang/jev-toolspace) | — | 0 | Python | 2026-09-22 |
| [xuboboo/ashare-trader](https://github.com/xuboboo/ashare-trader) | 基于 Jev 的 A 股 T+1 决策台：盘前预选 + 交易时段全程决策 + 本地概率模型 + 严格成本回测 + QMT 桥接（默认不下单）。1 万本金影子盘记录中；策略未证实正期望（README 有全部数据）。 | 0 | TypeScript | 2026-09-22 |
| [Xubqpanda/everything2jev](https://github.com/Xubqpanda/everything2jev) | — | 0 | TypeScript | 2026-09-21 |
| [xxkuboxx/jev-eval](https://github.com/xxkuboxx/jev-eval) | — | 0 | Python | 2026-09-20 |
| [xxlya/evaljev](https://github.com/xxlya/evaljev) | Runtime assurance, replay, and auto-diagnostics for Jev/System-One decision workflows | 0 | Python | 2026-09-22 |
| [xzyozi/jev-localsystem](https://github.com/xzyozi/jev-localsystem) | — | 0 | Python | 2026-09-22 |
| [Y91R/jev-box](https://github.com/Y91R/jev-box) | — | 0 | TypeScript | 2026-09-22 |
| [yagi469/playground-Jev](https://github.com/yagi469/playground-Jev) | — | 0 | Python | 2026-09-21 |
| [yama4936/mahjong-agent](https://github.com/yama4936/mahjong-agent) | — | 0 | TypeScript | 2026-09-21 |
| [yamazaki-yuki-23/iekei-ramen-mcp-apps](https://github.com/yamazaki-yuki-23/iekei-ramen-mcp-apps) | 家系ラーメンを検索フォーム・現在地・日本地図の3モードで探せる MCP Apps。Cloudflare Workers で動作し、店舗データは OpenStreetMap 由来。 | 0 | TypeScript | 2026-09-21 |
| [yandong2023/jev-test](https://github.com/yandong2023/jev-test) | — | 0 | TypeScript | 2026-09-21 |
| [yangbaepark/frugal-llm](https://github.com/yangbaepark/frugal-llm) | High-performance LLM proxy server with dynamic prompt routing, multi-provider model registry, and OpenAI API … | 0 | Go | 2026-09-21 |
| [yangzhou-chaofan/awesome-jev-prompt](https://github.com/yangzhou-chaofan/awesome-jev-prompt) | latest top 100 showcases for jev (keep updating) from x / github / latest sources | 0 | JavaScript | 2026-09-21 |
| [yanmad27/ask-jev](https://github.com/yanmad27/ask-jev) | Ask Jev before asking you — a Claude Code plugin that answers AskUserQuestion from conversation context, and … | 0 | JavaScript | 2026-09-22 |
| [yannip1234/codex-jev](https://github.com/yannip1234/codex-jev) | Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client. | 0 | Rust | 2026-09-19 |
| [yasuhito/jev-computer-use](https://github.com/yasuhito/jev-computer-use) | Safe computer-use automation guided by typed Jev decisions | 0 | JavaScript | 2026-09-22 |
| [yelgabo/job-fraud](https://github.com/yelgabo/job-fraud) | — | 0 | HTML | 2026-09-22 |
| [yesitsfebreeze/pearde](https://github.com/yesitsfebreeze/pearde) | pearde — a PRD board worked by one orchestrator session: specs ahead, dispatches implementers, asks when it m… | 0 | TypeScript | 2026-09-19 |
| [yinlu01/interview-coach](https://github.com/yinlu01/interview-coach) | 模拟面试 Agent：LLM 面试官 + JEV 实时五维测评。基于简历与 JD 出题、智能追问、本地语音转写、复盘报告 | 0 | Python | 2026-09-20 |
| [yixuexiaoao/astrbot_plugin_typesafe_autoreply](https://github.com/yixuexiaoao/astrbot_plugin_typesafe_autoreply) | 使用 TypeSafe AI 判断聊天消息是否需要 AI 主动参与，并调用 AstrBot 已配置的大语言模型生成自然回复。 | 0 | Python | 2026-09-22 |
| [yizhiyanhua-ai/fireworks-vibe-cleaner](https://github.com/yizhiyanhua-ai/fireworks-vibe-cleaner) | Offline-first disk cleanup Skill and CLI for Codex and Claude Code, with plan-bound recovery and optional Jev… | 0 | Python | 2026-09-22 |
| [yjsplay2002/jev-router-dashboard](https://github.com/yjsplay2002/jev-router-dashboard) | Local, privacy-first dashboard for Jev Router classification and model-routing history | 0 | Python | 2026-09-22 |
| [yldm-tech/loom](https://github.com/yldm-tech/loom) | Generate a landing page from one sentence: an LLM writes the copy, Jev makes the judgement calls, code owns t… | 0 | TypeScript | 2026-09-21 |
| [yn01/jev-stormboard](https://github.com/yn01/jev-stormboard) | Jev × 東京の防災電文 — 気象庁の防災情報XMLをリアルタイムに取り込み、TypeSafe の Jev が「自分にとって何を意味するか」を判定する Streamlit デモ | 0 | Python | 2026-09-22 |
| [yo4e/JevPip](https://github.com/yo4e/JevPip) | GMOのFX/BTC市場データに対応したローカル市場研究ターミナル。ライブチャート、ペーパートレード、バックテスト、安全監督、TypeSafe Jev連携。安全機構を整えたうえで実売買対応予定。 | 0 | Python | 2026-09-22 |
| [yodablocks/commitjev](https://github.com/yodablocks/commitjev) | Reads a commit before a reviewer has to: whether the message matches the diff, whether the edits belong in on… | 0 | Python | 2026-09-20 |
| [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) | Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and inv… | 0 | Python | 2026-09-20 |
| [yoonshilee/pi-sieve](https://github.com/yoonshilee/pi-sieve) | On-demand retrieval with Jev relevance selection for Pi agents. | 0 | TypeScript | 2026-09-22 |
| [yoonshilee/pi-sieve-bench](https://github.com/yoonshilee/pi-sieve-bench) | Reproducible long-workflow benchmarks for Pi Sieve, with Astra and Luna comparisons. | 0 | TypeScript | 2026-09-22 |
| [YosAwed/python-jev-if](https://github.com/YosAwed/python-jev-if) | Use TypeSafe Jev yes/no probabilities in Python if conditions. | 0 | Python | 2026-09-21 |
| [yotiosoft/Yapps](https://github.com/yotiosoft/Yapps) | 自作Webアプリ集 | 0 | HTML | 2026-09-22 |
| [yottayoshida/jev-intent-review](https://github.com/yottayoshida/jev-intent-review) | Verify a pull request against the intent that caused it, across the whole repository, with small typed judgme… | 0 | TypeScript | 2026-09-22 |
| [yousefalwahami/BlankCheck](https://github.com/yousefalwahami/BlankCheck) | — | 0 | TypeScript | 2026-09-20 |
| [yslinear/cartpole-jev](https://github.com/yslinear/cartpole-jev) | A tug-of-war over one shared actuator — you and TypeSafe's Jev push the same CartPole and the forces add. Phy… | 0 | JavaScript | 2026-09-21 |
| [yuan-phd/jev-rlcd-research](https://github.com/yuan-phd/jev-rlcd-research) | — | 0 | Python | 2026-09-21 |
| [yubol-bobo/jev-as-a-judge](https://github.com/yubol-bobo/jev-as-a-judge) | — | 0 | HTML | 2026-09-21 |
| [yuias/gmail-auto-labeling](https://github.com/yuias/gmail-auto-labeling) | Automatically labels new mail in one personal Gmail inbox. | 0 | TypeScript | 2026-09-21 |
| [yuki-dev26/jev-test](https://github.com/yuki-dev26/jev-test) | Jevの検証用 | 0 | JavaScript | 2026-09-19 |
| [yurenju/jev-playground](https://github.com/yurenju/jev-playground) | — | 0 | TypeScript | 2026-09-20 |
| [yyy-router/QA-Classifier-Jev](https://github.com/yyy-router/QA-Classifier-Jev) | Question classification experiment using TypeSafe AI Jev for QA/RAG routing. | 0 | Python | 2026-09-22 |
| [zahere-dev/sentiment-analysis-with-jev](https://github.com/zahere-dev/sentiment-analysis-with-jev) | — | 0 | HTML | 2026-09-20 |
| [zanedonkey/jev-pet](https://github.com/zanedonkey/jev-pet) | Telegram group pet — Jev decides when it speaks; an LLM decides what it says. | 0 | TypeScript | 2026-09-21 |
| [zavocc/ground-zero](https://github.com/zavocc/ground-zero) | Eval framework library to evaluate AI hallucinations, correctness, and instruction following, powered by Jev … | 0 | Python | 2026-09-21 |
| [zbloss/jev-plays-pokemon](https://github.com/zbloss/jev-plays-pokemon) | Like Claude Plays Pokemon, but with Jev | 0 | Python | 2026-09-21 |
| [zchee/typesafe-sdk-rust](https://github.com/zchee/typesafe-sdk-rust) | Unofficial async Rust SDK for the TypeSafe AI System One API: typed questions via #\[derive(QuestionSet)\], a… | 0 | Rust | 2026-09-21 |
| [zebedelu/sudoku-vs-jev](https://github.com/zebedelu/sudoku-vs-jev) | A terminal Sudoku game where TypeSafe's Jev model plays the game, built to probe its decision-making move by … | 0 | Python | 2026-09-20 |
| [ZeroX-01/jev-atlas](https://github.com/ZeroX-01/jev-atlas) | Continuously updated public index of real TypeSafe JEV projects, videos, articles, and open-source demos. | 0 | JavaScript | 2026-09-22 |
| [zhazhahuiyuxiaoxiao/jev-personal-radar](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar) | 基于 Jev、GitHub 和 RSS 的隐私优先每日信息雷达 | 0 | Go | 2026-09-22 |
| [zhijianzhouml/CELEUS-JEV](https://github.com/zhijianzhouml/CELEUS-JEV) | CELEUS × Jev evaluation dashboard | 0 | HTML | 2026-09-22 |
| [zhuyansen/x-reply-filter](https://github.com/zhuyansen/x-reply-filter) | Chrome extension: collapse spam, bait, off-topic and AI-filler replies on X. Local rules + TypeSafe Jev, lear… | 0 | JavaScript | 2026-09-21 |
| [zixiang0623/Jev-Openrouter](https://github.com/zixiang0623/Jev-Openrouter) | Vercelに一時的に依存 | 0 | HTML | 2026-09-22 |
| [zlZayn/AI-decision-maker](https://github.com/zlZayn/AI-decision-maker) | AI 只判断数据每列是什么类型，输出一个字符。支持两种引擎：生成式 LLM 与概率引擎 Jev，实测清洗与分类结论一致。 | 0 | Python | 2026-09-21 |
| [zohaibtanwir/jev-inbox-lab](https://github.com/zohaibtanwir/jev-inbox-lab) | Local lab for exploring TypeSafe's Jev model on a frozen personal email corpus | 0 | Python | 2026-09-21 |
| [zojeda/llama-cpp-system-one](https://github.com/zojeda/llama-cpp-system-one) | A Rust implementation of the System One API for structured question answering with DiffusionGemma and llama.c… | 0 | Rust | 2026-09-21 |
| [zong09/cane](https://github.com/zong09/cane) | — | 0 | Python | 2026-09-22 |
| [zsoist/BUILD-DAY---Danis-Project](https://github.com/zsoist/BUILD-DAY---Danis-Project) | Fable 5.1 comanda 8 agentes deepseek-flash con juez Jev — DAG ship-first, thinking por tarea, budget auto-sto… | 0 | Python | 2026-09-22 |
| [zyphr-labs/turnstile](https://github.com/zyphr-labs/turnstile) | Guardrails for AI agent actions. Deterministic policy, Jev semantic checks, and replayable decisions. | 0 | TypeScript | 2026-09-22 |
| [Zyw052/astrbot_plugin_jev_radar](https://github.com/Zyw052/astrbot_plugin_jev_radar) | Jev 意图雷达 — 用 TypeSafe SystemOne(Jev) 读懂消息背后的意图、情绪与风险 | 0 | Python | 2026-09-22 |
| [zzimickQ/fin-log](https://github.com/zzimickQ/fin-log) | financial logging and observing app. | 0 | TypeScript | 2026-09-20 |
## Contributing

Open a pull request. The index is swept automatically, so you do not need to add a project by
hand — but a Featured entry is a human judgment and always welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).
