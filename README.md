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

**2,170 more active projects**, out of 5,684 indexed.

Swept daily, and listed here if anyone committed to it after the day it was published.
That one filter separates a project from a launch-week drop, and it removes 3,514 of the
5,684 repos in the index.

The complete index — all 5,684, dormant ones included, with the search signals that found each
— is [`data/projects.json`](data/projects.json). It is generated, so grep it rather than read it.

| Project | What it is | ★ | Language | Last commit |
| --- | --- | ---: | --- | --- |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 | 390,198 | TypeScript | 2026-09-21 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you | 247,694 | Python | 2026-09-21 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the to… | 187,475 | Python | 2026-09-21 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | The agent engineering platform. | 146,795 | Python | 2026-09-21 |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastruc… | 87,146 | TypeScript | 2026-09-21 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team | 63,650 | Python | 2026-09-18 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack… | 46,701 | Python | 2026-09-21 |
| [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 | 42,271 | Go | 2026-09-21 |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more. Makers of the AG-UI P… | 37,450 | TypeScript | 2026-09-21 |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | ⌥ Coding agent with the IDE wired in | 32,278 | TypeScript | 2026-09-21 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | CLI tool for configuring and monitoring Claude Code | 30,879 | Python | 2026-09-21 |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to… | 30,270 | TypeScript | 2026-09-21 |
| [trycua/cua](https://github.com/trycua/cua) | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for training, evaluation, an… | 25,559 | HTML | 2026-09-21 |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Hindsight: Agent Memory That Learns | 24,196 | Python | 2026-09-21 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tra… | 22,182 | Python | 2026-09-21 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | The most RAM efficient harness | 19,971 | Rust | 2026-09-21 |
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | Open source agentic operating system | 19,406 | TypeScript | 2026-09-21 |
| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | The agent engineering platform | 18,215 | TypeScript | 2026-09-21 |
| [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。\| AI-era Berkshire: a value inv… | 16,478 | HTML | 2026-09-20 |
| [Effect-TS/effect](https://github.com/Effect-TS/effect) | Build production-ready applications in TypeScript | 16,158 | TypeScript | 2026-09-21 |
| [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | Udemy & Hotmart course downloader, YouTube downloader (yt-dlp GUI, 1,800+ sites) + desktop app for AI agents:… | 14,099 | Rust | 2026-09-21 |
| [elie222/inbox-zero](https://github.com/elie222/inbox-zero) | The world's best AI personal assistant for email. Open source app to help you reach inbox zero fast. | 12,272 | TypeScript | 2026-09-20 |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build … | 11,907 | Python | 2026-09-21 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | AI Observability & Evaluation | 11,563 | Python | 2026-09-21 |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | ⚙️🦀 Build modular and scalable LLM Applications in Rust | 8,691 | Rust | 2026-09-21 |
| [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | git push no-mistakes | 8,591 | Go | 2026-09-21 |
| [tbphp/gpt-load](https://github.com/tbphp/gpt-load) | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, sched… | 6,927 | Go | 2026-09-21 |
| [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | Talk to one agent. Ship with a crew. | 6,903 | Shell | 2026-09-21 |
| [op7418/CodePilot](https://github.com/op7418/CodePilot) | A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your … | 6,474 | TypeScript | 2026-09-18 |
| [ThinkInAIXYZ/deepchat](https://github.com/ThinkInAIXYZ/deepchat) | 🐬DeepChat - A smart assistant that connects powerful AI to your personal world | 6,336 | TypeScript | 2026-09-21 |
| [lightdash/lightdash](https://github.com/lightdash/lightdash) | Agentic BI. Analytics at the speed of code ⚡️ | 6,147 | TypeScript | 2026-09-21 |
| [samchon/typia](https://github.com/samchon/typia) | Super-fast/easy runtime validators and serializers via transformation | 5,911 | TypeScript | 2026-09-21 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | Open-source auth gateway connecting 1500+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAP… | 5,856 | TypeScript | 2026-09-21 |
| [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | A framework for building agentic apps | 5,695 | TypeScript | 2026-09-21 |
| [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | Experiential is the open source, zero markup gateway for BYOK, self-hosted and 1000+ marketplace models. It l… | 5,379 | Python | 2026-09-21 |
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | Next Generation Agentic Proxy for AI Agents and MCP servers | 4,961 | Rust | 2026-09-21 |
| [aipoch/open-science](https://github.com/aipoch/open-science) | The open-source AI research workbench for scientific research and agent workflows. Local-first, model-agnosti… | 4,877 | TypeScript | 2026-09-21 |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | The platform for LLM evaluations and AI agent testing | 4,847 | TypeScript | 2026-09-21 |
| [daveebbelaar/ai-cookbook](https://github.com/daveebbelaar/ai-cookbook) | Examples and tutorials to help developers build AI systems | 4,546 | Python | 2026-09-21 |
| [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | A persistent workspace for development work that self-improves and continues beyond one session. | 4,065 | Python | 2026-09-21 |
| [Ontos-AI/knowhere](https://github.com/Ontos-AI/knowhere) | Knowhere extracts, parses, and outputs structured chunks ready for AI Agents and RAG. | 3,422 | Python | 2026-09-21 |
| [TanStack/ai](https://github.com/TanStack/ai) | 🤖 Type-safe, provider-agnostic TypeScript AI SDK for streaming chat, tool calling, agents, and multimodal app… | 3,128 | TypeScript | 2026-09-21 |
| [ax-llm/ax](https://github.com/ax-llm/ax) | The pretty much "official" DSPy framework for Typescript | 2,937 | TypeScript | 2026-09-18 |
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. | 2,934 | Python | 2026-09-19 |
| [elie222/rakazo](https://github.com/elie222/rakazo) | Open-source Grok Bot alternative. Choose your own model and sandbox. | 2,803 | TypeScript | 2026-09-21 |
| [Armur-Ai/Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) | Autonomous penetration testing using a swarm of AI agents. Orchestrates recon, classification, exploitation, … | 2,551 | Go | 2026-09-21 |
| [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | VCP 部署在 AI 模型 API 与前端应用之间，是面向AGI OS开发和探索的工业级基建示范项目。通过统一指令协议、多层级持久化记忆、分布式插件引擎及多 Agent 协作框架，将原本“无状态、无记忆、无工具调用能力… | 2,318 | JavaScript | 2026-09-21 |
| [xerj-org/xerj](https://github.com/xerj-org/xerj) | XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data withou… | 2,241 | Rust | 2026-09-21 |
| [SimonSchubert/LinuxCommandLibrary](https://github.com/SimonSchubert/LinuxCommandLibrary) | 2M+ app downloads, 500k+ monthly website visitors, Linux basics, tips and formatted man pages | 2,020 | Kotlin | 2026-09-21 |
| [plateaukao/einkbro](https://github.com/plateaukao/einkbro) | A small, fast web browser based on Android WebView. It's tailored for E-Ink devices but also works great on n… | 2,016 | Kotlin | 2026-09-20 |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own | 1,966 | Python | 2026-09-21 |
| [oficcejo/aiagents-stock](https://github.com/oficcejo/aiagents-stock) | 复合多AI智能体股票团队分析盯盘系统，基于多个ai智能体，模拟证券分析师团队分析过程，提供全方位的股票投资分析和决策建议，新增游资龙虎榜跟踪分析、板块预警轮动分析，支持批量多线程分析，支持实时监测关键点位，发送警报信息… | 1,942 | Python | 2026-09-21 |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline. | 1,751 | Python | 2026-09-21 |
| [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | One AI trade decision every Monad block. Jev on Kuru MON-USDC. | 1,740 | TypeScript | 2026-09-17 |
| [nicobailon/pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter) | Token-efficient MCP adapter for Pi coding agent | 1,516 | TypeScript | 2026-09-21 |
| [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) | Local typed decisions, contrastive data curation, and model evaluation. | 1,436 | Python | 2026-09-20 |
| [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) | Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real U… | 1,401 | Rust | 2026-09-21 |
| [JoasASantos/NeuroSploit](https://github.com/JoasASantos/NeuroSploit) | NeuroSploit is an advanced, AI-powered penetration testing framework designed to automate and augment various… | 1,374 | Rust | 2026-09-21 |
| [astaxie/TokenHub](https://github.com/astaxie/TokenHub) | TokenHub gives enterprises a private gateway to unify AI model access and governance, making every request co… | 1,323 | Go | 2026-09-21 |
| [elvisun/newsjack](https://github.com/elvisun/newsjack) | The open-source skills that turn your agent into a full PR team. | 1,278 | Go | 2026-09-19 |
| [caliber-ai-org/ai-setup](https://github.com/caliber-ai-org/ai-setup) | Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files… | 1,277 | TypeScript | 2026-09-19 |
| [Arize-ai/openinference](https://github.com/Arize-ai/openinference) | OpenTelemetry Instrumentation for AI Observability | 1,226 | Python | 2026-09-21 |
| [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠 | 1,102 | JavaScript | 2026-09-21 |
| [CelestoAI/celesto](https://github.com/CelestoAI/celesto) | Secure and persistent computer for AI agents -- build your own Grokbot, and Muse. | 956 | Python | 2026-09-21 |
| [repoprompt/repoprompt-ce](https://github.com/repoprompt/repoprompt-ce) | Community edition of RepoPrompt: a native macOS context engineering app for AI coding agents, with an MCP CLI. | 935 | Swift | 2026-09-21 |
| [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One mode… | 881 | Python | 2026-09-21 |
| [konbakuyomu/smartsearch](https://github.com/konbakuyomu/smartsearch) | — | 834 | Python | 2026-09-21 |
| [bastani-inc/atomic](https://github.com/bastani-inc/atomic) | The verifiable coding agent runtime. Define your coding agent's process in natural language with stages, chec… | 809 | TypeScript | 2026-09-21 |
| [reticlehq/reticle](https://github.com/reticlehq/reticle) | AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machi… | 796 | TypeScript | 2026-09-21 |
| [lioensky/VCPChat](https://github.com/lioensky/VCPChat) | VCPChat，VCP原生分布式引擎终端项目，地球上第一个AGI-OS桌面级交互系统，语义级垂直打穿AI-UI/UX-APP以及人类想象力的一切。 | 777 | JavaScript | 2026-09-21 |
| [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) | Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast… | 751 | Python | 2026-09-20 |
| [chujianyun/skills](https://github.com/chujianyun/skills) | WuMing's Claude Skills | 737 | JavaScript | 2026-09-20 |
| [samuelfaj/distill](https://github.com/samuelfaj/distill) | Get FAR MORE done with FAR FEWER tokens 🔥 | 682 | Rust | 2026-09-21 |
| [automateyournetwork/netclaw](https://github.com/automateyournetwork/netclaw) | An AI agent that claws through your network | 664 | Python | 2026-09-20 |
| [milind-soni/tiptour-macos](https://github.com/milind-soni/tiptour-macos) | Open-Source fast local computer use | 634 | Swift | 2026-09-19 |
| [duanebester/gooey](https://github.com/duanebester/gooey) | Gooey is a hybrid immediate/retained mode UI framework designed for building fast, GPU-rendered applications … | 631 | Zig | 2026-09-20 |
| [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent) | AgentiLoop Agent! An Autonomous Agentic Agent for Mac, and exclusive Apple only harnesss. Supports automation… | 622 | Swift | 2026-09-21 |
| [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | The CLI for AI agents to control Chrome. Zero config, agent-agnostic, battle-tested. | 620 | TypeScript | 2026-09-21 |
| [narumiruna/pi-extensions](https://github.com/narumiruna/pi-extensions) | A monorepo of Pi Coding Agent extensions | 592 | TypeScript | 2026-09-21 |
| [nicobailon/pi-interactive-shell](https://github.com/nicobailon/pi-interactive-shell) | Pi coding agent extension that allows Pi to autonomously control interactive CLIs in an observable overlay. F… | 587 | TypeScript | 2026-09-21 |
| [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) | Follow your curiosity. Build across disciplines. Open-source software and hardware for polymaths in the makin… | 545 | C | 2026-09-21 |
| [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) | — | 536 | JavaScript | 2026-09-21 |
| [BennyKok/omg.dev](https://github.com/BennyKok/omg.dev) | omg.dev — Remote control for claude, codex, cursor, opencode, pi, grok, jcocde with mobile client | 533 | TypeScript | 2026-09-21 |
| [dxos/dxos](https://github.com/dxos/dxos) | TypeScript implementation of the DXOS protocols, SDK, toolchain and Composer. | 522 | TypeScript | 2026-09-21 |
| [pulseaiclub/phi](https://github.com/pulseaiclub/phi) | a coding agent, rpc plugin, sub-agents, hashline edits, and mcp | 481 | Go | 2026-09-21 |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | A staged code-review workflow and local dashboard built with TypeSafe Jev. | 460 | TypeScript | 2026-09-17 |
| [CoWork-OS/CoWork-OS](https://github.com/CoWork-OS/CoWork-OS) | Local-first personal agentic OS and everything app for coding, knowledge work, web design, automations, and a… | 457 | TypeScript | 2026-09-21 |
| [thruwire/foreman](https://github.com/thruwire/foreman) | Software factory foreman based on TypeSafe's Jev model | 455 | Python | 2026-09-20 |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | Monorepo & docs | 449 | Rust | 2026-09-21 |
| [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) | Turn any open model into a classifier/jev endpoint | 438 | Python | 2026-09-21 |
| [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) | Awesome Jev: a source-backed field guide to TypeSafe's System One model, with SDKs, live demos, agent tools, … | 423 | JavaScript | 2026-09-21 |
| [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) | VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agen… | 422 | Python | 2026-09-21 |
| [langchain-ai/docs](https://github.com/langchain-ai/docs) | Unified LangChain documentation. | 418 | MDX | 2026-09-21 |
| [bitsocialnet/seedit](https://github.com/bitsocialnet/seedit) | A Bitsocial app with an old.reddit UI | 416 | TypeScript | 2026-09-21 |
| [mrmps/classifier-dev](https://github.com/mrmps/classifier-dev) | Zero-shot text classification over plain HTTP — no API key, no account. One Cloudflare Worker, a CLI, and an … | 402 | TypeScript | 2026-09-21 |
| [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops) | Vibe-Coding is easy. DevOps is hard. OpenCode & Git token-efficient AI agent automation for your app, busines… | 401 | Shell | 2026-09-21 |
| [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite) | Open-source IFC toolkit: WebGPU rendering, columnar in-memory store, exact-arithmetic geometry kernel. Runs f… | 381 | TypeScript | 2026-09-21 |
| [ImChong/Robotics_Notebooks](https://github.com/ImChong/Robotics_Notebooks) | 机器人技术栈资料汇总 | 366 | Python | 2026-09-21 |
| [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (a… | 365 | Python | 2026-09-21 |
| [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) | Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with S… | 363 | TypeScript | 2026-09-20 |
| [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) | — | 353 | TypeScript | 2026-09-21 |
| [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) | An awesome collection of Jev use cases, workflows, and agent skills. | 335 | Python | 2026-09-21 |
| [EthanAlgoX/AIStock](https://github.com/EthanAlgoX/AIStock) | A multi-agent AI trading system using LLMs to optimize strategies and adapt to market conditions in real-time. | 331 | Python | 2026-09-21 |
| [WrongStack/WrongStack](https://github.com/WrongStack/WrongStack) | An AI coding agent that reads your code, edits files, runs commands, and reasons through bugs — across a term… | 331 | TypeScript | 2026-09-21 |
| [rwjdk/agent-framework-samples](https://github.com/rwjdk/agent-framework-samples) | Samples demonstrating the Microsoft Agent Framework in C# | 329 | C# | 2026-09-19 |
| [cognesy/instructor-php](https://github.com/cognesy/instructor-php) | Unified LLM API, structured data outputs with LLMs, and agent SDK - in PHP | 327 | PHP | 2026-09-17 |
| [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) | Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per p… | 323 | TypeScript | 2026-09-20 |
| [wfzyx/von](https://github.com/wfzyx/von) | The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSaf… | 323 | Python | 2026-09-21 |
| [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) | 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp. | 308 | JavaScript | 2026-09-19 |
| [warmbly/warmbly](https://github.com/warmbly/warmbly) | The largest open-source B2B cold outreach and email warmup service. | 307 | Go | 2026-09-21 |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) | A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions. | 301 | — | 2026-09-21 |
| [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) | 200+ production-ready Claude Code skills for sales, marketing, design, engineering, and AI agent architecture… | 301 | Python | 2026-09-21 |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | Route to the cheapest model in claude code for your task using jev-router | 299 | JavaScript | 2026-09-19 |
| [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) | Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHu… | 288 | JavaScript | 2026-09-21 |
| [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) | The Complete AI Development Toolkit for Claude Code. 106 skills, 36 agents, 171 hooks. Install `ork` for stab… | 280 | TypeScript | 2026-09-21 |
| [realZachi/pg-jev](https://github.com/realZachi/pg-jev) | Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev. | 272 | Shell | 2026-09-18 |
| [razorback16/openjev](https://github.com/razorback16/openjev) | Open, Jev-compatible System One decision server on DiffusionGemma | 262 | Python | 2026-09-21 |
| [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) | Build calibrated AI Functions from human feedback using Jev and GEPA. | 258 | Python | 2026-09-20 |
| [RooCodeInc/Roomote](https://github.com/RooCodeInc/Roomote) | Your own cloud coding agent. Everything you want from an AI engineering teammate, without building from scrat… | 251 | TypeScript | 2026-09-21 |
| [stella/stella](https://github.com/stella/stella) | Open-source legal workspace | 249 | TypeScript | 2026-09-21 |
| [cequence-io/openai-scala-client](https://github.com/cequence-io/openai-scala-client) | Scala client for OpenAI API and other major LLM providers | 248 | Scala | 2026-09-18 |
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | Jev-compatible API endpoint based on open models (prefill-only) | 247 | Python | 2026-09-21 |
| [monotykamary/pi-fabric](https://github.com/monotykamary/pi-fabric) | A programmable tool and agent runtime for Pi | 241 | TypeScript | 2026-09-21 |
| [Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) | Calibrated 151M Non-Autoregressive Decision Engine beating TypeSafe Jev & Laya on LocalLLaMA/typed-decisions … | 234 | Python | 2026-09-20 |
| [DemonDamon/AgenticX](https://github.com/DemonDamon/AgenticX) | AgenticX is a unified, production-ready multi-agent platform — Python SDK + CLI (agx) + Studio server + Machi… | 233 | Python | 2026-09-21 |
| [morganlinton/Albatross](https://github.com/morganlinton/Albatross) | Open source, terminal-first AI coding agent with fully transparent multi-model routing. Local (Ollama, LM Stu… | 228 | Rust | 2026-09-21 |
| [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) | Drop-in TypeSafeClient replacement backed by LLM APIs | 226 | Python | 2026-09-18 |
| [rokbenko/quackd](https://github.com/rokbenko/quackd) | One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a b… | 224 | Python | 2026-09-21 |
| [jkudish/jev-browser](https://github.com/jkudish/jev-browser) | Browser use using Typesafe's Jev model | 221 | TypeScript | 2026-09-21 |
| [kitze/skillbox](https://github.com/kitze/skillbox) | Self-hosted, versioned skills library for AI agents. MCP, scoped clients, and optional Jev recommendations. | 221 | TypeScript | 2026-09-19 |
| [damianvtran/local-operator](https://github.com/damianvtran/local-operator) | An open-source AI agent hub for your own machine: build organizations of collaborating agents that message ea… | 214 | Python | 2026-09-21 |
| [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) | Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools. | 213 | TypeScript | 2026-09-21 |
| [ielab/llm-rankers](https://github.com/ielab/llm-rankers) | Document Ranking with Large Language Models. | 212 | Python | 2026-09-19 |
| [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) | A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources. | 211 | — | 2026-09-21 |
| [hr98w/jev-visual](https://github.com/hr98w/jev-visual) | An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scorin… | 208 | Python | 2026-09-21 |
| [socai-io/socai](https://github.com/socai-io/socai) | A Browser Use Agent that actually reads social media. Fast. Precise. Deep. | 206 | Rust | 2026-09-21 |
| [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) | The official TypeScript/JavaScript library for the TypeSafe API | 206 | TypeScript | 2026-09-15 |
| [liuyanghejerry/Clausura](https://github.com/liuyanghejerry/Clausura) | CI-native agent CLI tool for deterministic pipeline gating. | 203 | Rust | 2026-09-20 |
| [qiz029/dscode](https://github.com/qiz029/dscode) | A DeepSeek coding agent harness: persistent shell, Ultra subagents, auto approval, Chrome MCP and session tel… | 201 | JavaScript | 2026-09-21 |
| [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word… | 193 | JavaScript | 2026-09-21 |
| [logan-markewich/jeff](https://github.com/logan-markewich/jeff) | A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer. | 192 | Python | 2026-09-20 |
| [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) | mcp connector to give your AI agent direct access to typesafe ai's jev model | 187 | Go | 2026-09-20 |
| [Knuckles92/OpenWhisper](https://github.com/Knuckles92/OpenWhisper) | Local speech-to-text, dictation, and meetings with Whisper and OpenAI API. Optional Windows x64 engines: Para… | 187 | Python | 2026-09-20 |
| [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) | A source-backed Jev project directory with a reusable Jev-only GitHub review workflow. | 186 | JavaScript | 2026-09-20 |
| [marvikomo/code-lens-ai](https://github.com/marvikomo/code-lens-ai) | — | 182 | TypeScript | 2026-09-20 |
| [lakeday-org/perch](https://github.com/lakeday-org/perch) | Semantic code linting with Jev | 167 | JavaScript | 2026-09-21 |
| [kevinbadi/hyperedit](https://github.com/kevinbadi/hyperedit) | AI-powered video editor with FFMPEG, Remotion, & Obsidian Agents Baked in | 166 | TypeScript | 2026-09-20 |
| [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser) | "Work appears completed or recorded. Run /compact to save tokens." | 165 | TypeScript | 2026-09-21 |
| [glowbom/glowbom-oss](https://github.com/glowbom/glowbom-oss) | Build software like writing a book | 163 | Go | 2026-09-20 |
| [jongwony/epistemic-protocols](https://github.com/jongwony/epistemic-protocols) | Epistemic protocols for Claude Code — structure human-AI interaction quality at every decision point - https:… | 162 | JavaScript | 2026-09-21 |
| [kitze/unclutter](https://github.com/kitze/unclutter) | WXT browser extension: Jev-powered page clutter removal with reusable template rules. | 160 | TypeScript | 2026-09-18 |
| [FBddcz/embodied-jev](https://github.com/FBddcz/embodied-jev) | EmbodiedJev: MuJoCo robot decision workbench with MiniCPM5-2B, Jev and compatible model APIs | 159 | Python | 2026-09-21 |
| [fighthealthinsurance/fighthealthinsurance](https://github.com/fighthealthinsurance/fighthealthinsurance) | — | 156 | Python | 2026-09-21 |
| [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking … | 153 | Python | 2026-09-21 |
| [NiceEval/NiceEval](https://github.com/NiceEval/NiceEval) | build eval for your agent in 10 mins | 153 | TypeScript | 2026-09-21 |
| [AgentEvalHQ/AgentEval](https://github.com/AgentEvalHQ/AgentEval) | AgentEval is the comprehensive .NET toolkit for AI agent evaluation—tool usage validation, RAG quality metric… | 146 | C# | 2026-09-21 |
| [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) | 🔥🔥 Papers, open reproductions and independent evaluations behind System One models and Jev. | 145 | JavaScript | 2026-09-21 |
| [Nine-Minds/alga-psa](https://github.com/Nine-Minds/alga-psa) | An open source MSP PSA from Nine Minds | 141 | TypeScript | 2026-09-21 |
| [PatrickSUDO/fadacai-portfolio](https://github.com/PatrickSUDO/fadacai-portfolio) | Claude Code 投資研究與組合管理框架：skills + MCP + 第一性原理紀律 + thesis ledger | 140 | Python | 2026-09-21 |
| [juspay/neurolink](https://github.com/juspay/neurolink) | One TypeScript interface for 40 AI providers across three inference types — generate, stream, and decide. Dec… | 135 | TypeScript | 2026-09-21 |
| [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) | A lightweight Jev-powered router for models, tools, and subagents | 133 | TypeScript | 2026-09-21 |
| [bitsocialnet/5chan](https://github.com/bitsocialnet/5chan) | A peer-to-peer 4chan alternative. | 132 | TypeScript | 2026-09-21 |
| [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) | Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it | 131 | TypeScript | 2026-09-21 |
| [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) | TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, c… | 131 | TypeScript | 2026-09-19 |
| [catlog22/pi-maestro-flow](https://github.com/catlog22/pi-maestro-flow) | Maestro workflow tools as Pi extensions — pi-teammate + pi-maestro-agent | 127 | TypeScript | 2026-09-21 |
| [hyprstream/hyprstream](https://github.com/hyprstream/hyprstream) | HyprStream: agentic infrastructure for continous online-learning applications | 127 | Rust | 2026-09-21 |
| [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) | Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversi… | 124 | TypeScript | 2026-09-21 |
| [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) | grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AN… | 123 | JavaScript | 2026-09-21 |
| [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | Adapt local language models into Jev-compatible structured decision engines with Choice, Score, and Noul outp… | 120 | Python | 2026-09-21 |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) | A community directory of projects built on Jev, TypeSafe AI's System One model. | 119 | JavaScript | 2026-09-21 |
| [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) | Typed decisions with TypeSafe's Jev, the first System One model | 118 | JavaScript | 2026-09-21 |
| [receptron/laya](https://github.com/receptron/laya) | Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime | 116 | TypeScript | 2026-09-21 |
| [SamSaffron/term-llm](https://github.com/SamSaffron/term-llm) | LLM Swiss Army Knife for your Terminal | 116 | Go | 2026-09-21 |
| [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) | An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs… | 113 | TypeScript | 2026-09-21 |
| [devagrawal09/stanley-code](https://github.com/devagrawal09/stanley-code) | Bounded TypeSafe Jev workflows for coding agents. | 109 | TypeScript | 2026-09-19 |
| [miptgirl/miptgirl_medium](https://github.com/miptgirl/miptgirl_medium) | Code for Medium blog posts | 109 | Jupyter Notebook | 2026-09-18 |
| [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) | Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context… | 108 | Rust | 2026-09-21 |
| [cookiespiggy/agentic-rl](https://github.com/cookiespiggy/agentic-rl) | Agentic RL 中文零基础教程（25 章）：从概念到 GRPO 实战，含 TRL 最小可跑示例。第 25 章讲清 Jev / TypeSafe System One 判别模型与 RL 的能力边界 \| Chine… | 106 | Python | 2026-09-21 |
| [FerryCorleone/crush-monitor](https://github.com/FerryCorleone/crush-monitor) | Crush 好感监控器：用 Jev 分析微信聊天的情绪、意图和回复表现。本机部署，使用自己的 API Key。 | 104 | TypeScript | 2026-09-21 |
| [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz | 104 | Python | 2026-09-17 |
| [dom-actions/doma](https://github.com/dom-actions/doma) | The open-source of DomA, an AI automation agent for the browser. | 103 | TypeScript | 2026-09-21 |
| [sonnylazuardi/superterminal](https://github.com/sonnylazuardi/superterminal) | a native multiplexer terminal for Windows, Linux and Mac | 99 | Rust | 2026-09-21 |
| [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) | A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creat… | 98 | Python | 2026-09-21 |
| [timrogers/formanator](https://github.com/timrogers/formanator) | Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) cl… | 98 | Rust | 2026-09-21 |
| [thisisnsh/aithing](https://github.com/thisisnsh/aithing) | AI, Agents, and Automation | 92 | Swift | 2026-09-21 |
| [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway) | An easy way to use jev with your coding agent for tool calling reasoning | 90 | TypeScript | 2026-09-21 |
| [fabricioctelles/skills](https://github.com/fabricioctelles/skills) | A collection of skills for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusa… | 89 | Python | 2026-09-21 |
| [pithings/advocaat](https://github.com/pithings/advocaat) | A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev. | 88 | TypeScript | 2026-09-18 |
| [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) | Code quality and coverage for coding agents | 87 | Rust | 2026-09-21 |
| [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) | A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fas… | 85 | — | 2026-09-21 |
| [MarcelMichau/fake-survey-generator](https://github.com/MarcelMichau/fake-survey-generator) | A slightly more-than-trivial full-stack application built with DDD & CQRS concepts | 85 | C# | 2026-09-21 |
| [daseinlabs/open-jev](https://github.com/daseinlabs/open-jev) | Open Jev implementation with custom finetuning | 84 | Python | 2026-09-19 |
| [merefield/discourse-chatbot](https://github.com/merefield/discourse-chatbot) | An AI bot with RAG capability for Topics, Chat & Customer Support in Discourse, currently powered by OpenAI | 84 | Ruby | 2026-09-21 |
| [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) | Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification | 81 | C | 2026-09-20 |
| [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) | Detect youtube sponsor segment with live audio and transcript powered by Jev | 81 | JavaScript | 2026-09-18 |
| [agent-labs-dev/fastbrowse](https://github.com/agent-labs-dev/fastbrowse) | A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim… | 79 | Python | 2026-09-21 |
| [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) | Live Jev trader on Hyperliquid | 79 | TypeScript | 2026-09-21 |
| [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel) | A WebMCP benchmark, measures WebMCP against other browser-agent interfaces. | 75 | HTML | 2026-09-18 |
| [openclaw/docs](https://github.com/openclaw/docs) | OpenClaw docs + translation | 75 | JavaScript | 2026-09-21 |
| [baldaworks/callee](https://github.com/baldaworks/callee) | Markdown-defined provider-backed agents and deterministic workflows for ACP runtimes. | 74 | Go | 2026-09-21 |
| [tonone-ai/tonone](https://github.com/tonone-ai/tonone) | One session. Two commands. Full team. Zero meetings. | 73 | Python | 2026-09-20 |
| [Bodila51/grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) | Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples | 70 | Python | 2026-09-20 |
| [tkersey/dotfiles](https://github.com/tkersey/dotfiles) | public dot files | 70 | Python | 2026-09-21 |
| [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) | Curated Jev resources and runnable examples for typed AI decisions. | 69 | Python | 2026-09-21 |
| [can1357/jegrep](https://github.com/can1357/jegrep) | Semantic grep: find code by describing what you're looking for, powered by Jev. | 69 | Rust | 2026-09-20 |
| [escapeboy/agent-fleet-o](https://github.com/escapeboy/agent-fleet-o) | Open-source AI agent orchestration platform — self-hosted mission control for autonomous multi-agent systems.… | 69 | PHP | 2026-09-21 |
| [Ratimon/openquok-monorepo](https://github.com/Ratimon/openquok-monorepo) | An agentic social media scheduling workspace engine/tool (CLI + Dashboard) | 69 | TypeScript | 2026-09-21 |
| [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) | A verified, community-maintained catalog of 530 open-source projects built with Jev. | 66 | Astro | 2026-09-21 |
| [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) | Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server. | 66 | JavaScript | 2026-09-18 |
| [virtual-context/virtual-context](https://github.com/virtual-context/virtual-context) | Virtual Context Swapping System - Virtual Memory for AI | 65 | Python | 2026-09-21 |
| [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) | A decision cache for TypeSafe Jev-class models — memoize decisions so repeats are free, deterministic, and sh… | 64 | — | 2026-09-19 |
| [BrokkAi/mjolnir](https://github.com/BrokkAi/mjolnir) | Manage Codex, Claude Code, Muse Code, Kimi Code, Grok Build, and DeepSeek Harness with durable sessions, isol… | 63 | Rust | 2026-09-21 |
| [Heman10x-NGU/Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) | Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev b… | 62 | Python | 2026-09-20 |
| [jexp/neo4jev](https://github.com/jexp/neo4jev) | Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationshi… | 62 | Jupyter Notebook | 2026-09-18 |
| [NanmiCoder/jev-arena](https://github.com/NanmiCoder/jev-arena) | Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、… | 62 | JavaScript | 2026-09-20 |
| [Parcha-ai/parcha-skills](https://github.com/Parcha-ai/parcha-skills) | Skills I use to execute long-running coding agents without breaking my back. | 60 | Python | 2026-09-21 |
| [Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | — | 60 | Python | 2026-09-21 |
| [Dun-sin/HearItFresh](https://github.com/Dun-sin/HearItFresh) | Get a personalized spotify playlist based on your current taste of music | 59 | TypeScript | 2026-09-20 |
| [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router) | CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered b… | 59 | TypeScript | 2026-09-21 |
| [mizchi/jev-lint](https://github.com/mizchi/jev-lint) | lint text in code by jev scorerer | 58 | TypeScript | 2026-09-21 |
| [temporal-community/temporal-agent-harness](https://github.com/temporal-community/temporal-agent-harness) | Temporal-native Durable Multi Agent Harness | 58 | Python | 2026-09-20 |
| [danielgshea/jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge) | Using Jev as an evaluator. | 57 | Python | 2026-09-19 |
| [kyh/vibedgames](https://github.com/kyh/vibedgames) | A game studio for your agent 🎮 | 57 | TypeScript | 2026-09-21 |
| [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) | The system one Harness for system one models | 55 | Python | 2026-09-21 |
| [rexleimo/aios](https://github.com/rexleimo/aios) | Local-first AI agent bootstrap: Playwright Browser MCP + ContextDB for Codex CLI, Claude Code, Gemini CLI, an… | 54 | JavaScript | 2026-09-21 |
| [TimeWarpEngineering/timewarp-architecture](https://github.com/TimeWarpEngineering/timewarp-architecture) | A distributed application template for dotnet. Utilizing Blazor, Web API, gRPC, Tye, YARP etc. | 54 | C# | 2026-09-21 |
| [opencues/opencues](https://github.com/opencues/opencues) | The open standard for omnipresent AI. Claude Code, OpenCode, Gemini CLI, Shell, Chrome, DeepSeek Harness. Mod… | 53 | TypeScript | 2026-09-20 |
| [benelog/devnote](https://github.com/benelog/devnote) | 정상혁의 개발수첩 | 52 | Shell | 2026-09-18 |
| [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) | Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one … | 52 | Python | 2026-09-21 |
| [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) | JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open. | 52 | Python | 2026-09-21 |
| [iamaamir/pi-bifrost](https://github.com/iamaamir/pi-bifrost) | Automatically route each Pi prompt to a model based on task complexity, price, speed, or context length. Smar… | 52 | TypeScript | 2026-09-21 |
| [wobsoriano/oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev) | — | 52 | TypeScript | 2026-09-21 |
| [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) | Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。 | 52 | HTML | 2026-09-21 |
| [caudena/beam_weaver](https://github.com/caudena/beam_weaver) | Elixir-native LangChain, LangGraph, and DeepAgents for traceable LLM apps: OTP workflows, tools, memory, huma… | 51 | Elixir | 2026-09-21 |
| [monteduro/killmyidea](https://github.com/monteduro/killmyidea) | Describe your startup idea. Jev decides: kill it, fix it or ship it. | 51 | TypeScript | 2026-09-18 |
| [YEDASAVG/Stratum](https://github.com/YEDASAVG/Stratum) | AI-powered Log Intelligence System - Semantic search, anomaly detection, and root cause analysis for logs usi… | 51 | Rust | 2026-09-19 |
| [quantskills/QuantStudio](https://github.com/quantskills/QuantStudio) | 本地 AI 研究与办公工作台 · 技能、专家、专家团、数据与成果 \| A local AI workspace for research and everyday work | 50 | JavaScript | 2026-09-21 |
| [GinSing1226/ScreenClaw](https://github.com/GinSing1226/ScreenClaw) | Record once, replay anytime & screenshots + percentage-coordinate grids: non-blocking Windows desktop RPA / C… | 49 | Python | 2026-06-23 |
| [everruns/everruns](https://github.com/everruns/everruns) | Headless durable agentic harness engine. Run durable AI agents reliably and scalably. | 48 | Rust | 2026-09-21 |
| [achimala/jev-paint](https://github.com/achimala/jev-paint) | Use Jev to make art! | 46 | JavaScript | 2026-09-19 |
| [affirmitv/ghosthands](https://github.com/affirmitv/ghosthands) | Give an agent real hands and eyes: undetectable, DOM-independent GUI automation. A $4 USB-HID microcontroller… | 46 | Python | 2026-09-18 |
| [deepanwadhwa/OpenDecision](https://github.com/deepanwadhwa/OpenDecision) | OpenDecision is an open-source semantic decision engine like typesafe's jev. | 46 | Python | 2026-09-21 |
| [Dimweaker/jev-libero](https://github.com/Dimweaker/jev-libero) | Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks. | 46 | Python | 2026-09-21 |
| [RafalWilinski/vibecheck](https://github.com/RafalWilinski/vibecheck) | Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post | 46 | JavaScript | 2026-09-20 |
| [SiliconLabAI/OpenJev](https://github.com/SiliconLabAI/OpenJev) | OpenSource Jev | 46 | TypeScript | 2026-09-21 |
| [ikermoel/open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) | Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisi… | 45 | Python | 2026-09-21 |
| [skeptrunedev/jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) | A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence a… | 44 | Python | 2026-09-19 |
| [agentsea/nautilo](https://github.com/agentsea/nautilo) | AI goes multiplayer. A self-hosted workspace for people and machine people. Create, code, and work together a… | 43 | TypeScript | 2026-09-21 |
| [walidboulanouar/awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) | Awesome list of TypeSafe AI Jev use cases: 74 demos ranked by likes, 150+ GitHub repos, limits, cost and API … | 43 | — | 2026-09-20 |
| [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | — | 42 | Python | 2026-09-18 |
| [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) | Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as s… | 40 | Python | 2026-09-21 |
| [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enter… | 40 | Python | 2026-09-19 |
| [pinecone-io/cultivar](https://github.com/pinecone-io/cultivar) | Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents. | 40 | Python | 2026-09-18 |
| [r-ms/mini-jev](https://github.com/r-ms/mini-jev) | mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter'… | 40 | Python | 2026-09-18 |
| [socai-io/jev-social](https://github.com/socai-io/jev-social) | Jev-powered Instagram, TikTok, and LinkedIn research: typed routing, real browser evidence, streamed post car… | 40 | JavaScript | 2026-09-21 |
| [okinaaudio/live-jev](https://github.com/okinaaudio/live-jev) | Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done. | 39 | Python | 2026-09-21 |
| [IgorGanapolsky/trading](https://github.com/IgorGanapolsky/trading) | Paper-only SPY put-credit validation lab. Broker-backed ledgers and hard risk gates. Live capital blocked; no… | 38 | Python | 2026-09-21 |
| [tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge) | ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex… | 37 | TypeScript | 2026-09-21 |
| [bilune/jev-design](https://github.com/bilune/jev-design) | Can a model design a dashboard? A console whose whole design system is generated at runtime by Jev from a one… | 36 | TypeScript | 2026-09-21 |
| [Diogenesoftoronto/keating](https://github.com/Diogenesoftoronto/keating) | The hyperteacher, autoteaching in a metaharness. | 36 | TypeScript | 2026-09-20 |
| [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) | This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev. | 36 | TypeScript | 2026-09-19 |
| [zhengxuyu/litjev](https://github.com/zhengxuyu/litjev) | Turn any off-the-shelf LLM into a Jev -like decision layer | 36 | Python | 2026-09-21 |
| [MichelKerkmeester/skilled-agent-harness_spec-driven-loops](https://github.com/MichelKerkmeester/skilled-agent-harness_spec-driven-loops) | AI-assisted coding setup that helps you spend less time re-explaining context, and more time shipping with be… | 35 | TypeScript | 2026-09-21 |
| [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp) | MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client | 34 | TypeScript | 2026-09-19 |
| [TypeLLM/TypeLLM](https://github.com/TypeLLM/TypeLLM) | Type-Safe Decoding for Autoregressive LLMs | 34 | Python | 2026-09-21 |
| [Alurith/jeff](https://github.com/Alurith/jeff) | Catch code issues before they catch you. | 33 | Go | 2026-09-20 |
| [kieranklaassen/thinkroom](https://github.com/kieranklaassen/thinkroom) | Thinkroom — where deeper thinking compounds. Try it free at https://thinkroom.kieranklaassen.com | 33 | Ruby | 2026-09-19 |
| [DevMortimer/pi-typesafe](https://github.com/DevMortimer/pi-typesafe) | TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors | 32 | TypeScript | 2026-09-21 |
| [hakari-bench/hakari-bench](https://github.com/hakari-bench/hakari-bench) | ⚖️ HAKARI-Bench is a lightweight IR benchmark that rebuilds retrieval tasks as small Nano-sets, making model … | 32 | Python | 2026-09-19 |
| [maruel/genai](https://github.com/maruel/genai) | The opinionated high performance professional-grade AI package for Go | 32 | Go | 2026-09-21 |
| [nicholasgriffintn/ai-platform](https://github.com/nicholasgriffintn/ai-platform) | A multi-model AI chat platform built to be a complete solution for your own personal assistant or an ai assis… | 32 | TypeScript | 2026-09-21 |
| [piyush97/PiyushMehta.com](https://github.com/piyush97/PiyushMehta.com) | A modern, fast, and SEO-optimized personal website built with Astro, showcasing my work as a Senior Software … | 32 | HTML | 2026-09-17 |
| [seznam/jailoc](https://github.com/seznam/jailoc) | 🔒 Jail your AI agents — sandboxed Docker environments with network isolation for Opencode agents | 32 | Go | 2026-09-20 |
| [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) | We only curate source-reviewed JEV-related projects with 100+ GitHub stars — integrations, tools, open models… | 31 | JavaScript | 2026-09-21 |
| [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer) | Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your e… | 31 | JavaScript | 2026-09-19 |
| [samdotmak/jev-recall](https://github.com/samdotmak/jev-recall) | Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev | 31 | TypeScript | 2026-09-20 |
| [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev) | Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev | 30 | TypeScript | 2026-09-20 |
| [tshmieldev/sharp](https://github.com/tshmieldev/sharp) | Filter your X.com feed with Jev or any LLM | 29 | TypeScript | 2026-09-21 |
| [joshuaeroman/plasmallm](https://github.com/joshuaeroman/plasmallm) | A KDE Plasma plasmoid to add desktop chat with LLMs | 28 | QML | 2026-09-18 |
| [AlbionaHoti/refgarden](https://github.com/AlbionaHoti/refgarden) | A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked col… | 27 | TypeScript | 2026-09-19 |
| [boozedog/pi-codemode](https://github.com/boozedog/pi-codemode) | — | 27 | TypeScript | 2026-09-21 |
| [braintrustdata/braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) | JavaScript Tracing & Evals library for Braintrust | 27 | TypeScript | 2026-09-21 |
| [AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo) | 100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuc… | 26 | Rust | 2026-09-21 |
| [dannote/jev](https://github.com/dannote/jev) | TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer | 26 | Elixir | 2026-09-21 |
| [DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest) | A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. | 26 | TypeScript | 2026-09-18 |
| [wundercorp/loki](https://github.com/wundercorp/loki) | The agent that evolves with you 𖤍 | 26 | Python | 2026-09-17 |
| [Hulupeep/Specflow](https://github.com/Hulupeep/Specflow) | Specs that enforce themselves. Turn specs into contracts that can't be broken by helpful LLMs. | 25 | JavaScript | 2026-09-21 |
| [myc0576/SmartMoney-Cub](https://github.com/myc0576/SmartMoney-Cub) | Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible fina… | 25 | Python | 2026-09-21 |
| [JackZeng/Jev_apps](https://github.com/JackZeng/Jev_apps) | 看看 Jev 能做什么：用中英文讲清热门应用、工作原理和各自优缺点。Explore Jev apps with plain-language examples, explanations, and comparison… | 24 | Python | 2026-09-21 |
| [lykycy123/RoboJEV](https://github.com/lykycy123/RoboJEV) | Two-stage JEV control of a Franka Panda in MuJoCo | 24 | Python | 2026-09-21 |
| [sdras/jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension) | — | 24 | JavaScript | 2026-09-20 |
| [tomcounsell/ai](https://github.com/tomcounsell/ai) | A productive AI coworker that learns, self-improves, and ships work. | 24 | Python | 2026-09-21 |
| [rorshopping/jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) | Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benc… | 23 | Python | 2026-09-17 |
| [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) | Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call rece… | 23 | Python | 2026-09-21 |
| [aarora79/my-ai-assets](https://github.com/aarora79/my-ai-assets) | A curated collection of advanced prompt templates for Claude and other LLMs, featuring systematic analysis fr… | 22 | HTML | 2026-09-19 |
| [fidecastro/jevify](https://github.com/fidecastro/jevify) | Supersimple way to serve LLMs as a Jev-like endpoint | 22 | Python | 2026-09-20 |
| [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) | JEV HUB · X 上关于 TypeSafe AI「系统一模型」Jev 的长文与演示视频聚合（保留原链与作者）｜ 谁是专家 出品 | 22 | CSS | 2026-09-21 |
| [sabeel111/OpenSourceJev](https://github.com/sabeel111/OpenSourceJev) | Turning an LLM model into a Jev like System. | 22 | Python | 2026-09-20 |
| [altryne/jevify](https://github.com/altryne/jevify) | An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent communit… | 21 | Python | 2026-09-21 |
| [andresguc1/hal-test](https://github.com/andresguc1/hal-test) | HAL-TEST is an Open Source visual automation framework for Playwright that lets developers design and orchest… | 21 | JavaScript | 2026-09-20 |
| [davila7/jev-explained](https://github.com/davila7/jev-explained) | Jev Explained | 21 | TypeScript | 2026-09-20 |
| [razaanstha/ulka](https://github.com/razaanstha/ulka) | Experimental browser agent powered by FX, Jev, and Vercel AI Gateway. Bring your own API key to read pages an… | 21 | TypeScript | 2026-09-19 |
| [zadescoxp/Jev-Trades](https://github.com/zadescoxp/Jev-Trades) | Trading bot with the all new TypeSafe AI's first system one model named as Jev | 21 | Python | 2026-09-18 |
| [Argos1111/jev_local](https://github.com/Argos1111/jev_local) | Replicating Jev with a local LLM | 20 | Python | 2026-09-21 |
| [mizchi/jev-playground](https://github.com/mizchi/jev-playground) | — | 20 | TypeScript | 2026-09-21 |
| [pome-sh/digital-twins](https://github.com/pome-sh/digital-twins) | Test mode for your integrations, built for the way agents build. | 20 | TypeScript | 2026-09-21 |
| [qkal/Canny](https://github.com/qkal/Canny) | Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Je… | 20 | TypeScript | 2026-09-21 |
| [zszz3/Pi-Jev-Guide](https://github.com/zszz3/Pi-Jev-Guide) | — | 20 | TypeScript | 2026-09-21 |
| [braintrustdata/braintrust-sdk-python](https://github.com/braintrustdata/braintrust-sdk-python) | Python Tracing & Evals library for Braintrust | 19 | Python | 2026-09-21 |
| [rhighs/jev-code](https://github.com/rhighs/jev-code) | Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation. | 19 | TypeScript | 2026-09-20 |
| [CheshiAI/Cheshi](https://github.com/CheshiAI/Cheshi) | Jev-powered conversation memory: find past sessions and revisit decisions with original sources. A macOS work… | 18 | C | 2026-09-21 |
| [everyinfra/jev-radar](https://github.com/everyinfra/jev-radar) | 📡 全网最全 · The world's most comprehensive tracker of the Jev (TypeSafe AI System One) ecosystem — 220+ document… | 18 | — | 2026-09-21 |
| [luantak/is-malicious](https://github.com/luantak/is-malicious) | A codebase scanner that helps you not run malicous code | 18 | TypeScript | 2026-09-21 |
| [OmniJev/PlayJev](https://github.com/OmniJev/PlayJev) | 🚀🚀 A 0.8B JEV-like multimodal model playing GUI games directly from raw pixels. | 18 | JavaScript | 2026-09-21 |
| [philipbrembeck/pi-advisor](https://github.com/philipbrembeck/pi-advisor) | Fully customizable Advisor and Executor flow plugin for the Pi Coding Agent | 18 | TypeScript | 2026-09-19 |
| [BlackJaxDev/XRENGINE](https://github.com/BlackJaxDev/XRENGINE) | This is my custom open-source C# game engine designed from the ground-up for maximum possible performance ren… | 17 | C# | 2026-09-18 |
| [colliber/duckdb-jev](https://github.com/colliber/duckdb-jev) | DuckDB extension: typed Jev answers as real SQL types | 17 | C++ | 2026-09-18 |
| [Davidcreador/pi-dcp](https://github.com/Davidcreador/pi-dcp) | Cut LLM token spend in long Pi sessions, automatically. Dedup redundant tool calls, strip errored payloads, a… | 17 | TypeScript | 2026-09-19 |
| [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi) | Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) fr… | 17 | TypeScript | 2026-09-19 |
| [TypeSafeAI/typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground) | Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts,… | 17 | TypeScript | 2026-09-21 |
| [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) | Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails… | 17 | JavaScript | 2026-09-20 |
| [wd041216-bit/zero-api-key-web-search](https://github.com/wd041216-bit/zero-api-key-web-search) | Jev-powered search infrastructure for AI agents: zero API keys, MCP-ready, LLM-context aware, with local neur… | 17 | Python | 2026-09-21 |
| [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) | Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases: repos, patterns, benchmarks, and … | 16 | — | 2026-09-20 |
| [keltokhy/jgrep](https://github.com/keltokhy/jgrep) | grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms … | 16 | Python | 2026-09-21 |
| [Nasrallah-AL/jev-cli](https://github.com/Nasrallah-AL/jev-cli) | Command-line tool for TypeSafe's Jev AI model | 16 | TypeScript | 2026-09-20 |
| [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) | Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Ever… | 15 | — | 2026-09-21 |
| [Brainwires/jevwire](https://github.com/Brainwires/jevwire) | Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code… | 15 | TypeScript | 2026-09-21 |
| [getaskclaw/amber](https://github.com/getaskclaw/amber) | 琥珀式封存历史回放评测（AMBER）：封进琥珀，重做当时的题 —— 真实事件回放、物理封存、预注册评分的方法规范 | 15 | Python | 2026-09-21 |
| [machina-sports/sportsclaw](https://github.com/machina-sports/sportsclaw) | — | 15 | TypeScript | 2026-09-21 |
| [oso95/x-scanner](https://github.com/oso95/x-scanner) | Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter | 15 | TypeScript | 2026-09-19 |
| [Ray-Hughes/jevalyn](https://github.com/Ray-Hughes/jevalyn) | The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, ca… | 15 | Ruby | 2026-09-21 |
| [utk2103/jev-studio](https://github.com/utk2103/jev-studio) | if you're experimenting with jev it will be easier from here | 15 | Python | 2026-09-21 |
| [XiaoConstantine/sgrep](https://github.com/XiaoConstantine/sgrep) | semantic grep | 15 | Go | 2026-09-19 |
| [atanasster/electionsbg](https://github.com/atanasster/electionsbg) | Data statistics for Bulgaria | 14 | TypeScript | 2026-09-19 |
| [chy4pro/jev-for-chrome](https://github.com/chy4pro/jev-for-chrome) | Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community p… | 14 | TypeScript | 2026-09-21 |
| [hraness/wordcell](https://github.com/hraness/wordcell) | A knowledge base for coding agents, built from Markdown, backlinks, semantic search, and Git context. | 14 | TypeScript | 2026-09-21 |
| [masharratt/claude-flow-novice](https://github.com/masharratt/claude-flow-novice) | Simplified Claude Flow for beginners - AI agent orchestration made easy | 14 | Shell | 2026-09-21 |
| [packstub/filament-flow](https://github.com/packstub/filament-flow) | Visual workflow automation for Filament panels: triggers, conditions and actions drawn on a canvas, run by yo… | 14 | PHP | 2026-09-21 |
| [rlaope/jeval](https://github.com/rlaope/jeval) | Measures what your Jev classifier's confidence is really worth, and sets the human hand-off line from what a … | 14 | Python | 2026-09-21 |
| [BorisLeMeec/jev](https://github.com/BorisLeMeec/jev) | A claude code plugin for jev | 13 | Go | 2026-09-18 |
| [carldaws/hunch](https://github.com/carldaws/hunch) | Probabilistic control flow for Ruby and Rails - powered by TypeSafe's Jev | 13 | Ruby | 2026-09-19 |
| [erendikmenn/jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark) | Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG | 13 | Python | 2026-09-20 |
| [everyai-com/jev-directory](https://github.com/everyai-com/jev-directory) | — | 13 | HTML | 2026-09-21 |
| [genai-craft/openvons](https://github.com/genai-craft/openvons) | openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド | 13 | Python | 2026-09-21 |
| [jon-devlapaz/jev-me](https://github.com/jon-devlapaz/jev-me) | Grill-me with Jev optional each turn | 13 | — | 2026-09-19 |
| [kyu1204/jgrep](https://github.com/kyu1204/jgrep) | grep for what code does, not what it's called. Semantic code search powered by TypeSafe Jev. | 13 | TypeScript | 2026-09-21 |
| [mossyfield/ST-jeved](https://github.com/mossyfield/ST-jeved) | SillyTavern extension that measures each reply and instructs the narrator only when a rule matches. | 13 | JavaScript | 2026-09-21 |
| [PanAchy/jevvy](https://github.com/PanAchy/jevvy) | Jev-powered plugins for coding agents | 13 | TypeScript | 2026-09-21 |
| [shitianfang/jev-use](https://github.com/shitianfang/jev-use) | Claude Code / Codex / pi plugin that hands agent steps needing no text output to Jev (TypeSafe's judgment mod… | 13 | JavaScript | 2026-09-20 |
| [whilehq/whileai-sdk](https://github.com/whilehq/whileai-sdk) | Scientific RL and SFT post-training for AI agents: build evals that can fail, simulate situations, judge chec… | 13 | Python | 2026-09-21 |
| [AkashPriyadarshii/jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) | Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed de… | 12 | JavaScript | 2026-09-21 |
| [Hiwoniu/Jev-Case](https://github.com/Hiwoniu/Jev-Case) | 收集全网优秀 case 的收藏库 \| A curated collection of excellent cases from across the web | 12 | TypeScript | 2026-09-19 |
| [keeltrace/hermes-jev](https://github.com/keeltrace/hermes-jev) | Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev. | 12 | Python | 2026-09-20 |
| [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) | Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance. | 12 | TypeScript | 2026-09-21 |
| [maplezzk/pi-extensions](https://github.com/maplezzk/pi-extensions) | Extensions for pi coding agent (i18n, distill, tool-supervisor) | 12 | TypeScript | 2026-09-21 |
| [mayank953/Jev](https://github.com/mayank953/Jev) | — | 12 | JavaScript | 2026-09-21 |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | A live Haskell notebook where agents compose commands, semantic judgments, and delegation into programs. Agen… | 12 | Rust | 2026-09-19 |
| [abhishek085/open-spark-jev](https://github.com/abhishek085/open-spark-jev) | Open-source, local decision models inspired by TypeSafe’s Jev and System One - built on Qwen3 for NVIDIA DGX … | 11 | Python | 2026-09-21 |
| [anpicasso/hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) | TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measu… | 11 | Python | 2026-09-20 |
| [huntedman/JevLint](https://github.com/huntedman/JevLint) | Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. | 11 | TypeScript | 2026-09-20 |
| [kavehmz/typesafe-playground](https://github.com/kavehmz/typesafe-playground) | Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisi… | 11 | JavaScript | 2026-09-21 |
| [kylemclaren/jevql](https://github.com/kylemclaren/jevql) | Semantic SQL for Postgres, powered by Jev | 11 | Go | 2026-09-19 |
| [madeye/pi-jev](https://github.com/madeye/pi-jev) | Jev-assisted file retrieval and request caching for faster Pi workflows | 11 | TypeScript | 2026-09-21 |
| [parth-kp/jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier) | Classify your inbox with Jev (TypeSafe's System One model) — tag, move, flag, and notify, all config-driven. | 11 | Python | 2026-09-20 |
| [tickernelz/sub2api](https://github.com/tickernelz/sub2api) | Fork of sub2api some improvements | 11 | Go | 2026-09-21 |
| [tyler-dot-earth/patdown](https://github.com/tyler-dot-earth/patdown) | Block, steer, and "fuzzy lint" with Jev to make agents follow your rules and conventions. CLI, github action,… | 11 | TypeScript | 2026-09-21 |
| [wh000wh000/awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) | Awesome Jev — evidence-graded index of TypeSafe System One: SDKs, MCP tools, agents, apps and open models. 20… | 11 | Python | 2026-09-21 |
| [2951461586/Jev-Register-Tool](https://github.com/2951461586/Jev-Register-Tool) | TypeSafe（Jev / System One）申请 → 确认邮件 → 获批 → 注册 → 建 API Key 全链路工具，纯 HTTP 无浏览器 | 10 | Python | 2026-09-21 |
| [bestagentkits/cloud-harness-mcp](https://github.com/bestagentkits/cloud-harness-mcp) | Remote coding harness exposed as a secure Streamable HTTP MCP server | 10 | TypeScript | 2026-09-21 |
| [buberlo/dsh-jev](https://github.com/buberlo/dsh-jev) | Jev-powered decision layer for DeepSeek Harness | 10 | TypeScript | 2026-09-20 |
| [cocktailpeanut/jevthoven](https://github.com/cocktailpeanut/jevthoven) | AI Music (MIDI) generator powered by Jev | 10 | TypeScript | 2026-09-18 |
| [Coolhand-Labs/coolhand-ruby](https://github.com/Coolhand-Labs/coolhand-ruby) | Zero-config LLM cost & quality monitoring for Ruby apps - automatically log AI API calls and collect user fee… | 10 | Ruby | 2026-09-21 |
| [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) | 1v1 Jev quickscope arena — Three.js + TypeSafe System One | 10 | TypeScript | 2026-09-18 |
| [Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev) | Public examples of Jev used for robot control, 3D modeling and adjacent control tasks, with sources and archi… | 10 | — | 2026-09-21 |
| [HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask) | TypeSafe Jev as the pi coding agent's quiet decision layer | 10 | TypeScript | 2026-09-18 |
| [kikoncuo/jevfire](https://github.com/kikoncuo/jevfire) | JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, an… | 10 | JavaScript | 2026-09-18 |
| [koltyakov/varro](https://github.com/koltyakov/varro) | 🤖 An OpenCode workbench for VS Code with project-aware AI chat and parallel agent sessions | 10 | TypeScript | 2026-09-21 |
| [manifoldor/xtags](https://github.com/manifoldor/xtags) | 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。 | 10 | JavaScript | 2026-09-21 |
| [mejiasd3v/pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) | Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway | 10 | JavaScript | 2026-09-21 |
| [nico-martin/open-jev](https://github.com/nico-martin/open-jev) | open-jev is a browser-focused TypeScript library for typed decisions: one piece of text (the state) plus any … | 10 | TypeScript | 2026-09-21 |
| [tinyhumansai/tinyhivemind](https://github.com/tinyhumansai/tinyhivemind) | Hive mind mechanics for agents. A step closer towards AGI | 10 | Rust | 2026-09-20 |
| [zhangcy122/OpenJev](https://github.com/zhangcy122/OpenJev) | OpenJev: Open-source alternative to TypeSafe Jev. Typed probabilistic decision API (Choice, Noul, Score) powe… | 10 | HTML | 2026-09-21 |
| [zjunlp/JevLoop](https://github.com/zjunlp/JevLoop) | The agent loop where decisions don't cost a large language model call. Zero deps, runs offline, no API key ne… | 10 | TypeScript | 2026-09-21 |
| [akakaule/NimBus](https://github.com/akakaule/NimBus) | — | 9 | C# | 2026-09-21 |
| [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, … | 9 | Rust | 2026-09-21 |
| [atharvamhaske/typesafe-sdk-go](https://github.com/atharvamhaske/typesafe-sdk-go) | unofficial go sdk for typesafe ai. not affiliated with or endorsed by typesafe ai. a side project built to fi… | 9 | Go | 2026-09-21 |
| [ckaraca/awesome-jev](https://github.com/ckaraca/awesome-jev) | A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast,… | 9 | Python | 2026-09-21 |
| [ClassicMiniDIY/classicminidiy](https://github.com/ClassicMiniDIY/classicminidiy) | Classic Mini DIY is the best place to find all the reference material, how-to videos, and much much more for … | 9 | Vue | 2026-09-21 |
| [fellowship-dev/navvi](https://github.com/fellowship-dev/navvi) | Give your AI agent a real browser identity. MCP server with persistent personas, anti-detection browser, and … | 9 | TypeScript | 2026-09-21 |
| [keltokhy/jsort](https://github.com/keltokhy/jsort) | sort by meaning: order lines along a plain-English dimension, from pairwise comparisons judged by TypeSafe's … | 9 | Python | 2026-09-21 |
| [LiJiaHua1024/ModlessChatTrans](https://github.com/LiJiaHua1024/ModlessChatTrans) | Real-time Minecraft Chat Translator - No Mods Needed \| 无需模组的 Minecraft 实时聊天翻译器 | 9 | Python | 2026-09-21 |
| [magnus919/SlopSearX](https://github.com/magnus919/SlopSearX) | Cloud-native, stateless, AI-agent-first meta search engine. Drop-in SearXNG replacement built for the GroktoC… | 9 | Python | 2026-09-21 |
| [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs) | Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. | 9 | TypeScript | 2026-09-18 |
| [rottenpen/agent-stardew](https://github.com/rottenpen/agent-stardew) | 星露谷农场小助手：Jev 自主游玩、dsh 插件、独立 CLI 与 SMAPI Mod | 9 | TypeScript | 2026-09-20 |
| [shaharia-lab/jev-cli](https://github.com/shaharia-lab/jev-cli) | Command-line tool for TypeSafe AI's Jev model. Ask yes/no, multiple-choice and rubric questions about any tex… | 9 | Rust | 2026-09-20 |
| [Synxneuos/jevbrain](https://github.com/Synxneuos/jevbrain) | — | 9 | JavaScript | 2026-09-20 |
| [TannerMidd/specpi-jev-guard](https://github.com/TannerMidd/specpi-jev-guard) | — | 9 | JavaScript | 2026-09-20 |
| [trungdq88/jev-tetris](https://github.com/trungdq88/jev-tetris) | Jev play Tetris in real-time against other AI models | 9 | JavaScript | 2026-09-21 |
| [tumf/jev-cli](https://github.com/tumf/jev-cli) | Small dependency-free CLI for TypeSafe Jev | 9 | Python | 2026-09-19 |
| [ZYHUO/nyat-bot](https://github.com/ZYHUO/nyat-bot) | NyatBot — a Telegram group-chat agent on the path from chatLLM to AGI | 9 | TypeScript | 2026-09-21 |
| [coil398/dotfiles](https://github.com/coil398/dotfiles) | my best dotfiles. | 8 | Shell | 2026-09-21 |
| [collapseindex/jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed) | BRRRRRRRRRRRRRRRRRRRRRR | 8 | Python | 2026-09-21 |
| [cristianoliveira/jeq](https://github.com/cristianoliveira/jeq) | What happens when jev meets jq? Intelligence you can pipe | 8 | Go | 2026-09-21 |
| [DECRUX9812/typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router) | TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-… | 8 | Python | 2026-09-21 |
| [DGarbs51/solo-orchestrator-skill](https://github.com/DGarbs51/solo-orchestrator-skill) | A skill I have created for using Solo's MCP for creating an orchestration mechanic for making a frontier mode… | 8 | Python | 2026-09-19 |
| [fakoli/anvil](https://github.com/fakoli/anvil) | Anvil — local-first, runtime-neutral project state for humans and AI coding agents (beta). | 8 | Python | 2026-09-21 |
| [hotchpotch/jev-reranker](https://github.com/hotchpotch/jev-reranker) | Jev-powered relevance filtering and reranking for RAG in Python. | 8 | Python | 2026-09-21 |
| [infiquetra/infiquetra-claude-plugins](https://github.com/infiquetra/infiquetra-claude-plugins) | Claude Code plugins for Infiquetra development workflows | 8 | Python | 2026-09-20 |
| [jerryfane/omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction) | Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter | 8 | TypeScript | 2026-09-19 |
| [jiawei686/jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp) | Hand the browser work off: an MCP server where a decision model drives the page for your agent, so a flow cos… | 8 | Python | 2026-09-21 |
| [Kevthetech143/super-jev](https://github.com/Kevthetech143/super-jev) | A small, extensible decision-to-action harness for TypeSafe Jev | 8 | Python | 2026-09-21 |
| [MauroPello/stop-the-slop](https://github.com/MauroPello/stop-the-slop) | 🚫 Spot AI-generated YouTube scripts and content farms in real-time. Open-source browser extension for Chrome … | 8 | JavaScript | 2026-09-20 |
| [miikkij/aimeat-protocol](https://github.com/miikkij/aimeat-protocol) | The Linux of AI - an open, federated, self-hosted AI operating system. Humans, AI agents, and local LLMs shar… | 8 | TypeScript | 2026-09-20 |
| [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) | A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model. | 8 | Python | 2026-09-21 |
| [rajdhakad9826/jev-router](https://github.com/rajdhakad9826/jev-router) | Cost-aware LLM router that picks the cheapest model capable of handling a query, using TypeSafe's Jev for fas… | 8 | TypeScript | 2026-09-21 |
| [ranjan2829/AskJev](https://github.com/ranjan2829/AskJev) | AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude) | 8 | TypeScript | 2026-09-18 |
| [stefw/lkclean](https://github.com/stefw/lkclean) | Chrome extension that cleans up your LinkedIn feed: hides engagement bait, self-promo and off-topic posts usi… | 8 | TypeScript | 2026-09-20 |
| [sunil-sadasivan/jevernetes](https://github.com/sunil-sadasivan/jevernetes) | Live Kubernetes log analysis, contextual investigation, and agent handoff powered by Jev. | 8 | Python | 2026-09-21 |
| [Tangerg/typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go) | Go SDK for the TypeSafe AI API — typed questions in, probability distributions out. | 8 | Go | 2026-09-19 |
| [Towow-ai/jpp](https://github.com/Towow-ai/jpp) | J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，… | 8 | Python | 2026-09-21 |
| [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit) | pre-commit hook: one Jev call judges whether your commit message matches the diff, plus debug leftovers, scop… | 8 | Python | 2026-09-19 |
| [alfdav/music-dl](https://github.com/alfdav/music-dl) | CLI tool for downloading music from Tidal | 7 | Python | 2026-09-21 |
| [arunav25/jev-mcp](https://github.com/arunav25/jev-mcp) | Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and m… | 7 | JavaScript | 2026-09-21 |
| [cdot65/prisma-airs-cli](https://github.com/cdot65/prisma-airs-cli) | CLI tool that provides full operational coverage over Palo Alto Prisma AIRS AI security capabilities | 7 | TypeScript | 2026-09-21 |
| [frostney/clean-code-review](https://github.com/frostney/clean-code-review) | Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by … | 7 | TypeScript | 2026-09-21 |
| [h1bomb/bluff](https://github.com/h1bomb/bluff) | — | 7 | TypeScript | 2026-09-21 |
| [harshwasan/jev-sentinel](https://github.com/harshwasan/jev-sentinel) | Pi coding-agent extension: TypeSafe Jev checks for tool calls, tool outputs and replies (prompt injection, ap… | 7 | TypeScript | 2026-09-20 |
| [HexyeDEV/JevPR](https://github.com/HexyeDEV/JevPR) | PR Risk review, automated by Jev | 7 | Python | 2026-09-21 |
| [HsiangNianian/GlyphWeave](https://github.com/HsiangNianian/GlyphWeave) | Infinite-canvas ASCII roguelike tilemap editor. Paint dungeons, weave glyphs. Multi-layer editing, preset roo… | 7 | Rust | 2026-09-20 |
| [inanna-malick/jev-dsl](https://github.com/inanna-malick/jev-dsl) | Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the s… | 7 | Haskell | 2026-09-18 |
| [inso1337/revl](https://github.com/inso1337/revl) | A language for safe, universal spatiotemporal composability (Cordis paradigm) and orchestration. | 7 | Python | 2026-09-21 |
| [jekhov/jekhov](https://github.com/jekhov/jekhov) | Policy-bounded Jev target selection for resilient Playwright workflows | 7 | TypeScript | 2026-09-19 |
| [jjyr/any-auto](https://github.com/jjyr/any-auto) | Auto approve mode for Pi and Antigravity | 7 | Rust | 2026-09-21 |
| [kushals256/jevcache](https://github.com/kushals256/jevcache) | Skip expensive LLM calls when TypeSafe Jev says same intent. OpenAI-compatible local cache proxy — npx @kusha… | 7 | TypeScript | 2026-09-21 |
| [linny006/mcp-servers-live](https://github.com/linny006/mcp-servers-live) | Auto-updated index of MCP servers shipping on GitHub, refreshed every 15 minutes | 7 | HTML | 2026-09-21 |
| [lucasmartins-ai/lcc](https://github.com/lucasmartins-ai/lcc) | Local Context Compiler (lcc): clean, dedupe and compact prompt context before it reaches the model, then repo… | 7 | Python | 2026-09-21 |
| [OskarLebuda/precog](https://github.com/OskarLebuda/precog) | Your links, loaded before the click. | 7 | TypeScript | 2026-09-20 |
| [Papr-ai/paprwork](https://github.com/Papr-ai/paprwork) | Papr Work is a local-first app that lets you collaborate with AI agents that can access your computer, rememb… | 7 | TypeScript | 2026-09-21 |
| [PixelML/av](https://github.com/PixelML/av) | Video Memory CLI: index once, search/ask forever (dense captions + transcripts + timestamps). Built for agent… | 7 | Python | 2026-09-21 |
| [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) | All things awesome related to Jev | 7 | — | 2026-09-21 |
| [thejorgg/omp-jev](https://github.com/thejorgg/omp-jev) | — | 7 | TypeScript | 2026-09-18 |
| [tickernelz/omp-fabric](https://github.com/tickernelz/omp-fabric) | Fabric for OMP: deterministic, LLM-free orchestration of the Oh My Pi host toolchain | 7 | TypeScript | 2026-09-21 |
| [virolea/lintus](https://github.com/virolea/lintus) | A linter whose rules are written in plain language. | 7 | Ruby | 2026-09-21 |
| [24601/Augustus](https://github.com/24601/Augustus) | Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto dec… | 6 | Python | 2026-09-21 |
| [backmeupplz/jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot) | Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev | 6 | TypeScript | 2026-09-21 |
| [berkayturk/appstore-precheck](https://github.com/berkayturk/appstore-precheck) | Read-only iOS App Store pre-submission check: scans 52 rejection vectors, wraps Apple's fastlane precheck, wa… | 6 | Shell | 2026-09-18 |
| [blazejkustra/softlint](https://github.com/blazejkustra/softlint) | Enforce rules a linter can't. A GitHub Action that reviews PRs against plain-English rules, judged by Jev. | 6 | TypeScript | 2026-09-20 |
| [cablehead/jev.nu](https://github.com/cablehead/jev.nu) | Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities | 6 | Nushell | 2026-09-19 |
| [chengyongru/fastjev](https://github.com/chengyongru/fastjev) | SDK-first, independently maintained SemIf fork for fast, self-hosted semantic decisions. | 6 | Python | 2026-09-21 |
| [collapseindex/dinostomp](https://github.com/collapseindex/dinostomp) | A verification layer for AI evaluations. Checks the instrument, not just the score: data, scorer, runs, numbe… | 6 | Python | 2026-09-19 |
| [eas4ai/cairn](https://github.com/eas4ai/cairn) | A way to keep AI-assisted development tied to what you actually agreed to build. | 6 | JavaScript | 2026-09-20 |
| [forvela/jev-agent-browser](https://github.com/forvela/jev-agent-browser) | Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and … | 6 | JavaScript | 2026-09-21 |
| [himomohi/aside-jev](https://github.com/himomohi/aside-jev) | Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, … | 6 | Python | 2026-09-21 |
| [iefnaf/pi-jev](https://github.com/iefnaf/pi-jev) | Pi extension suite powered by Jev: selective context compaction and model routing | 6 | TypeScript | 2026-09-20 |
| [imMamdouhaboammar/get-fable](https://github.com/imMamdouhaboammar/get-fable) | Make the model you already use work more like a frontier model with better planning, persistent context, skil… | 6 | TypeScript | 2026-09-21 |
| [intersoftdatalabs-in/percussioncms](https://github.com/intersoftdatalabs-in/percussioncms) | Percussion CMS — formerly CM1 / Rhythmyx / CM System by Percussion Software. Actively maintained by Intersoft… | 6 | Java | 2026-09-21 |
| [jackbarunz/jev-tool-router](https://github.com/jackbarunz/jev-tool-router) | Jev-powered MCP tool routing for Codex | 6 | JavaScript | 2026-09-21 |
| [joevidev/ui-generator-instinct-jev](https://github.com/joevidev/ui-generator-instinct-jev) | — | 6 | TypeScript | 2026-09-18 |
| [joshmn/typesafe-sdk](https://github.com/joshmn/typesafe-sdk) | Ruby client for typesafe.ai | 6 | Ruby | 2026-09-19 |
| [larguesa/jev-search](https://github.com/larguesa/jev-search) | Experimental semantic line search with TypeSafe Jev via OpenRouter. Python CLI with no runtime dependencies. | 6 | Python | 2026-09-20 |
| [MoeclubM/PlayJev](https://github.com/MoeclubM/PlayJev) | Better Jev playground | 6 | TypeScript | 2026-09-20 |
| [Nancy-Chauhan/hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) | Autonomous multi-source rental search powered by TypeSafe Jev | 6 | JavaScript | 2026-09-21 |
| [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) | Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, bef… | 6 | TypeScript | 2026-09-19 |
| [okooo5km/jev](https://github.com/okooo5km/jev) | Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe's Jev model, via… | 6 | Python | 2026-09-19 |
| [phaseoteam/Phaseo](https://github.com/phaseoteam/Phaseo) | Open-source, OpenAI-compatible AI gateway with health-aware routing, failover, and live telemetry (cost, late… | 6 | TypeScript | 2026-09-21 |
| [podcctv/Narwhal-Cloud-podman-watcher](https://github.com/podcctv/Narwhal-Cloud-podman-watcher) | — | 6 | Python | 2026-09-21 |
| [Qew7/jev-feels](https://github.com/Qew7/jev-feels) | Semantic decisions as ordinary Ruby — feels?, decide, score, Rails validations and pattern matching powered b… | 6 | Ruby | 2026-09-21 |
| [saibimajdi/typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) | Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structur… | 6 | C# | 2026-09-18 |
| [scale-venture-partners/riff](https://github.com/scale-venture-partners/riff) | A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model | 6 | Python | 2026-09-18 |
| [Adityakhalkar/JevNQL](https://github.com/Adityakhalkar/JevNQL) | — | 5 | Rust | 2026-09-20 |
| [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) | Can a decision model beat dedicated rerankers? TypeSafe Jev vs Cohere Rerank 4 vs ZeroEntropy zerank-2 vs a c… | 5 | Python | 2026-09-17 |
| [cyberofficial/dsh-plugin-jev](https://github.com/cyberofficial/dsh-plugin-jev) | — | 5 | JavaScript | 2026-09-20 |
| [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) | TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai) | 5 | TypeScript | 2026-09-21 |
| [docxology/daf-jev](https://github.com/docxology/daf-jev) | daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confiden… | 5 | Python | 2026-09-18 |
| [endomorphosis/JevOps](https://github.com/endomorphosis/JevOps) | — | 5 | Python | 2026-09-21 |
| [enoyola/jev-grand-prix](https://github.com/enoyola/jev-grand-prix) | An F1 racing game where TypeSafe's Jev picks the racing line and the pedals, and learns each corner's limit b… | 5 | JavaScript | 2026-09-21 |
| [gabrielmoreira/awesome-ai-rabbit-holes](https://github.com/gabrielmoreira/awesome-ai-rabbit-holes) | A never-complete, already-outdated catalog of AI agents and tools. | 5 | TypeScript | 2026-09-21 |
| [jagsan-cyber/reflex-gate](https://github.com/jagsan-cyber/reflex-gate) | A local, privacy-focused alternative to JEv — fast, lightweight, and fully offline. | 5 | Go | 2026-09-21 |
| [jaibhasin/jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver) | A Chrome extension that covers distracting YouTube videos with Jev. Show anyway whenever you want. | 5 | JavaScript | 2026-09-20 |
| [jammaru/jev-lab](https://github.com/jammaru/jev-lab) | 100 AI NPCs live in a tiny town. Jev chooses the next action; the world writes the story. | 5 | TypeScript | 2026-09-18 |
| [johnhughes3/LegalForecastBench](https://github.com/johnhughes3/LegalForecastBench) | LegalForecast-MTD benchmark alpha and official evaluation workflows | 5 | Python | 2026-09-21 |
| [LeahyCC/kungfu-kanban](https://github.com/LeahyCC/kungfu-kanban) | Local-first kanban board where Claude Code agents work your cards — dependency chains with merge gates, an AI… | 5 | JavaScript | 2026-09-18 |
| [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem) | Jev-Mem: System-One Controlled Agentic Memory | 5 | Python | 2026-09-21 |
| [lukstei/slop-grader](https://github.com/lukstei/slop-grader) | Jev-powered, rule-based grader for text files. Runs every rule against every line in parallel. No skimming, n… | 5 | TypeScript | 2026-09-21 |
| [mastepanoski/ce-ai](https://github.com/mastepanoski/ce-ai) | ce-ai orchestrates distributions of the open-source Compound Engineering Plugin — a suite of specialized skil… | 5 | Rust | 2026-09-19 |
| [mertcicekci0/S1Code](https://github.com/mertcicekci0/S1Code) | Rust-native, decision-first coding agent. | 5 | Rust | 2026-09-19 |
| [muratmirgun/owncode](https://github.com/muratmirgun/owncode) | An experimental terminal coding agent with configurable models, Witch orchestration, and multiple context com… | 5 | Go | 2026-09-21 |
| [muthuishere/toolnexus](https://github.com/muthuishere/toolnexus) | One agent SDK, hand-ported to 7 languages — JavaScript, Python, Go, Java, C#, Elixir, Clojure — every port he… | 5 | MDX | 2026-09-21 |
| [nshkrdotcom/typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) | An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM int… | 5 | Elixir | 2026-09-20 |
| [Nyarlathoteppppp/pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context) | Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verb… | 5 | TypeScript | 2026-09-21 |
| [oldmoldycake/jev_vampire_survivors](https://github.com/oldmoldycake/jev_vampire_survivors) | TypeSafe's Jev model plays Vampire Survivors on Steam: BepInEx plugin + Python brain + live decision dashboar… | 5 | Python | 2026-09-19 |
| [ponyo877/jev-telop-live](https://github.com/ponyo877/jev-telop-live) | — | 5 | JavaScript | 2026-09-19 |
| [rashedInt32/jev-mcp](https://github.com/rashedInt32/jev-mcp) | MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Sh… | 5 | TypeScript | 2026-09-20 |
| [redwood-labs-ai/cambium](https://github.com/redwood-labs-ai/cambium) | — | 5 | TypeScript | 2026-09-18 |
| [sametcn99/my-stars-atlas](https://github.com/sametcn99/my-stars-atlas) | A generated catalog of starred GitHub repositories, grouped into stable categories. | 5 | TypeScript | 2026-09-19 |
| [Shashank-H/pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator) | A Jev based context curator for pi | 5 | TypeScript | 2026-09-21 |
| [sinhaparth5/coraza-waf-mod](https://github.com/sinhaparth5/coraza-waf-mod) | A single-binary Web Application Firewall + reverse proxy for Go, built on Coraza (OWASP CRS) with a built-in … | 5 | Go | 2026-09-21 |
| [Softtor/nestjs-hexagonal](https://github.com/Softtor/nestjs-hexagonal) | Claude Code plugin for building NestJS bounded contexts with Hexagonal Architecture, DDD, CQRS, and event-dri… | 5 | TypeScript | 2026-09-21 |
| [taodav/jev_deep_rl](https://github.com/taodav/jev_deep_rl) | — | 5 | Python | 2026-09-20 |
| [tontoko/jev-browser](https://github.com/tontoko/jev-browser) | One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations an… | 5 | JavaScript | 2026-09-21 |
| [ufec/jev-block-android-ad](https://github.com/ufec/jev-block-android-ad) | JevNoiseGate filters unwanted notifications and SMS on Android. Rather than matching keywords, an LLM decides… | 5 | Kotlin | 2026-09-19 |
| [VTSTech/AgentKthx](https://github.com/VTSTech/AgentKthx) | ⚛️ AgentKthx - Inspired by OpenClaw - Aims to do similar things using local models. Also Supports ZAI, OpenRo… | 5 | Python | 2026-09-21 |
| [who/ortus](https://github.com/who/ortus) | Ortus autonomously closes a backlog of bd-tracked issues using Claude Code, ChatGPT Codex, Grok Build, or loc… | 5 | Python | 2026-09-21 |
| [y0usaf/jev-lm](https://github.com/y0usaf/jev-lm) | A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-toke… | 5 | TypeScript | 2026-09-19 |
| [AiPersonacademy/Awesome-jev-use](https://github.com/AiPersonacademy/Awesome-jev-use) | A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources - curated by APA (… | 4 | — | 2026-09-21 |
| [alexwestco/llm-to-jev](https://github.com/alexwestco/llm-to-jev) | Convert LLM prompts to Jev prompts | 4 | JavaScript | 2026-09-21 |
| [andrelandgraf/safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) | Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing. | 4 | TypeScript | 2026-09-18 |
| [antonpictures/ANTON-SIFTA](https://github.com/antonpictures/ANTON-SIFTA) | #SIFTA Swarm Robotics: Crypto Stigmergic Organism | 4 | Python | 2026-09-19 |
| [araray/llmcore](https://github.com/araray/llmcore) | A unified, async Python framework for LLM applications—chat, autonomous agents, RAG, and sandboxed code execu… | 4 | Python | 2026-09-21 |
| [BenjaminG/ai-skills](https://github.com/BenjaminG/ai-skills) | — | 4 | Python | 2026-09-21 |
| [buchmark/claude-jev](https://github.com/buchmark/claude-jev) | Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — cal… | 4 | TypeScript | 2026-09-21 |
| [caiovicentino/jev-align](https://github.com/caiovicentino/jev-align) | Calibrated alignment verifier for LLM responses and agent plans — powered by Jev | 4 | JavaScript | 2026-09-20 |
| [doeixd/jev-pref](https://github.com/doeixd/jev-pref) | Turn your AGENTS.md preferences into a fast, Jev-powered AI linter. | 4 | JavaScript | 2026-09-18 |
| [doronp/jevc](https://github.com/doronp/jevc) | Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the … | 4 | TypeScript | 2026-09-20 |
| [flitsinc/go-llms](https://github.com/flitsinc/go-llms) | A simple way to deal with streaming text, tools, images from LLMs. | 4 | Go | 2026-09-17 |
| [FogMoe/necro](https://github.com/FogMoe/necro) | Abandoned Qwen3.5-0.8B LoRA fine-tuning experiments for Jev-like typed judgments, with datasets, adapters, ev… | 4 | Python | 2026-09-21 |
| [Gachon-Cocone-School/gcs-pulse](https://github.com/Gachon-Cocone-School/gcs-pulse) | — | 4 | Python | 2026-09-21 |
| [gokulnair2001/Convoy](https://github.com/gokulnair2001/Convoy) | Semantic end-to-end agent testing for iOS, Android, and web. | 4 | TypeScript | 2026-09-21 |
| [hallelx2/vectorless-engine](https://github.com/hallelx2/vectorless-engine) | A retrieval engine that reasons over document structure — not embeddings. No chunking, no top-K, no vector DB. | 4 | Go | 2026-09-19 |
| [harrymunro/beadsort](https://github.com/harrymunro/beadsort) | The intelligence layer for beads: typed, calibrated labels for your backlog | 4 | Python | 2026-09-18 |
| [hraness/algal](https://github.com/hraness/algal) | ALGAL is a new take on the agent graph: a language and runtime for agentic program evolution. | 4 | TypeScript | 2026-09-21 |
| [jerryxff26-alt/session-top](https://github.com/jerryxff26-alt/session-top) | Session Top — htop for AI coding sessions, making usage, quota, and token consumption observable and explaina… | 4 | Go | 2026-09-21 |
| [keltokhy/jlink](https://github.com/keltokhy/jlink) | Record linkage for economists: write the match rule in plain English, get a probability per pair, audit it, c… | 4 | Python | 2026-09-21 |
| [Kushwho/jev-codes](https://github.com/Kushwho/jev-codes) | Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI age… | 4 | TypeScript | 2026-09-19 |
| [lhemerly/mcts-agent](https://github.com/lhemerly/mcts-agent) | Discriminative Monte Carlo Tree Search using TypeSafe Jev System One Primitives and Gemini | 4 | Python | 2026-09-21 |
| [mblode/taste-lint](https://github.com/mblode/taste-lint) | Catch AI slop before you ship. | 4 | TypeScript | 2026-09-21 |
| [mkotlikov/jev-grug](https://github.com/mkotlikov/jev-grug) | Helping JEV speak <3 | 4 | TypeScript | 2026-09-18 |
| [muhammedilyasy/jev-mail](https://github.com/muhammedilyasy/jev-mail) | Chrome extension that triages Gmail with TypeSafe's Jev model: category, priority, spam % and reply % on ever… | 4 | JavaScript | 2026-09-20 |
| [nozomi-koborinai/jev-spec](https://github.com/nozomi-koborinai/jev-spec) | ⚡ Catch spec drift on every commit: check your code against your Markdown specs with TypeSafe AI's Jev model. | 4 | TypeScript | 2026-09-21 |
| [perixtar/jev-e2e](https://github.com/perixtar/jev-e2e) | Natural-language end-to-end tests for web apps, powered by Jev and Playwright. | 4 | TypeScript | 2026-09-19 |
| [Peu77/JevFind](https://github.com/Peu77/JevFind) | Fast semantic code search powered by Jev. Find the relevant files, line ranges, and snippets | 4 | Rust | 2026-09-20 |
| [polarsen-io/padwan-ai](https://github.com/polarsen-io/padwan-ai) | Minimal, provider-agnostic Python client for large language models, built on niquests. | 4 | Python | 2026-09-21 |
| [RahulBalakavi/claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev) | Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks | 4 | Python | 2026-09-19 |
| [raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury) | DiffJury — TypeSafe Jev PR risk router + code review coach | 4 | TypeScript | 2026-09-18 |
| [rupeshpoojary9/poorjev](https://github.com/rupeshpoojary9/poorjev) | Open-source, local Jev alternative: a System One decision layer with provably calibrated confidence (ECE 0.17… | 4 | Python | 2026-09-21 |
| [smartaces/jev-plays-streetfighter-2](https://github.com/smartaces/jev-plays-streetfighter-2) | — | 4 | Python | 2026-09-20 |
| [sugarforever/tryjev](https://github.com/sugarforever/tryjev) | Jev Playground | 4 | Svelte | 2026-09-20 |
| [takkub/agent-takkub](https://github.com/takkub/agent-takkub) | Desktop cockpit for orchestrating Claude Code dev teammates on Windows (PyQt6 + pywinpty + pyte) | 4 | Python | 2026-09-21 |
| [tonyzdev/pijev](https://github.com/tonyzdev/pijev) | PiJev: a terminal coding agent with Jev in the loop — Jev ranks the repository's files before the first call,… | 4 | TypeScript | 2026-09-20 |
| [TypeSafeAI/typesafe-ui](https://github.com/TypeSafeAI/typesafe-ui) | shadcn-style reusable components and blocks for using TypeSafe AI. | 4 | TypeScript | 2026-09-20 |
| [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) | Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibrat… | 4 | Python | 2026-09-19 |
| [y0usaf/typesafe-cli](https://github.com/y0usaf/typesafe-cli) | Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose | 4 | TypeScript | 2026-09-19 |
| [Yasserbhb/conflict-atlas](https://github.com/Yasserbhb/conflict-atlas) | An interactive world map of geopolitical conflicts, genocides, occupations and atrocities from 1490 to today.… | 4 | Python | 2026-09-21 |
| [Yeping-Hu/ai-workshop-tracker](https://github.com/Yeping-Hu/ai-workshop-tracker) | Find AI/ML/Robotics workshop deadlines and search across thousands of accepted papers, all in one place. | 4 | JavaScript | 2026-09-21 |
| [yqlizeao/TCER](https://github.com/yqlizeao/TCER) | Token-to-Code Efficiency Ratio | 4 | Python | 2026-09-21 |
| [yzfly/edgejev](https://github.com/yzfly/edgejev) | 离线可用的本地类型化决策：4 核 CPU 单题 15.6ms。Local & offline Jev / System One inference on CPU — ONNX + INT8, no torch at r… | 4 | Python | 2026-09-21 |
| [zcoder-run/rust-sysone](https://github.com/zcoder-run/rust-sysone) | System One TypeSafe AI Rust Client (unofficial) | 4 | Rust | 2026-09-21 |
| [0x7067/jev-browse](https://github.com/0x7067/jev-browse) | Browser automation with Jev (TypeSafe) as decision model | 3 | JavaScript | 2026-09-20 |
| [a-dev/quizbun](https://github.com/a-dev/quizbun) | Quizbun is a static, explanation-first quiz catalog built around the Quiz Object Standard | 3 | TypeScript | 2026-09-21 |
| [adamnroman/slop-filter](https://github.com/adamnroman/slop-filter) | Chrome extension that hides AI-generated posts and comments on X, LinkedIn, and Reddit. Scored by TypeSafe Je… | 3 | JavaScript | 2026-09-21 |
| [akash-kamat/system-one-gemma](https://github.com/akash-kamat/system-one-gemma) | Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decision… | 3 | Python | 2026-09-18 |
| [antiyro/jevdroid](https://github.com/antiyro/jevdroid) | A typed Python framework for controlling Android over ADB with Jev. | 3 | Python | 2026-09-19 |
| [Bald0Wang/jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh) | Jev 模型（TypeSafe AI）官方使用文档的中文翻译 \| Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — htt… | 3 | Python | 2026-09-21 |
| [baronunread/leanest](https://github.com/baronunread/leanest) | Local-first test selector using Jev judgments to determine which tests are affected by a code change | 3 | TypeScript | 2026-09-21 |
| [buluoray/JevOnly](https://github.com/buluoray/JevOnly) | Pure Jev that can "type" and drive towards task completion. | 3 | Python | 2026-09-21 |
| [casungo/noflow-runtime](https://github.com/casungo/noflow-runtime) | Tired of knowing exactly what your button does? NoFlow lets buttons describe intent and picks from your regis… | 3 | TypeScript | 2026-09-19 |
| [cejor6/kalshi-mcp-server](https://github.com/cejor6/kalshi-mcp-server) | Self-hosted MCP server for Kalshi prediction markets. Native RSA-PSS auth, token-bucket rate limiting, demo/p… | 3 | Python | 2026-09-20 |
| [cheeaun/jevmoji](https://github.com/cheeaun/jevmoji) | Type anything. Get related emojis scored 0–3 with Jev. | 3 | JavaScript | 2026-09-21 |
| [chenmingtang830/jevarena](https://github.com/chenmingtang830/jevarena) | Open-source BYOK arena for Jev and other AI judges. Find failures, compare quality, cost, and latency. | 3 | TypeScript | 2026-09-20 |
| [ChosenXu/newsletter-link-harvester](https://github.com/ChosenXu/newsletter-link-harvester) | Agent Skill: harvest links from newsletter emails into Raindrop.io with the author editorial context attached… | 3 | Python | 2026-09-20 |
| [christian-taillon/opencode-jev-compactor](https://github.com/christian-taillon/opencode-jev-compactor) | Jev powered OpenCode compaction | 3 | TypeScript | 2026-09-20 |
| [ClemensSchartmueller/jev-guard](https://github.com/ClemensSchartmueller/jev-guard) | — | 3 | Go | 2026-09-21 |
| [cobusgreyling/Jev](https://github.com/cobusgreyling/Jev) | Unofficial TypeSafe Jev showcase — System One decisions, not chat. | 3 | Python | 2026-09-20 |
| [codeitlikemiley/typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust) | Rust SDK for the TypeSafe AI API | 3 | Rust | 2026-09-17 |
| [collapseindex/jev-builder](https://github.com/collapseindex/jev-builder) | A browser form for building requests to TypeSafe's Jev: pick a template, fill in the blanks, copy the request… | 3 | JavaScript | 2026-09-20 |
| [dnplus/genio-one](https://github.com/dnplus/genio-one) | The control plane for every AI agent and resource | 3 | TypeScript | 2026-09-21 |
| [eachann1024/pi-jev-reply](https://github.com/eachann1024/pi-jev-reply) | Pi extension: clearer replies via Jev review + optional rewrite/visuals | 3 | TypeScript | 2026-09-20 |
| [EmreKaplaner/rag-jev](https://github.com/EmreKaplaner/rag-jev) | Make room for useful evidence. Inspectable context selection for RAG, with Jev reranking and open benchmark s… | 3 | Python | 2026-09-19 |
| [EugeneBoondock/jevsql](https://github.com/EugeneBoondock/jevsql) | SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by mea… | 3 | JavaScript | 2026-09-19 |
| [ever-just/agentskills](https://github.com/ever-just/agentskills) | Agent skills for Claude Code and other file-reading coding agents — 130+ SKILL.md procedures for deep researc… | 3 | Python | 2026-09-18 |
| [Friedjof/jev-mobile](https://github.com/Friedjof/jev-mobile) | Fast structured Android control loops with TypeSafe Jev and Mobile MCP | 3 | Python | 2026-09-18 |
| [fritzprix/systemone-lite](https://github.com/fritzprix/systemone-lite) | Toy local System One–style decision API (Jev-shaped). Not affiliated with TypeSafe. | 3 | Python | 2026-09-21 |
| [godspede/construct-auto-classifier](https://github.com/godspede/construct-auto-classifier) | Effect-based safety gate for AI coding agents' shell commands (OpenCode, Antigravity): fast structural rules,… | 3 | TypeScript | 2026-09-19 |
| [gudcks0305/jev-java](https://github.com/gudcks0305/jev-java) | Unofficial Java SDK for TypeSafe Jev and Vercel AI Gateway, with Spring Boot and WebClient support | 3 | Java | 2026-09-21 |
| [guybrush1984/purelink](https://github.com/guybrush1984/purelink) | Chrome plugin to highlight AI generated posts | 3 | JavaScript | 2026-09-20 |
| [hndrr/ComfyUI-Jev](https://github.com/hndrr/ComfyUI-Jev) | Jev text interpretation and judgments for ComfyUI. | 3 | Python | 2026-09-20 |
| [iamvatsalpatel/tiershift](https://github.com/iamvatsalpatel/tiershift) | Shift every LLM call to the cheapest model that can handle it. Routing decided by TypeSafe Jev in ~180 ms. No… | 3 | TypeScript | 2026-09-21 |
| [ishantanu/jevmetrics](https://github.com/ishantanu/jevmetrics) | — | 3 | Go | 2026-09-21 |
| [JanOstrowka/typesafe-assist](https://github.com/JanOstrowka/typesafe-assist) | Home Assistant Assist conversation agent powered by TypeSafe's Jev (System One) model | 3 | Python | 2026-09-21 |
| [jcressler/jev-codex-token-saver](https://github.com/jcressler/jev-codex-token-saver) | Experimental Jev evidence selection for token-efficient Codex investigations | 3 | JavaScript | 2026-09-21 |
| [jtnkminimal/awesome-jev](https://github.com/jtnkminimal/awesome-jev) | A curated projects built with Jev, TypeSafe's System One model. | 3 | Python | 2026-09-21 |
| [justrach/folio](https://github.com/justrach/folio) | Architecture for Folio, a Next.js workspace for site readiness, SEO context, and agent evidence reviews. | 3 | TypeScript | 2026-09-19 |
| [jzone3/nice-chat](https://github.com/jzone3/nice-chat) | — | 3 | JavaScript | 2026-09-20 |
| [kenhuangus/jev-usecases](https://github.com/kenhuangus/jev-usecases) | Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic | 3 | Python | 2026-09-21 |
| [kiendle/hophacks-2026](https://github.com/kiendle/hophacks-2026) | — | 3 | Python | 2026-09-20 |
| [koksalkapucuoglu/resume-enhance](https://github.com/koksalkapucuoglu/resume-enhance) | An open-source, AI-powered resume builder designed to craft high-impact resumes. Features smart content enhan… | 3 | Python | 2026-09-20 |
| [konstantinosbotonakis/codex-context-diet](https://github.com/konstantinosbotonakis/codex-context-diet) | Codex plugin: Jev-guided dieting of bulky tool results | 3 | TypeScript | 2026-09-20 |
| [kvnloo/z0intelligence](https://github.com/kvnloo/z0intelligence) | Can we run something like Jev on a 3090 at home? | 3 | Python | 2026-09-21 |
| [kyrylosyzonenko/jev-browse](https://github.com/kyrylosyzonenko/jev-browse) | — | 3 | JavaScript | 2026-09-17 |
| [leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) | Codex plugin: verbatim Jev-guided context restoration around session compaction. Port of tamaratran/fast-jev-… | 3 | TypeScript | 2026-09-19 |
| [Level6me/antigravity-feishu-bot](https://github.com/Level6me/antigravity-feishu-bot) | antigravity可用的飞书插件 | 3 | Python | 2026-09-21 |
| [lynellf/pi-conductor](https://github.com/lynellf/pi-conductor) | — | 3 | TypeScript | 2026-09-21 |
| [maayanlevy/mysql-ailike](https://github.com/maayanlevy/mysql-ailike) | Natural-language row filtering for MySQL, powered by TypeSafe Jev. | 3 | C++ | 2026-09-20 |
| [maxlibin/moomoo-jev-trader](https://github.com/maxlibin/moomoo-jev-trader) | Live Moomoo trading dashboard with TypeSafe Jev market reviews | 3 | Python | 2026-09-20 |
| [milanboers/jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) | Playing Pokemon Red using TypeSafe Jev | 3 | Python | 2026-09-18 |
| [miniLV/Jev-Auto-Router](https://github.com/miniLV/Jev-Auto-Router) | Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local … | 3 | TypeScript | 2026-09-20 |
| [Mintzs/jevify](https://github.com/Mintzs/jevify) | An optimized inference engine to turn LLMs into Jev-like machines: optimized for quick, lightweight, and accu… | 3 | Python | 2026-09-19 |
| [MongLong0214/jev-gate](https://github.com/MongLong0214/jev-gate) | Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prot… | 3 | TypeScript | 2026-09-21 |
| [mstf-svndk/jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice) | Türkçe ve İngilizce doğal konuşmayla Windows 10/11 bilgisayar kontrolü: OpenAI Realtime, local Whisper, Jev, … | 3 | JavaScript | 2026-09-20 |
| [NobleSpartan6/otto](https://github.com/NobleSpartan6/otto) | Open-source native computer use for macOS and Windows: TypeSafe Jev, local OCR, and selective planning. | 3 | TypeScript | 2026-09-20 |
| [nocoo/signoff.now](https://github.com/nocoo/signoff.now) | ✍️ Developer and Git activity analytics | 3 | TypeScript | 2026-09-21 |
| [noetion/dsh-jev](https://github.com/noetion/dsh-jev) | DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers. | 3 | TypeScript | 2026-09-18 |
| [okisdev/claude-code-fusion](https://github.com/okisdev/claude-code-fusion) | Multi-model orchestration for Claude Code: Claude worker tiers plus the Codex and Grok CLIs as peer engineers | 3 | JavaScript | 2026-09-20 |
| [Olti1947/jev-java](https://github.com/Olti1947/jev-java) | Idiomatic Java SDK for TypeSafe AI Jev System One decision engine | 3 | Java | 2026-09-20 |
| [ozkannceylan/rag-configurator](https://github.com/ozkannceylan/rag-configurator) | A low-code platform for building and deploying custom RAG pipelines through a visual interface. | 3 | Python | 2026-09-21 |
| [paulsmith/computer-use-jev](https://github.com/paulsmith/computer-use-jev) | macOS computer use driven by Jev (TypeSafe System One) as the decision maker | 3 | Go | 2026-09-17 |
| [Pinutss/jev-model-router](https://github.com/Pinutss/jev-model-router) | Route among multiple LLMs and multi-model provider keys without leaking secrets. | 3 | Python | 2026-09-18 |
| [Premo-Cloud/typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java) | Community Java client for the TypeSafe System One API (unofficial) | 3 | Java | 2026-09-21 |
| [qtnx/omppp](https://github.com/qtnx/omppp) | OMP++ | 3 | TypeScript | 2026-09-21 |
| [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study) | Independent Jev 1.13.0 behavior study: report, controlled prompt experiments, raw results, and offline verifi… | 3 | Python | 2026-09-17 |
| [samat2003/mini-Jev](https://github.com/samat2003/mini-Jev) | — | 3 | Python | 2026-09-21 |
| [SamuelSacco/jev-exploration](https://github.com/SamuelSacco/jev-exploration) | Jev (TypeSafe) exploratory thread: claim audit, live demos, and runnable code | 3 | Python | 2026-09-21 |
| [SaratAngajalaoffl/jeeva](https://github.com/SaratAngajalaoffl/jeeva) | Modular trading framework for Mid-Frequency Trading | 3 | TypeScript | 2026-09-21 |
| [satviksinha/jev-model-router](https://github.com/satviksinha/jev-model-router) | Model router for Claude Code using Jev | 3 | TypeScript | 2026-09-21 |
| [sd109/typesafe-go](https://github.com/sd109/typesafe-go) | A collection of typesafe.ai API utilities | 3 | Go | 2026-09-20 |
| [SeeAPI/awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases) | Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model … | 3 | Python | 2026-09-20 |
| [sgaabdu4/capture](https://github.com/sgaabdu4/capture) | Private Mac voice diary: local Parakeet transcription, Jev sorting, Notion library | 3 | Dart | 2026-09-21 |
| [shamazharikh/qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd) | Jev-style calibrated decision model (Choice/Score/Noul) on Qwen3.5-0.8B | 3 | Python | 2026-09-17 |
| [ShuhanSun/jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel) | Catch breaking API behavior hidden in OpenAPI prose with deterministic checks and TypeSafe JEV System One sem… | 3 | Python | 2026-09-20 |
| [smithclay/dbt_jev](https://github.com/smithclay/dbt_jev) | use jev in dbt | 3 | Python | 2026-09-21 |
| [sriinnu/kosha-discovery](https://github.com/sriinnu/kosha-discovery) | Discovery registry for AI models, credentials, and pricing across local and cloud providers. Library, CLI, an… | 3 | TypeScript | 2026-09-19 |
| [stardeckai/lgtm](https://github.com/stardeckai/lgtm) | Prove that your tests actually test something. Powered by Jev and your own API Key. | 3 | TypeScript | 2026-09-21 |
| [Stumble/jev-go](https://github.com/Stumble/jev-go) | Community Go SDK for TypeSafe AI Jev / System One | 3 | Go | 2026-09-18 |
| [SuperInstance/AI-Writings](https://github.com/SuperInstance/AI-Writings) | Creative writing, essays, and philosophical explorations from the Exocortex project | 3 | HTML | 2026-09-21 |
| [teempai/jev-in-codex](https://github.com/teempai/jev-in-codex) | Jev-powered tool and skill selection, context search, and output triage for Codex via MCP | 3 | TypeScript | 2026-09-21 |
| [theodorexli/Caret](https://github.com/theodorexli/Caret) | Cursor tab-style completion in every app, aware of who you are, what you’ve been doing, and capable of using … | 3 | Swift | 2026-09-20 |
| [thisyearnofear/VOISSS](https://github.com/thisyearnofear/VOISSS) | next-generation decentralized voice recording platform that transforms how we capture, organize, and share au… | 3 | TypeScript | 2026-09-20 |
| [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip) | YouTube sponsor skipper that reads the captions and decides at watch time: a probability heatmap on the seek … | 3 | TypeScript | 2026-09-19 |
| [valentynkit/jev.nvim](https://github.com/valentynkit/jev.nvim) | Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, pro… | 3 | Lua | 2026-09-19 |
| [virolea/jev](https://github.com/virolea/jev) | Ruby client for the typesafe AI Jev model | 3 | Ruby | 2026-09-20 |
| [woduseh/Uimori](https://github.com/woduseh/Uimori) | — | 3 | TypeScript | 2026-09-21 |
| [wolvesdotink/owlat](https://github.com/wolvesdotink/owlat) | Self-hosted, modular email platform: marketing campaigns, team inbox, personal mailbox, and an AI agent, gate… | 3 | TypeScript | 2026-09-21 |
| [Xubqpanda/JevRepo](https://github.com/Xubqpanda/JevRepo) | — | 3 | Python | 2026-09-21 |
| [yohanargentina-oss/Foq](https://github.com/yohanargentina-oss/Foq) | ⚡ Foq — the FREE, local, open-source alternative to Jev. Typed System 1 decisions in ~25 ms — no waitlist, no… | 3 | Python | 2026-09-20 |
| [zhangxaochen/dsh-jev](https://github.com/zhangxaochen/dsh-jev) | Jev (System One decision model) plugin suite for DeepSeek Harness (dsh) | 3 | TypeScript | 2026-09-21 |
| [Zoverions/AXIOM-MESH](https://github.com/Zoverions/AXIOM-MESH) | AXIOM Mesh 0.12.0-dev.3: local-first, fail-closed coordination substrate for human and machine principals, wi… | 3 | JavaScript | 2026-09-21 |
| [0xtrou/rubikjev](https://github.com/0xtrou/rubikjev) | Challenge the Jev's intelligence in Rubik Cube puzzles | 2 | TypeScript | 2026-09-20 |
| [0xtrou/yggdrasight](https://github.com/0xtrou/yggdrasight) | Inteligence crypto currency terminal | 2 | TypeScript | 2026-09-17 |
| [2389-research/typesafe-go](https://github.com/2389-research/typesafe-go) | A Go client for the TypeSafe System One API — typed judgments and probabilities, zero dependencies outside th… | 2 | Go | 2026-09-19 |
| [24601/rh-guard](https://github.com/24601/rh-guard) | Reward-hack radar for coding agents: structural denies + TypeSafe Jev System One sidecar for Claude Code & Cu… | 2 | TypeScript | 2026-09-21 |
| [455-dIAO/windows-save-token-jev-setup](https://github.com/455-dIAO/windows-save-token-jev-setup) | Windows Codex Skill：通过 npx 或 Git 安装，安全配置 save-token-jev 的 PreCompact/SessionStart Hooks，并提供信任、原生压缩与旧内容隔离验证。 | 2 | PowerShell | 2026-09-21 |
| [4anti/jev-broadcast-lab](https://github.com/4anti/jev-broadcast-lab) | Testing Lab for Jev AI | 2 | JavaScript | 2026-09-20 |
| [7155/personal-agent-workbench](https://github.com/7155/personal-agent-workbench) | Local-first personal agent workbench with Rooms, tools, governed memory, and optional input, voice, and brows… | 2 | Python | 2026-09-20 |
| [aadhil-kh/jevx](https://github.com/aadhil-kh/jevx) | Jev-powered Chrome extension that categorizes X posts and classifies replies in context. | 2 | JavaScript | 2026-09-20 |
| [abhishekmamdapure/jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction) | Parsing the PDF and extracting the relevant information | 2 | Python | 2026-09-21 |
| [abhixhek/feedwall](https://github.com/abhixhek/feedwall) | Your feed, your rules, in plain English. A browser extension that filters X, YouTube, Reddit, LinkedIn and Ha… | 2 | JavaScript | 2026-09-19 |
| [aibangjuxin/knowledge](https://github.com/aibangjuxin/knowledge) | My knowledge | 2 | HTML | 2026-09-21 |
| [AkashPriyadarshii/jev-git](https://github.com/AkashPriyadarshii/jev-git) | Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev | 2 | Rust | 2026-09-21 |
| [AkashPriyadarshii/jev-scout](https://github.com/AkashPriyadarshii/jev-scout) | Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring | 2 | Rust | 2026-09-21 |
| [alexsatch/omp-auto-mode](https://github.com/alexsatch/omp-auto-mode) | Plugin for oh-my-pi that uses Typesafe Jev API to classify tool calls as safe/unsafe/ask | 2 | TypeScript | 2026-09-19 |
| [Amrit-Nigam/jev-royal](https://github.com/Amrit-Nigam/jev-royal) | — | 2 | TypeScript | 2026-09-18 |
| [andrueandersoncs/jev-semantic-linter](https://github.com/andrueandersoncs/jev-semantic-linter) | — | 2 | TypeScript | 2026-09-18 |
| [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) | Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducib… | 2 | Python | 2026-09-19 |
| [AppSprout-dev/Unsga3](https://github.com/AppSprout-dev/Unsga3) | U-NSGA-III multi-objective evolutionary optimization for .NET (Seada & Deb) — ZDT/DTLZ, IGD oracle vs pymoo | 2 | C# | 2026-09-19 |
| [ariel-frischer/jevkit](https://github.com/ariel-frischer/jevkit) | Fast Rust CLI for TypeSafe Jev: typed decisions, offline linting before you pay | 2 | Rust | 2026-09-19 |
| [Aryan2624/Aryan2624](https://github.com/Aryan2624/Aryan2624) | # Hi, I'm Aryan Dubey 👋 ## B.Tech AI & ML Student Building Intelligent Systems, One Model at a Time | 2 | — | 2026-09-16 |
| [bensyverson/goodall](https://github.com/bensyverson/goodall) | A simple and extensible agent loop for Golang projects | 2 | Go | 2026-09-18 |
| [bojansandhaus/jev-decisions](https://github.com/bojansandhaus/jev-decisions) | Jev Decisions Plugin for Hermes (and other AI Agents): tool risk reviews, human approval recommendations, evi… | 2 | Python | 2026-09-20 |
| [brnyxx/jev-ra](https://github.com/brnyxx/jev-ra) | Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every ste… | 2 | Python | 2026-09-21 |
| [Charlyhno-eng/jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot) | A Codex overlay incorporating JEV to make the best decisions regarding model selection and depth of reasoning… | 2 | TypeScript | 2026-09-20 |
| [Charlyhno-eng/jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification) | JEV Document Classification enables the rapid and cost-effective classification of text-based documents using… | 2 | TypeScript | 2026-09-19 |
| [chat-prompt/gpters-ai-toolkit](https://github.com/chat-prompt/gpters-ai-toolkit) | GPTers AI Toolkit - Skills, Agents, and Prompts Catalog for Claude Code | 2 | TypeScript | 2026-09-21 |
| [chris-wozniczek/jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control) | Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-… | 2 | Swift | 2026-09-21 |
| [coco-research/jev-use](https://github.com/coco-research/jev-use) | Voice-driven control layer for macOS. Jev is the fallback, not the router. Rust core, Tauri shell. | 2 | Rust | 2026-09-21 |
| [codefionn/llmleaf](https://github.com/codefionn/llmleaf) | A fast llm proxy | 2 | Rust | 2026-09-20 |
| [coo-quack/jev-pii-checker](https://github.com/coo-quack/jev-pii-checker) | CLI that finds PII in text with TypeSafe Jev: presence, sensitivity, and located spans | 2 | TypeScript | 2026-09-20 |
| [croll83/jarvis](https://github.com/croll83/jarvis) | AI driven smart home | 2 | Python | 2026-09-21 |
| [CrowdLinker/JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach) | Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improvin… | 2 | TypeScript | 2026-09-20 |
| [Devonance/rover-claude-jev-demo](https://github.com/Devonance/rover-claude-jev-demo) | Just a weekend project with Claude as system two, and Jev as system One. | 2 | JavaScript | 2026-09-21 |
| [Dimesio/typesafe-chess](https://github.com/Dimesio/typesafe-chess) | FUn little experiment with Typesafe AI Jev Model playing chess against stockfish :) | 2 | JavaScript | 2026-09-20 |
| [drewling/zero](https://github.com/drewling/zero) | Keep every Gmail inbox at only what still needs you — reversibly. A macOS menu-bar app: agent-judged open loo… | 2 | Python | 2026-09-20 |
| [droid-Q/jev-skill-router](https://github.com/droid-Q/jev-skill-router) | — | 2 | JavaScript | 2026-09-19 |
| [dwamianm/prism](https://github.com/dwamianm/prism) | Portable Relational Memory Engine — local-first memory substrate for LLM-powered systems | 2 | Python | 2026-09-19 |
| [elpumberto/barrunto](https://github.com/elpumberto/barrunto) | A Chrome extension that brings TypeSafe's Jev to X.com to analyze posts as you browse | 2 | TypeScript | 2026-09-20 |
| [embwl0x/native-agent](https://github.com/embwl0x/native-agent) | A Swift-native macOS and iOS personal agent runtime. | 2 | Swift | 2026-09-20 |
| [enovikov11/tigor-ai](https://github.com/enovikov11/tigor-ai) | Personal AI monorepo | 2 | Jupyter Notebook | 2026-09-21 |
| [ferraroroberto/local-llm-hub](https://github.com/ferraroroberto/local-llm-hub) | playground to use different local LLM models as a API hub | 2 | Python | 2026-09-21 |
| [FindMalek/guesswork](https://github.com/FindMalek/guesswork) | Fish-style zsh history autosuggestions, ranked by an AI model instead of prefix matching | 2 | TypeScript | 2026-09-21 |
| [FirasSX914/Janus](https://github.com/FirasSX914/Janus) | Measure when to use Jev and other models on your data, then route accordingly. | 2 | Python | 2026-09-18 |
| [geocine/geocine-pi](https://github.com/geocine/geocine-pi) | Local-first control layer for Pi. TypeSafe routes tasks, manages cache-aware model leases, gates bounded spec… | 2 | TypeScript | 2026-09-18 |
| [geofffranks/polytoken-quota](https://github.com/geofffranks/polytoken-quota) | — | 2 | Go | 2026-09-20 |
| [gholtzap/jev-codex-model-and-effort-router](https://github.com/gholtzap/jev-codex-model-and-effort-router) | — | 2 | Python | 2026-09-20 |
| [glamboyosa/docket](https://github.com/glamboyosa/docket) | A Go TUI that uses Jev to classify documents, assess sensitivity and urgency, and determine whether action is… | 2 | Go | 2026-09-20 |
| [guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector) | Conservative CI task selection for GitHub Actions with Jev, a pure policy engine, and shadow mode by default. | 2 | TypeScript | 2026-09-21 |
| [hamakyo/jev-starter](https://github.com/hamakyo/jev-starter) | Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation,… | 2 | TypeScript | 2026-09-18 |
| [Hawxy/TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) | .NET SDK for the TypeSafe AI platform | 2 | C# | 2026-09-19 |
| [hellogumbo/should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all) | We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actua… | 2 | JavaScript | 2026-09-18 |
| [hemanth/jev-chess](https://github.com/hemanth/jev-chess) | Chess moves, evaluations, persona opponents, and game classification with TypeSafe AI System One | 2 | TypeScript | 2026-09-21 |
| [IAnMove/jev-game-agent](https://github.com/IAnMove/jev-game-agent) | Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your o… | 2 | Python | 2026-09-18 |
| [ibrahemid/git-jev-stage](https://github.com/ibrahemid/git-jev-stage) | Select Git changes for staging with a plain-language description. | 2 | TypeScript | 2026-09-20 |
| [ibrahemid/jevprune](https://github.com/ibrahemid/jevprune) | Filter command output for coding agents using a task description. | 2 | TypeScript | 2026-09-20 |
| [imrishit98/jev.aitools.fyi](https://github.com/imrishit98/jev.aitools.fyi) | Jev is all the rage right now and this directory lists all things Jev! Docs, SDKs, and the full tool map one … | 2 | TypeScript | 2026-09-21 |
| [innocentdiaz/s1_ruby](https://github.com/innocentdiaz/s1_ruby) | Makes S1-model 'measurement' (and the collapse that follows it) a Ruby primitive. | 2 | Ruby | 2026-09-21 |
| [inteligenciamilgrau/jevstudio](https://github.com/inteligenciamilgrau/jevstudio) | Jev Studio para criar programas usando Jev da TypeSafe | 2 | Python | 2026-09-20 |
| [ItisShikhar/gg-friggin-ez](https://github.com/ItisShikhar/gg-friggin-ez) | Fast, drop-in profanity and toxicity screener for Node.js, powered by TypeSafe AI Jev. Catches leetspeak, cha… | 2 | TypeScript | 2026-09-20 |
| [javiersaguar/HS-Maisa](https://github.com/javiersaguar/HS-Maisa) | — | 2 | Python | 2026-09-20 |
| [jb2197/pydantic-jev](https://github.com/jb2197/pydantic-jev) | A thin shim between Pydantic and Jev. | 2 | Python | 2026-09-18 |
| [jevbook/jevscan](https://github.com/jevbook/jevscan) | Typed onchain verdicts for EVM tokens: ape / watch /avoid with calibrated probabilities. CLI + library +MCP s… | 2 | JavaScript | 2026-09-19 |
| [jexp/watfile](https://github.com/jexp/watfile) | Text/PDF - File categorization and sorting with Typesafe AI Jev or local calibrated decision model | 2 | Python | 2026-09-21 |
| [jkrup/jeveryword](https://github.com/jkrup/jeveryword) | Text extraction with Jev: field extraction, PII detection and exact quotes, built on TypeSafe's Jev. | 2 | JavaScript | 2026-09-20 |
| [jsagir/mindrian-os-plugin](https://github.com/jsagir/mindrian-os-plugin) | The AI co-founder that pushes back. Bring a real problem worth solving and it reframes what you are actually … | 2 | JavaScript | 2026-09-17 |
| [jtsang4/jev-cli](https://github.com/jtsang4/jev-cli) | CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out | 2 | TypeScript | 2026-09-18 |
| [Justmalhar/awesome-jev-apps](https://github.com/Justmalhar/awesome-jev-apps) | Awesome Collection of apps built with Jev - a System One model | 2 | Python | 2026-09-19 |
| [KamilPostrozny/pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction) | Fast JEV compaction extension for pi | 2 | TypeScript | 2026-09-20 |
| [kbitgood/jev-cdp](https://github.com/kbitgood/jev-cdp) | A small Jev-powered bridge to Chrome through the Chrome DevTools Protocol. | 2 | TypeScript | 2026-09-18 |
| [kindintelligence/jev-rust-review](https://github.com/kindintelligence/jev-rust-review) | Rust-aware code review for Claude Code and coding agents, powered by TypeSafe Jev | 2 | Rust | 2026-09-20 |
| [kitze/pagegrade](https://github.com/kitze/pagegrade) | Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev. | 2 | TypeScript | 2026-09-18 |
| [kotoba-lang/typed-decisions](https://github.com/kotoba-lang/typed-decisions) | Jev-shaped typed-decision model (state + Choice/Score/Noul questions -> calibrated probabilities, one pass) o… | 2 | Python | 2026-09-21 |
| [krimvp/goaly](https://github.com/krimvp/goaly) | Deterministic goal cli for your harness | 2 | TypeScript | 2026-09-17 |
| [kuhung/understanding-jev](https://github.com/kuhung/understanding-jev) | 深入解读 Jev 模型：毫秒级判定与工程边界 | 2 | HTML | 2026-09-19 |
| [liao96312/jev-arena-nanojev](https://github.com/liao96312/jev-arena-nanojev) | 完全本地的 NanoJev 网格决策游戏实验场，支持中文 Pygame、多关卡与 GTX 1660S 训练 | 2 | Python | 2026-09-21 |
| [lithdew/hands](https://github.com/lithdew/hands) | General Learning Hacks 2026 (1st place) | 2 | TypeScript | 2026-09-21 |
| [lmvdz/rpg-jev](https://github.com/lmvdz/rpg-jev) | A living-world RPG whose NPCs are decided by TypeSafe's Jev judge model; code owns rules, numbers and state. | 2 | TypeScript | 2026-09-20 |
| [luxus/ha-conversation-jev](https://github.com/luxus/ha-conversation-jev) | Home Assistant custom component: Conversation agent with Jev fast-path + Grok fallback | 2 | Python | 2026-09-19 |
| [maruthiprithivi/break-free](https://github.com/maruthiprithivi/break-free) | — | 2 | TypeScript | 2026-09-21 |
| [masa-med-ai/typesafe-screening-mcp](https://github.com/masa-med-ai/typesafe-screening-mcp) | MCP server: screen PubMed titles/abstracts against a query or clinical question with TypeSafe Jev | 2 | Python | 2026-09-19 |
| [mastwet/dsh-fast-jev-compaction](https://github.com/mastwet/dsh-fast-jev-compaction) | fast-jev-compaction dsh插件 | 2 | JavaScript | 2026-09-20 |
| [MaTriXy/Monkey.D.Loopy](https://github.com/MaTriXy/Monkey.D.Loopy) | Factory for runnable, crash-resumable agent loops. | 2 | TypeScript | 2026-09-17 |
| [memarino92/AgentPlayground](https://github.com/memarino92/AgentPlayground) | An agentic digital garden for exploring new tools and techniques for working with AI. | 2 | C# | 2026-09-21 |
| [memovai/openevals](https://github.com/memovai/openevals) | Fast and cheap agent evals. jev as judge. | 2 | TypeScript | 2026-09-20 |
| [merefield/clai](https://github.com/merefield/clai) | A command line ai helper | 2 | Go | 2026-09-20 |
| [molis-ai/jev-workbench](https://github.com/molis-ai/jev-workbench) | Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your bac… | 2 | TypeScript | 2026-09-18 |
| [morcoan/JMP](https://github.com/morcoan/JMP) | JMP — Joint Model Participation. A local coding workspace where Jev routes actions and OpenAI, DeepSeek, or l… | 2 | Python | 2026-09-20 |
| [Mrlyk/jev-browser](https://github.com/Mrlyk/jev-browser) | Browser automation CLI for AI agents, powered by the Jev model's millisecond decisions and near-zero inferenc… | 2 | Rust | 2026-09-21 |
| [n3ndor/n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev) | n8n community node for TypeSafe Jev structured AI decisions | 2 | TypeScript | 2026-09-19 |
| [Nachom3/jevTrader](https://github.com/Nachom3/jevTrader) | A High Frecuncy Trader made in Rust using Jev as a decision maker. | 2 | Rust | 2026-09-20 |
| [Nainish-Rai/jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa) | Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo. | 2 | Python | 2026-09-18 |
| [NAlexPear/scruple](https://github.com/NAlexPear/scruple) | Semantic-aware linting for enforcing taste | 2 | TypeScript | 2026-09-21 |
| [newuser7171/antivirus](https://github.com/newuser7171/antivirus) | — | 2 | Python | 2026-09-20 |
| [noripto/pigeonhole](https://github.com/noripto/pigeonhole) | Classify notes with Jev and file them into folders by attribute. | 2 | TypeScript | 2026-09-21 |
| [nshkrdotcom/system_one_sdk](https://github.com/nshkrdotcom/system_one_sdk) | Provider-neutral Elixir/BEAM SDK for System One semantics: typed Noul, Choice and Score decisions, prepared e… | 2 | Elixir | 2026-09-21 |
| [omkarghugarkar007/actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev) | Open-source Jev tool-calling authorization gateway for AI agents: deterministic policy, exact-action single-u… | 2 | TypeScript | 2026-09-20 |
| [open-gsd/gsd-path](https://github.com/open-gsd/gsd-path) | Disk-backed pipeline that takes AI coding agents from raw idea to shipped code — gated phases, orchestrated s… | 2 | Python | 2026-09-21 |
| [overfit-lab/OpenJev](https://github.com/overfit-lab/OpenJev) | — | 2 | Python | 2026-09-20 |
| [oxwen11/awesome-jev](https://github.com/oxwen11/awesome-jev) | A curated list of what people built with Jev | 2 | — | 2026-09-21 |
| [pCwOrM/werr](https://github.com/pCwOrM/werr) | A 0-byte memory alternative to LLMs. Ultra-fast, type-safe System-1 decision engine powered by Mandelbrot wav… | 2 | Python | 2026-09-21 |
| [phureewat29/jev-got](https://github.com/phureewat29/jev-got) | Jev (TypeSafe AI) PoC through Game of Thrones | 2 | TypeScript | 2026-09-19 |
| [PIGU-PPPgu/edupi-desktop](https://github.com/PIGU-PPPgu/edupi-desktop) | EduPi teacher agent desktop | 2 | TypeScript | 2026-09-21 |
| [PingpowerTW/7-Phase-Agentic-Workflow](https://github.com/PingpowerTW/7-Phase-Agentic-Workflow) | 「整合 Spec-Driven Development 與 Karpathy 的精準開刀原則，建立完整的 Phase 0-6 協作架構。並導入 Rule #8 Token 經濟學，結合 /teamwork 多代理人品質… | 2 | Python | 2026-09-20 |
| [prateekmedia/ly](https://github.com/prateekmedia/ly) | Manipulate images via chat, uses Jev like model to classify prompt | 2 | JavaScript | 2026-09-19 |
| [Programalyst/realtime-vision-decision-agent](https://github.com/Programalyst/realtime-vision-decision-agent) | Combining YOLO and Jev models to play a mobile game. | 2 | Jupyter Notebook | 2026-09-21 |
| [pulkitxm/jev-chess-agent](https://github.com/pulkitxm/jev-chess-agent) | A chess bot opponent player with typed move selection and browser controls | 2 | JavaScript | 2026-09-20 |
| [Ravinder82/jev-flash-router](https://github.com/Ravinder82/jev-flash-router) | open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model. AI coding agents waste hundreds of… | 2 | TypeScript | 2026-09-20 |
| [replynodes/jev-web-analyzer](https://github.com/replynodes/jev-web-analyzer) | See what Jev thinks about your SaaS website — powered by ReplyNodes web context and Vercel AI Gateway. | 2 | TypeScript | 2026-09-21 |
| [RevocGG/typesafe-jev-bridge](https://github.com/RevocGG/typesafe-jev-bridge) | Use the TypeSafe Jev decision model (System One) anywhere: zero-dependency OpenAI-compatible bridge for 9Rout… | 2 | JavaScript | 2026-09-21 |
| [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) | Open auto mode for AI agents — a calibrated tool-call firewall powered by TypeSafe Jev. Ships as a Claude Cod… | 2 | TypeScript | 2026-09-20 |
| [rizafahmi/pi-jev-task-router](https://github.com/rizafahmi/pi-jev-task-router) | Per-prompt model routing for the Pi coding agent: classify each prompt with Jev, pick a model tier, and switc… | 2 | TypeScript | 2026-09-21 |
| [Roberdan/roberdan-os](https://github.com/Roberdan/roberdan-os) | Copilot CLI-first workflows for AI agents: shared instructions, reusable skills, multi-model delegation, huma… | 2 | Shell | 2026-09-20 |
| [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) | A curated list of resources for Jev — TypeSafe AI's System One decision model. Maintained by RoboKrunch. | 2 | — | 2026-09-21 |
| [rorshopping/jev-browser-local](https://github.com/rorshopping/jev-browser-local) | Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, mea… | 2 | Python | 2026-09-19 |
| [Saik0s/diffusiongemma-jev-macos](https://github.com/Saik0s/diffusiongemma-jev-macos) | Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples. | 2 | Python | 2026-09-19 |
| [savka777/jev-search](https://github.com/savka777/jev-search) | Fast deep research for the pi coding agent: reads up to 100 pages in full per round, Jev keeps only the passa… | 2 | TypeScript | 2026-09-20 |
| [ShahriarBijoy/eslint-plugin-jev](https://github.com/ShahriarBijoy/eslint-plugin-jev) | Today's linters read the shape of your code. This one would read what it means. | 2 | TypeScript | 2026-09-20 |
| [shashwtd/catanova](https://github.com/shashwtd/catanova) | An open-source Catan-style game focused on reliable multiplayer and a richly illustrated board. | 2 | TypeScript | 2026-09-20 |
| [sifrious/molly](https://github.com/sifrious/molly) | Local AI coding tasks for Laravel, with Pest verification and visible complexity review. | 2 | PHP | 2026-09-21 |
| [sightmap/jev-turbo](https://github.com/sightmap/jev-turbo) | Jev-powered semantic browser use | 2 | Go | 2026-09-20 |
| [simota/tenbin](https://github.com/simota/tenbin) | MCP server and agent skill for the TypeSafe AI System One API (Jev): decompose a judgment into Choice / Score… | 2 | TypeScript | 2026-09-21 |
| [simxnherrera/jevr](https://github.com/simxnherrera/jevr) | A native R client for Jev System 1 model decisions | 2 | R | 2026-09-20 |
| [Skyvern-AI/destroy-email-spam](https://github.com/Skyvern-AI/destroy-email-spam) | Gmail triage with Jev: flag urgent mail and archive cold pitches using Google Apps Script. | 2 | JavaScript | 2026-09-19 |
| [stanprokopenko/skell-e-router](https://github.com/stanprokopenko/skell-e-router) | Simple AI router using LiteLLM. | 2 | Python | 2026-09-21 |
| [superradcompany/multiverse-of-madness](https://github.com/superradcompany/multiverse-of-madness) | Jev and Microsandbox explore alternate game futures with a reusable TypeScript learning harness | 2 | TypeScript | 2026-09-19 |
| [tanayvasishtha/Slither-Me-Jev](https://github.com/tanayvasishtha/Slither-Me-Jev) | 8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time | 2 | JavaScript | 2026-09-20 |
| [TheOnlyArtz/TheOnlyArtz.github.io](https://github.com/TheOnlyArtz/TheOnlyArtz.github.io) | ג'ב — יועצת בחירת מפלגה. Hebrew/RTL React app ranking the 14 Knesset-26 lists against your ideology. | 2 | JavaScript | 2026-09-18 |
| [tu11aa/squadrant](https://github.com/tu11aa/squadrant) | Multi-project agent orchestration for Claude Code. One command session controls everything. | 2 | TypeScript | 2026-09-21 |
| [turbobeest/modelspec](https://github.com/turbobeest/modelspec) | — | 2 | Python | 2026-09-20 |
| [tylerjharden/ailerix](https://github.com/tylerjharden/ailerix) | Type-safe model router. Jev (System One) banks each request to a typed catalog route. | 2 | TypeScript | 2026-09-20 |
| [typakon4/jev-layer](https://github.com/typakon4/jev-layer) | Portable System-1 decision layer for agent harnesses with host-owned routing, receipts, replay, and fail-open… | 2 | JavaScript | 2026-09-21 |
| [TypeSafeAI/clarity-judge](https://github.com/TypeSafeAI/clarity-judge) | Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its o… | 2 | TypeScript | 2026-09-21 |
| [undeemed/Jcyber](https://github.com/undeemed/Jcyber) | Agent-driven bug bounty / pentest framework: one gated chain over five systems (Caido, HexStrike, Jev, Memgra… | 2 | Python | 2026-09-21 |
| [unownone/jevsume](https://github.com/unownone/jevsume) | ATS-friendly resume review powered by Jev (TypeSafe System One). The frontend extracts resume text the way a … | 2 | TypeScript | 2026-09-21 |
| [VakeDomen/DIY-Jev](https://github.com/VakeDomen/DIY-Jev) | — | 2 | Rust | 2026-09-21 |
| [VladyslavHontar/clear-head](https://github.com/VladyslavHontar/clear-head) | Claude Code Stop hook that checks an AI assistant's claims against what it actually read this session, using … | 2 | Python | 2026-09-19 |
| [wodsmith/thewodapp](https://github.com/wodsmith/thewodapp) | — | 2 | TypeScript | 2026-09-21 |
| [XyraSinclair/llmsort](https://github.com/XyraSinclair/llmsort) | Score a list by any fuzzy attribute with an LLM judge: pairwise ratio questions fitted into consistent scores… | 2 | Rust | 2026-09-20 |
| [y9Finsi/jev-mcp](https://github.com/y9Finsi/jev-mcp) | — | 2 | JavaScript | 2026-09-21 |
| [zdenham/jev-lint](https://github.com/zdenham/jev-lint) | Lint JavaScript and TypeScript against plain-English project conventions with Jev. | 2 | TypeScript | 2026-09-20 |
| [zkjoie/jevbus](https://github.com/zkjoie/jevbus) | A streaming event bus whose routing, subscription and consumption are decided by a probabilistic judge. The r… | 2 | Rust | 2026-09-21 |
| [207studio/jev-codex-tools](https://github.com/207studio/jev-codex-tools) | Experimental opt-in Jev decision tools for bounded Codex session reading and guarded UI workflows. | 1 | JavaScript | 2026-09-20 |
| [4esv/jev-eval](https://github.com/4esv/jev-eval) | Benchmark TypeSafe Jev against any OpenRouter model on your own labelled classification data: accuracy, calib… | 1 | Python | 2026-09-21 |
| [a-Fig/jev-score](https://github.com/a-Fig/jev-score) | Local-first document evaluation workspaces powered by Jev | 1 | JavaScript | 2026-09-21 |
| [aashishpahwa/instagram-reel-transcriber](https://github.com/aashishpahwa/instagram-reel-transcriber) | Free, self-hosted Instagram Reel transcriber — download Reels, transcribe them locally with Whisper, and see … | 1 | Python | 2026-09-21 |
| [acoyfellow/nightglass](https://github.com/acoyfellow/nightglass) | Owned, deterministic classifier for checking whether agent claims are supported by evidence, with optional Je… | 1 | JavaScript | 2026-09-19 |
| [Acurioustractor/grantscope](https://github.com/Acurioustractor/grantscope) | Open-source Australian funding transparency platform — government grants, philanthropic foundations, corporat… | 1 | TypeScript | 2026-09-21 |
| [ady95/jev_tutorial](https://github.com/ady95/jev_tutorial) | — | 1 | Python | 2026-09-21 |
| [afurm/typesafe-sdk-ruby](https://github.com/afurm/typesafe-sdk-ruby) | Unofficial Ruby SDK for the TypeSafe AI API (Jev model) - typed questions, retries, and typed errors. Communi… | 1 | Ruby | 2026-09-21 |
| [agent-chaperone/agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) | Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy p… | 1 | TypeScript | 2026-09-21 |
| [ajmeese7/hdd-analyzer](https://github.com/ajmeese7/hdd-analyzer) | Use Jev to quickly search your old hard drives and identify anything of value. | 1 | Python | 2026-09-20 |
| [albri/nxk](https://github.com/albri/nxk) | Your agent can't ask people what they think. nxk gives it a crowd to ask. | 1 | JavaScript | 2026-09-21 |
| [alee792/robojev](https://github.com/alee792/robojev) | Natural-language control of a WidowX AI arm with Jev typed judgments (Doom-style loop) | 1 | Python | 2026-09-18 |
| [AleksaZCodes/fiducial](https://github.com/AleksaZCodes/fiducial) | Declare each fact once. Derive every artifact from it. | 1 | Rust | 2026-09-21 |
| [alexkarpandrus/tickettrain](https://github.com/alexkarpandrus/tickettrain) | Provider-neutral ticket tool (ttt) linking change requests to tracker issues | 1 | Clojure | 2026-09-21 |
| [alperenerol/jev-1.13-mini-benchmark](https://github.com/alperenerol/jev-1.13-mini-benchmark) | Mini benchmark of TypeSafe's jev-1.13 structured decision model (OpenRouter Decisions API) on labeled support… | 1 | Python | 2026-09-21 |
| [alsoleg89/decide](https://github.com/alsoleg89/decide) | Bulk decisions for AI agents. Jev classifies files and logs; your agent reviews exceptions. Reproducible cost… | 1 | Python | 2026-09-20 |
| [altqx/honya](https://github.com/altqx/honya) | A calm, literary Ratatui terminal app for AI-assisted Japanese to Thai light-novel translation. | 1 | Rust | 2026-09-21 |
| [amishah1998/said-done](https://github.com/amishah1998/said-done) | Report card for your AI coding agent: grades every Claude Code session on disk with Jev, cheaply | 1 | JavaScript | 2026-09-20 |
| [anderescaray/every-hackspain](https://github.com/anderescaray/every-hackspain) | Score de salud financiera explicable con trayectoria, Cash Truth y optimizador de tesorería para grupos empre… | 1 | Python | 2026-09-20 |
| [andragon3110/laya-mcp](https://github.com/andragon3110/laya-mcp) | MCP server exposing Laya's typed-decision tools to coding agents. Optional, self-hosted, 7x faster than Jev. | 1 | Python | 2026-09-21 |
| [andrei10k/claude-jev-model-router](https://github.com/andrei10k/claude-jev-model-router) | A local proxy that sits between Claude Code and the Anthropic API and uses TypeSafe's Jev to route each subag… | 1 | TypeScript | 2026-09-21 |
| [andrueandersoncs/visual-jev](https://github.com/andrueandersoncs/visual-jev) | Image-native typed decisions with shared visual encoding and Qwen3-VL | 1 | Python | 2026-09-20 |
| [andyhorn/jev](https://github.com/andyhorn/jev) | — | 1 | Dart | 2026-09-21 |
| [antoniofulg/jev-parser](https://github.com/antoniofulg/jev-parser) | Experimental bounded semantic verbalizer for Jev judgments: SRR, protected values, compact-model training, an… | 1 | Python | 2026-09-20 |
| [aoprisan/typesafe-ai-rust-sdk](https://github.com/aoprisan/typesafe-ai-rust-sdk) | — | 1 | Rust | 2026-09-21 |
| [aranlucas/ai-shopping-mcp](https://github.com/aranlucas/ai-shopping-mcp) | Kroger MCP server | 1 | TypeScript | 2026-09-19 |
| [ARCJ137442/jev-2048](https://github.com/ARCJ137442/jev-2048) | An instrumented 2048 web lab where every move is a Jev (TypeSafe AI System One) Choice, with no heuristic fal… | 1 | TypeScript | 2026-09-21 |
| [Ashfaqbs/jev-mcp-spring](https://github.com/Ashfaqbs/jev-mcp-spring) | Java/Spring Boot MCP server for TypeSafe Jev | 1 | Java | 2026-09-21 |
| [auggie246/dsh-jev](https://github.com/auggie246/dsh-jev) | Jev integration to Deepseek harness | 1 | JavaScript | 2026-09-20 |
| [avgon/jev-seo-geo](https://github.com/avgon/jev-seo-geo) | AI visibility toolkit. Measure and optimize how AI models see your brand. GEO (Generative Engine Optimization… | 1 | Python | 2026-09-21 |
| [az9713/jev-model-router](https://github.com/az9713/jev-model-router) | Jev (TypeSafe) model router on the Vercel AI Gateway | 1 | JavaScript | 2026-09-20 |
| [azterizm/jev-vs-sovereign-benchmark](https://github.com/azterizm/jev-vs-sovereign-benchmark) | — | 1 | Python | 2026-09-20 |
| [Barneyjm/decision-circuits](https://github.com/Barneyjm/decision-circuits) | Decision circuits: typed questions to a System One model, calibrated probabilities back, gates in code. Zero-… | 1 | Python | 2026-09-21 |
| [bchaney/jev_speedway](https://github.com/bchaney/jev_speedway) | Uses jev to control race cars on a virtual track | 1 | JavaScript | 2026-09-19 |
| [beamnxw/minelog](https://github.com/beamnxw/minelog) | MineLog harness - GPT-6 Astra plans, Jev decides, one Minecraft body. Backend behind minelog.xyz | 1 | JavaScript | 2026-09-21 |
| [bgrablin/hermes-switchyard](https://github.com/bgrablin/hermes-switchyard) | Jev-powered decision plugin for Hermes Agent: automatic skill selection, policy-constrained model routing, ty… | 1 | Python | 2026-09-21 |
| [binnash/typesafe-sdk](https://github.com/binnash/typesafe-sdk) | PHP & Laravel SDK for TypeSafe AI's JEV Model series | 1 | PHP | 2026-09-18 |
| [bitomule/jevi](https://github.com/bitomule/jevi) | Ask typed questions about a text and branch on the answer. A shell front end for TypeSafe's Jev. | 1 | Rust | 2026-09-21 |
| [bitsocialnet/bitsocial-web](https://github.com/bitsocialnet/bitsocial-web) | Monorepo for bitsocial.net: landing pages, docs, apps explorer, and future flagship client | 1 | JavaScript | 2026-09-21 |
| [bmccarn/tracecheck](https://github.com/bmccarn/tracecheck) | Evidence-backed code review for AI coding agents, powered by Jev. | 1 | TypeScript | 2026-09-18 |
| [br41s/hermes-sandbox](https://github.com/br41s/hermes-sandbox) | — | 1 | Python | 2026-09-21 |
| [bricef/factor-q](https://github.com/bricef/factor-q) | A high-leverage agentic platform | 1 | Rust | 2026-09-21 |
| [Bthornton1994/Manipulation-score](https://github.com/Bthornton1994/Manipulation-score) | — | 1 | JavaScript | 2026-09-21 |
| [buckmoon/jev-issue-router](https://github.com/buckmoon/jev-issue-router) | Jev recommends model and reasoning settings for GitHub issues across OpenAI, Claude, and Grok | 1 | Python | 2026-09-20 |
| [BYK/jev-mcp](https://github.com/BYK/jev-mcp) | An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, s… | 1 | TypeScript | 2026-09-18 |
| [CarlosCaoLopez/HACKSPAIN-2026](https://github.com/CarlosCaoLopez/HACKSPAIN-2026) | Taiafox filters a hundred incoming messages down to the three that matter, coordinates responders by voice, a… | 1 | Python | 2026-09-20 |
| [cephalization/jev-triage](https://github.com/cephalization/jev-triage) | Uses typeful jev, zero sync to pull and sync large repositories for issue triage | 1 | TypeScript | 2026-09-20 |
| [chahero/driving-jev](https://github.com/chahero/driving-jev) | Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews. | 1 | Python | 2026-09-19 |
| [choxos/jevchess](https://github.com/choxos/jevchess) | Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app… | 1 | JavaScript | 2026-09-20 |
| [chy4pro/jev-dev-kit](https://github.com/chy4pro/jev-dev-kit) | Framework for agents on TypeSafe Jev: turns candidates into valid Jev questions and answers into validated ch… | 1 | TypeScript | 2026-09-21 |
| [chy4pro/jev-in-mcp](https://github.com/chy4pro/jev-in-mcp) | MCP relay that adds use_jev to every server: Jev picks the tool calls, the calling model writes the values Je… | 1 | TypeScript | 2026-09-21 |
| [clouatre-labs/decisions-judge-mcp](https://github.com/clouatre-labs/decisions-judge-mcp) | Typed decisions for AI agents as an MCP tool: yes/no probability (noul), choice, and score in one fast reques… | 1 | JavaScript | 2026-09-21 |
| [clownware/bouncer](https://github.com/clownware/bouncer) | Jev-powered Judgment layer for Claude Code. Stops paying reasoning prices for if-statements: a PreToolUse hoo… | 1 | TypeScript | 2026-09-20 |
| [CompleteDotTech/paper-package](https://github.com/CompleteDotTech/paper-package) | Jev research manuscript, evidence, and reproducible paper package | 1 | Python | 2026-09-20 |
| [ctaxnagomi/dgui-hypermem](https://github.com/ctaxnagomi/dgui-hypermem) | DGUI-HyperMem (DeckerGUI HyperMemory) - self-hosted hybrid memory MCP server on Cloudflare Workers with a JEV… | 1 | TypeScript | 2026-09-21 |
| [da-vinci-noob/pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router) | Route pi prompts to task-appropriate model tiers with TypeSafe Jev typed judgments. Budget-aware, with automa… | 1 | TypeScript | 2026-09-20 |
| [daidr/browser-jev](https://github.com/daidr/browser-jev) | Run Jev-like decisions in your browser with the Prompt API. | 1 | TypeScript | 2026-09-21 |
| [danielhirt/jev-lab](https://github.com/danielhirt/jev-lab) | Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM … | 1 | TypeScript | 2026-09-20 |
| [DanielKillenberger/telperion](https://github.com/DanielKillenberger/telperion) | A procedural tree generator. Authored silhouette, space colonization, conserved thickness, one continuous pla… | 1 | Rust | 2026-09-20 |
| [day253/microjev](https://github.com/day253/microjev) | GPT-2 124M with Jev-style typed probabilistic decisions on Apple Silicon (MLX), plus a pure-Python teaching m… | 1 | Python | 2026-09-21 |
| [de-niji/jev-hermes](https://github.com/de-niji/jev-hermes) | Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter | 1 | Python | 2026-09-20 |
| [DECRUX9812/openjev-lm](https://github.com/DECRUX9812/openjev-lm) | open-Jev LM arm: Qwen2.5-0.5B + LoRA reproducing a hosted decision model's judgment at 92.9% on hand-labelled… | 1 | Python | 2026-09-20 |
| [dees91/agent-skill-manager](https://github.com/dees91/agent-skill-manager) | A macOS app, TUI, and CLI to manage skills for AI coding tools. Turn skills on or off without deleting them. | 1 | Go | 2026-09-21 |
| [Dev916/mech-crate](https://github.com/Dev916/mech-crate) | AI-native meta-framework for standing up and operating service ecosystems: Docker scaffolding with recipes, a… | 1 | Rust | 2026-09-19 |
| [Dharundp6/jev-carryforward](https://github.com/Dharundp6/jev-carryforward) | What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written … | 1 | TypeScript | 2026-09-19 |
| [dhava-gautama/noulgate](https://github.com/dhava-gautama/noulgate) | A gate for your agent's expensive steps, powered by TypeSafe Jev (System One). Offline-first, OpenRouter or d… | 1 | Python | 2026-09-19 |
| [digitopvn/clarkcant](https://github.com/digitopvn/clarkcant) | Conversation-first agent platform: portable runtime, paired execution nodes, rich widgets and capability packs | 1 | TypeScript | 2026-09-21 |
| [djhoomin/local-system-one](https://github.com/djhoomin/local-system-one) | Local stand-ins for TypeSafe Jev's System One interface: typed calibrated decisions from small models, with a… | 1 | Python | 2026-09-19 |
| [dorkitude/webctl](https://github.com/dorkitude/webctl) | Smart web search CLI for agents, backed by Jev. Saves a lot of tokens. | 1 | Go | 2026-09-21 |
| [dtheofr/typesafe-jev-ruby](https://github.com/dtheofr/typesafe-jev-ruby) | Ruby client for Jev, TypeSafe's System One model: typed questions, probabilistic answers. Zero runtime depend… | 1 | Ruby | 2026-09-21 |
| [dwisiswant0/typesafe-sdk-go](https://github.com/dwisiswant0/typesafe-sdk-go) | Go SDK for TypeSafe AI. | 1 | Go | 2026-09-19 |
| [eai-support/eai-gofer](https://github.com/eai-support/eai-gofer) | Spec-driven delivery workflow for VS Code and AI coding CLIs | 1 | JavaScript | 2026-09-21 |
| [edgardcham/huncho](https://github.com/edgardcham/huncho) | Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journa… | 1 | TypeScript | 2026-09-21 |
| [EffNine/CodeBro](https://github.com/EffNine/CodeBro) | Persistent engineering context and memory for AI coding agents, exposed through MCP. | 1 | Rust | 2026-09-18 |
| [EkagraAgarwal/Steve](https://github.com/EkagraAgarwal/Steve) | Steve | 1 | Python | 2026-09-20 |
| [Eliran-Turgeman/reaper](https://github.com/Eliran-Turgeman/reaper) | Semantic linter for AI coding agents and CI code review. Detects silent failures, weakened tests, scope creep… | 1 | Go | 2026-09-21 |
| [ellistev/typesafe-minecraft-demo](https://github.com/ellistev/typesafe-minecraft-demo) | A Minecraft Java player controlled by TypeSafe AI, with live decisions, Canadian flag building, and a side-by… | 1 | JavaScript | 2026-09-17 |
| [Embodied-AI-System/Qwen3.5-OneForward](https://github.com/Embodied-AI-System/Qwen3.5-OneForward) | Jev-style typed decisions from Qwen3.5-2B logits — one forward pass, zero decoding, zero fine-tuning. | 1 | Python | 2026-09-21 |
| [EnesYilmazcode/JevMinesweeper](https://github.com/EnesYilmazcode/JevMinesweeper) | Jev Plays Minesweeper | 1 | Python | 2026-09-21 |
| [Enucatl/docker-airflow](https://github.com/Enucatl/docker-airflow) | — | 1 | Python | 2026-09-18 |
| [EpicEric/safe-sh](https://github.com/EpicEric/safe-sh) | Static shell script analysis with Jev. | 1 | Nix | 2026-09-19 |
| [etnt/unsafe-c-finder](https://github.com/etnt/unsafe-c-finder) | Classify C/C++ snippets via TypeSafe Jev through OpenRouter. | 1 | Python | 2026-09-19 |
| [etweisberg/jev-ui](https://github.com/etweisberg/jev-ui) | React components that resolve which component to render, how to order a list, and whether to show an affordan… | 1 | TypeScript | 2026-09-21 |
| [evanzyang91/jevis](https://github.com/evanzyang91/jevis) | — | 1 | Python | 2026-09-20 |
| [fakechris/lumenbox](https://github.com/fakechris/lumenbox) | A multi-agent orchestrator with a remote Docker box and Linux computer-use — one X11 desktop per agent, watch… | 1 | TypeScript | 2026-09-20 |
| [fanly/Jev-awesome](https://github.com/fanly/Jev-awesome) | — | 1 | Python | 2026-09-20 |
| [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) | Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model. | 1 | JavaScript | 2026-09-20 |
| [fiale-plus/jev-cli](https://github.com/fiale-plus/jev-cli) | — | 1 | TypeScript | 2026-09-19 |
| [finetuningsingh/jev-chatbot](https://github.com/finetuningsingh/jev-chatbot) | Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time | 1 | JavaScript | 2026-09-19 |
| [fraserxu/node-decision-model](https://github.com/fraserxu/node-decision-model) | Node client for decision models such as Typesafe Jev | 1 | TypeScript | 2026-09-19 |
| [frimoldi/jev-palette](https://github.com/frimoldi/jev-palette) | A palette generator using Jev | 1 | TypeScript | 2026-09-20 |
| [g0runmezadam/what-is-jev](https://github.com/g0runmezadam/what-is-jev) | Independent, source-linked research on TypeSafe AI's Jev (System One), with 947 rubric-scored public reposito… | 1 | Python | 2026-09-21 |
| [gaborishka/jev-wrapped](https://github.com/gaborishka/jev-wrapped) | Telegram channel X-ray: Jev judges a year of posts, you get a card. One Cloudflare Worker. | 1 | JavaScript | 2026-09-21 |
| [gaborishka/jevtown](https://github.com/gaborishka/jevtown) | Jevtown: a social network where people write and 10,000 AI personas react | 1 | JavaScript | 2026-09-21 |
| [galitianu/jev4j](https://github.com/galitianu/jev4j) | Java SDK for the TypeSafe AI API. Typed questions, typed answers, Java 21. | 1 | Java | 2026-09-21 |
| [gargpratyush/journey-evals](https://github.com/gargpratyush/journey-evals) | Drive a real browser or a real LangGraph agent through one declared user journey, and report what actually ha… | 1 | Python | 2026-09-21 |
| [glud123/jev-assist](https://github.com/glud123/jev-assist) | Don't burn your expensive main model on grep-and-guess grunt work — let jev rank the whole repo, and save the… | 1 | JavaScript | 2026-09-21 |
| [gmaxxxie/jev-cli](https://github.com/gmaxxxie/jev-cli) | — | 1 | Shell | 2026-09-20 |
| [golergka/jev-plays-starcraft-2](https://github.com/golergka/jev-plays-starcraft-2) | — | 1 | Python | 2026-09-20 |
| [govindup63/skillpick](https://github.com/govindup63/skillpick) | Pick the right agent skill for every prompt with TypeSafe's Jev. Hooks for Claude Code, Codex, Gemini CLI, Dr… | 1 | TypeScript | 2026-09-20 |
| [grayrepo-byte/jev_filter_for_x](https://github.com/grayrepo-byte/jev_filter_for_x) | A browser extension that scores and filters X posts in real time with Jev, folding low-signal content while k… | 1 | TypeScript | 2026-09-20 |
| [greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi) | Fast semantic code search & diff sanity auditor for AI coding assistants (Antigravity, Cursor, Claude Code) p… | 1 | Python | 2026-09-18 |
| [gregb100/gavel](https://github.com/gregb100/gavel) | Stop burning LLM calls on classification. Route bugs, triage failures, and gate PRs in 200ms for $0.00002. Op… | 1 | Python | 2026-09-19 |
| [GregDixonMXN/annalist](https://github.com/GregDixonMXN/annalist) | Local-first flight recorder for autonomous coding agents (Zig + SQLite) | 1 | Zig | 2026-09-17 |
| [Growth-Kinetics/jev-context](https://github.com/Growth-Kinetics/jev-context) | — | 1 | TypeScript | 2026-09-20 |
| [guchengod/typesafe-sdk-go](https://github.com/guchengod/typesafe-sdk-go) | Go SDK for TypeSafe AI — classification and rating primitives over text and JSON | 1 | Go | 2026-09-20 |
| [haibt163/jev](https://github.com/haibt163/jev) | — | 1 | TypeScript | 2026-09-19 |
| [hello-wy/sub2api](https://github.com/hello-wy/sub2api) | — | 1 | Go | 2026-09-20 |
| [hemanth/hfjev](https://github.com/hemanth/hfjev) | Classify Hugging Face datasets across typed semantic dimensions with TypeSafe Jev System One. | 1 | TypeScript | 2026-09-21 |
| [hemanth/jevish](https://github.com/hemanth/jevish) | — | 1 | JavaScript | 2026-09-21 |
| [herval/openclaw-jev-plugin](https://github.com/herval/openclaw-jev-plugin) | Jev as a message gate to determine if agents should respond | 1 | TypeScript | 2026-09-21 |
| [HisuiKoh/jev-vtuber-ime-core](https://github.com/HisuiKoh/jev-vtuber-ime-core) | 読み→VTuber表記を Web検索の根拠 + Jev で解決。辞書データなし。 | 1 | TypeScript | 2026-09-21 |
| [howtimeschange/listingfy](https://github.com/howtimeschange/listingfy) | — | 1 | TypeScript | 2026-09-21 |
| [Hugo-DDT/JevTape](https://github.com/Hugo-DDT/JevTape) | Jev 决策的 Record / Replay 工具：CLI + 本地代理 + JSON 磁带，回放彻底离线。 | 1 | Java | 2026-09-21 |
| [HusDev/LinguaTrace](https://github.com/HusDev/LinguaTrace) | The lesson notebook that writes itself. A live tutoring lesson becomes structured notes and a personalised Le… | 1 | TypeScript | 2026-09-20 |
| [ianrtracey/www](https://github.com/ianrtracey/www) | ian.so | 1 | TypeScript | 2026-09-19 |
| [ibnuh/Flow.Launcher.Plugin.JevFileSearch](https://github.com/ibnuh/Flow.Launcher.Plugin.JevFileSearch) | Flow Launcher predictive file search with Jev intent reranking. Type natural language like 'the pdf I just do… | 1 | C# | 2026-09-19 |
| [inematds/jev](https://github.com/inematds/jev) | Análise crítica e plano de aplicação do Jev em decisões estruturadas | 1 | Python | 2026-09-21 |
| [integrate-your-mind/jev-nethack](https://github.com/integrate-your-mind/jev-nethack) | Jev x NetHack: bounded runner, research code, and completed recording releases | 1 | Python | 2026-09-21 |
| [jackboykin/quarry](https://github.com/jackboykin/quarry) | Let agents read web sources themselves, with Exa and Jev | 1 | Go | 2026-09-21 |
| [JacobLinCool/Weave-In](https://github.com/JacobLinCool/Weave-In) | Keep the thread. Weave everyone in. | 1 | TypeScript | 2026-09-18 |
| [jamesward/evals-demo](https://github.com/jamesward/evals-demo) | — | 1 | Shell | 2026-09-20 |
| [jangya/jev-in-action](https://github.com/jangya/jev-in-action) | — | 1 | JavaScript | 2026-09-19 |
| [jay1803/ship-skills](https://github.com/jay1803/ship-skills) | Skills for Codex to ship your idea automatically. | 1 | Python | 2026-09-20 |
| [jcressler/fast-jev-compaction-codex](https://github.com/jcressler/fast-jev-compaction-codex) | Task-aware Jev evidence selection and exact local recovery around native Codex compaction. | 1 | JavaScript | 2026-09-19 |
| [JeelGajera/Dispatch](https://github.com/JeelGajera/Dispatch) | Programmable triage for GitHub. | 1 | TypeScript | 2026-09-20 |
| [JEFF7712/homelab-new](https://github.com/JEFF7712/homelab-new) | NixOS homelab desired state, mirrored from GitLab | 1 | Python | 2026-09-21 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | MASC - Multi-Agent Shared Context | 1 | OCaml | 2026-09-21 |
| [JeronimoRepetto/DwarfAI-Miners](https://github.com/JeronimoRepetto/DwarfAI-Miners) | Local desktop panel that turns your AI coding sessions into an isometric dwarf mining colony - watch, message… | 1 | TypeScript | 2026-09-21 |
| [jimmyliao/jev-storyboard-lab](https://github.com/jimmyliao/jev-storyboard-lab) | Google ADK vs Microsoft Agent Framework for structured-output agents, with TypeSafe Jev as a vendor-neutral Q… | 1 | Python | 2026-09-21 |
| [jmanhype/jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) | Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows | 1 | Python | 2026-09-20 |
| [JoacoMarc/jev-harness-router](https://github.com/JoacoMarc/jev-harness-router) | Per-turn router for agent harnesses: one 350ms Jev call picks the model tier, effort, tools and skill, behind… | 1 | TypeScript | 2026-09-21 |
| [JoeSun-421/robotic_agent_use_jev](https://github.com/JoeSun-421/robotic_agent_use_jev) | A UR5e arm use jev and qwen to gain an ability like neural reflexes | 1 | Python | 2026-09-21 |
| [jonathanavis96/jev-kit](https://github.com/jonathanavis96/jev-kit) | Everything you need to run TypeSafe's Jev with Claude Code: a tool-call guard, tier guard, file search, brows… | 1 | Python | 2026-09-21 |
| [Joymfl/dag-jev](https://github.com/Joymfl/dag-jev) | DAG creation out of unordered items via Jev | 1 | Rust | 2026-09-21 |
| [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev) | A curated list of TypeSafe Jev resources, SDKs, agents, MCP servers, integrations, benchmarks, examples, and … | 1 | — | 2026-09-21 |
| [jstdlee/jev-spaceshooter-demo](https://github.com/jstdlee/jev-spaceshooter-demo) | Space shooter demo of bounded Jev movement choices, swept collision prediction, stale-response rejection, and… | 1 | — | 2026-09-20 |
| [juanlentino/jev-connector](https://github.com/juanlentino/jev-connector) | WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core C… | 1 | PHP | 2026-09-20 |
| [jyatesdotdev/jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) | Jev decides whether a batch of logs is worth acting on. Typed questions, confidence gates, nothing executed. | 1 | Python | 2026-09-20 |
| [JYeswak/jev_playground](https://github.com/JYeswak/jev_playground) | Measure what Jev can actually do before you build on it. Graded findings, ruled-out candidates, and recipes w… | 1 | JavaScript | 2026-09-20 |
| [jzhg6/jev-embodied-media-agent](https://github.com/jzhg6/jev-embodied-media-agent) | Jev-based local-first gesture and gaze media-control agent with guarded page-close intent. | 1 | TypeScript | 2026-09-20 |
| [Kaidera-AI/skills](https://github.com/Kaidera-AI/skills) | Kaidera Skills Marketplace for vetted reusable agent skills | 1 | JavaScript | 2026-09-19 |
| [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) | Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation. | 1 | JavaScript | 2026-09-19 |
| [kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search) | Recursive semantic file search using TypeSafe Jev and fzf | 1 | JavaScript | 2026-09-21 |
| [keiffff/jev-kit](https://github.com/keiffff/jev-kit) | Jev toolkit for building fast, testable AI decision points for agent permissions, routing, semantic change de… | 1 | TypeScript | 2026-09-21 |
| [Kelbie/hunch](https://github.com/Kelbie/hunch) | Semantic code review with Jev, plain-English rules and Agent Skills. | 1 | TypeScript | 2026-09-21 |
| [KennethAshley/fez](https://github.com/KennethAshley/fez) | Orchestrate your own AI agents and build extensions for them — summon an agent by name, watch it think, ship … | 1 | TypeScript | 2026-09-21 |
| [kentaro/jevex](https://github.com/kentaro/jevex) | Jev inference as composable Elixir expressions, with typed requests and runtime-configurable backends | 1 | Elixir | 2026-09-21 |
| [KevinArce/ExoNotes](https://github.com/KevinArce/ExoNotes) | Do astronomers' notes carry disposition signal beyond numeric catalogues? Pre-registered study on TESS Object… | 1 | Python | 2026-09-21 |
| [khaledsAlshibani/jev-ci-classifier](https://github.com/khaledsAlshibani/jev-ci-classifier) | CI example using Jev to classify failed PR checks and return structured decisions with probabilities. | 1 | TypeScript | 2026-09-20 |
| [kilolonion/excelmanus](https://github.com/kilolonion/excelmanus) | ExcelManus - AI-powered Excel Agent | 1 | Python | 2026-09-21 |
| [kingkillery/oh-my-pk](https://github.com/kingkillery/oh-my-pk) | ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subag… | 1 | TypeScript | 2026-09-21 |
| [KKiJJ1024/crush-monitor2](https://github.com/KKiJJ1024/crush-monitor2) | 基于大佬-劈个茄子的开源项目，免去了jev模型钥匙的获取，直接接入deepseek，效果会有差异，但可以暂时满足一定趣味性 | 1 | — | 2026-09-21 |
| [kleosr/cursor-clijev-compaction](https://github.com/kleosr/cursor-clijev-compaction) | TypeSafe Jev-scored context recovery for Cursor CLI (agent). Capture tool I/O, score keep/drop, re-inject aft… | 1 | TypeScript | 2026-09-19 |
| [krlmrr/dotfiles](https://github.com/krlmrr/dotfiles) | — | 1 | Lua | 2026-09-21 |
| [KsanaDock/verdict-lab](https://github.com/KsanaDock/verdict-lab) | An experiment comparing the capabilities and costs of the JEV model and LLM models in the field of content mo… | 1 | Python | 2026-09-20 |
| [kspviswa/chakravyuha-jev](https://github.com/kspviswa/chakravyuha-jev) | Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: t… | 1 | JavaScript | 2026-09-18 |
| [kw2828/OpenJev](https://github.com/kw2828/OpenJev) | Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control | 1 | Python | 2026-09-21 |
| [laguagu/jev-skills](https://github.com/laguagu/jev-skills) | Practical agent skills and examples for building with Jev. API setup, routing, ranking, and evidence checks. | 1 | — | 2026-09-21 |
| [lazniak/jevskill](https://github.com/lazniak/jevskill) | Teach your coding agent to stop burning context. Jev (System One) via OpenRouter or TypeSafe: 325ms, 0.000013… | 1 | Python | 2026-09-21 |
| [lbyxiaolizi/sub2api](https://github.com/lbyxiaolizi/sub2api) | Sub2API-CRS2 一站式开源中转服务，让 Claude、Openai 、Gemini、Antigravity订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 | 1 | Go | 2026-09-20 |
| [leojacinto/my-name-jev](https://github.com/leojacinto/my-name-jev) | — | 1 | TypeScript | 2026-09-21 |
| [levi-qiao/SemaLoom](https://github.com/levi-qiao/SemaLoom) | Ontology-driven business layer for serious AI Q&A over existing data sources, with deterministic semantics, e… | 1 | Python | 2026-09-21 |
| [LiuHao-1443/jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis) | Table tennis vs. TypeSafe's Jev (System One). Every paddle move on the right is a live model decision — no lo… | 1 | Python | 2026-09-21 |
| [liuqihonggit/JoinCode](https://github.com/liuqihonggit/JoinCode) | This is Coding Agent | 1 | C# | 2026-09-21 |
| [llt22/jev-lab](https://github.com/llt22/jev-lab) | Hands-on research lab for TypeSafe's Jev (System One model): reproducible benchmarks of Noul/Choice/Score pri… | 1 | Python | 2026-09-21 |
| [logicrw/ask-jev](https://github.com/logicrw/ask-jev) | Ultra-fast, fail-open advisory decisions and verbatim extractive reading view for AI coding agents and CLI pi… | 1 | Python | 2026-09-21 |
| [loktar00/llm-lan-party](https://github.com/loktar00/llm-lan-party) | A language model plays Unreal Tournament 99 on real Windows 98 hardware by answering small typed questions, s… | 1 | TypeScript | 2026-09-21 |
| [maddygoround/typesafeai-cli](https://github.com/maddygoround/typesafeai-cli) | Give your AI agent a CLI companion who has access to TypeSafe AI's Jev. | 1 | Python | 2026-09-20 |
| [majiayu000/awesome-jev](https://github.com/majiayu000/awesome-jev) | A curated list of Jev / TypeSafe System One projects, SDKs, tutorials, and evaluations. English and 简体中文. | 1 | Python | 2026-09-21 |
| [makefinks/jev-feed-filter](https://github.com/makefinks/jev-feed-filter) | Smart, dynamic AI filtering for X and YouTube feeds using Jev | 1 | TypeScript | 2026-09-19 |
| [Mani212005/GameTester](https://github.com/Mani212005/GameTester) | Interactive 3D Game Physics & Collision Simulator built with Three.js, Cannon-es, and Playwright automated vi… | 1 | TypeScript | 2026-09-19 |
| [markjaquith/typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground) | A playground for experiments around Jev, TypeSafe's System One model. | 1 | Rust | 2026-09-18 |
| [MartinPuli/f1](https://github.com/MartinPuli/f1) | JEV Prix: five AI drivers, unknown procedural circuits, Formula-inspired racing, BYOK Jev and saved replays. | 1 | JavaScript | 2026-09-21 |
| [mattneel/typesafe](https://github.com/mattneel/typesafe) | An idiomatic Elixir client for the TypeSafe AI API | 1 | Elixir | 2026-09-17 |
| [mcftira/jev-route](https://github.com/mcftira/jev-route) | — | 1 | Python | 2026-09-21 |
| [micahchoo/qualitative-query](https://github.com/micahchoo/qualitative-query) | Saved questions that select source passages with Jev scoring and connect them through native Obsidian block e… | 1 | TypeScript | 2026-09-21 |
| [miounet11/jevcode](https://github.com/miounet11/jevcode) | JevCode — Jev (TypeSafe System One) 技术解决方案与最佳实践 · https://www.jevcode.ai | 1 | TypeScript | 2026-09-21 |
| [misty-step/harness](https://github.com/misty-step/harness) | Shared agent primitives and thin pi/OMP harness adapters; one versioned workspace | 1 | TypeScript | 2026-09-20 |
| [misty-step/polymorph](https://github.com/misty-step/polymorph) | Chrome extension: collapse posts that match rules you wrote in English. Jev is the judge. | 1 | TypeScript | 2026-09-20 |
| [montaguegabe/answerfit](https://github.com/montaguegabe/answerfit) | One AI answer, fitted to what each reader already knows — a personalization overlay that re-renders Claude Co… | 1 | TypeScript | 2026-09-21 |
| [MrDesjardins/jevrealtimecodecheck](https://github.com/MrDesjardins/jevrealtimecodecheck) | — | 1 | TypeScript | 2026-09-18 |
| [mrmt/elevator-three](https://github.com/mrmt/elevator-three) | Jev に判断を任せる自動生成のエレクトロの楽器 | 1 | HTML | 2026-09-21 |
| [MumuTW/awesome-jev](https://github.com/MumuTW/awesome-jev) | Get Jev fast — TypeSafe’s sharp System One for typed decisions, plus kindred models the community is buzzing … | 1 | — | 2026-09-19 |
| [muratmirgun/compact-engine](https://github.com/muratmirgun/compact-engine) | — | 1 | Go | 2026-09-21 |
| [muse0509/jev-preflight](https://github.com/muse0509/jev-preflight) | A bounded Jev risk check for Claude Code: eight risk axes, one request, one optional reinspection. | 1 | Go | 2026-09-20 |
| [Nabsku/pi-follow-through](https://github.com/Nabsku/pi-follow-through) | Nudge your agent, when jev deems it so! | 1 | TypeScript | 2026-09-20 |
| [nanami-0713/dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide) | DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrate… | 1 | JavaScript | 2026-09-21 |
| [naveenreddy61/jev-experiments](https://github.com/naveenreddy61/jev-experiments) | experiments with system one model jev | 1 | Python | 2026-09-21 |
| [nekowasabi/jev-routing](https://github.com/nekowasabi/jev-routing) | Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server. | 1 | Go | 2026-09-21 |
| [newuser7171/jev-gamepilot](https://github.com/newuser7171/jev-gamepilot) | — | 1 | Python | 2026-09-21 |
| [nibzard/decision-model-benchmark](https://github.com/nibzard/decision-model-benchmark) | Independent, reproducible benchmark: a decision model (jev), eight constrained LLMs, and deterministic baseli… | 1 | Python | 2026-09-19 |
| [Nicksxs/Nicksxs.github.io](https://github.com/Nicksxs/Nicksxs.github.io) | my personal blog for tech and life | 1 | HTML | 2026-09-20 |
| [Nolane-x/JEV-language](https://github.com/Nolane-x/JEV-language) | Give your Jev language, i'm not finish now | 1 | TypeScript | 2026-09-20 |
| [NomaDamas/kojev](https://github.com/NomaDamas/kojev) | Quick experiment for Korean specialized Jev-style decision model | 1 | Python | 2026-09-21 |
| [nottelabs/notte-jevmaxxing](https://github.com/nottelabs/notte-jevmaxxing) | Run Jev on Notte browser sessions | 1 | TypeScript | 2026-09-21 |
| [nurf-ai/ai](https://github.com/nurf-ai/ai) | Multimodal Go AI module with realistic cost tracking, not just tokens. | 1 | Go | 2026-09-20 |
| [Obrais-cloud/typesafe-mcp](https://github.com/Obrais-cloud/typesafe-mcp) | MCP server exposing TypeSafe (Jev/System One) to the fleet: judge, rerank, systemone | 1 | Python | 2026-09-20 |
| [omribenami/Omarchy-AI](https://github.com/omribenami/Omarchy-AI) | — | 1 | Python | 2026-09-20 |
| [onlyjq04/jev-agent-hooks](https://github.com/onlyjq04/jev-agent-hooks) | TypeSafe Jev hooks for Claude Code, Codex and pi: per-turn skill suggestion and subagent model routing | 1 | JavaScript | 2026-09-21 |
| [osuki-dev/opencode-osuki-agent](https://github.com/osuki-dev/opencode-osuki-agent) | Effect-native OpenCode coordinator with Jev routing and persistent goals | 1 | TypeScript | 2026-09-21 |
| [ourines/hermes-jev](https://github.com/ourines/hermes-jev) | Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill | 1 | Python | 2026-09-19 |
| [patiently/anti-tangent-mcp](https://github.com/patiently/anti-tangent-mcp) | Keep your coding agent focused and prevent it from drifting out on a tangent. | 1 | Go | 2026-09-20 |
| [phyous/tsai-civ2](https://github.com/phyous/tsai-civ2) | TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-g… | 1 | Python | 2026-09-18 |
| [Pinutss/jev-mcp-router](https://github.com/Pinutss/jev-mcp-router) | Select relevant MCP tools under a context-token budget, without executing them. | 1 | Python | 2026-09-18 |
| [pjdurden/jevkit-js](https://github.com/pjdurden/jevkit-js) | jevkit for JavaScript/TypeScript: static linter and shared record format for building on TypeSafe's Jev (Syst… | 1 | TypeScript | 2026-09-21 |
| [plenoai/pleno-anonymize](https://github.com/plenoai/pleno-anonymize) | Small Language Model(SLM) for PII Detect and Anonymize | 1 | Python | 2026-09-21 |
| [pokertools-arena/pokertools-arena.github.io](https://github.com/pokertools-arena/pokertools-arena.github.io) | A browser-first AI poker benchmark. Seat Jev and OpenAI-compatible models at the same no-limit Texas Hold'em … | 1 | JavaScript | 2026-09-21 |
| [powerset-co/powerpacks](https://github.com/powerset-co/powerpacks) | — | 1 | Python | 2026-09-21 |
| [Pranavk098/turnstile](https://github.com/Pranavk098/turnstile) | Turnstile — a margin profiler for voice-AI agents (instrument · price · adjudicate · replay). Honest, tier-la… | 1 | Python | 2026-09-21 |
| [prasanthj/duckdb-jev](https://github.com/prasanthj/duckdb-jev) | High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scorin… | 1 | C++ | 2026-09-21 |
| [pulkitxm/jev-form-filler](https://github.com/pulkitxm/jev-form-filler) | Browser extension that fills forms from your profiles and portfolio in one click, powered by Jev. | 1 | JavaScript | 2026-09-21 |
| [purplesmoke05/opencode-plugin-jev-auto-model-router](https://github.com/purplesmoke05/opencode-plugin-jev-auto-model-router) | Opt-in Auto (Jev) model routing for OpenCode with a configurable model allowlist | 1 | TypeScript | 2026-09-20 |
| [pZacca/askjev](https://github.com/pZacca/askjev) | Unofficial MCP server for Jev (Typesafe AI) | 1 | TypeScript | 2026-09-18 |
| [RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev) | A crawler-maintained directory of projects built on Jev, TypeSafe AI's System One model. Daily GitHub + npm s… | 1 | JavaScript | 2026-09-21 |
| [rashedInt32/jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim) | Neovim popup for jev-lens verdicts: do I need to look, which files, strip the debris | 1 | Lua | 2026-09-20 |
| [rashedInt32/jury.nvim](https://github.com/rashedInt32/jury.nvim) | Calibrated picks for Neovim, judged by TypeSafe Jev. First source: effect-error-pretty.nvim | 1 | Lua | 2026-09-21 |
| [redrossa/pi-model-router](https://github.com/redrossa/pi-model-router) | Pi extension that classifies each prompt with TypeSafe's Jev and routes it to the best model you're logged in… | 1 | TypeScript | 2026-09-18 |
| [reiswaffel78/jev-agent-toolkit](https://github.com/reiswaffel78/jev-agent-toolkit) | Jev-first portable Agent Skill and optional MCP bridge for Claude Code, Codex, Cursor and compatible agents. | 1 | JavaScript | 2026-09-20 |
| [remotehostai/jg](https://github.com/remotehostai/jg) | MIT-licensed semantic code search CLI for coding agents, powered by Jev. | 1 | JavaScript | 2026-09-21 |
| [renchris/claude-infrastructure](https://github.com/renchris/claude-infrastructure) | Custom Claude Code infrastructure — versioned updates, lifecycle hooks, backup system, session search, agent … | 1 | Shell | 2026-09-21 |
| [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev) | Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself. | 1 | TypeScript | 2026-09-21 |
| [RIA-Spec/one-agent](https://github.com/RIA-Spec/one-agent) | The `one tool to rule them all` agent that implements Re in Act pattern | 1 | TypeScript | 2026-09-21 |
| [rikkooo/jev-trade](https://github.com/rikkooo/jev-trade) | A market-data trading simulator powered by auditable Jev judgments | 1 | TypeScript | 2026-09-20 |
| [ROCKET941/trencher-agent-harness](https://github.com/ROCKET941/trencher-agent-harness) | Multi Agent Harness | 1 | JavaScript | 2026-09-21 |
| [rogeriochaves/jev-experiments](https://github.com/rogeriochaves/jev-experiments) | — | 1 | Go | 2026-09-19 |
| [rolottr/x-jev-classifier](https://github.com/rolottr/x-jev-classifier) | Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev … | 1 | JavaScript | 2026-09-19 |
| [ruban-24/switchboard](https://github.com/ruban-24/switchboard) | An open-source, model-agnostic decision router for Claude Code and Codex. | 1 | TypeScript | 2026-09-21 |
| [RudyJunyu/Jev-MCP](https://github.com/RudyJunyu/Jev-MCP) | Jev MCP Hub is a small Go gateway that exposes TypeSafe's Jev model through the Model Context Protocol. | 1 | Go | 2026-09-21 |
| [russellromney/jevons](https://github.com/russellromney/jevons) | — | 1 | TypeScript | 2026-09-18 |
| [russfranky/jev-crawlers](https://github.com/russfranky/jev-crawlers) | Jev learns your repo's decision norms, then adversarially judges past decisions against them. Unix-style prim… | 1 | JavaScript | 2026-09-21 |
| [ryantsai/jev-llm-router](https://github.com/ryantsai/jev-llm-router) | — | 1 | Python | 2026-09-21 |
| [S-O-A-TECH/Jev-search-Kor](https://github.com/S-O-A-TECH/Jev-search-Kor) | — | 1 | TypeScript | 2026-09-20 |
| [sago-cream/mini-sago](https://github.com/sago-cream/mini-sago) | A Discord bot for... everything? | 1 | TypeScript | 2026-09-20 |
| [sathariels/jevcheck](https://github.com/sathariels/jevcheck) | Behavioral contracts for TypeSafe Jev — pin production expectations, eval model upgrades, catch flips and con… | 1 | Python | 2026-09-21 |
| [sathariels/jevtriage](https://github.com/sathariels/jevtriage) | GitHub Action + CLI: triage PRs with TypeSafe Jev (ready / needs review / risky) with confidence gates and je… | 1 | Python | 2026-09-21 |
| [satyawikananda/gits](https://github.com/satyawikananda/gits) | Gits is a browser extension powered by Jev to search the leads data on the Google Maps | 1 | TypeScript | 2026-09-21 |
| [scarif-labs/jev-software-decision-benchmark](https://github.com/scarif-labs/jev-software-decision-benchmark) | Reproducible benchmark evaluating JEV as a software decision primitive for dependency-update automation under… | 1 | TypeScript | 2026-09-19 |
| [seahsky/kelpie](https://github.com/seahsky/kelpie) | Delegation policy for Claude Code, cut down to what its own benchmark supports: two pinned roles, and a skill… | 1 | JavaScript | 2026-09-20 |
| [seanperkins/omp-jev-watchdog](https://github.com/seanperkins/omp-jev-watchdog) | Experimental shadow-only watchdog for OMP using TypeSafe Jev. Records verification and tool-action instructio… | 1 | TypeScript | 2026-09-19 |
| [SecurityMindedSolutions/ai-skills](https://github.com/SecurityMindedSolutions/ai-skills) | Skills that let a coding agent do real work on a codebase: auditing, vulnerability remediation, and unattende… | 1 | Python | 2026-09-20 |
| [senoldogann/chatgpt-system](https://github.com/senoldogann/chatgpt-system) | Secure local MCP authority gateway for controlled filesystem, Git, process, and future computer-use access fr… | 1 | TypeScript | 2026-09-21 |
| [Shashank-H/jev-trader](https://github.com/Shashank-H/jev-trader) | An automated trader using SystemOne model - TypesafeAI Jev | 1 | JavaScript | 2026-09-21 |
| [shibadogcap/kyotsu-ai-bench](https://github.com/shibadogcap/kyotsu-ai-bench) | AI benchmark on Japan's 2026 Common Test: Jev vs luna-none vs luna-low (static dashboard) | 1 | HTML | 2026-09-17 |
| [shinpr/agent-clinic](https://github.com/shinpr/agent-clinic) | Diagnostic plugins for Claude Code and Codex: why a session went wrong, and whether a proposed change is too … | 1 | Python | 2026-09-21 |
| [siddicky/omp-typesafe](https://github.com/siddicky/omp-typesafe) | TypeSafe AI (Jev) adversarial reviewer and typesafe_ask tool for the omp coding agent | 1 | TypeScript | 2026-09-19 |
| [skamprogiannis/system-manifest](https://github.com/skamprogiannis/system-manifest) | A Flake-based NixOS configuration featuring a glassmorphism Hyprland environment, Dank Material Shell, and a … | 1 | Nix | 2026-09-20 |
| [skastr0/pulsar](https://github.com/skastr0/pulsar) | pulsar | 1 | TypeScript | 2026-09-18 |
| [skcache/jevtrafficsim](https://github.com/skcache/jevtrafficsim) | TypeSafe AI's first model Jev takes on an entire city's traffic | 1 | TypeScript | 2026-09-21 |
| [skhlo/rlcd-brwsr](https://github.com/skhlo/rlcd-brwsr) | Fast browser execution for Pi using Jev classification and Chrome DevTools CLI | 1 | — | 2026-09-20 |
| [Solido/jev_dart](https://github.com/Solido/jev_dart) | Typesafe Jev Api | 1 | Dart | 2026-09-21 |
| [sontakey/awesome-jev](https://github.com/sontakey/awesome-jev) | Unofficial list of insanely useful TypeSafe AI Jev / System One projects | 1 | Python | 2026-09-21 |
| [spate141/jev-wordfeel](https://github.com/spate141/jev-wordfeel) | Turn any word into probability distributions over taste, material, scent, and shape. Powered by Jev. | 1 | TypeScript | 2026-09-19 |
| [sseanliu/Jev-Vision](https://github.com/sseanliu/Jev-Vision) | Open-weight step verifier for computer-use agents: calibrated ground/skip/effect/done judgments from screensh… | 1 | Python | 2026-09-21 |
| [sstehniy/jev-calculator](https://github.com/sstehniy/jev-calculator) | iOS 6-inspired Jev calculator demo with a lifetime API budget | 1 | TypeScript | 2026-09-18 |
| [stoopid-computers/jev-bot](https://github.com/stoopid-computers/jev-bot) | Computer Use Agent developed with Jev | 1 | TypeScript | 2026-09-20 |
| [sungatetop/Jev-robot](https://github.com/sungatetop/Jev-robot) | System One\Two Driven Robot demo | 1 | TypeScript | 2026-09-21 |
| [sunholo-data/ailang-demos](https://github.com/sunholo-data/ailang-demos) | AILANG vertical demos: ecommerce with AI, BigQuery, capability budgets | 1 | HTML | 2026-09-21 |
| [SupratikB23/JevCanvas](https://github.com/SupratikB23/JevCanvas) | Jev-driven interfaces with on-demand diffusion visuals and constrained rendering. | 1 | TypeScript | 2026-09-21 |
| [syabdulr/responsible-ai-harness](https://github.com/syabdulr/responsible-ai-harness) | A model-agnostic, Jev-first Responsible AI harness for assessing AI systems for prompt injection, secret/PII … | 1 | TypeScript | 2026-09-20 |
| [Tatuck/jev-boe-demo](https://github.com/Tatuck/jev-boe-demo) | Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE). | 1 | TypeScript | 2026-09-21 |
| [the-metafactory/sage](https://github.com/the-metafactory/sage) | Botanical-named code review agent on pi.dev substrate, speaking Myelin envelopes | 1 | TypeScript | 2026-09-20 |
| [TheBous/jev-flash-review](https://github.com/TheBous/jev-flash-review) | — | 1 | TypeScript | 2026-09-19 |
| [thehumanworks/jevgrep](https://github.com/thehumanworks/jevgrep) | — | 1 | Rust | 2026-09-21 |
| [themsquared/jev-benchmark](https://github.com/themsquared/jev-benchmark) | Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and w… | 1 | Python | 2026-09-19 |
| [theSekyi/jevusecases](https://github.com/theSekyi/jevusecases) | What people are actually shipping with Jev — real builds, tracked as they ship. | 1 | TypeScript | 2026-09-20 |
| [thomasbrueggemann/jeffrey](https://github.com/thomasbrueggemann/jeffrey) | A coding agent CLI where Jev (TypeSafe System One) or Laya decide what to do next and a configurable LLM does… | 1 | TypeScript | 2026-09-20 |
| [TomRichner/can-jev-bayes](https://github.com/TomRichner/can-jev-bayes) | Can Jev Bayes? No. Testing TypeSafe AI's Jev model against Bayesian-optimal strategies. | 1 | Python | 2026-09-21 |
| [tpaulshippy/syft-listening](https://github.com/tpaulshippy/syft-listening) | Real time speech analysis | 1 | JavaScript | 2026-09-21 |
| [trajectoire-ai/hermes-structured-aux-models](https://github.com/trajectoire-ai/hermes-structured-aux-models) | A Hermes Agent model-provider plugin that routes selected auxiliary tasks through bounded Jev decision calls … | 1 | Python | 2026-09-20 |
| [tripathiarpan20/openarm-jev-lab](https://github.com/tripathiarpan20/openarm-jev-lab) | — | 1 | JavaScript | 2026-09-19 |
| [Tsagaanbayr1/jev-tetris](https://github.com/Tsagaanbayr1/jev-tetris) | Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched… | 1 | JavaScript | 2026-09-21 |
| [tsu-ld/chamuy0](https://github.com/tsu-ld/chamuy0) | Feed slop classifier using Jev. LinkedIn only for now. | 1 | HTML | 2026-09-21 |
| [tubone24/jev-practice-speed](https://github.com/tubone24/jev-practice-speed) | A WebGL demo where you play the card game Speed against a CPU whose brain is TypeSafe AI's Jev. The whole poi… | 1 | JavaScript | 2026-09-21 |
| [TwoPartDesign/project-os](https://github.com/TwoPartDesign/project-os) | Spec-driven development scaffold for Claude Code — workflow pipeline, memory system, sub-agent orchestration,… | 1 | TypeScript | 2026-09-21 |
| [TypeSafeAI/typesafe-router](https://github.com/TypeSafeAI/typesafe-router) | Route models and tools with TypeSafe | 1 | TypeScript | 2026-09-19 |
| [umstek/zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench) | Zero-shot information extraction & classification: GLiNER 2.5 vs GLiFormer vs Laya vs Jev — demos, cross-benc… | 1 | Python | 2026-09-21 |
| [using76/TypeEvacSafe](https://github.com/using76/TypeEvacSafe) | 화재 피난자 개인별 판단 엔진 — 타입 안전 판독(Bonsai 2 27B / TypeSafe Jev) + 소셜포스 이동, FDS-GPU 화재장 위에서 역할·구조·경로 결정 · Meteor Simu… | 1 | Python | 2026-09-19 |
| [uspraveen/Jevify](https://github.com/uspraveen/Jevify) | Turn Any Open-LLM into a System-one Jev model | 1 | Python | 2026-09-21 |
| [valsecchi75/squint](https://github.com/valsecchi75/squint) | Claude reads the part of a large file that answers your question, not the whole file. A PreToolUse hook. Meas… | 1 | TypeScript | 2026-09-21 |
| [venumadhav7484/jev-bot](https://github.com/venumadhav7484/jev-bot) | — | 1 | Python | 2026-09-21 |
| [vhwg06/ExHarness](https://github.com/vhwg06/ExHarness) | — | 1 | JavaScript | 2026-09-21 |
| [Victor-Casado/if-ai](https://github.com/Victor-Casado/if-ai) | Plain-English pull request checks powered by Jev. One condition, a minimum confidence, one check. | 1 | TypeScript | 2026-09-20 |
| [vinilana/jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench) | Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off | 1 | JavaScript | 2026-09-19 |
| [vinnie357/typesafe_sdk_ex](https://github.com/vinnie357/typesafe_sdk_ex) | Typesafe AI SDK in Elixir using Req | 1 | Elixir | 2026-09-18 |
| [vvedantb/vmem](https://github.com/vvedantb/vmem) | Universal Memory Layer/Context Engine for LLMs | 1 | TypeScript | 2026-09-21 |
| [waddle-zoo/signal-weave](https://github.com/waddle-zoo/signal-weave) | Typed decisions for operational signals in BI. Powered by TypeSafeAI Jev | 1 | Python | 2026-09-21 |
| [watany-dev/jev-playground](https://github.com/watany-dev/jev-playground) | — | 1 | TypeScript | 2026-09-18 |
| [Whamp/skills](https://github.com/Whamp/skills) | Public agent skills authored and maintained by Will Hampson. | 1 | Shell | 2026-09-19 |
| [wieslawsoltes/XamoraStudio](https://github.com/wieslawsoltes/XamoraStudio) | — | 1 | JavaScript | 2026-09-20 |
| [willfish/pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev) | Jev decides what to keep. Compaction never rewrites the transcript. | 1 | TypeScript | 2026-09-19 |
| [wustep/jev-playground](https://github.com/wustep/jev-playground) | Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI. | 1 | TypeScript | 2026-09-21 |
| [xinyao27/jevonian](https://github.com/xinyao27/jevonian) | — | 1 | TypeScript | 2026-09-21 |
| [yamanoku/archives](https://github.com/yamanoku/archives) | yamanoku's archive contents | 1 | JavaScript | 2026-09-21 |
| [ynitto/sandbox](https://github.com/ynitto/sandbox) | — | 1 | Python | 2026-09-21 |
| [youshinh/md-memo](https://github.com/youshinh/md-memo) | A zero-latency, local-first Markdown scratchpad with offline AI (Ollama/vLLM) and autonomous IME control. Bui… | 1 | JavaScript | 2026-09-21 |
| [YuSa0-6/jeviews](https://github.com/YuSa0-6/jeviews) | Jev で repo 全体をコードレビューする CLI | 1 | TypeScript | 2026-09-20 |
| [Z761293629/pi-jev-helm](https://github.com/Z761293629/pi-jev-helm) | Pi extension that uses Jev task classification (via OpenRouter) to route each run to explicitly configured mo… | 1 | TypeScript | 2026-09-21 |
| [zbush/jev-context](https://github.com/zbush/jev-context) | Codex code-search plugin using Jev relevance filtering with auditable token metrics | 1 | JavaScript | 2026-09-19 |
| [zerodegress/jevinf](https://github.com/zerodegress/jevinf) | Jev-like model inference engine + Jev-compatible API | 1 | Python | 2026-09-20 |
| [zhirschtritt/typesafe-go](https://github.com/zhirschtritt/typesafe-go) | Idiomatic Go SDK for the TypeSafe AI API | 1 | Go | 2026-09-17 |
| [ZHYsfl/learn-jev](https://github.com/ZHYsfl/learn-jev) | a repo that helps you learn jev model. | 1 | Python | 2026-09-20 |
| [zsoXi/FeedGate](https://github.com/zsoXi/FeedGate) | Safe-controls Chrome feed filter (v3.3.0) with TypeSafe Jev judgments, temporal topic mutes, repeat grouping,… | 1 | JavaScript | 2026-09-19 |
| [zurfyx/jev-browser-skill](https://github.com/zurfyx/jev-browser-skill) | Let Jev, TypeSafe's ~100ms decision model, drive your browser. A plug-and-play skill for Claude Code and Code… | 1 | JavaScript | 2026-09-20 |
| [08820048/welight-cli](https://github.com/08820048/welight-cli) | 公众号推文创作排版CLI版本,桌面端:https://welight.fyi | 0 | TypeScript | 2026-09-21 |
| [0M4R0/jev-discord-bot](https://github.com/0M4R0/jev-discord-bot) | — | 0 | Python | 2026-09-21 |
| [0x7067/claude-jev](https://github.com/0x7067/claude-jev) | — | 0 | Python | 2026-09-21 |
| [0xArx/jevegis](https://github.com/0xArx/jevegis) | Guardrails for LLM apps in one API call. Prompt injection, jailbreaks, leaks, unsafe content. Built on TypeSa… | 0 | TypeScript | 2026-09-18 |
| [0xm0w/ship-checklist](https://github.com/0xm0w/ship-checklist) | The final check pass for shipping web apps: mechanical gates + AI-judged quality scoring + is-agentic measure… | 0 | Python | 2026-09-21 |
| [121212165/jev-ecosystem-analysis](https://github.com/121212165/jev-ecosystem-analysis) | JEV 生态普查全量过程资产：259 库清单 · 9 批 stay/go 矩阵 · 11 深读档 · 复审 gold 数据集（CC-BY-4.0 + MIT） | 0 | Python | 2026-09-20 |
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
| [674019130/674019130.github.io](https://github.com/674019130/674019130.github.io) | — | 0 | Vue | 2026-09-21 |
| [99hansling/bb-jev-browser](https://github.com/99hansling/bb-jev-browser) | — | 0 | JavaScript | 2026-09-21 |
| [9sako6/learn-jev](https://github.com/9sako6/learn-jev) | — | 0 | — | 2026-09-20 |
| [aamanlamba/jev-explore](https://github.com/aamanlamba/jev-explore) | An example repository for exploring Jev - the System One model | 0 | Python | 2026-09-19 |
| [aarora79/jev-samples](https://github.com/aarora79/jev-samples) | Runnable samples for Jev, TypeSafe AI's System One model. Send state and questions carrying their own answer … | 0 | — | 2026-09-20 |
| [abdelrahmanmagdii/jevci](https://github.com/abdelrahmanmagdii/jevci) | — | 0 | Go | 2026-09-20 |
| [abhay-2108/agent-foundry](https://github.com/abhay-2108/agent-foundry) | — | 0 | Python | 2026-09-20 |
| [abhibansal60/tidy](https://github.com/abhibansal60/tidy) | Keeps your YouTube subscriptions current: Jev judges, code sets the limits, you approve. Watch-history discov… | 0 | Python | 2026-09-21 |
| [abhishekmishragithub/semantic-microscope](https://github.com/abhishekmishragithub/semantic-microscope) | Label every sentence of a document with calibrated probabilities from Jev, rendered as a heatmap | 0 | Python | 2026-09-21 |
| [ably-labs/jev-pong](https://github.com/ably-labs/jev-pong) | Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and ag… | 0 | TypeScript | 2026-09-19 |
| [acoyfellow/edit](https://github.com/acoyfellow/edit) | A small, approval-first Pi tool for safe, checked code changes. | 0 | Elixir | 2026-09-21 |
| [adagora/jev-experiments](https://github.com/adagora/jev-experiments) | — | 0 | TypeScript | 2026-09-21 |
| [adamjralph/skill-broker](https://github.com/adamjralph/skill-broker) | Deterministic pre-agent skill routing for Hermes agents: audit, canonical catalog, profile policy, and bounde… | 0 | Python | 2026-09-21 |
| [adammichaelwood/jev-music-theory-1](https://github.com/adammichaelwood/jev-music-theory-1) | — | 0 | TypeScript | 2026-09-18 |
| [adamtopaz/jevhammer](https://github.com/adamtopaz/jevhammer) | — | 0 | Lean | 2026-09-20 |
| [adamtopaz/jevhammer_benchmark](https://github.com/adamtopaz/jevhammer_benchmark) | — | 0 | Python | 2026-09-20 |
| [adamtopaz/jevselector](https://github.com/adamtopaz/jevselector) | — | 0 | Lean | 2026-09-20 |
| [adebmbng/jev-trade-prediction](https://github.com/adebmbng/jev-trade-prediction) | — | 0 | TypeScript | 2026-09-20 |
| [adhamelhayek-lab/jev-connector](https://github.com/adhamelhayek-lab/jev-connector) | — | 0 | JavaScript | 2026-09-20 |
| [adihex/typesafeai-fafo](https://github.com/adihex/typesafeai-fafo) | Jev-as-merge-adjudicator fafo: selector-not-generator harness | 0 | TypeScript | 2026-09-20 |
| [adnanlah/scopus-smart-search](https://github.com/adnanlah/scopus-smart-search) | Smart Scopus search with Jev | 0 | TypeScript | 2026-09-20 |
| [AdoCbl/JEV-RESUME-POLISHER](https://github.com/AdoCbl/JEV-RESUME-POLISHER) | — | 0 | Python | 2026-09-21 |
| [advayc/instructional-agent](https://github.com/advayc/instructional-agent) | teach you how to do anything on your computer (using jev and openrouter) | 0 | Swift | 2026-09-21 |
| [advision-development/jevicle](https://github.com/advision-development/jevicle) | Jev LLM Skills | 0 | Python | 2026-09-20 |
| [aesgalexis/model-switch](https://github.com/aesgalexis/model-switch) | Local model and reasoning router for OpenAI Codex, powered by TypeSafe Jev. | 0 | JavaScript | 2026-09-21 |
| [agaches/jev-test](https://github.com/agaches/jev-test) | Hook PreToolUse Claude Code adossé à Jev : décision de sécurité typée, pré-filtre anti-exfiltration local, re… | 0 | Shell | 2026-09-21 |
| [agentik-os/jev-radar](https://github.com/agentik-os/jev-radar) | — | 0 | JavaScript | 2026-09-21 |
| [AHTOOOXA/jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit) | Does TypeSafe's Jev keep its accuracy and calibration on Russian? Independent RU vs EN audit (ECE, reliabilit… | 0 | Python | 2026-09-21 |
| [AI-PM-Wiki/aipm-annotation-server](https://github.com/AI-PM-Wiki/aipm-annotation-server) | AI-PM Wiki 自建批注后端:GitHub OAuth + 公开/私有批注存储 + Jev/LLM 智能高亮 judge(子模块,主仓库 AI-PM-Wiki/AIPM) | 0 | — | 2026-09-21 |
| [aieo-product/jev-gamebenchmark](https://github.com/aieo-product/jev-gamebenchmark) | Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-… | 0 | Python | 2026-09-18 |
| [AiPersonacademy/jev-sales-radar](https://github.com/AiPersonacademy/jev-sales-radar) | Live Sub-25ms Sales AI Teleprompter & Objection Anticipation Engine in Rust. Anticipates prospect subtext and… | 0 | HTML | 2026-09-21 |
| [Aitejiu/jev-harness-lab](https://github.com/Aitejiu/jev-harness-lab) | — | 0 | Python | 2026-09-21 |
| [akaiHuang/btc-dual-ai-trader](https://github.com/akaiHuang/btc-dual-ai-trader) | Dual-AI crypto trading system: one model for strategy/analysis and another for low-latency execution. | 0 | Python | 2026-02-11 |
| [akanthed/jev-migrate](https://github.com/akanthed/jev-migrate) | — | 0 | TypeScript | 2026-09-21 |
| [akash-kamat/jev-llm](https://github.com/akash-kamat/jev-llm) | An LLM built without a language model — using TypeSafe Jev's non-generative AI for contextual response select… | 0 | JavaScript | 2026-09-21 |
| [AkashPriyadarshii/cdpx](https://github.com/AkashPriyadarshii/cdpx) | Driverless Chrome DevTools Protocol engine in pure Rust. Zero Node.js. 95%+ fewer tokens for LLM coding agent… | 0 | Rust | 2026-09-18 |
| [akeldgord/JevDeck](https://github.com/akeldgord/JevDeck) | — | 0 | TypeScript | 2026-09-21 |
| [AkiraWinds/jev-game](https://github.com/AkiraWinds/jev-game) | — | 0 | Python | 2026-09-20 |
| [akrupa-appto/sash](https://github.com/akrupa-appto/sash) | Browser tasks with Jev, optional LLM planning, and Anchor Browser. | 0 | JavaScript | 2026-09-21 |
| [alecstein/rceb-repair-form](https://github.com/alecstein/rceb-repair-form) | — | 0 | JavaScript | 2026-09-17 |
| [alektebel/jev-mindustry](https://github.com/alektebel/jev-mindustry) | — | 0 | Python | 2026-09-20 |
| [alepee/keep-the-thread](https://github.com/alepee/keep-the-thread) | Compaction that keeps the thread: the transcript stays verbatim, stale tool results go, the moment is judged,… | 0 | TypeScript | 2026-09-21 |
| [Aleskyy/Jevsona](https://github.com/Aleskyy/Jevsona) | — | 0 | TypeScript | 2026-09-21 |
| [alex-sun-kuo/jev-consumer-research](https://github.com/alex-sun-kuo/jev-consumer-research) | Consumer research explorations using TypeSafe's Jev | 0 | Jupyter Notebook | 2026-09-18 |
| [alexbejan/jevkit](https://github.com/alexbejan/jevkit) | TypeSafe Jev as a bounded judgement layer for computer use: verify, pick, classify over Cua Driver and phone-… | 0 | Python | 2026-09-18 |
| [alexei-led/pi-model-router](https://github.com/alexei-led/pi-model-router) | Independent Pi extension for four-tier model routing with optional privacy-gated Jev advice, deterministic ba… | 0 | TypeScript | 2026-09-21 |
| [alexhawat/jev-catalog-gate](https://github.com/alexhawat/jev-catalog-gate) | Pre-LLM catalog gate: TypeSafe/Jev scores tools & skills; keep only high-probability items | 0 | — | 2026-09-19 |
| [alexhawat/judge-jev](https://github.com/alexhawat/judge-jev) | Jev-native LLM output judge kit (skill + agents + core) | 0 | Rust | 2026-09-21 |
| [alexshpunt/pi-agent-foreman](https://github.com/alexshpunt/pi-agent-foreman) | Send Pi agents back to work when they stop before the job is done. | 0 | TypeScript | 2026-09-17 |
| [alexykn/jevscan](https://github.com/alexykn/jevscan) | custom linter with treesitter + jev | 0 | Python | 2026-09-20 |
| [ali-abassi/pi-jev](https://github.com/ali-abassi/pi-jev) | Jev advisor for the pi coding agent: loop detection + goal-alignment steers | 0 | Shell | 2026-09-18 |
| [AliyuYahaya/ritza-typesafe-trial](https://github.com/AliyuYahaya/ritza-typesafe-trial) | — | 0 | — | 2026-08-14 |
| [AliZareh-CoE/JevRev](https://github.com/AliZareh-CoE/JevRev) | Narrow a literature review with Jev: typed, calibrated relevance judgments over abstracts and paragraphs. | 0 | Python | 2026-09-21 |
| [allenporter/home-assistant-laya](https://github.com/allenporter/home-assistant-laya) | Conversation agent based on Laya, a multilingual, non-autoregressive System 1 decision model. | 0 | Python | 2026-09-21 |
| [allenporter/home-assistant-typesafe](https://github.com/allenporter/home-assistant-typesafe) | Home Assistant conversation integration powered by the Jev / TypeSafe AI API for fast, structured intent rout… | 0 | Python | 2026-09-21 |
| [alMohimanul/jev-play](https://github.com/alMohimanul/jev-play) | — | 0 | TypeScript | 2026-09-21 |
| [alsoleg89/jev-bouncer](https://github.com/alsoleg89/jev-bouncer) | Claude Code plugin: a 3-cent bouncer for your agent's shell. Jev typed probabilities auto-allow routine comma… | 0 | Python | 2026-09-20 |
| [ALucky1/jevf-cursor](https://github.com/ALucky1/jevf-cursor) | A drop-in custom cursor for the web that plays a sound when you click. | 0 | HTML | 2026-09-21 |
| [Amal-David/awesome-jev](https://github.com/Amal-David/awesome-jev) | — | 0 | Python | 2026-09-21 |
| [amaljithkuttamath/amaljithkuttamath.github.io](https://github.com/amaljithkuttamath/amaljithkuttamath.github.io) | — | 0 | TypeScript | 2026-09-19 |
| [amansoory/JEV2048](https://github.com/amansoory/JEV2048) | — | 0 | C++ | 2026-09-19 |
| [amapara27/jev-pilot](https://github.com/amapara27/jev-pilot) | control your desktop smoothly. powered by typesafe's jev. | 0 | Swift | 2026-09-21 |
| [amberwhitehead/jevscript](https://github.com/amberwhitehead/jevscript) | — | 0 | JavaScript | 2026-09-17 |
| [Amidwestnoob/being-compacted](https://github.com/Amidwestnoob/being-compacted) | Lossless tool-row context compact. No summarizer. No Jev. | 0 | TypeScript | 2026-09-19 |
| [amoreX/jevvy](https://github.com/amoreX/jevvy) | Some cool experiments with jev jevvy | 0 | JavaScript | 2026-09-21 |
| [an-author-1/gisbey-lab](https://github.com/an-author-1/gisbey-lab) | Gibsey Lab explores Field Intelligence through QDPI: a laboratory for context assembly, literary navigation, … | 0 | Python | 2026-09-20 |
| [andrewdeng318/paperclip-plugin-jev](https://github.com/andrewdeng318/paperclip-plugin-jev) | Community Paperclip plugin for Jev-powered issue triage and automatic routing. | 0 | TypeScript | 2026-09-21 |
| [andreylukin/jev-bcp](https://github.com/andreylukin/jev-bcp) | BrowseComp-Plus with a cheap LLM and Jev (TypeSafe's non-generative classifier): agent pipeline, the jevlog l… | 0 | Python | 2026-09-21 |
| [anduriroshan/jev-doom-game](https://github.com/anduriroshan/jev-doom-game) | — | 0 | Python | 2026-09-21 |
| [Andymulb/jev_the_philosopher](https://github.com/Andymulb/jev_the_philosopher) | Measuring a decision model's moral judgements: constant latency regardless of difficulty, sensitivity to fram… | 0 | TeX | 2026-09-21 |
| [andyrewlee/awesome-system-one](https://github.com/andyrewlee/awesome-system-one) | Curated list of tools related to system one models | 0 | — | 2026-09-20 |
| [AndyTheFactory/jev-skill](https://github.com/AndyTheFactory/jev-skill) | — | 0 | Python | 2026-09-21 |
| [angadjosan/Jevplayground](https://github.com/angadjosan/Jevplayground) | — | 0 | Python | 2026-09-19 |
| [angribot/pi-jev](https://github.com/angribot/pi-jev) | Single-file pi extension for batched TypeSafe Jev judgments | 0 | TypeScript | 2026-09-20 |
| [aniruddh-krovvidi/switchboard](https://github.com/aniruddh-krovvidi/switchboard) | Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/… | 0 | Python | 2026-09-20 |
| [anirudh-mandahr/Repo-Agent](https://github.com/anirudh-mandahr/Repo-Agent) | Multi-agent codebase Q&A: five MCP servers over a Neo4j knowledge graph of the FastAPI repo, fronted by a Fas… | 0 | Python | 2026-09-21 |
| [ankitkapooor/autocode](https://github.com/ankitkapooor/autocode) | OrthoCode AI is an evidence-first orthopedic medical-coding platform. Its runtime is constrained to a normali… | 0 | Python | 2026-09-20 |
| [annadmin-cyber/jevvvvvvvvvvvvvvvvv](https://github.com/annadmin-cyber/jevvvvvvvvvvvvvvvvv) | — | 0 | — | 2026-09-20 |
| [ansidium/jev-codex-bridge](https://github.com/ansidium/jev-codex-bridge) | Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates | 0 | JavaScript | 2026-09-20 |
| [anthony-maio/codex-decision-layer](https://github.com/anthony-maio/codex-decision-layer) | Shadow-mode evidence selection for Codex with Jev, local Eve FP32, and Q8 GGUF. CLI, MCP server, plugin, and … | 0 | Python | 2026-09-21 |
| [AnthusAI/Jev-Flywheel](https://github.com/AnthusAI/Jev-Flywheel) | Jev plus a decision head that learns from feedback: can a loop name a bias we planted in our own dataset? | 0 | Python | 2026-09-21 |
| [Antony-Jia/JevChromePlugin](https://github.com/Antony-Jia/JevChromePlugin) | Chrome extension for scoring X and Weibo posts with Jev, with optional LLM deep analysis and Tavily-powered w… | 0 | JavaScript | 2026-09-21 |
| [Anushlinux/voice-agents-benchmarks](https://github.com/Anushlinux/voice-agents-benchmarks) | — | 0 | Python | 2026-09-21 |
| [AO-HyS/development-system](https://github.com/AO-HyS/development-system) | Canonical, installable, and reversible AOHYS multi-harness development contract. | 0 | JavaScript | 2026-09-20 |
| [aoi-yoneda/haikyuBattleJev](https://github.com/aoi-yoneda/haikyuBattleJev) | Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風 | 0 | HTML | 2026-09-20 |
| [aoprisan/jev-demo](https://github.com/aoprisan/jev-demo) | — | 0 | Rust | 2026-09-19 |
| [aoprisan/jev-ts-repl](https://github.com/aoprisan/jev-ts-repl) | — | 0 | TypeScript | 2026-09-21 |
| [api-evangelist/typesafe-ai](https://github.com/api-evangelist/typesafe-ai) | TypeSafe AI is a San Francisco AI lab building System One models — a class of model trained to return typed, … | 0 | — | 2026-09-20 |
| [ar077685-beep/jevansrot](https://github.com/ar077685-beep/jevansrot) | — | 0 | TypeScript | 2026-09-18 |
| [Arby2026/PolyJev](https://github.com/Arby2026/PolyJev) | — | 0 | Python | 2026-09-21 |
| [ariasnico/jevtest](https://github.com/ariasnico/jevtest) | Un laboratorio para construir algo creativo, divertido y útil con Jev de TypeSafe AI. | 0 | JavaScript | 2026-09-21 |
| [Ascurse/typed-judge-kit](https://github.com/Ascurse/typed-judge-kit) | Typed questions to a model, verdict in code, thresholds from your labels | 0 | Python | 2026-09-21 |
| [AseemPrasad/JevGuard](https://github.com/AseemPrasad/JevGuard) | JevGuard : Deterministic Runtime Governance, Reliability & Evaluation Engine for Structured AI Systems | 0 | Go | 2026-09-20 |
| [asfarsadewa/werewolf](https://github.com/asfarsadewa/werewolf) | Werewolf against seven villagers whose suspicions are calibrated probabilities from TypeSafe Jev | 0 | TypeScript | 2026-09-19 |
| [ashaazami/river-run-typesafe](https://github.com/ashaazami/river-run-typesafe) | River shooter game in Python, inspired by Atari's River Raid, played by a TypeSafe AI pilot | 0 | Python | 2026-09-18 |
| [Ashadeepa/typesafe-showcase](https://github.com/Ashadeepa/typesafe-showcase) | Next.js UI showing off TypeSafe's System One model (Jev) — parallel Noul judgments and a Choice-based citatio… | 0 | TypeScript | 2026-09-21 |
| [asmirrr/DriftLab](https://github.com/asmirrr/DriftLab) | Reproducible quantitative research CLI for testing momentum strategies and auditing research methodology with… | 0 | Python | 2026-09-21 |
| [aurenz-max/mountamo-tutor](https://github.com/aurenz-max/mountamo-tutor) | — | 0 | TypeScript | 2026-09-21 |
| [AustinDKB/grass-optimizer](https://github.com/AustinDKB/grass-optimizer) | Daily SK lawn watering and winter shutdown schedule — hydrology in code, Jev for growth/rain/freeze judgments. | 0 | Python | 2026-09-20 |
| [automaticdai/jev-linux-cleaner](https://github.com/automaticdai/jev-linux-cleaner) | — | 0 | Python | 2026-09-21 |
| [AutoPasha/jevcode](https://github.com/AutoPasha/jevcode) | Coding agent driven by a model that cannot write text | 0 | Python | 2026-09-21 |
| [avshalomd/longjev](https://github.com/avshalomd/longjev) | Long inputs for TypeSafe AI's Jev decision model. An experiment. | 0 | Python | 2026-09-19 |
| [awjreynolds/agentic-satn-compiler](https://github.com/awjreynolds/agentic-satn-compiler) | Agentic SATN Compiler (ASATNC): governed AI-assisted network compilation for strategic transport planning | 0 | Python | 2026-09-21 |
| [AydinAdnan/ai-email-agent](https://github.com/AydinAdnan/ai-email-agent) | AI email agent simulation using Jev + LLM hybrid model | 0 | HTML | 2026-09-20 |
| [Ayush0054/menso](https://github.com/Ayush0054/menso) | — | 0 | Swift | 2026-09-18 |
| [az9713/jev-email-triage](https://github.com/az9713/jev-email-triage) | Email triage with Jev (TypeSafe) over the Vercel AI Gateway | 0 | JavaScript | 2026-09-20 |
| [az9713/jev-projects](https://github.com/az9713/jev-projects) | Small demos of Jev (TypeSafe) through the Vercel AI Gateway: wiki race, town of agents, bullet chess, and more | 0 | JavaScript | 2026-09-21 |
| [azumag/soviet_now](https://github.com/azumag/soviet_now) | Soviet Game Auto Play with AI | 0 | Python | 2026-09-21 |
| [B0und/jev_content_filter](https://github.com/B0und/jev_content_filter) | — | 0 | TypeScript | 2026-09-19 |
| [badroneai/eventlive-sa](https://github.com/badroneai/eventlive-sa) | — | 0 | JavaScript | 2026-09-21 |
| [bahramzada/jev-canvas](https://github.com/bahramzada/jev-canvas) | — | 0 | JavaScript | 2026-09-21 |
| [bahramzada/jev-taxi-dispatch](https://github.com/bahramzada/jev-taxi-dispatch) | Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə | 0 | JavaScript | 2026-09-18 |
| [Bali-Zero/Teman2](https://github.com/Bali-Zero/Teman2) | Zantara RAG Backend - AI-powered Indonesian business & immigration consulting | 0 | Python | 2026-09-21 |
| [Barneyjm/circuit](https://github.com/Barneyjm/circuit) | Open-weights System One models (text, images, audio) and the harness that trains and measures them: LoRA plus… | 0 | Python | 2026-09-21 |
| [basmilius/homey-jev](https://github.com/basmilius/homey-jev) | Jev - AI decisions in your Homey Flows. | 0 | TypeScript | 2026-09-21 |
| [bdecrem/hilma](https://github.com/bdecrem/hilma) | — | 0 | TypeScript | 2026-09-21 |
| [bebe0307mz/jevs-kitchen-chaos](https://github.com/bebe0307mz/jevs-kitchen-chaos) | 3D Overcooked-style AI benchmark: four chefs driven per-decision by the Jev decision model or frontier LLMs (… | 0 | TypeScript | 2026-09-19 |
| [beejsbj/voice-gate](https://github.com/beejsbj/voice-gate) | Self-hosted Jev voice and text decision engine. HTTP, CLI and MCP integrations for your devices and assistant… | 0 | Python | 2026-09-21 |
| [behindthedash/worktrail](https://github.com/behindthedash/worktrail) | Spec-format-agnostic task orchestration: parallel git-worktree fan-out execution, a deterministic route class… | 0 | Python | 2026-09-21 |
| [BeLazy167/argus](https://github.com/BeLazy167/argus) | Self-hostable AI code review GitHub App — multi-pass specialist review pipeline posts inline PR comments with… | 0 | Go | 2026-09-21 |
| [benson/inflection](https://github.com/benson/inflection) | Explore how small wording changes shift Jev's probability distributions | 0 | TypeScript | 2026-09-20 |
| [bestony/bestony-userscripts](https://github.com/bestony/bestony-userscripts) | Personal userscripts | 0 | JavaScript | 2026-09-20 |
| [beto11-gif/jev-trading-backend](https://github.com/beto11-gif/jev-trading-backend) | — | 0 | TypeScript | 2026-09-19 |
| [bfalkowski/jev-experiments](https://github.com/bfalkowski/jev-experiments) | — | 0 | Python | 2026-09-21 |
| [bidurkhatri/jev-mcp-lab](https://github.com/bidurkhatri/jev-mcp-lab) | — | 0 | JavaScript | 2026-09-19 |
| [Bigthap/canvas-quiz-ai-solver](https://github.com/Bigthap/canvas-quiz-ai-solver) | High-performance Canvas LMS quiz assistant & scraper designed for TypeSafe AI System One decision primitives | 0 | JavaScript | 2026-09-20 |
| [BILLKISHORE/opensysone](https://github.com/BILLKISHORE/opensysone) | Open System One model for Apple Silicon: typed decisions with calibrated probabilities from one forward pass. | 0 | Python | 2026-09-21 |
| [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) | Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines | 0 | Jupyter Notebook | 2026-09-18 |
| [blazskufca/typesafe-sdk-go](https://github.com/blazskufca/typesafe-sdk-go) | Community SDK for Typesafe.ai in Go | 0 | Go | 2026-09-19 |
| [blck-snwmn/playground-jev](https://github.com/blck-snwmn/playground-jev) | Small apps for experimenting with Jev. | 0 | TypeScript | 2026-09-21 |
| [BleedingDev/fastest-e2e](https://github.com/BleedingDev/fastest-e2e) | — | 0 | TypeScript | 2026-09-21 |
| [blisspixel/fragr](https://github.com/blisspixel/fragr) | Agentic-first retro 3D arena FPS: Rust authoritative server, Godot client, MCP door for agents, in-game pirat… | 0 | Rust | 2026-09-21 |
| [BlueLvRen/lvren-jev](https://github.com/BlueLvRen/lvren-jev) | 自用codex对接jev的工具 | 0 | Python | 2026-09-21 |
| [bogusweb/cv-by-jev](https://github.com/bogusweb/cv-by-jev) | — | 0 | TypeScript | 2026-09-20 |
| [bogusweb/ship-game-with-jev](https://github.com/bogusweb/ship-game-with-jev) | — | 0 | TypeScript | 2026-09-21 |
| [bonsai/furui](https://github.com/bonsai/furui) | エラトステネスの篩 — jev + ML埋め込みでフォルダを意味ごとに振るう整理の槍 (py/ts/rs) | 0 | Python | 2026-09-21 |
| [boriscardano/herdr-jev-router](https://github.com/boriscardano/herdr-jev-router) | Mandatory Jev-based routing for Herdr-managed agent spawns | 0 | Python | 2026-09-21 |
| [bornakapusta/slop-guard](https://github.com/bornakapusta/slop-guard) | Guideline-driven code review bot for Ruby: code finds what to inspect, TypeSafe Jev judges it, explicit rules… | 0 | Ruby | 2026-09-20 |
| [bottlebrushes/jev-orb](https://github.com/bottlebrushes/jev-orb) | Siri-style push-to-talk voice orb for autonomous browser control with Jev and Metal Whisper | 0 | Makefile | 2026-09-19 |
| [box-community/box-jev-incident-triage](https://github.com/box-community/box-jev-incident-triage) | — | 0 | Python | 2026-09-18 |
| [bramtechs/Focus](https://github.com/bramtechs/Focus) | Browser extension that blocks distracting websites using TypeSafe: Jev | 0 | JavaScript | 2026-09-20 |
| [brandonbryant12/transcript-scorecard](https://github.com/brandonbryant12/transcript-scorecard) | ACME live support-call scoring demo with TypeSafe AI, Effect, SQLite, React, Vite, and Turborepo | 0 | TypeScript | 2026-09-17 |
| [braustin20/pi-jev-guard](https://github.com/braustin20/pi-jev-guard) | A Jev-powered safety gate for Pi tool and shell calls | 0 | TypeScript | 2026-09-20 |
| [BrendanH18/jev-lab](https://github.com/BrendanH18/jev-lab) | Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do | 0 | Python | 2026-09-18 |
| [BrendanH18/jev_fsd](https://github.com/BrendanH18/jev_fsd) | JEV AI Model Demo with FSD | 0 | JavaScript | 2026-09-19 |
| [brickfrog/moongate](https://github.com/brickfrog/moongate) | Semantic CI gate: evaluates committed repository changes against rules with TypeSafe Jev | 0 | MoonBit | 2026-09-20 |
| [btcjon/agent-tools](https://github.com/btcjon/agent-tools) | Practical, guarded tools for AI agents—maintenance, skill discovery, email triage, harness routing, and conte… | 0 | Python | 2026-09-21 |
| [Btheriot83/jev-academy](https://github.com/Btheriot83/jev-academy) | Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot | 0 | TypeScript | 2026-09-19 |
| [BubbatheVTOG/pi-jev-anti-slop](https://github.com/BubbatheVTOG/pi-jev-anti-slop) | — | 0 | TypeScript | 2026-09-20 |
| [BubbatheVTOG/pi-jev-redact](https://github.com/BubbatheVTOG/pi-jev-redact) | — | 0 | TypeScript | 2026-09-21 |
| [buberlo/jev-pastepilot](https://github.com/buberlo/jev-pastepilot) | Explicit paste-to-action launcher that routes text to useful tools without automatic side effects. | 0 | TypeScript | 2026-09-20 |
| [Bud-ro/jev-demos](https://github.com/Bud-ro/jev-demos) | Demos to test the effectiveness of TypeSafe's "Jev" System One Model | 0 | Dart | 2026-09-18 |
| [bugkiwi/turing-jail](https://github.com/bugkiwi/turing-jail) | Turing Jail - Let's get out! | 0 | TypeScript | 2026-09-18 |
| [buildwithgagan/zynn-explorer](https://github.com/buildwithgagan/zynn-explorer) | Zynn Explorer: browse any Postgres database and query it in plain English, powered by TypeSafe Jev | 0 | JavaScript | 2026-09-21 |
| [BunsDev/river-oaks](https://github.com/BunsDev/river-oaks) | NPCs of River Oaks Houston, Texas using Jev to power NPCs | 0 | JavaScript | 2026-09-21 |
| [Byrrajus12/voiceos](https://github.com/Byrrajus12/voiceos) | — | 0 | C# | 2026-09-21 |
| [cagbal/awesome-jev](https://github.com/cagbal/awesome-jev) | Curated list of jev related stuff | 0 | — | 2026-09-19 |
| [calebl/text-adventure](https://github.com/calebl/text-adventure) | AI generated text choose your own adventure game | 0 | Ruby | 2026-09-21 |
| [camodeny/new_dnd_testing_lol](https://github.com/camodeny/new_dnd_testing_lol) | — | 0 | Python | 2026-09-21 |
| [CamonZ/vertebrae](https://github.com/CamonZ/vertebrae) | — | 0 | Rust | 2026-09-21 |
| [caniko/chaosbox](https://github.com/caniko/chaosbox) | — | 0 | Rust | 2026-09-21 |
| [carlaiau/readwithjev](https://github.com/carlaiau/readwithjev) | A Demo of using JEV to classify various attributes of a book, and present that to the reader to augment the r… | 0 | TypeScript | 2026-09-19 |
| [carlchou0dailyfresh/jev-gates](https://github.com/carlchou0dailyfresh/jev-gates) | Composable three-valued semantic logic circuits powered by JEV. Stack small judgments into auditable decision… | 0 | TypeScript | 2026-09-20 |
| [cassiomc1/fast-jev-compaction-alt](https://github.com/cassiomc1/fast-jev-compaction-alt) | Continuous, verbatim context compaction for LLM agents using TypeSafe's Jev model. | 0 | TypeScript | 2026-09-19 |
| [CathedralOS/Omega](https://github.com/CathedralOS/Omega) | — | 0 | Rust | 2026-09-21 |
| [catsonkeyboard/sgs](https://github.com/catsonkeyboard/sgs) | Lua/LÖVE2D 三国杀身份局：纯 Lua 规则引擎 + 牌桌 UI + LLM 驱动的 AI 玩家——任意座位可交给大模型托管，带跨步骤记忆推理隐藏身份，牌桌实时展示 AI 的身份猜测过程，支持联机对局。 | 0 | Lua | 2026-09-21 |
| [cdepuy/hermes-skill-router](https://github.com/cdepuy/hermes-skill-router) | Hermes plugin: Jev-style skill pre-routing with a local Laya model (421M System-1). Injects the top-N relevan… | 0 | Python | 2026-09-21 |
| [CeciliaW888/jev-town](https://github.com/CeciliaW888/jev-town) | A 3D town where 50 AI citizens each decide how to react to your broadcast, in parallel, in under a second - p… | 0 | TypeScript | 2026-09-20 |
| [cedarmuse-creator/jev-decision-maker-at-meteora](https://github.com/cedarmuse-creator/jev-decision-maker-at-meteora) | Decision Maker at Meteora - a decision agent for Meteora DLMM liquidity on Solana. Named after Jev, TypeSafe … | 0 | Python | 2026-09-21 |
| [chaewonkong/claude_evaluator](https://github.com/chaewonkong/claude_evaluator) | Claude answer evaluator with Jev | 0 | TypeScript | 2026-09-21 |
| [chalkychalk42/jev](https://github.com/chalkychalk42/jev) | A guide-directed leveling agent for a private TBC 2.4.3 server, built so it gets cheaper to run the longer it… | 0 | Python | 2026-09-21 |
| [chanrute/jev-ui](https://github.com/chanrute/jev-ui) | — | 0 | TypeScript | 2026-09-21 |
| [chanwata/jev-bassist](https://github.com/chanwata/jev-bassist) | — | 0 | Swift | 2026-09-21 |
| [chapel/hermes-jev-skills](https://github.com/chapel/hermes-jev-skills) | — | 0 | Python | 2026-09-17 |
| [charliejimi/reliable-hook-workshop](https://github.com/charliejimi/reliable-hook-workshop) | 自學工作坊：確定性 Cursor hook + deferred Jev 加註，六關 PR 驗收 | 0 | Python | 2026-09-21 |
| [CharryLee0426/jev-test](https://github.com/CharryLee0426/jev-test) | Testing TypeSafe's Jev model on real-time browser games (flappybird.io, play.tetris.com) | 0 | TypeScript | 2026-09-20 |
| [ChasLui/ds2jev](https://github.com/ChasLui/ds2jev) | — | 0 | TypeScript | 2026-09-20 |
| [ChasLui/vai2jev](https://github.com/ChasLui/vai2jev) | vercel ai-gateway 转换为标准TypeSafe-AI接口 | 0 | JavaScript | 2026-09-21 |
| [chaspy/jev-education](https://github.com/chaspy/jev-education) | — | 0 | HTML | 2026-09-21 |
| [chewcw/project-scale-jev-demonstration](https://github.com/chewcw/project-scale-jev-demonstration) | — | 0 | TypeScript | 2026-09-21 |
| [chocopc123/jev-ai-ppon-grand-prix](https://github.com/chocopc123/jev-ai-ppon-grand-prix) | — | 0 | TypeScript | 2026-09-20 |
| [ChosenXu/raindrop-collection-governance](https://github.com/ChosenXu/raindrop-collection-governance) | Agent Skills-compatible skill: govern a Raindrop.io library's collection structure via raindrop-mcp — audit, … | 0 | Python | 2026-09-21 |
| [christianj6/.dotfiles](https://github.com/christianj6/.dotfiles) | Miscellaneous configuration files for a reproducible workspace. | 0 | Python | 2026-09-20 |
| [ChristianTracy/jev-terrarium-dinosaurs](https://github.com/ChristianTracy/jev-terrarium-dinosaurs) | Autonomous dinosaur ecosystem where code runs the physics and TypeSafe's Jev decides each creature's intent f… | 0 | Python | 2026-09-21 |
| [chuehnone/news](https://github.com/chuehnone/news) | 每日新聞重要性評分：5 面向 100 分制，SQLite + 靜態站 | 0 | Python | 2026-09-20 |
| [chungsubeen0/jevmcp](https://github.com/chungsubeen0/jevmcp) | Unofficial MCP for Jev | 0 | Python | 2026-09-18 |
| [Chunky83/jev-workbench](https://github.com/Chunky83/jev-workbench) | Jev Workbench: a C++ desktop workspace with Python diagnostics and structured TypeSafe evaluations | 0 | Python | 2026-09-21 |
| [cinjoff/firehorse](https://github.com/cinjoff/firehorse) | Firehorse agentic skills framework | 0 | TypeScript | 2026-09-21 |
| [cis2042/orca_agent](https://github.com/cis2042/orca_agent) | Oagent: Native Multi-Agent Orchestration & Desktop Workspace with Cursor CLI Resume & A2A Bridge | 0 | TypeScript | 2026-09-21 |
| [claudiuthree/dualtron-jev-parts-finder](https://github.com/claudiuthree/dualtron-jev-parts-finder) | — | 0 | JavaScript | 2026-09-21 |
| [clduab11/jev-test](https://github.com/clduab11/jev-test) | Pre-registered benchmark: can a 2B local model (Gemma 4 E2B) answer web questions without making things up wh… | 0 | Python | 2026-09-20 |
| [Clueless-Creations/Brigade](https://github.com/Clueless-Creations/Brigade) | Consumer-business primitives for AI agents: capabilities, providers, recipes, and evidence through a CLI, MCP… | 0 | TypeScript | 2026-09-21 |
| [Clueless-Creations/jev-ios-ultrafast](https://github.com/Clueless-Creations/jev-ios-ultrafast) | Run iOS Simulator goals with Jev, compare decision models, and replay every attempt. Python CLI and Brigade h… | 0 | Python | 2026-09-21 |
| [cmartinez9/jev-judge-bench](https://github.com/cmartinez9/jev-judge-bench) | Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and a… | 0 | — | 2026-09-18 |
| [cmk404/UGRP-Multi-Robot-Collaboration-Project](https://github.com/cmk404/UGRP-Multi-Robot-Collaboration-Project) | Private source for ugrp | 0 | Python | 2026-09-21 |
| [CN-AlbertWu96/DoomJev](https://github.com/CN-AlbertWu96/DoomJev) | — | 0 | Python | 2026-09-21 |
| [co1smos/jev-demo](https://github.com/co1smos/jev-demo) | Historical paper-trading simulator for evaluating TypeSafe AI JEV decisions | 0 | Python | 2026-09-21 |
| [CodeCampusCo/jev-mcp](https://github.com/CodeCampusCo/jev-mcp) | MCP server exposing one tool: ask Jev a typed question and get a short answer back. | 0 | TypeScript | 2026-09-20 |
| [coderexpert123/jev-browser-wingman](https://github.com/coderexpert123/jev-browser-wingman) | Browser automation where TypeSafe's Jev model picks each step. Attaches to an existing Chrome via CDP and run… | 0 | TypeScript | 2026-09-21 |
| [coding-hermes/auger](https://github.com/coding-hermes/auger) | Auger — spec drilling for the coding-hermes fleet: a CLI that interrogates a project into a git-backed spec o… | 0 | Python | 2026-09-21 |
| [cog-pr/jev-hackathon](https://github.com/cog-pr/jev-hackathon) | — | 0 | HTML | 2026-09-20 |
| [cognesy/instructor-polyglot](https://github.com/cognesy/instructor-polyglot) | \[READ-ONLY\] Access LLMs via unified API | 0 | PHP | 2026-09-17 |
| [colazeta/criminal_infiltration_in_legal_economy_review](https://github.com/colazeta/criminal_infiltration_in_legal_economy_review) | This repository is meant to store a systematic review on the topic of criminal infiltration in the legal econ… | 0 | Python | 2026-09-21 |
| [colinmcdermott/grok-jev-router](https://github.com/colinmcdermott/grok-jev-router) | Jev decides, Grok Bot executes, humans control irreversible actions. A decision router for Grok Bot built on … | 0 | Python | 2026-09-21 |
| [copyleftdev/braess-router](https://github.com/copyleftdev/braess-router) | Bounded semantic routing with Jev and Poise. Rust, single-server, alpha. | 0 | Rust | 2026-09-21 |
| [CorieW/JevTest](https://github.com/CorieW/JevTest) | Bounded exploratory browser testing with Jev, deterministic assertions, and replayable evidence. | 0 | TypeScript | 2026-09-20 |
| [cristiancolon/jev-hft](https://github.com/cristiancolon/jev-hft) | Research pipeline testing whether TypeSafe's Jev (via Vercel AI Gateway) can judge news and market data fast … | 0 | TypeScript | 2026-09-21 |
| [CrowBe/weave](https://github.com/CrowBe/weave) | Agent Harness for System One model | 0 | TypeScript | 2026-09-21 |
| [ctmx/openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp) | High-speed System One Jev AI decision gateway and MCP server powered by OpenRouter | 0 | Python | 2026-09-20 |
| [CWBudde/simtgo](https://github.com/CWBudde/simtgo) | — | 0 | Go | 2026-09-19 |
| [cydevo202020/dsh-jev-warden](https://github.com/cydevo202020/dsh-jev-warden) | DeepSeek Harness plugin: enforces agent-constraint skills (grill-me / find-simplifications) by judging tool c… | 0 | TypeScript | 2026-09-19 |
| [cyrusasco/JevCompact](https://github.com/cyrusasco/JevCompact) | Lossless LLM session compaction for Claude Code, Codex and ZCode — Jev keep/drop decisions plus a Chinese-opt… | 0 | JavaScript | 2026-09-21 |
| [D3v0ps/jev](https://github.com/D3v0ps/jev) | — | 0 | — | 2026-09-20 |
| [dafsic/jev-xmr](https://github.com/dafsic/jev-xmr) | xmr hyperliquid trading agent | 0 | Python | 2026-09-21 |
| [dagfinndybvig/Fight](https://github.com/dagfinndybvig/Fight) | An arcade style fighting game controllable by Jev | 0 | JavaScript | 2026-09-20 |
| [dagfinndybvig/Go](https://github.com/dagfinndybvig/Go) | A Jev driven Go game | 0 | HTML | 2026-09-21 |
| [Daiwik-Chilukuri/DYAD](https://github.com/Daiwik-Chilukuri/DYAD) | — | 0 | TypeScript | 2026-09-20 |
| [daneknudsen8-maker/jev-voice-control](https://github.com/daneknudsen8-maker/jev-voice-control) | Control your browser by voice. A Chrome extension that turns speech into typed commands using TypeSafe's Jev … | 0 | JavaScript | 2026-09-20 |
| [dangquan1402/jev-extract](https://github.com/dangquan1402/jev-extract) | Paragraph information extraction using TypeSafe AI Jev — closed-set extractive spans via Choice over candidat… | 0 | Python | 2026-09-21 |
| [DanielJD1216/magic-computer-use](https://github.com/DanielJD1216/magic-computer-use) | Meet Jev, Fastest Computer Use | 0 | Swift | 2026-09-21 |
| [danielscoffee/nixos](https://github.com/danielscoffee/nixos) | — | 0 | Shell | 2026-09-19 |
| [DanM3rcurius/real-estate-tracker](https://github.com/DanM3rcurius/real-estate-tracker) | — | 0 | Python | 2026-09-21 |
| [DanMcInerney/robots-world](https://github.com/DanMcInerney/robots-world) | A modular multi-robot control testbed with swappable physics, sensors, AI controllers, and impaired swarm com… | 0 | TypeScript | 2026-09-21 |
| [danstoyell/jevnalysis](https://github.com/danstoyell/jevnalysis) | Playing around with Typesafe's Jev | 0 | Python | 2026-09-20 |
| [Danu28/pi-jev-harness](https://github.com/Danu28/pi-jev-harness) | Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback | 0 | TypeScript | 2026-09-20 |
| [daraskme/darask-code](https://github.com/daraskme/darask-code) | Terminal coding-agent harness: append-only session log, evidence-gated completion controller, optional Jev re… | 0 | TypeScript | 2026-09-21 |
| [datamonsterr/jev_auto_select_skills](https://github.com/datamonsterr/jev_auto_select_skills) | — | 0 | TypeScript | 2026-09-21 |
| [davafons/focus-jev](https://github.com/davafons/focus-jev) | A focused Chromium extension that uses JEV to keep browsing aligned with one session goal. | 0 | JavaScript | 2026-09-21 |
| [david-j-lustig/jev-fantasy-football-manager](https://github.com/david-j-lustig/jev-fantasy-football-manager) | Experimenting with using Jev to manage my fantasy football team | 0 | Python | 2026-09-19 |
| [davidrydberg/git-judge-jev](https://github.com/davidrydberg/git-judge-jev) | GitHub Action for agent-written PRs: one comment that says what the PR really does, which hunks need a human,… | 0 | TypeScript | 2026-09-20 |
| [dazreil/jev-npc-interaction-prototype](https://github.com/dazreil/jev-npc-interaction-prototype) | Browser-based NPC interaction prototype using authored dialogue and TypeSafe Jev action selection | 0 | JavaScript | 2026-09-20 |
| [dbredesen/jev-sheets](https://github.com/dbredesen/jev-sheets) | — | 0 | JavaScript | 2026-09-19 |
| [debamitro/yc-or-not-checker](https://github.com/debamitro/yc-or-not-checker) | See if your idea can qualify for YC - powered by Jev | 0 | TypeScript | 2026-09-21 |
| [Debasishhh/jevguard](https://github.com/Debasishhh/jevguard) | — | 0 | Python | 2026-09-21 |
| [Deepusleepy/jeff](https://github.com/Deepusleepy/jeff) | A chatbot that cannot write: TypeSafe Jev ranks a checked-in bank of replies. | 0 | JavaScript | 2026-09-20 |
| [dej-h/jevseek](https://github.com/dej-h/jevseek) | — | 0 | TypeScript | 2026-09-20 |
| [den0206/agent-tool](https://github.com/den0206/agent-tool) | Find Skills, Install Easily! | 0 | TypeScript | 2026-09-21 |
| [dene-/Arcadia](https://github.com/dene-/Arcadia) | — | 0 | GDScript | 2026-09-21 |
| [derekchen14/personal_assistants](https://github.com/derekchen14/personal_assistants) | Assistant Factory that spins up peronal assistants at the click of a button | 0 | HTML | 2026-07-29 |
| [dev-willbird1936/pi-auto-model-router](https://github.com/dev-willbird1936/pi-auto-model-router) | Score-based auto router for Pi Coding Agent (experimental Jev default) | 0 | TypeScript | 2026-09-20 |
| [dev-willbird1936/pi-compact-jev](https://github.com/dev-willbird1936/pi-compact-jev) | Verbatim Jev context compaction for Pi Coding Agent | 0 | TypeScript | 2026-09-20 |
| [dev1556/jev-reranker-benchmark](https://github.com/dev1556/jev-reranker-benchmark) | — | 0 | Python | 2026-09-20 |
| [DevinRobinson1/dstack](https://github.com/DevinRobinson1/dstack) | Dstack: nine stages, one command, and readable evidence at every gate. A delivery process built for an owner … | 0 | JavaScript | 2026-09-20 |
| [deviprasadshetty-dev/jev-independent-test-report](https://github.com/deviprasadshetty-dev/jev-independent-test-report) | — | 0 | HTML | 2026-09-21 |
| [devjtv/jev-router](https://github.com/devjtv/jev-router) | — | 0 | TypeScript | 2026-09-21 |
| [devos-ing/jevbrain](https://github.com/devos-ing/jevbrain) | — | 0 | TypeScript | 2026-09-20 |
| [dfa1/typesafe-java](https://github.com/dfa1/typesafe-java) | Java client and CLI for the TypeSafe AI API | 0 | Java | 2026-09-21 |
| [dglazkov/gev](https://github.com/dglazkov/gev) | Jev from DiffusionGemma | 0 | TypeScript | 2026-09-20 |
| [dglazkov/jev2ui](https://github.com/dglazkov/jev2ui) | Jev + A2UI = ? | 0 | TypeScript | 2026-09-21 |
| [dholzric/jevmarket](https://github.com/dholzric/jevmarket) | — | 0 | Python | 2026-09-21 |
| [digitalfoudnry-vb/JevBrowser](https://github.com/digitalfoudnry-vb/JevBrowser) | JEV Browser | 0 | TypeScript | 2026-09-21 |
| [DihRJ/claude-code-jev-compaction](https://github.com/DihRJ/claude-code-jev-compaction) | Reduza tokens de entrada no Claude Code com compactação de contexto por relevância (LiteLLM + TypeSafe Jev). … | 0 | Shell | 2026-09-21 |
| [divyekant/jev-qa](https://github.com/divyekant/jev-qa) | Jev-only browser UAT and measured design QA with a Luna wrapper and frozen evaluation evidence. | 0 | Python | 2026-09-19 |
| [dizk/jev-lens](https://github.com/dizk/jev-lens) | jev picks what a coding agent gets to see of large tool results: core library, pi extension and Claude Code p… | 0 | TypeScript | 2026-09-19 |
| [DKeAlvaro/batallas-gallos](https://github.com/DKeAlvaro/batallas-gallos) | Corpus de batallas de gallos en español: transcripciones de YouTube y visor web | 0 | Python | 2026-09-21 |
| [dnakhoa/jev-deferred-crispification](https://github.com/dnakhoa/jev-deferred-crispification) | Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision… | 0 | TeX | 2026-09-17 |
| [dngames/JevChess](https://github.com/dngames/JevChess) | — | 0 | JavaScript | 2026-09-21 |
| [doctor-ew/nightshift-community](https://github.com/doctor-ew/nightshift-community) | Nightshift community pilot for the GSU Girls Who Code Hack-her-thon; publication audit in progress | 0 | Python | 2026-09-21 |
| [dominusDeus/jev-trader-fork](https://github.com/dominusDeus/jev-trader-fork) | — | 0 | TypeScript | 2026-09-19 |
| [DomMonte/n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai) | n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibra… | 0 | TypeScript | 2026-09-21 |
| [DonaldMurillo/system-one-playground](https://github.com/DonaldMurillo/system-one-playground) | Readable scripting, semantic code checks, a Go System One client, and Studio. | 0 | Go | 2026-09-21 |
| [dooreelko/jeb](https://github.com/dooreelko/jeb) | The adopted but dear brother of jev | 0 | Python | 2026-09-21 |
| [doublerobust/rjif](https://github.com/doublerobust/rjif) | jif: calibrated if-statements in R via TypeSafe Jev — judgment-based control flow with reliability curves for… | 0 | R | 2026-09-20 |
| [DowLucas/browser-jev](https://github.com/DowLucas/browser-jev) | Adversarial browser testing: personas explore your web app while Jev judges every page state | 0 | TypeScript | 2026-09-21 |
| [dpaluy/pi-jev-compact](https://github.com/dpaluy/pi-jev-compact) | Smart Compact for Harnesses using Jev model | 0 | TypeScript | 2026-09-20 |
| [drgg/ai-trending-radar](https://github.com/drgg/ai-trending-radar) | 每周自动更新的 GitHub AI 热门项目周报（近 90 天新建、Stars > 5000） | 0 | HTML | 2026-09-21 |
| [drillan/jevapan](https://github.com/drillan/jevapan) | — | 0 | Python | 2026-09-19 |
| [dsandrade/jevra](https://github.com/dsandrade/jevra) | An open-source decision layer connecting coding agents with TypeSafe Jev. | 0 | TypeScript | 2026-09-18 |
| [dtduc-git/jev-packs](https://github.com/dtduc-git/jev-packs) | Evidence-gated registry of Jev question packs — curated questions, golden cases and measured evidence for Jev… | 0 | Python | 2026-09-20 |
| [dtduc-git/jev-table](https://github.com/dtduc-git/jev-table) | AI columns for CSV/JSONL files with TypeSafe's Jev — typed answers, confidence, review queue, resume and cost… | 0 | Python | 2026-09-20 |
| [dtduc-git/jevassert](https://github.com/dtduc-git/jevassert) | Record/replay regression tests for Jev (TypeSafe System One) question packs — accuracy, calibration and cost … | 0 | Python | 2026-09-20 |
| [dtsuka/jev-review](https://github.com/dtsuka/jev-review) | — | 0 | TypeScript | 2026-09-20 |
| [dugufeng666/jev-ai-guide](https://github.com/dugufeng666/jev-ai-guide) | jev-ai-guide | 0 | MDX | 2026-09-21 |
| [Dujaydis/JevSysUno](https://github.com/Dujaydis/JevSysUno) | — | 0 | TypeScript | 2026-09-19 |
| [duketopceo/dayflow-linux](https://github.com/duketopceo/dayflow-linux) | Automatic local work journal for Linux — tracks your day and summarizes it with vision models via OpenRouter. | 0 | Go | 2026-09-19 |
| [duketopceo/dim-agent](https://github.com/duketopceo/dim-agent) | Jev-powered voice computer-use agent for Omarchy (Hyprland/Asahi): push-to-talk → whisper.cpp → Jev decision … | 0 | Python | 2026-09-20 |
| [duketopceo/jev-compact](https://github.com/duketopceo/jev-compact) | Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP | 0 | Python | 2026-09-19 |
| [dy-ma/jev-world](https://github.com/dy-ma/jev-world) | — | 0 | TypeScript | 2026-09-18 |
| [dyusuf/BinfoCheck](https://github.com/dyusuf/BinfoCheck) | — | 0 | Python | 2026-09-21 |
| [eachann1024/pi-jev-route](https://github.com/eachann1024/pi-jev-route) | Pi extension: Jev model selection before subagent dispatch | 0 | TypeScript | 2026-09-20 |
| [earayu/jevnews](https://github.com/earayu/jevnews) | — | 0 | TypeScript | 2026-09-20 |
| [edgelabs-ai/jev48](https://github.com/edgelabs-ai/jev48) | Open, auditable reproduction of TypeSafe Jev: a 2B probabilistic decision model benchmarked across six public… | 0 | Python | 2026-09-21 |
| [EdwardHong0627/jev-poc](https://github.com/EdwardHong0627/jev-poc) | — | 0 | Python | 2026-09-20 |
| [EdytaKucharska/ticket-quest](https://github.com/EdytaKucharska/ticket-quest) | Playful ticket triage that shows how TypeSafe Jev's typed, probability-backed decisions compare with promptin… | 0 | TypeScript | 2026-09-18 |
| [Eggwardhan/open-jev](https://github.com/Eggwardhan/open-jev) | — | 0 | Python | 2026-09-21 |
| [Elmata2/LaVega](https://github.com/Elmata2/LaVega) | Building of the personal Finance Agent | 0 | TypeScript | 2026-09-21 |
| [elsejj/mtools](https://github.com/elsejj/mtools) | Intelligently process the content you copy. | 0 | Rust | 2026-09-21 |
| [elyashium/atlas-replay-lab](https://github.com/elyashium/atlas-replay-lab) | capability-aware quality ladder, a privacy-safe trace recorder, deterministic replay, and with an all new Jev… | 0 | JavaScript | 2026-09-21 |
| [Emanon4/tonight-cinema](https://github.com/Emanon4/tonight-cinema) | 今夜放映：用一句观影心情找到下一部电影，Jev 辅助筛选。 | 0 | JavaScript | 2026-09-21 |
| [emergency-lee/decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills) | Agent Skills for decision-native RAG: retrieve wide, decide explicitly, build evidence sets. Site: https://je… | 0 | HTML | 2026-09-19 |
| [enriquejuncorichi-create/pi-jev-assist](https://github.com/enriquejuncorichi-create/pi-jev-assist) | Pi extension: checks an agent's work against observation, not against its own account of itself | 0 | TypeScript | 2026-09-19 |
| [Eric-Zhou-0302/jev-A-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader) | A Jev-powered technical analysis workspace for China A-shares, supporting AKShare/Tushare, market scans, and … | 0 | Python | 2026-09-21 |
| [ericboehs/wrangle](https://github.com/ericboehs/wrangle) | Hand one Safari window to a program, and no more than that. | 0 | Ruby | 2026-09-20 |
| [erickardus/jev-lab](https://github.com/erickardus/jev-lab) | — | 0 | Python | 2026-09-20 |
| [ericmartinezr/are-you-smarter-than-jev](https://github.com/ericmartinezr/are-you-smarter-than-jev) | A small app to test Jev | 0 | Python | 2026-09-19 |
| [EricsenSemedo/t3code-jev](https://github.com/EricsenSemedo/t3code-jev) | Personal T3 Code fork with an opt-in Jev model-routing trial. Based on pingdotgg/t3code. | 0 | TypeScript | 2026-09-21 |
| [Eronmmer/jev-cua](https://github.com/Eronmmer/jev-cua) | Production local Cua + TypeSafe Jev fast-path runtime for Codex and Waku | 0 | TypeScript | 2026-09-21 |
| [ethereumdegen/jev-discord-bot](https://github.com/ethereumdegen/jev-discord-bot) | — | 0 | Rust | 2026-09-19 |
| [ethereumdegen/starkbot-neo](https://github.com/ethereumdegen/starkbot-neo) | Fast, local-first macOS agent with Jev navigation and Hypercanvas | 0 | Rust | 2026-09-21 |
| [Evgen-rus/JEV_voice_browser](https://github.com/Evgen-rus/JEV_voice_browser) | — | 0 | JavaScript | 2026-09-21 |
| [expanso-io/demo-expanso-jev](https://github.com/expanso-io/demo-expanso-jev) | Expanso x Jev demos: live edge-pipeline dashboard, pipeline configs, and flow UI. | 0 | HTML | 2026-09-20 |
| [eyenpi/actionreflex](https://github.com/eyenpi/actionreflex) | A pre-execution gate for AI agent actions, powered by TypeSafe's Jev (System One) model. | 0 | Python | 2026-09-21 |
| [fagnersouza666/Jev-plugin-for-hermes](https://github.com/fagnersouza666/Jev-plugin-for-hermes) | — | 0 | Python | 2026-09-21 |
| [fangligamedev/deskfront-jevlab](https://github.com/fangligamedev/deskfront-jevlab) | 桌面前线：Godot + Blender 开源桌面战术游戏，三阵营玩具兵、掩体 AI、RTS 操作与 Agent 接口 | 0 | GDScript | 2026-09-21 |
| [farukkavlak/vocabboost](https://github.com/farukkavlak/vocabboost) | Look up a word from the subtitles and see what it means in that line, without leaving the video. | 0 | TypeScript | 2026-09-18 |
| [fast-facts/jev-mcp](https://github.com/fast-facts/jev-mcp) | — | 0 | Go | 2026-09-19 |
| [favoyang/jevfast-public](https://github.com/favoyang/jevfast-public) | Public project submissions for jevfast.com. Issues only; website source is maintained separately. | 0 | — | 2026-09-20 |
| [fblissjr/typesafe-experiments](https://github.com/fblissjr/typesafe-experiments) | tinkering and experiments with jev and typesafe ai | 0 | TypeScript | 2026-09-19 |
| [fengyiqicoder/jevfeed](https://github.com/fengyiqicoder/jevfeed) | An infinite feed built from your own browser history, ranked in real time by TypeSafe's Jev. No likes, no fol… | 0 | JavaScript | 2026-09-21 |
| [FibonacciAi/sam-presence](https://github.com/FibonacciAi/sam-presence) | Sam — intelligence, in the moment. Realtime presence, live voice, and Jev-powered understanding. | 0 | HTML | 2026-09-21 |
| [FieldmouseWorks/redshirt](https://github.com/FieldmouseWorks/redshirt) | A shared, observable experiment runner with interchangeable environments, evaluators, and decision providers. | 0 | Rust | 2026-09-20 |
| [flaviomartil/herdr-jev](https://github.com/flaviomartil/herdr-jev) | Jev-driven multi-model triage and Triad orchestration plugin for Herdr and AI-Harness | 0 | TypeScript | 2026-09-20 |
| [fol2/jev-playground](https://github.com/fol2/jev-playground) | — | 0 | Python | 2026-09-21 |
| [formigacamuflada/jev-computer-use](https://github.com/formigacamuflada/jev-computer-use) | — | 0 | Python | 2026-09-19 |
| [FranprzDev/Jev-To-Hackathon](https://github.com/FranprzDev/Jev-To-Hackathon) | — | 0 | JavaScript | 2026-09-20 |
| [frederickrohn/jev-harness](https://github.com/frederickrohn/jev-harness) | experimenting with Jev | 0 | TypeScript | 2026-09-21 |
| [frinfo702/cowork](https://github.com/frinfo702/cowork) | — | 0 | HTML | 2026-09-21 |
| [fsmiamoto/pi-jev-prune](https://github.com/fsmiamoto/pi-jev-prune) | Experimental pi extension: Jev-driven, cache-aware, recoverable pruning of stale tool results | 0 | TypeScript | 2026-09-21 |
| [funkadelic/ha-gutcheck](https://github.com/funkadelic/ha-gutcheck) | Home Assistant integration that makes small judgment calls about your install | 0 | Python | 2026-09-21 |
| [furedea/reflex-state](https://github.com/furedea/reflex-state) | Jev-powered execution state for Pi coding agents. Track changes, checks, and blockers outside the main LLM, w… | 0 | TypeScript | 2026-09-21 |
| [furuCRM-Inc/400ms-agentic-sf](https://github.com/furuCRM-Inc/400ms-agentic-sf) | 400ms Agentic Salesforce demo — Jev System 1 AI + WebMCP Direct UI Control. No screen-scraping. No token stre… | 0 | Apex | 2026-09-20 |
| [futex-ai/ai](https://github.com/futex-ai/ai) | — | 0 | Rust | 2026-09-21 |
| [geckguy/job-posting-triage](https://github.com/geckguy/job-posting-triage) | Four engines answer the same four questions about the same job postings, on one labelled test split, with the… | 0 | Python | 2026-09-20 |
| [gecm0/jev-judge-mcp](https://github.com/gecm0/jev-judge-mcp) | MCP server exposing TypeSafe's Jev as a judge tool: typed judgments with calibrated probabilities, for any MC… | 0 | JavaScript | 2026-09-20 |
| [ghiffarsabda/easynest_v2](https://github.com/ghiffarsabda/easynest_v2) | Industrial 2D irregular nesting engine with Superposition concurrency and TypeSafe Jev System One AI intellig… | 0 | Python | 2026-09-20 |
| [ghubnab99/jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric) | Architecture for running many semantic decisions through one validated path, with a labelled 111-case benchma… | 0 | C# | 2026-09-20 |
| [giangeralcus/gee-fundriving](https://github.com/giangeralcus/gee-fundriving) | Gee-FunDriving — 2D top-down autonomous driving sim (System-One decision loop demo) | 0 | JavaScript | 2026-09-21 |
| [Gilbert09/jev-cli](https://github.com/Gilbert09/jev-cli) | A Jev-powered judgement layer for Claude Code: semantic permission gating, prompt-injection screening, comple… | 0 | TypeScript | 2026-09-20 |
| [gnkm/jev-prompts](https://github.com/gnkm/jev-prompts) | — | 0 | Python | 2026-09-21 |
| [godspede/jev-auto-classifier](https://github.com/godspede/jev-auto-classifier) | Retired: Jev support lives in godspede/construct-auto-classifier. | 0 | — | 2026-09-19 |
| [goodruizhan/pi-jev-control](https://github.com/goodruizhan/pi-jev-control) | System-One control plane for Pi Coding Agent powered by TypeSafe Jev. | 0 | TypeScript | 2026-09-21 |
| [gopalanj/jevons](https://github.com/gopalanj/jevons) | Local System One for typed decisions. Scores noul, choice, and score from option logits — never free JSON. Ty… | 0 | Python | 2026-09-20 |
| [gorock007/jev-atlas](https://github.com/gorock007/jev-atlas) | An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for codin… | 0 | TypeScript | 2026-09-19 |
| [gpazo/jev-vphone-cli](https://github.com/gpazo/jev-vphone-cli) | Jev from Typesafe.ai + vphone-cli | 0 | Swift | 2026-09-20 |
| [gradient30/typesafe-handbook](https://github.com/gradient30/typesafe-handbook) | TypeSafe AI 官方文档中文手册（明/暗/彩三套风格，官网同步日志，GitHub Pages） | 0 | TypeScript | 2026-09-21 |
| [grayslawson/ha-switchboard](https://github.com/grayslawson/ha-switchboard) | Portable Jev-backed decision and control layer for Home Assistant | 0 | Python | 2026-09-20 |
| [GreyssonEnterprises/s1-graphify-indexer](https://github.com/GreyssonEnterprises/s1-graphify-indexer) | System-1 codebase indexer: semantic code graphs from small zero-shot models (GLiNER default; Jev/Needle-compa… | 0 | — | 2026-09-19 |
| [GrinZero/live-mira](https://github.com/GrinZero/live-mira) | — | 0 | JavaScript | 2026-09-20 |
| [guilhermesalviano/koris-hub](https://github.com/guilhermesalviano/koris-hub) | Koris hub website. | 0 | TypeScript | 2026-09-21 |
| [guozhiwei01/langgraph-agent-practice](https://github.com/guozhiwei01/langgraph-agent-practice) | — | 0 | Python | 2026-09-21 |
| [gzawadzki/jev-usecases](https://github.com/gzawadzki/jev-usecases) | TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage | 0 | Python | 2026-09-18 |
| [h1code2/mobile-jev-local](https://github.com/h1code2/mobile-jev-local) | — | 0 | JavaScript | 2026-09-21 |
| [hamakyo/jev-mahjong-bench](https://github.com/hamakyo/jev-mahjong-bench) | Reproducible riichi mahjong benchmark for Jev, GPT, Mortal, and hybrid agents using MJAI and RiichiEnv. | 0 | TypeScript | 2026-09-19 |
| [hamanpaul/session-health](https://github.com/hamanpaul/session-health) | a little tool to analysis agent cli session health | 0 | Python | 2026-09-21 |
| [hanzpo/dogfight-bench](https://github.com/hanzpo/dogfight-bench) | — | 0 | TypeScript | 2026-09-19 |
| [harlanljones/jev-roster-shapes](https://github.com/harlanljones/jev-roster-shapes) | Interactive workspace for comparing baseball roster acquisitions — positional coverage, playing-time transfer… | 0 | TypeScript | 2026-09-21 |
| [havietkok-sys/BizzJev](https://github.com/havietkok-sys/BizzJev) | Experiments with TypeSafe/Jev semantic gates and a Semantic Operations Lab demo. | 0 | C# | 2026-09-21 |
| [haydarsahin0/Jev](https://github.com/haydarsahin0/Jev) | — | 0 | Python | 2026-09-21 |
| [hectorlcastro09/jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales) | Winner-stays-on animal tournament refereed by Jev (TypeSafe System One): a local game to feel how fast typed … | 0 | HTML | 2026-09-21 |
| [heiko-hotz/jev-evaluation](https://github.com/heiko-hotz/jev-evaluation) | — | 0 | Python | 2026-09-21 |
| [heliowap/diff-risk-sentinel](https://github.com/heliowap/diff-risk-sentinel) | Risk triage for large git diffs (CRAP + TypeSafe Jev) and a repository-wide dead-code scan for Python and JS/… | 0 | Python | 2026-09-20 |
| [hemloeth/jev-todo](https://github.com/hemloeth/jev-todo) | — | 0 | JavaScript | 2026-09-21 |
| [HenkDz/butterfly-jev](https://github.com/HenkDz/butterfly-jev) | — | 0 | TypeScript | 2026-09-20 |
| [heyitsR1/killslop](https://github.com/heyitsR1/killslop) | Block AI slop videos on YouTube. A Chrome extension and an open, reviewed list of AI slop channels (CC BY-SA … | 0 | JavaScript | 2026-09-21 |
| [hfiguera/typesafe_ai](https://github.com/hfiguera/typesafe_ai) | An Elixir client for TypeSafe AI with typed responses and bounded concurrency | 0 | Elixir | 2026-09-18 |
| [hide-G/magi-system-on-jev](https://github.com/hide-G/magi-system-on-jev) | MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate … | 0 | JavaScript | 2026-09-18 |
| [HiepPP/hiep-paseo-plugin](https://github.com/HiepPP/hiep-paseo-plugin) | Local Paseo plugin exposing Jev evaluations through MCP | 0 | TypeScript | 2026-09-21 |
| [HikaruEgashira/jev-algorithms](https://github.com/HikaruEgashira/jev-algorithms) | Runtime-agnostic algorithms built on TypeSafe's Jev structured-evaluation model | 0 | JavaScript | 2026-09-21 |
| [HikaruEgashira/jev-kitchen](https://github.com/HikaruEgashira/jev-kitchen) | — | 0 | TypeScript | 2026-09-21 |
| [Hinstein/jev-vip](https://github.com/Hinstein/jev-vip) | — | 0 | TypeScript | 2026-09-21 |
| [Hinstein/jevhub](https://github.com/Hinstein/jevhub) | — | 0 | TypeScript | 2026-09-21 |
| [HiQS-Labs/Jev-unofficial-toolkit](https://github.com/HiQS-Labs/Jev-unofficial-toolkit) | HiQS' unofficial starter code for Jev model with examples and toolkit based on our testing | 0 | Python | 2026-09-21 |
| [hiroyannnn/yuru-poll](https://github.com/hiroyannnn/yuru-poll) | Loose polling: free-text comments become fractional votes via TypeSafe Jev (System One) | 0 | MoonBit | 2026-09-19 |
| [hnegishi/typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby) | Ruby client for the TypeSafe AI(Jev) System One API | 0 | Ruby | 2026-09-20 |
| [hoaphm/jev-decision-maker](https://github.com/hoaphm/jev-decision-maker) | omp plugin: JEV (TypeSafe System One) picks the next coding step from agent-supplied candidates | 0 | TypeScript | 2026-09-21 |
| [hobbs/jev-turn-analysis](https://github.com/hobbs/jev-turn-analysis) | Jev Turn Analysis is a Rust CLI for analyzing completed Claude Code and Codex sessions. | 0 | Rust | 2026-09-21 |
| [Hol1kgmg/jev-trpg](https://github.com/Hol1kgmg/jev-trpg) | jev aiを使ったショートTRPG | 0 | TypeScript | 2026-09-21 |
| [HorusJiang/dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) | Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gat… | 0 | TypeScript | 2026-09-21 |
| [hosseintoussi/jev-flappy-bird](https://github.com/hosseintoussi/jev-flappy-bird) | A live demo of TypeSafe's Jev model playing Flappy Bird, one flap-or-wait decision at a time. | 0 | TypeScript | 2026-09-20 |
| [hraness/sys1](https://github.com/hraness/sys1) | Typed decisions for agents: a local model router, Jev-compatible gateway, and Node/Bun client. | 0 | TypeScript | 2026-09-21 |
| [hraness/system-one-skills](https://github.com/hraness/system-one-skills) | System One skills for Devin, Claude Code and Codex. Cut noisy validation-log tokens with one deterministic sk… | 0 | Python | 2026-09-20 |
| [hulryung/jev-testbed](https://github.com/hulryung/jev-testbed) | Jev (TypeSafe System One) 테스트베드 — 클라우드 API와 로컬 셀프호스팅(jeff/GLiFormer) 양쪽 실행 예제 및 실측 결과 | 0 | Python | 2026-09-21 |
| [hxutixnnn/ui-jev](https://github.com/hxutixnnn/ui-jev) | — | 0 | TypeScript | 2026-09-19 |
| [hyper186/jev-pirate-sorter](https://github.com/hyper186/jev-pirate-sorter) | A hands-on Jev demo: sorting Pirate Nation PFPs into trait-aware piles with Venice AI. | 0 | TypeScript | 2026-09-21 |
| [hyspacex/jev-router](https://github.com/hyspacex/jev-router) | Route OpenAI-style chat requests to a model and reasoning effort, using TypeSafe's Jev decision model as the … | 0 | Python | 2026-09-20 |
| [i-priyanshuverma/laravel-jev-demo](https://github.com/i-priyanshuverma/laravel-jev-demo) | — | 0 | PHP | 2026-09-21 |
| [iamdin/pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench) | Benchmark for Pi skill routing: BM25 vs TypeSafe Jev across roster sizes 50–500 | 0 | TypeScript | 2026-09-20 |
| [ianlintner/jev-router](https://github.com/ianlintner/jev-router) | Shadow-mode Jev decision adapter for model-routing comparisons, with Prometheus metrics and Grafana dashboards | 0 | Python | 2026-09-20 |
| [icecold009/hacksocial-policylens](https://github.com/icecold009/hacksocial-policylens) | PolicyLens: a privacy-conscious AI tool for understanding public school policies. | 0 | JavaScript | 2026-09-20 |
| [ieee0824/jev-mcp](https://github.com/ieee0824/jev-mcp) | A Rust MCP server for TypeSafe AI Jev structured decisions | 0 | Rust | 2026-09-21 |
| [igormorais123/JEV](https://github.com/igormorais123/JEV) | Testes experimentais com o modelo de classificação JEV | 0 | HTML | 2026-09-21 |
| [iluoxw/jev-vs-llm-snake](https://github.com/iluoxw/jev-vs-llm-snake) | Jev 与 LLM 同页对照的贪吃蛇 | 0 | TypeScript | 2026-09-20 |
| [Im-neko/yachi8000](https://github.com/Im-neko/yachi8000) | Yachiyo | 0 | TypeScript | 2026-09-21 |
| [ImFeH2/jev-arcade](https://github.com/ImFeH2/jev-arcade) | — | 0 | TypeScript | 2026-09-20 |
| [imprfct-code/jevdokku](https://github.com/imprfct-code/jevdokku) | — | 0 | TypeScript | 2026-09-19 |
| [inematds/jev-curso](https://github.com/inematds/jev-curso) | Plano pedagógico do curso Jev: três trilhas, doze módulos e trinta e seis aulas | 0 | HTML | 2026-09-21 |
| [inkwell-finance/jev-switchyard](https://github.com/inkwell-finance/jev-switchyard) | — | 0 | Python | 2026-09-17 |
| [Ioluca/fili_Jev](https://github.com/Ioluca/fili_Jev) | Plugin WordPress: trova i link interni che mancano e gli articoli doppi. Propone, non scrive. Giudizi di Jev … | 0 | PHP | 2026-09-21 |
| [ioOvOoi/Pi-Jev](https://github.com/ioOvOoi/Pi-Jev) | — | 0 | TypeScript | 2026-09-18 |
| [Isaac-Flath/agentkb](https://github.com/Isaac-Flath/agentkb) | — | 0 | Python | 2026-09-17 |
| [Isaac12x/incident-resolver-agent](https://github.com/Isaac12x/incident-resolver-agent) | — | 0 | Python | 2026-09-21 |
| [isHeSatoshi/smalljev](https://github.com/isHeSatoshi/smalljev) | the open TypeSafe Jev that runs on your mama's phone. 2.5B params, one forward pass, zero generated tokens. | 0 | Python | 2026-09-21 |
| [isiomaC/jevkit](https://github.com/isiomaC/jevkit) | Native Swift SDK for TypeSafe Jev System One decisions. | 0 | Swift | 2026-09-20 |
| [IslamBaraka90/jev-typesafe-real-financial-use-cases](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases) | Fifty real-world financial use cases for TypeSafe's Jev model: typed, structured LLM answers over ledgers, fr… | 0 | JavaScript | 2026-09-20 |
| [ismailakdag/typesafe-jev](https://github.com/ismailakdag/typesafe-jev) | sahibinden ilanlarini tarayicida yakalayip TypeSafe (Jev) ile eleyen yerel arac — emlak ve vasita icin ayri s… | 0 | Python | 2026-09-20 |
| [ItIsCuthNotCup/SameThing](https://github.com/ItIsCuthNotCup/SameThing) | SameThing test with Jev | 0 | Python | 2026-09-21 |
| [its-panzer/skilltree](https://github.com/its-panzer/skilltree) | A local-first skill library and visual skill tree, with Jev routing and MCP access. | 0 | JavaScript | 2026-09-18 |
| [itsaam/slop-detector](https://github.com/itsaam/slop-detector) | A Chrome extension that flags low-substance engagement bait on X using Jev. | 0 | JavaScript | 2026-09-20 |
| [itsKarad/jev-poker](https://github.com/itsKarad/jev-poker) | — | 0 | TypeScript | 2026-09-20 |
| [iurysza/logview](https://github.com/iurysza/logview) | Keyboard-driven Android log viewer with live capture, recording, and replay | 0 | TypeScript | 2026-09-20 |
| [izworskic/tahquamenon-falls-live](https://github.com/izworskic/tahquamenon-falls-live) | — | 0 | JavaScript | 2026-09-20 |
| [J12003LPZ/davinci](https://github.com/J12003LPZ/davinci) | — | 0 | Rust | 2026-09-21 |
| [JabbaKadabra/SystemOneDotNet](https://github.com/JabbaKadabra/SystemOneDotNet) | DotNet Wrapper for the Jev Model | 0 | C# | 2026-09-21 |
| [Jacarte/pepi](https://github.com/Jacarte/pepi) | My Personal Pi config | 0 | TypeScript | 2026-09-21 |
| [jackojacko05/jev-keiba-calling](https://github.com/jackojacko05/jev-keiba-calling) | Compare direct LLM horse-race commentary with Jev-assisted structured decisions. | 0 | TypeScript | 2026-09-20 |
| [JackZH26/Jev-Live](https://github.com/JackZH26/Jev-Live) | Open-source Windows studio for Steam games: local AI host, editable avatars/chat, manual or JEV-assisted play… | 0 | TypeScript | 2026-09-21 |
| [JacobLinCool/lookline](https://github.com/JacobLinCool/lookline) | LookLine, a complete fashion experience that connects acquisition and creation in one continuous loop. Find t… | 0 | TypeScript | 2026-09-20 |
| [jagenaujagenau/ground-truth](https://github.com/jagenaujagenau/ground-truth) | Ground News style bias check for the article in your current tab. | 0 | TypeScript | 2026-09-18 |
| [jakenbear/the-jev-enator](https://github.com/jakenbear/the-jev-enator) | The Jev-enator: three Jev-backed Claude Code hooks - a danger gate, a failure notice, and a completion check. | 0 | Python | 2026-09-21 |
| [jamilxt/typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java) | Community-maintained Java SDK for the TypeSafe AI System One (Jev) API. Not an official TypeSafe product. | 0 | Java | 2026-09-21 |
| [jangya/jev-webmcp](https://github.com/jangya/jev-webmcp) | — | 0 | TypeScript | 2026-09-18 |
| [jaredwerba/xword](https://github.com/jaredwerba/xword) | Crossword agent: Tavily grounds, Jev ranks, Token Factory writes leftovers | 0 | Python | 2026-09-20 |
| [jasondotsetHacked/jev-discord-gate-v1](https://github.com/jasondotsetHacked/jev-discord-gate-v1) | — | 0 | JavaScript | 2026-09-20 |
| [jaswanthsanjay88/rev](https://github.com/jaswanthsanjay88/rev) | Fast, prefill-only decision model. Typed questions in, calibrated probabilities out, single forward pass with… | 0 | TypeScript | 2026-09-20 |
| [jawauntb/mapvest](https://github.com/jawauntb/mapvest) | Mapvest — Google-Maps/Zillow-style investable-brand explorer. Photo scanning identifies public companies + ET… | 0 | TypeScript | 2026-09-20 |
| [jay34986/DevContainerStaticAnalysis](https://github.com/jay34986/DevContainerStaticAnalysis) | — | 0 | Python | 2026-09-21 |
| [jaysonsantos/sudoku-jev](https://github.com/jaysonsantos/sudoku-jev) | Sudoku game played by the TypeSafe Jev decision model through OpenRouter | 0 | TypeScript | 2026-09-21 |
| [jcardama/bird-jev](https://github.com/jcardama/bird-jev) | Private maintenance fork of Bird for reading and searching X; JEV integration planned | 0 | TypeScript | 2026-09-21 |
| [jdhornsby/typesafe-jev](https://github.com/jdhornsby/typesafe-jev) | — | 0 | Python | 2026-09-20 |
| [jdorado/ez-fast-browser](https://github.com/jdorado/ez-fast-browser) | Bounded Jev-powered browser sessions for Ez agents | 0 | Python | 2026-09-19 |
| [jdubpark/jevcode](https://github.com/jdubpark/jevcode) | — | 0 | TypeScript | 2026-09-20 |
| [Je1zzz/Jev-Codex-accelerator](https://github.com/Je1zzz/Jev-Codex-accelerator) | — | 0 | Python | 2026-09-21 |
| [JeffNa1/social-anti-ragebait](https://github.com/JeffNa1/social-anti-ragebait) | Automatically detect, classify, and blur outrage-inducing posts and drama on X (Twitter), Threads, and Facebo… | 0 | JavaScript | 2026-09-20 |
| [jekozyra/pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) | — | 0 | TypeScript | 2026-09-20 |
| [jevbook/jevbook](https://github.com/jevbook/jevbook) | The typed social network. Agents post. Jev decides. | 0 | — | 2026-09-19 |
| [jevido/omarchy-jevido](https://github.com/jevido/omarchy-jevido) | My Omarchy 4 shell plugins: a daily wiki digest, a calendar clock, and media controls | 0 | QML | 2026-09-17 |
| [JevolUkraine/jevol-website](https://github.com/JevolUkraine/jevol-website) | — | 0 | TypeScript | 2026-09-21 |
| [jevrl/jevrl.github.io](https://github.com/jevrl/jevrl.github.io) | — | 0 | HTML | 2026-09-21 |
| [jevtail/jevtail](https://github.com/jevtail/jevtail) | Nothing to read: a message only when your app is actually broken, with what kind of problem it is. Log and al… | 0 | TypeScript | 2026-09-20 |
| [JGalego/JevForge](https://github.com/JGalego/JevForge) | Let Jev judge. Let the model learn. 🧠⚡🎯 | 0 | Python | 2026-09-21 |
| [jgodmere808/tetris-with-jev](https://github.com/jgodmere808/tetris-with-jev) | A tetris game written in C and automated with JEV | 0 | C | 2026-09-20 |
| [jh1373/jev-search](https://github.com/jh1373/jev-search) | Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only aft… | 0 | JavaScript | 2026-09-20 |
| [jianrong7/jev-codex-model-router](https://github.com/jianrong7/jev-codex-model-router) | — | 0 | JavaScript | 2026-09-20 |
| [jinwon-int/ccc-node](https://github.com/jinwon-int/ccc-node) | Reusable template to bootstrap a Seoyoon/Hermes node into a Claude Code/Codex node (클코·코덱스 노드). Sanitized fro… | 0 | Python | 2026-09-21 |
| [jiwenbo0803-hub/btc-jev-radar](https://github.com/jiwenbo0803-hub/btc-jev-radar) | BTC Jev + GPT market radar | 0 | JavaScript | 2026-09-21 |
| [jjd-lab/jev-synthetic-survey](https://github.com/jjd-lab/jev-synthetic-survey) | Jev vs GPT-4.1 as synthetic survey respondents on Twin-2K-500. How you ask mattered more than which model you… | 0 | Python | 2026-09-21 |
| [jjjjuuudde/jev-ad-blocker](https://github.com/jjjjuuudde/jev-ad-blocker) | — | 0 | JavaScript | 2026-09-18 |
| [jkup/jevprint](https://github.com/jkup/jevprint) | — | 0 | TypeScript | 2026-09-21 |
| [JLegends/opencode-jev-compaction](https://github.com/JLegends/opencode-jev-compaction) | opencode plugins that replace lossy compaction with Jev decisions: score every tool call and result, drop or … | 0 | TypeScript | 2026-09-21 |
| [jlov7/jev-decision-lab](https://github.com/jlov7/jev-decision-lab) | A local lab for seeing what TypeSafe's Jev judgment model does on realistic business cases: typed answers, pr… | 0 | Python | 2026-09-21 |
| [joaoh82/coffee-under-fire](https://github.com/joaoh82/coffee-under-fire) | Coffee Under Fire: a free browser shooter with NPC tactics powered by TypeSafe AI’s Jev model. Play at https:… | 0 | TypeScript | 2026-09-21 |
| [JoelLewis/game-coach](https://github.com/JoelLewis/game-coach) | Browser chess coach on Cloudflare: Stockfish owns truth, Jev owns judgment | 0 | TypeScript | 2026-09-20 |
| [johnpozy/codriver](https://github.com/johnpozy/codriver) | Instead of locking a whole session to one model, you pick Auto in the model picker — and for every turn, Codr… | 0 | TypeScript | 2026-09-20 |
| [JohnsonRan/pi-jev](https://github.com/JohnsonRan/pi-jev) | Claude-style auto-mode classifier for Pi, powered by TypeSafe Jev | 0 | TypeScript | 2026-09-21 |
| [jolehuit/jev-downloads-sorter](https://github.com/jolehuit/jev-downloads-sorter) | A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon | 0 | Python | 2026-09-21 |
| [jon-devlapaz/jev-decisions](https://github.com/jon-devlapaz/jev-decisions) | — | 0 | — | 2026-09-17 |
| [jongyunhur/jev-webagent-bench](https://github.com/jongyunhur/jev-webagent-bench) | Evaluating System-One Action Selection in Long-Horizon Web Agents | 0 | Python | 2026-09-20 |
| [jose-troche/live-rubric](https://github.com/jose-troche/live-rubric) | A writing editor that re-scores 15 typed rubric dimensions on every typing pause — one Jev System One call pe… | 0 | TypeScript | 2026-09-20 |
| [joseluissaorin/prosper-jev](https://github.com/joseluissaorin/prosper-jev) | Recepcionista de voz con Jev (Sistema 1) y Gemini (Sistema 2) para el reto Prosper de HackSpain | 0 | Python | 2026-09-20 |
| [jourdanlabs/assay-001](https://github.com/jourdanlabs/assay-001) | ASSAY-001: independent, pre-registered verification of TypeSafe Jev's calibration and type-safety claims. Spl… | 0 | Python | 2026-09-21 |
| [jpollard-cs/jev-observatory](https://github.com/jpollard-cs/jev-observatory) | — | 0 | JavaScript | 2026-09-21 |
| [jpowersdev/neuralint](https://github.com/jpowersdev/neuralint) | AI code review against your repository's rules, powered by TypeSafe AI's Jev. | 0 | HTML | 2026-09-21 |
| [jsherman999/engineer-assistant](https://github.com/jsherman999/engineer-assistant) | — | 0 | Swift | 2026-09-17 |
| [jsherman999/jev_local_web_seatch-](https://github.com/jsherman999/jev_local_web_seatch-) | — | 0 | Python | 2026-09-19 |
| [juan294/sutura](https://github.com/juan294/sutura) | AI agents make CI pass. Sutura verifies the fix, filters flaky failures, rejects unsafe shortcuts, and opens … | 0 | TypeScript | 2026-09-21 |
| [JuanCarJ/dautia-agent-workflow](https://github.com/JuanCarJ/dautia-agent-workflow) | — | 0 | Python | 2026-09-21 |
| [juanlentino/jev-comment-analysis](https://github.com/juanlentino/jev-comment-analysis) | Backs the WordPress AI plugin's Comment Moderation with TypeSafe Jev, through Connector for TypeSafe Jev | 0 | PHP | 2026-09-20 |
| [judoaseeta/duckdb-jev](https://github.com/judoaseeta/duckdb-jev) | Ask your DuckDB tables questions in plain language. A DuckDB port of pg-jev, powered by TypeSafe's Jev. | 0 | C++ | 2026-09-21 |
| [Jul0t/jevent-bot](https://github.com/Jul0t/jevent-bot) | JEvent Bot | 0 | JavaScript | 2026-09-21 |
| [julianarchila/jev-experiments](https://github.com/julianarchila/jev-experiments) | — | 0 | TypeScript | 2026-09-19 |
| [JulianLee1117/jev-moneyprinter](https://github.com/JulianLee1117/jev-moneyprinter) | — | 0 | Python | 2026-09-19 |
| [junyeong-nero/jev-doom](https://github.com/junyeong-nero/jev-doom) | Play DOOM with Jev | 0 | Python | 2026-09-20 |
| [just-be-dev/jev-sat](https://github.com/just-be-dev/jev-sat) | — | 0 | TypeScript | 2026-09-20 |
| [JustinRoderick/jev-test](https://github.com/JustinRoderick/jev-test) | Testing typesafe.ai new model Jev | 0 | TypeScript | 2026-09-21 |
| [JustSebNL/timekeeper](https://github.com/JustSebNL/timekeeper) | Local-first project execution memory system for humans and agents. | 0 | Go | 2026-09-21 |
| [JYbill/xqv-skills](https://github.com/JYbill/xqv-skills) | 个人认为非常适合opencode、codecode的skills | 0 | JavaScript | 2026-09-21 |
| [jyje/pilot-typesafeai-jev](https://github.com/jyje/pilot-typesafeai-jev) | 👩‍🔬 Pilot of the decision model 'jev' from TypeSafe AI | 0 | Python | 2026-09-21 |
| [jyothepro/jev-games](https://github.com/jyothepro/jev-games) | — | 0 | — | 2026-09-21 |
| [ka10ryu1/smart-leger](https://github.com/ka10ryu1/smart-leger) | クレジットカード利用履歴をAIで自動分類し、家計の支出を管理・分析する家計簿アプリ。初期検証ではJevを利用。 | 0 | Python | 2026-09-21 |
| [kabeza/JEV_ebaysearch](https://github.com/kabeza/JEV_ebaysearch) | — | 0 | TypeScript | 2026-09-21 |
| [kabishou-lab/keepdrop](https://github.com/kabishou-lab/keepdrop) | Jev-compatible System One on the LLM you already pay for. Verbatim keep/drop compaction. No waitlist. | 0 | TypeScript | 2026-09-21 |
| [kablewithak/auragateway](https://github.com/kablewithak/auragateway) | Cache-aware agent runtime and evaluation harness for controlled AI reliability benchmarking. | 0 | Python | 2026-09-20 |
| [Kadihx/jev-x-kit](https://github.com/Kadihx/jev-x-kit) | Offline $0 decision layer for coding agents: Choice/Score/Noul primitives, BELKI confidence gatekeeper, ultra… | 0 | TypeScript | 2026-09-21 |
| [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) | TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness | 0 | JavaScript | 2026-09-20 |
| [kanaharu20/jev-learn](https://github.com/kanaharu20/jev-learn) | — | 0 | HTML | 2026-09-19 |
| [kang9307/lotto-generator](https://github.com/kang9307/lotto-generator) | BrainDetox Utility Box | 0 | HTML | 2026-09-20 |
| [kangshifu1/jev-skills-market](https://github.com/kangshifu1/jev-skills-market) | Community Jev skill market and assistant for automation testing, finance research and voice workflows. Comput… | 0 | JavaScript | 2026-09-21 |
| [kaustav1996/reflex](https://github.com/kaustav1996/reflex) | A coding agent and personal assistant with System One reflexes (TypeSafe Jev) on top of the Pi coding agent | 0 | TypeScript | 2026-09-21 |
| [ke-suke0215/contract-review-demo](https://github.com/ke-suke0215/contract-review-demo) | Bun + Hono + TypeScript contract review demo with GPT-5.6 Luna and Jev | 0 | HTML | 2026-09-20 |
| [keepwonder/jev-hub](https://github.com/keepwonder/jev-hub) | Jev / TypeSafe AI 中文跟踪与文档聚合站 | 0 | Astro | 2026-09-21 |
| [keewai704/nixos-configuration](https://github.com/keewai704/nixos-configuration) | — | 0 | Nix | 2026-09-20 |
| [kentaro/jev-shogi](https://github.com/kentaro/jev-shogi) | 判定特化モデル Jev に将棋を指させる実験（ロリポップ！AIゲートウェイ経由） | 0 | Python | 2026-09-19 |
| [kevin9327/jev-master](https://github.com/kevin9327/jev-master) | Typed System One decisions with Jev: Choice + Score + Noul composed in code. | 0 | Python | 2026-09-20 |
| [KeWang0622/jev-board-game](https://github.com/KeWang0622/jev-board-game) | Belief as a primitive: instrumenting social-deduction games (Undercover, Werewolf, Avalon) with TypeSafe's ca… | 0 | Python | 2026-09-21 |
| [KhaiStimpson/JevGen](https://github.com/KhaiStimpson/JevGen) | — | 0 | C# | 2026-09-19 |
| [kierandotai/jev-scout](https://github.com/kierandotai/jev-scout) | Jev-scored observable web research for MCP agents — every query, result, and fetched page judged for relevanc… | 0 | TypeScript | 2026-09-21 |
| [kijung4290/maeum-on-attendance-care](https://github.com/kijung4290/maeum-on-attendance-care) | 어르신 프로그램 출석 위험 모니터링 대시보드 · TypeSafe AI JEV 연동 | 0 | JavaScript | 2026-09-21 |
| [kinoko34077/jev-audit](https://github.com/kinoko34077/jev-audit) | — | 0 | Python | 2026-09-20 |
| [kitepon/dotagents](https://github.com/kitepon/dotagents) | Claude Code / Codex のカスタムスキル・コマンドを複数端末で symlink 同期する個人 dotfiles | 0 | JavaScript | 2026-09-21 |
| [kleosr/jevsor](https://github.com/kleosr/jevsor) | Jev-compatible decision engine over caller-provided models | 0 | Python | 2026-09-19 |
| [klren0312/jev-trade](https://github.com/klren0312/jev-trade) | — | 0 | JavaScript | 2026-09-21 |
| [Kmassidik/Everything-with-jev-ai](https://github.com/Kmassidik/Everything-with-jev-ai) | a single project for all product using jev ai | 0 | Go | 2026-09-21 |
| [knowlet/JevGuard-NSFA](https://github.com/knowlet/JevGuard-NSFA) | Experimental System One implementation of the SingGuard-NSFA agent-security taxonom. | 0 | Python | 2026-09-21 |
| [koderhack/readproof](https://github.com/koderhack/readproof) | — | 0 | Swift | 2026-09-21 |
| [koh11235813/skills](https://github.com/koh11235813/skills) | — | 0 | TeX | 2026-09-20 |
| [kong75/jev-directory](https://github.com/kong75/jev-directory) | Copyable prompts, typed decision patterns, and practical guides for Jev by TypeSafe. Free, independent, and s… | 0 | Astro | 2026-09-20 |
| [Korbeil/opencode-jev-plugin](https://github.com/Korbeil/opencode-jev-plugin) | — | 0 | TypeScript | 2026-09-21 |
| [kostysh/goblin-hr](https://github.com/kostysh/goblin-hr) | Simple Jev usage demo | 0 | TypeScript | 2026-09-17 |
| [kp84-hub/kyrex](https://github.com/kp84-hub/kyrex) | "Terminal AI agent — Go TUI + Python engine with agentic coding tools" | 0 | Python | 2026-09-21 |
| [krushideep/Worldtour](https://github.com/krushideep/Worldtour) | An interesting idea to test Jev's capabilities to travers to all the capitals of the world in a shortest dist… | 0 | TypeScript | 2026-09-21 |
| [KsanaDock/jev-go](https://github.com/KsanaDock/jev-go) | — | 0 | JavaScript | 2026-09-21 |
| [kspviswa/chakravyuha-oss](https://github.com/kspviswa/chakravyuha-oss) | Chakravyuha (OSS) — the polar ring-maze where every move is a Laya decision. Same experiment as chakravyuha-j… | 0 | JavaScript | 2026-09-20 |
| [kt3k/jevmaze](https://github.com/kt3k/jevmaze) | — | 0 | TypeScript | 2026-09-19 |
| [ktaletsk/jevframe](https://github.com/ktaletsk/jevframe) | Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-la… | 0 | Python | 2026-09-19 |
| [ktsu2i/jevgate](https://github.com/ktsu2i/jevgate) | — | 0 | Go | 2026-09-20 |
| [ktsu2i/jevgate-action](https://github.com/ktsu2i/jevgate-action) | — | 0 | Shell | 2026-09-21 |
| [kunobi-ninja/kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev) | Rust client for the TypeSafe System One API (Jev) | 0 | Rust | 2026-09-18 |
| [kurihada/pi-jev-permit](https://github.com/kurihada/pi-jev-permit) | A Jev (TypeSafe System One) permission gate for the Pi coding agent: judges every bash / write / edit call be… | 0 | TypeScript | 2026-09-21 |
| [Kylejeong2/jev-judge](https://github.com/Kylejeong2/jev-judge) | — | 0 | TypeScript | 2026-09-21 |
| [LachlanLindsay/is-jev-calibrated](https://github.com/LachlanLindsay/is-jev-calibrated) | — | 0 | — | 2026-09-21 |
| [Lagnajit09/sgrep](https://github.com/Lagnajit09/sgrep) | sgrep - semantic grep, powered by Jev | 0 | Python | 2026-09-21 |
| [laihenyi/pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser) | Browser and macOS desktop agent for pi: Jev (TypeSafe System One) chooses each action from a structured obser… | 0 | TypeScript | 2026-09-20 |
| [lalitsonawane/jev-one-system](https://github.com/lalitsonawane/jev-one-system) | — | 0 | TypeScript | 2026-09-20 |
| [latere-ai/typesafe-ai-go-sdk](https://github.com/latere-ai/typesafe-ai-go-sdk) | Archived: Go client for the TypeSafe API. Use latere.ai/x/pkg/typesafeai. | 0 | Go | 2026-09-19 |
| [laurentfabre/databricks-jev-pdf-lab](https://github.com/laurentfabre/databricks-jev-pdf-lab) | Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs a… | 0 | Python | 2026-09-20 |
| [LauricellaAndrea/Jev-browser-remote](https://github.com/LauricellaAndrea/Jev-browser-remote) | beta project di use-computer su google chrome mediante l'uso di Jerv, riducendo notevolmente la latenza e i c… | 0 | TypeScript | 2026-09-21 |
| [lawzhougc/jev-openclash](https://github.com/lawzhougc/jev-openclash) | jev-openclash | 0 | Python | 2026-09-21 |
| [lazniak/Jev-UltraCuse](https://github.com/lazniak/Jev-UltraCuse) | Najszybszy Computer Use na Jev 1.13: Rust, portable exe, UIA + SendInput + PowerShell, realtime STT (PL) | 0 | Rust | 2026-09-21 |
| [lazyoft/jev-explorer](https://github.com/lazyoft/jev-explorer) | Goal-driven browser exploration with Jev, compact evidence, and persistent supervisor handoff over MCP. | 0 | TypeScript | 2026-09-20 |
| [ledgerwerk/pyjev](https://github.com/ledgerwerk/pyjev) | Reusable, inspectable Jev decision contracts for Python applications and automation. | 0 | Python | 2026-09-21 |
| [lennon-li/HMA](https://github.com/lennon-li/HMA) | — | 0 | Go | 2026-09-18 |
| [leonininder/remember-me](https://github.com/leonininder/remember-me) | Agent memory that decides what to hydrate — local topology recall + TypeSafe Jev gates (not another dump-ever… | 0 | Python | 2026-09-20 |
| [lhotwll217/jev-cli](https://github.com/lhotwll217/jev-cli) | JSON-in, typed-decisions-out CLI for the TypeSafe System One API | 0 | TypeScript | 2026-09-21 |
| [LiamCarlin/Navi](https://github.com/LiamCarlin/Navi) | Jev-powered Spotlight replacement for macOS — typed fast decisions, Claude for answers and computer use, loca… | 0 | Swift | 2026-09-21 |
| [lifefesta/jev-mail-router](https://github.com/lifefesta/jev-mail-router) | — | 0 | TypeScript | 2026-09-20 |
| [LightningK0ala/jev-marshal](https://github.com/LightningK0ala/jev-marshal) | Semantic PR policy checks powered by Jev. | 0 | TypeScript | 2026-09-20 |
| [LilDojd/jevons](https://github.com/LilDojd/jevons) | A bounded Pi execution supervisor powered by TypeSafe Jev: decisions, recovery, review and verification. | 0 | TypeScript | 2026-09-21 |
| [linksawakening/jev-harness](https://github.com/linksawakening/jev-harness) | Self-hosted project harness: code owns the loop, TypeSafe Jev owns the judgments, the LLM owns the content. | 0 | Python | 2026-09-21 |
| [liou666/senseek](https://github.com/liou666/senseek) | Senseek — Semantic Page Search browser extension. Find what you mean. Powerd by Jev | 0 | JavaScript | 2026-09-21 |
| [lirantal/discoprint](https://github.com/lirantal/discoprint) | Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it a… | 0 | JavaScript | 2026-09-21 |
| [listepo/cox](https://github.com/listepo/cox) | A modular terminal coding agent in Rust with a safe, event-driven core. | 0 | Rust | 2026-09-20 |
| [liuup/jev-research](https://github.com/liuup/jev-research) | 📊 The third-party research implementation of jev. | 0 | Python | 2026-09-20 |
| [liuyejinghong/ai-mud](https://github.com/liuyejinghong/ai-mud) | Server-authoritative dark-fantasy Web MUD with governed AI narrative systems. | 0 | TypeScript | 2026-09-21 |
| [liyumini/Jev-driven-agent-loop](https://github.com/liyumini/Jev-driven-agent-loop) | — | 0 | TypeScript | 2026-09-20 |
| [llevasseur/my-command](https://github.com/llevasseur/my-command) | You wish is My Command | 0 | JavaScript | 2026-09-17 |
| [lorensation/llm-cost-optimizer-jev](https://github.com/lorensation/llm-cost-optimizer-jev) | An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM… | 0 | Python | 2026-09-20 |
| [LoTwT/uno-jev](https://github.com/LoTwT/uno-jev) | — | 0 | TypeScript | 2026-09-21 |
| [Loule95450/jev-free-router](https://github.com/Loule95450/jev-free-router) | Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router) | 0 | JavaScript | 2026-09-21 |
| [luanewb/jevai](https://github.com/luanewb/jevai) | — | 0 | Python | 2026-09-19 |
| [lucasfth/config](https://github.com/lucasfth/config) | Relevant config files for meee | 0 | Nix | 2026-09-18 |
| [lukasikgrzegorz/jev-ai-test](https://github.com/lukasikgrzegorz/jev-ai-test) | — | 0 | JavaScript | 2026-09-21 |
| [lukaszraczylo/oh-my-pi-schema](https://github.com/lukaszraczylo/oh-my-pi-schema) | — | 0 | TypeScript | 2026-09-17 |
| [luw2007/omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions) | OMP / pi-coding-agent extensions that delegate acceptance gating and subagent routing to the Typesafe Jev dec… | 0 | TypeScript | 2026-09-20 |
| [LVTD-LLC/games](https://github.com/LVTD-LLC/games) | Small web games, independently built. Astro catalogue at games.lvtd.dev. | 0 | JavaScript | 2026-09-18 |
| [m-mizutani/semgate](https://github.com/m-mizutani/semgate) | Semantic request filtering and routing for Go HTTP, powered by TypeSafe AI. | 0 | Go | 2026-09-21 |
| [m-naw/ux-explore](https://github.com/m-naw/ux-explore) | Goal-driven synthetic persona testing for websites: Jev decides, Playwright acts, one Sonnet report per journ… | 0 | TypeScript | 2026-09-21 |
| [maci0/rebrew](https://github.com/maci0/rebrew) | Compiler-in-the-loop decompilation workbench for binary-matching game reversing. | 0 | Python | 2026-09-21 |
| [maguro777R/jev-test](https://github.com/maguro777R/jev-test) | jevのテストをします | 0 | JavaScript | 2026-09-21 |
| [mahavirn/mnjev-cli](https://github.com/mahavirn/mnjev-cli) | CLI for JEV Model | 0 | TypeScript | 2026-09-21 |
| [mahirmlk/mahirmalik](https://github.com/mahirmlk/mahirmalik) | sharing about myself, and my work through this personal website. | 0 | TypeScript | 2026-09-21 |
| [mahynotch/newsscore](https://github.com/mahynotch/newsscore) | One number per ticker from the week's news. Async Python library + CLI, pluggable scorer, Jev by default. | 0 | Python | 2026-09-19 |
| [maito1201/jev-harness](https://github.com/maito1201/jev-harness) | TypeSafe jev でエージェントの応答を審査し、形式的な完了を Stop hook で差し戻す Claude Code / Codex plugin | 0 | JavaScript | 2026-09-21 |
| [makefunstuff/clank](https://github.com/makefunstuff/clank) | minimal unix-style local-inference cli | 0 | Rust | 2026-09-20 |
| [makefunstuff/jev-lsp](https://github.com/makefunstuff/jev-lsp) | An LSP server whose ambient pass runs the rules a repository states in `.jev/rules/*.json`: each candidate li… | 0 | Rust | 2026-09-21 |
| [makeorbreakshop/djr3x_voice](https://github.com/makeorbreakshop/djr3x_voice) | — | 0 | Python | 2026-09-17 |
| [ManatoYamashita/tcu-setagayafes97-web](https://github.com/ManatoYamashita/tcu-setagayafes97-web) | 東京都市大学 第97回世田谷祭（2026）のwebサイト | 0 | TypeScript | 2026-09-21 |
| [MANI8148/the-daily-byte](https://github.com/MANI8148/the-daily-byte) | — | 0 | TypeScript | 2026-09-21 |
| [manjunathshiva/jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench) | TypeSafe Jev 1.13 vs Claude Fable 5.1, GPT-6 Astra, Kimi K3, MiniMax M3 and DeepSeek V4.1 Flash on 200 typed … | 0 | Python | 2026-09-20 |
| [manutej/jev](https://github.com/manutej/jev) | JEV — applied double operadic type system (Libkind–Myers, arXiv:2505.18329). Colored operads, masked-language… | 0 | TypeScript | 2026-09-21 |
| [maraichr/jev-triage](https://github.com/maraichr/jev-triage) | Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter | 0 | JavaScript | 2026-09-20 |
| [marcelormendes/diffninja](https://github.com/marcelormendes/diffninja) | Focused local PR reviews with calldiff and Jev | 0 | TypeScript | 2026-09-21 |
| [MarcoLoDico/pi-jev-router](https://github.com/MarcoLoDico/pi-jev-router) | — | 0 | JavaScript | 2026-09-21 |
| [marcosmartinez/jev-acento](https://github.com/marcosmartinez/jev-acento) | ¿Jev entiende tu acento? Pre-registered audit of TypeSafe AI's Jev on Spanish — accuracy, calibration and tok… | 0 | Python | 2026-09-21 |
| [mas2194/maybe-jev-bySol](https://github.com/mas2194/maybe-jev-bySol) | — | 0 | HTML | 2026-09-21 |
| [mashmalol/Vis-Jev-vibe](https://github.com/mashmalol/Vis-Jev-vibe) | — | 0 | HTML | 2026-09-19 |
| [maskjelly/TiVM](https://github.com/maskjelly/TiVM) | Computer-use agent for a throwaway Linux desktop: AT-SPI accessibility-tree perception, TypeSafe Jev / GPT-5.… | 0 | Python | 2026-09-20 |
| [matt-riley/pi-extensions](https://github.com/matt-riley/pi-extensions) | Personal pi extension collection: /exit alias, read-only /plan mode | 0 | JavaScript | 2026-09-21 |
| [mattneel/typesafe.zig](https://github.com/mattneel/typesafe.zig) | An idiomatic Zig client for the TypeSafe AI API | 0 | Zig | 2026-09-18 |
| [matu79go/jev-hanko](https://github.com/matu79go/jev-hanko) | Measuring TypeSafe AI's Jev on 41-clause contract review (CUAD, 20,500 decisions) against fast, cheap LLMs — … | 0 | Python | 2026-09-21 |
| [mavericksxx/typesafe-jev-history-globe](https://github.com/mavericksxx/typesafe-jev-history-globe) | — | 0 | TypeScript | 2026-09-21 |
| [max-lau/drone-swarm-max01](https://github.com/max-lau/drone-swarm-max01) | Command & control console for a 10,970-drone disaster-response swarm (scaling to 109,700). Three.js + Mapbox … | 0 | TypeScript | 2026-09-20 |
| [max1874/open-computer-use](https://github.com/max1874/open-computer-use) | A macOS computer-use agent with a dynamic, indexed action space. No screenshots, no coordinates. A macOS port… | 0 | Python | 2026-09-20 |
| [maybern-tripp-smith/fedjev-bench](https://github.com/maybern-tripp-smith/fedjev-bench) | FOMC hawkishness: TypeSafe Jev pairwise Choice vs rate actions (+ Haiku 4.5 comparison). Pages in /docs. | 0 | Python | 2026-09-21 |
| [mayonaka-ratori/60s-magic](https://github.com/mayonaka-ratori/60s-magic) | — | 0 | TypeScript | 2026-09-21 |
| [mcgalleg/grokbot-jev-jobs](https://github.com/mcgalleg/grokbot-jev-jobs) | Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cro… | 0 | TypeScript | 2026-09-19 |
| [meaningfree/jev-work](https://github.com/meaningfree/jev-work) | — | 0 | JavaScript | 2026-09-20 |
| [mednabouli/jev-ai-polymarket-copy-trading](https://github.com/mednabouli/jev-ai-polymarket-copy-trading) | Automated Polymarket copy trading bot with MCP servers, Telegram alerts, and profitable wallet tracking. Zero… | 0 | Python | 2026-09-21 |
| [meimingqi222/pi-plugins](https://github.com/meimingqi222/pi-plugins) | A bun workspace of independently published pi extensions: secret redaction (pi-redact) and Jev-based verbatim… | 0 | TypeScript | 2026-09-21 |
| [memeshee/nansen-league](https://github.com/memeshee/nansen-league) | A Telegram game where you draft proven smart-money wallets into weekly rounds settled on live Nansen PnL — pl… | 0 | Python | 2026-09-21 |
| [memorysaver/jev-atari-lab](https://github.com/memorysaver/jev-atari-lab) | Challenge Atari with Jev: structured decisions, value questions, and replayable experiments | 0 | Python | 2026-09-21 |
| [metrox-eth/moss-jev](https://github.com/metrox-eth/moss-jev) | MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision … | 0 | JavaScript | 2026-09-20 |
| [mfreeze77/oil](https://github.com/mfreeze77/oil) | — | 0 | Python | 2026-09-21 |
| [mheers/typesafeai-systemone-jev-go](https://github.com/mheers/typesafeai-systemone-jev-go) | Typed Go client for the TypeSafe System One API (Jev): structured questions and answers your code can act on.… | 0 | Go | 2026-09-21 |
| [mhingston/jev-cli](https://github.com/mhingston/jev-cli) | A small, provider-agnostic CLI for Jev. | 0 | TypeScript | 2026-09-21 |
| [mhmdkzr/jev](https://github.com/mhmdkzr/jev) | An unofficial Go client for TypeSafe's System One Jev model | 0 | Go | 2026-09-18 |
| [michaeljabbour/amplifier-bundle-fast-decisions](https://github.com/michaeljabbour/amplifier-bundle-fast-decisions) | Fast-decision layer for Amplifier: telemetry hook, read-only workspace tool, and an opt-in shadow/active deci… | 0 | Python | 2026-09-20 |
| [MidasMulli/kev-ane](https://github.com/MidasMulli/kev-ane) | Kev-0.6B, a Jev-class decision model, running on the Apple Neural Engine — with the gates and instruments use… | 0 | Python | 2026-09-21 |
| [mihir-s-05/jev-reward-model](https://github.com/mihir-s-05/jev-reward-model) | — | 0 | Python | 2026-09-18 |
| [mikaelweiss/dotfiles](https://github.com/mikaelweiss/dotfiles) | — | 0 | Shell | 2026-09-20 |
| [mikekelly/ex_jev](https://github.com/mikekelly/ex_jev) | — | 0 | Elixir | 2026-09-21 |
| [Milluna/jev-cloth](https://github.com/Milluna/jev-cloth) | — | 0 | HTML | 2026-09-21 |
| [Milo318/mailordinal](https://github.com/Milo318/mailordinal) | Decision-native enterprise inbox: typed AI signals, deterministic priority policy, confidence-aware routing. | 0 | TypeScript | 2026-09-20 |
| [minhgv/jev-mcp](https://github.com/minhgv/jev-mcp) | TypeSafe Jev MCP decision layer for coding agents and CI | 0 | TypeScript | 2026-09-18 |
| [Mishkun/judge-jev](https://github.com/Mishkun/judge-jev) | — | 0 | TypeScript | 2026-09-21 |
| [Mitravasu/jevu](https://github.com/Mitravasu/jevu) | JevU | 0 | Python | 2026-09-21 |
| [mittal-parth/jev-experiments](https://github.com/mittal-parth/jev-experiments) | — | 0 | Python | 2026-09-18 |
| [mizchi/jev-gomoku](https://github.com/mizchi/jev-gomoku) | — | 0 | MoonBit | 2026-09-18 |
| [mjj2332/Quincy_Portal](https://github.com/mjj2332/Quincy_Portal) | Photos review and delivery web app | 0 | TypeScript | 2026-09-21 |
| [mjyoke1111/jev-lab](https://github.com/mjyoke1111/jev-lab) | Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks | 0 | TypeScript | 2026-09-21 |
| [mkruglikov/droidjev](https://github.com/mkruglikov/droidjev) | A fast, screenshot-free Android emulator clicker powered by TypeSafe's jev | 0 | JavaScript | 2026-09-20 |
| [mleyvaz/jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse) | Jev (TypeSafe AI) y el colapso entre conflicto e ignorancia. 3 experimentos via Vercel AI Gateway. Nota de ca… | 0 | Python | 2026-09-20 |
| [modal-projects/goodhart](https://github.com/modal-projects/goodhart) | Jev for preventing reward hacking. | 0 | Python | 2026-09-20 |
| [mohammedwessam2007/uberbondd](https://github.com/mohammedwessam2007/uberbondd) | — | 0 | JavaScript | 2026-09-21 |
| [mohannadize/jev-ielts-test](https://github.com/mohannadize/jev-ielts-test) | — | 0 | TypeScript | 2026-09-19 |
| [MohtashamMurshid/jev-speed-test](https://github.com/MohtashamMurshid/jev-speed-test) | Reproducible Jev vs fast LLM experiment: BANKING77 data, raw responses, confidence evaluation, and analysis | 0 | HTML | 2026-09-21 |
| [MokiMeow/jev-fabric](https://github.com/MokiMeow/jev-fabric) | A typed decision control plane for bounded semantic choices with Jev and AI agents. | 0 | TypeScript | 2026-09-21 |
| [mondaychen/semantic-assert](https://github.com/mondaychen/semantic-assert) | Testing lib for asserting the real requirement. | 0 | TypeScript | 2026-09-21 |
| [monet88/chang-store](https://github.com/monet88/chang-store) | — | 0 | TypeScript | 2026-09-21 |
| [MoonTory/pi-jev-harness](https://github.com/MoonTory/pi-jev-harness) | Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards to… | 0 | TypeScript | 2026-09-18 |
| [MoRohn/meridian-demo](https://github.com/MoRohn/meridian-demo) | Meridian \| AI context-intake and contraction risk & compliance micro-app with live TypeSafe AI vs OpenAI eva… | 0 | TypeScript | 2026-09-21 |
| [moto-taka/jev-orchestrator](https://github.com/moto-taka/jev-orchestrator) | — | 0 | TypeScript | 2026-09-19 |
| [mozhuanzuojing/dsh-shadow](https://github.com/mozhuanzuojing/dsh-shadow) | dsh-shadow: agent 思维/上下文/灵魂的投影记忆树(一切皆文件,一记忆一文件,read_shadow 可穿透) | 0 | TypeScript | 2026-09-21 |
| [mpiv-ai/bb-plugin-typesafe-router](https://github.com/mpiv-ai/bb-plugin-typesafe-router) | Routes a thread's first message to the right harness and model with TypeSafe (Jev), then asks you to confirm. | 0 | TypeScript | 2026-09-18 |
| [MrDesjardins/jev-send-guard](https://github.com/MrDesjardins/jev-send-guard) | — | 0 | Python | 2026-09-19 |
| [mrkpatchaa/dotfiles](https://github.com/mrkpatchaa/dotfiles) | My dot files | 0 | Shell | 2026-09-20 |
| [Mrmimee/hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev) | Jev (TypeSafe AI) System One decision engine plugin for Hermes Agent, backed by Agnes AI Flash. | 0 | Python | 2026-09-20 |
| [MrTrigger/yardmaster](https://github.com/MrTrigger/yardmaster) | Routing layer for AI coding agents: model, effort and account selection with quota pacing | 0 | Rust | 2026-09-21 |
| [mtane0412/chat-sensei](https://github.com/mtane0412/chat-sensei) | Twitchのライブチャットから自分だけの語学教材を作る、Chrome内蔵AI(Gemini Nano)だけで完結するクライアントサイド専用ツール | 0 | TypeScript | 2026-09-19 |
| [mudassirnizamani/Bindery](https://github.com/mudassirnizamani/Bindery) | — | 0 | Python | 2026-09-21 |
| [mugenkyou/JEV-VS-ML](https://github.com/mugenkyou/JEV-VS-ML) | — | 0 | Jupyter Notebook | 2026-09-21 |
| [Muhammad-Zain01/jev-real-usecases](https://github.com/Muhammad-Zain01/jev-real-usecases) | — | 0 | Python | 2026-09-20 |
| [muratcanberber/JEV-TheFishGame](https://github.com/muratcanberber/JEV-TheFishGame) | 🐠 A multiplayer fish game where every AI decision is a TypeSafe Jev (System One) call — flee, hunt, roam, wit… | 0 | JavaScript | 2026-09-21 |
| [mushfiqk47/lms-jev](https://github.com/mushfiqk47/lms-jev) | Semantic ifs from open models, on a 3090 at home — or through LM Studio | 0 | Python | 2026-09-20 |
| [muthuishere/jevd](https://github.com/muthuishere/jevd) | Inference server for the openjev NLI cross-encoder. One command, downloads on first run, CPU and GPU. | 0 | Rust | 2026-09-20 |
| [Muzych/jev-x-tags](https://github.com/Muzych/jev-x-tags) | Tag X/Twitter accounts with TypeSafe Jev and hide posts by tag (Chrome MV3 / WXT). | 0 | TypeScript | 2026-09-21 |
| [myokoym/misereru-slide-jev](https://github.com/myokoym/misereru-slide-jev) | — | 0 | JavaScript | 2026-09-20 |
| [n-yokomachi/jev-dev](https://github.com/n-yokomachi/jev-dev) | 同じ発言を jev と LLM の両方に判定させ、感情の変動値のズレと応答速度を1画面で見比べるデモ（affectus + Vercel AI Gateway） | 0 | TypeScript | 2026-09-18 |
| [n0nuser/battlesnake-jev](https://github.com/n0nuser/battlesnake-jev) | A Battlesnake in Go where deterministic code owns tactics and a TypeSafe Jev classifier gets the judgment cal… | 0 | Go | 2026-09-20 |
| [nak1b/jev-experiments](https://github.com/nak1b/jev-experiments) | Small experiments with Jev by TypeSafe | 0 | TypeScript | 2026-09-21 |
| [NaluKicks-808/jev-field-guide-skill](https://github.com/NaluKicks-808/jev-field-guide-skill) | A Claude Code skill of field notes on Jev: which question shape fits which job, how to test a use before trus… | 0 | — | 2026-09-21 |
| [NaluKicks-808/jev-field-trial](https://github.com/NaluKicks-808/jev-field-trial) | A pre-registered field trial of Jev (TypeSafe's judgment model) on a second brain and Claude Code history: 20… | 0 | Python | 2026-09-21 |
| [NaluKicks-808/vault-search-bench](https://github.com/NaluKicks-808/vault-search-bench) | Test search over any Obsidian vault with zero labelling: the vault's own links are the answer key. Plain rank… | 0 | Python | 2026-09-21 |
| [namayasai/backstage-jev-operations-support](https://github.com/namayasai/backstage-jev-operations-support) | Jev-powered operations decision support for Backstage: readiness checks, incident triage, change review, temp… | 0 | TypeScript | 2026-09-21 |
| [nanami-0713/jev-resume-screening](https://github.com/nanami-0713/jev-resume-screening) | TypeSafe Jev (System One) 简历-JD 匹配度初筛：判据模板 + 正/负/陷阱三类样本测试档案，判据 v1→v3 迭代全程可复现 / Resume-JD screening with TypeS… | 0 | JavaScript | 2026-09-20 |
| [nardinmarcus/pi-jev-typesafe](https://github.com/nardinmarcus/pi-jev-typesafe) | TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discove… | 0 | TypeScript | 2026-09-19 |
| [narulaskaran/jev-data-questions](https://github.com/narulaskaran/jev-data-questions) | — | 0 | TypeScript | 2026-09-20 |
| [Nasrallah-AL/sessionwise](https://github.com/Nasrallah-AL/sessionwise) | Analyze, understand, and optimize AI sessions. Claude Code adapter, model-fit/cache/context/health metrics, o… | 0 | TypeScript | 2026-09-20 |
| [nawwwal/seriph](https://github.com/nawwwal/seriph) | — | 0 | TypeScript | 2026-09-18 |
| [naz3eh/raycast-jev](https://github.com/naz3eh/raycast-jev) | — | 0 | TypeScript | 2026-09-21 |
| [nekowasabi/jev-routing-mcp](https://github.com/nekowasabi/jev-routing-mcp) | — | 0 | TypeScript | 2026-09-18 |
| [neohum/class_game](https://github.com/neohum/class_game) | — | 0 | TypeScript | 2026-09-20 |
| [neohum/manuscript_editor](https://github.com/neohum/manuscript_editor) | — | 0 | TypeScript | 2026-09-20 |
| [neohum/pro-study](https://github.com/neohum/pro-study) | C23 & Go 프로젝트 학습 플랫폼 & E-ink 필사 앱 | 0 | TypeScript | 2026-09-21 |
| [neohum/Treasure-Collection](https://github.com/neohum/Treasure-Collection) | 5학년 역사 디지털 보물도감 — 크롬북 PWA, all_market 교실 허브 번들 | 0 | TypeScript | 2026-09-20 |
| [NeOMakinG/kev-model-router](https://github.com/NeOMakinG/kev-model-router) | Jev-style model routing powered by kev — a tiny local System One model classifies every request and picks the… | 0 | Python | 2026-09-21 |
| [neostryder/mercury](https://github.com/neostryder/mercury) | Semantic email filtering for rpgm.tools - Loremaster-reviewed spam/phishing triage via ForwardEmail webhooks | 0 | Python | 2026-09-21 |
| [nevzataksoy/jev-trader-bybit](https://github.com/nevzataksoy/jev-trader-bybit) | — | 0 | TypeScript | 2026-09-21 |
| [ngouard5/jeveuxaider-design](https://github.com/ngouard5/jeveuxaider-design) | — | 0 | HTML | 2026-09-21 |
| [ngpestelos-mirrors/hermes-agent](https://github.com/ngpestelos-mirrors/hermes-agent) | Mirror of NousResearch/hermes-agent (full history) | 0 | Python | 2026-09-21 |
| [ngpestelos-mirrors/openclaw](https://github.com/ngpestelos-mirrors/openclaw) | Public full-history mirror of openclaw/openclaw (not a fork) | 0 | TypeScript | 2026-09-21 |
| [Nibir1/typesafe-go](https://github.com/Nibir1/typesafe-go) | Zero-dependency Go SDK for TypeSafe's System One API (Jev). Typed questions in, calibrated probabilities out … | 0 | Go | 2026-09-19 |
| [nickylin/jev-harness](https://github.com/nickylin/jev-harness) | Typed decision control plane for agents, powered by TypeSafe Jev | 0 | TypeScript | 2026-09-20 |
| [nicolasalveshenrique-spec/medical-knowledge-triage](https://github.com/nicolasalveshenrique-spec/medical-knowledge-triage) | A typed decision-routing prototype for turning medical learning material into deterministic study actions, de… | 0 | — | 2026-09-21 |
| [nighthawk6389/Jev-credit-agreement-parser](https://github.com/nighthawk6389/Jev-credit-agreement-parser) | — | 0 | Python | 2026-09-21 |
| [nikotaronosuke/jev-voice-decision](https://github.com/nikotaronosuke/jev-voice-decision) | Japanese speech → local STT → Jev typed decisions → deterministic actions. | 0 | Python | 2026-09-20 |
| [nirgal-soft/typesafe-rs](https://github.com/nirgal-soft/typesafe-rs) | A rust client for the TypeSafe AI API | 0 | Rust | 2026-09-21 |
| [nishimotz/hello-jev](https://github.com/nishimotz/hello-jev) | — | 0 | Python | 2026-09-19 |
| [nitro527/jev_project](https://github.com/nitro527/jev_project) | — | 0 | Python | 2026-09-19 |
| [Nixz0824/rag-jev](https://github.com/Nixz0824/rag-jev) | 国服《英雄联盟》版本更新公告的本地 RAG 问答：数字只来自公告，Jev（TypeSafe System One）负责候选重排与回答自检 | 0 | Python | 2026-09-21 |
| [nmfisher/tina](https://github.com/nmfisher/tina) | Tina — a terminal multi-agent coding TUI (Tina Is No Agent) | 0 | Dart | 2026-09-21 |
| [noahbclarkson/typesafe-api-rs](https://github.com/noahbclarkson/typesafe-api-rs) | Ergonomic, strongly typed Rust client for the TypeSafe System One API (Jev) | 0 | Rust | 2026-09-21 |
| [Nomarcus/FoodSim](https://github.com/Nomarcus/FoodSim) | — | 0 | HTML | 2026-09-21 |
| [NoRaincheck/gliger](https://github.com/NoRaincheck/gliger) | Jev Adapter for GLiClass (GLiNER) Models | 0 | Python | 2026-09-20 |
| [notCorwin/SurfWax](https://github.com/notCorwin/SurfWax) | Chrome 侧边栏智能体插件 | 0 | TypeScript | 2026-09-21 |
| [notdogus/ai-adblocker](https://github.com/notdogus/ai-adblocker) | — | 0 | TypeScript | 2026-09-21 |
| [notfresh/big-news-at-2026](https://github.com/notfresh/big-news-at-2026) | — | 0 | — | 2026-09-21 |
| [ns2250225/voice-magic](https://github.com/ns2250225/voice-magic) | 基于jev模型的语音释放魔法技能网站 | 0 | JavaScript | 2026-09-21 |
| [nsillik/jevvin-off](https://github.com/nsillik/jevvin-off) | Prototyping against TypeSafe's Jev System One API: a one-ticket quickstart and a Bluesky Jetstream firehose d… | 0 | — | 2026-09-21 |
| [Nsilswal/opencode-toolrouter](https://github.com/Nsilswal/opencode-toolrouter) | opencode plugin: send the model only the MCP tools each request needs, picked by TypeSafe's Jev | 0 | TypeScript | 2026-09-19 |
| [oat431/oralita_md](https://github.com/oat431/oralita_md) | — | 0 | HTML | 2026-09-21 |
| [obekt/jev-agentic-ops](https://github.com/obekt/jev-agentic-ops) | — | 0 | Python | 2026-09-19 |
| [oceanByte/tsai-cli](https://github.com/oceanByte/tsai-cli) | Unofficial CLI for the TypeSafe AI System One API. | 0 | TypeScript | 2026-09-21 |
| [octanevz/jev-playground-openrouter](https://github.com/octanevz/jev-playground-openrouter) | Local browser playground for TypeSafe's Jev decision model via OpenRouter. Python stdlib only. | 0 | JavaScript | 2026-09-20 |
| [octkmr/jev-demo](https://github.com/octkmr/jev-demo) | — | 0 | HTML | 2026-09-20 |
| [oguressive/sample-jev](https://github.com/oguressive/sample-jev) | — | 0 | TypeScript | 2026-09-21 |
| [oh-ashen-one/jev-lab](https://github.com/oh-ashen-one/jev-lab) | — | 0 | JavaScript | 2026-09-20 |
| [ohernandezdev/jevmod](https://github.com/ohernandezdev/jevmod) | Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you ow… | 0 | Python | 2026-09-20 |
| [Okura66/kahn1](https://github.com/Okura66/kahn1) | High-throughput, sub-20ms System 1 decision engine on LLM logits. Zero text generation, calibrated probabilit… | 0 | Python | 2026-09-21 |
| [oluwadunni1/Instagram](https://github.com/oluwadunni1/Instagram) | — | 0 | Python | 2026-09-21 |
| [OmarAlaaeldein/jev-verifier-skill](https://github.com/OmarAlaaeldein/jev-verifier-skill) | Fast 'System One' reflex for reasoning LLMs: typed probabilistic second opinions from Jev via OpenCode Zen, w… | 0 | — | 2026-09-21 |
| [omerfeyzioglu/JevOps](https://github.com/omerfeyzioglu/JevOps) | — | 0 | Python | 2026-09-21 |
| [Openclaw-D/HUMAN-AGENT-LOOP](https://github.com/Openclaw-D/HUMAN-AGENT-LOOP) | — | 0 | JavaScript | 2026-09-21 |
| [openprose/prose-cli](https://github.com/openprose/prose-cli) | — | 0 | Python | 2026-09-21 |
| [oqzl/JevSamples](https://github.com/oqzl/JevSamples) | — | 0 | JavaScript | 2026-09-21 |
| [Oracle0703/xyai](https://github.com/Oracle0703/xyai) | 这是我们新项目的第一步 | 0 | Go | 2026-09-21 |
| [orlenko/aiq](https://github.com/orlenko/aiq) | Quota-aware router for pooled Claude Code and Codex subscriptions: PATH shims, rollover scoring, long-session… | 0 | Go | 2026-09-20 |
| [orlenko/skills](https://github.com/orlenko/skills) | — | 0 | Python | 2026-09-19 |
| [orvn/typesafe-tidbits](https://github.com/orvn/typesafe-tidbits) | — | 0 | TypeScript | 2026-09-20 |
| [OsirianLegacy/JevSimulation](https://github.com/OsirianLegacy/JevSimulation) | Building a Simulated world using Typesafe Ai's Jev to run entity choices, C++ 20, JSON for Jev Interactions, … | 0 | — | 2026-09-21 |
| [OsirianLegacy/JevTactics](https://github.com/OsirianLegacy/JevTactics) | — | 0 | JavaScript | 2026-09-19 |
| [OVRLab/jev-guided-decoding](https://github.com/OVRLab/jev-guided-decoding) | — | 0 | — | 2026-09-21 |
| [owainlewis/jev-examples](https://github.com/owainlewis/jev-examples) | Examples on how to use the AI model Jev. | 0 | Python | 2026-09-21 |
| [OxFrancesco/BeeGreat](https://github.com/OxFrancesco/BeeGreat) | — | 0 | TypeScript | 2026-09-21 |
| [ozzy2438/apply-os](https://github.com/ozzy2438/apply-os) | Apply OS — Personal career decision engine powered by TypeSafe AI (Jev). Ranks job postings, drafts applicati… | 0 | — | 2026-09-20 |
| [ozzy2438/flow-desk](https://github.com/ozzy2438/flow-desk) | Evidence-backed job discovery workspace with parallel browser flows, Jev-based typed decisions, and human-app… | 0 | — | 2026-09-21 |
| [pablozr/JevGuard](https://github.com/pablozr/JevGuard) | — | 0 | TypeScript | 2026-09-20 |
| [pakkio/nexus](https://github.com/pakkio/nexus) | — | 0 | Python | 2026-09-18 |
| [pangpond/herdr-theme-cobalt2](https://github.com/pangpond/herdr-theme-cobalt2) | Cobalt2 theme for Herdr (adapted from wesbos/cobalt2-iterm) | 0 | Python | 2026-09-18 |
| [pathak-r/how-good-is-jev](https://github.com/pathak-r/how-good-is-jev) | How good is Jev? TypeSafe Jev vs an LLM on the same intent-routing task. | 0 | TypeScript | 2026-09-21 |
| [PatrickLaflamme/typesafe-llm-router](https://github.com/PatrickLaflamme/typesafe-llm-router) | Experimental Typesafe.ai smart router: route prompts to LLMs with caching and cost awareness | 0 | Rust | 2026-09-20 |
| [Paul-Sizon/tab-organizer](https://github.com/Paul-Sizon/tab-organizer) | Chrome extension that groups your open tabs by category using TypeSafe AI | 0 | TypeScript | 2026-09-19 |
| [PavelLizunov/jev-sentinel](https://github.com/PavelLizunov/jev-sentinel) | — | 0 | Rust | 2026-09-21 |
| [pb-crackers/Jev-Cognigy-QA-Suite](https://github.com/pb-crackers/Jev-Cognigy-QA-Suite) | Score every Cognigy conversation against rubrics you write, using TypeSafe Jev instead of an LLM. CLI, local … | 0 | TypeScript | 2026-09-21 |
| [pedroknigge/mcp_jev](https://github.com/pedroknigge/mcp_jev) | Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor & agents | 0 | TypeScript | 2026-09-20 |
| [pedrorau/feedback-radar-jev](https://github.com/pedrorau/feedback-radar-jev) | — | 0 | Astro | 2026-09-21 |
| [peekuh/jev-vs-rerankers](https://github.com/peekuh/jev-vs-rerankers) | — | 0 | Python | 2026-09-20 |
| [PerryLink/jevcore](https://github.com/PerryLink/jevcore) | TypeSafe Jev for DeepSeek Harness, the Model Context Protocol, and plain Node: typed judgments instead of pro… | 0 | TypeScript | 2026-09-21 |
| [peskycipher/jevBMAD](https://github.com/peskycipher/jevBMAD) | — | 0 | Python | 2026-09-20 |
| [petercr/jev-orchestrator](https://github.com/petercr/jev-orchestrator) | An mini node orchestrator that uses Jev to handle routing to different LLMs based on difficulty. | 0 | TypeScript | 2026-09-21 |
| [peterrauscher/x-bookmark-sorter](https://github.com/peterrauscher/x-bookmark-sorter) | Chrome extension (Manifest V3) that auto-sorts your X bookmarks into your own folders using TypeSafe's Jev de… | 0 | JavaScript | 2026-09-21 |
| [phanngoc/browser-ai](https://github.com/phanngoc/browser-ai) | Jev-driven browser agent in pure Go — CDP over pipe/WebSocket, attach to real Chrome, built to measure real s… | 0 | Go | 2026-09-20 |
| [phareim/sfl](https://github.com/phareim/sfl) | Save For Later | 0 | JavaScript | 2026-09-19 |
| [phin-tech/pi-jev-approver](https://github.com/phin-tech/pi-jev-approver) | Shell command safety gate for the Pi coding agent, backed by TypeSafe's Jev judgment model | 0 | TypeScript | 2026-09-19 |
| [phureewat29/jev-moviebox](https://github.com/phureewat29/jev-moviebox) | Movies Recommendation Engine with Jev | 0 | TypeScript | 2026-09-21 |
| [phurley/daily-brief](https://github.com/phurley/daily-brief) | A sourced southeast Michigan daily brief generated by AI Overwatch | 0 | Python | 2026-09-21 |
| [pianistprogrammer/Jev-Browser](https://github.com/pianistprogrammer/Jev-Browser) | — | 0 | TypeScript | 2026-09-21 |
| [Pimmetjeoss/tribe-crm-jev](https://github.com/Pimmetjeoss/tribe-crm-jev) | TypeSafe Jev-powered lead intake and live CRM judgment demo for Tribe CRM | 0 | TypeScript | 2026-09-19 |
| [Pinutss/jev-agent-router](https://github.com/Pinutss/jev-agent-router) | Explainable AI agent selection with abstention, bounded fallback, and a multi-LLM catalog. | 0 | Python | 2026-09-18 |
| [Pinutss/jev-memory-selector](https://github.com/Pinutss/jev-memory-selector) | Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker. | 0 | Python | 2026-09-18 |
| [Pizzawookiee/jev-tree-memory](https://github.com/Pizzawookiee/jev-tree-memory) | TypeSafe’s Jev AI + an n-ary memory tree = efficient agentic memory routing and retrieval. | 0 | Python | 2026-09-21 |
| [pjrpjr/qingliu](https://github.com/pjrpjr/qingliu) | X 时间线清洁工 · FeedSieve(MIT) 衍生 · 带实测标定的 AI 判定层：误杀 0.7%，还能抓词库认不出的 47% | 0 | TypeScript | 2026-09-19 |
| [pksorensen/alp-pr-review](https://github.com/pksorensen/alp-pr-review) | ALP-linje: PR-review med Jev-routing (TypeSafe System One) og automerge bag port | 0 | JavaScript | 2026-09-20 |
| [plm66/hermes-delegate](https://github.com/plm66/hermes-delegate) | Route subagents to the right Hermes profile — model, provider, credentials, and personality per delegate_task… | 0 | Python | 2026-09-21 |
| [Plyntr-LLC/brain-app](https://github.com/Plyntr-LLC/brain-app) | Brain: the room in front of Agency Brain | 0 | TypeScript | 2026-09-21 |
| [pminnebach/hookmon](https://github.com/pminnebach/hookmon) | — | 0 | Go | 2026-09-20 |
| [ponyo877/jev-realtime-brain-scanner](https://github.com/ponyo877/jev-realtime-brain-scanner) | — | 0 | JavaScript | 2026-09-19 |
| [pozapas/jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding) | Calibrated conversion of police crash narratives into probabilistic crash variables with a System One model. … | 0 | Python | 2026-09-21 |
| [pozapas/jev-gold-labeling](https://github.com/pozapas/jev-gold-labeling) | Blind human labelling app for the Jev crash-narrative calibration reference set (private: contains redacted C… | 0 | TypeScript | 2026-09-21 |
| [Pragyan330/WHAT-s-Up-jev](https://github.com/Pragyan330/WHAT-s-Up-jev) | — | 0 | Python | 2026-09-21 |
| [pravinl23/htn2026](https://github.com/pravinl23/htn2026) | — | 0 | TypeScript | 2026-09-20 |
| [priyankark/jev-state](https://github.com/priyankark/jev-state) | Build and regression-test conversational state machines powered by Jev. Inspect decisions, capture failing co… | 0 | TypeScript | 2026-09-21 |
| [proshano/KCRU-website](https://github.com/proshano/KCRU-website) | — | 0 | JavaScript | 2026-09-20 |
| [PsyChaos/ai-team-harness](https://github.com/PsyChaos/ai-team-harness) | — | 0 | Python | 2026-09-21 |
| [pulseforgeatmns-ops/pulseforge-leadgen](https://github.com/pulseforgeatmns-ops/pulseforge-leadgen) | Modular AI platform for workflow automation, multi-agent orchestration, knowledge management, and human-gover… | 0 | JavaScript | 2026-09-21 |
| [punitarani/jeve](https://github.com/punitarani/jeve) | — | 0 | Python | 2026-09-21 |
| [qiaohaojie/Jev-MongoDB](https://github.com/qiaohaojie/Jev-MongoDB) | Real-time FMCG customer care triage: MongoDB Change Streams + TypeSafe Jev | 0 | JavaScript | 2026-09-21 |
| [Qingbolan/llm2jev-releases](https://github.com/Qingbolan/llm2jev-releases) | Inspired by Jev. Turn LLMs into decision engines—score choices, skip the chat. | 0 | Python | 2026-09-21 |
| [qpdbcoocdbqp/Geki-teikokukagekidan-kai](https://github.com/qpdbcoocdbqp/Geki-teikokukagekidan-kai) | Explore Jev in browser used. Playing with 檄! 帝国華撃団（改）. | 0 | Python | 2026-09-21 |
| [qte77/2026-09-12-WandB-AGIH-CoreWeave-Hack](https://github.com/qte77/2026-09-12-WandB-AGIH-CoreWeave-Hack) | A small, real critique-refine agent loop fixing Elixir bugs: a cheap draft model attempts a fix, the fix is g… | 0 | Python | 2026-09-13 |
| [quinnjr/opencode-jev-compaction](https://github.com/quinnjr/opencode-jev-compaction) | Jev-powered context compaction plugin for opencode: prune stale tool calls and results before every request, … | 0 | TypeScript | 2026-09-21 |
| [Quintonhogshead/docproof](https://github.com/Quintonhogshead/docproof) | LLM-assisted grammar review and InDesign layout prep for Word and InDesign documents | 0 | Python | 2026-09-19 |
| [r1z4x/tezgah](https://github.com/r1z4x/tezgah) | One shared working contract for every AI coding assistant you run: Claude Code, Codex, Cursor, opencode, dsh … | 0 | Python | 2026-09-21 |
| [rachit-srivastava-devx/jev-classification-benchmark](https://github.com/rachit-srivastava-devx/jev-classification-benchmark) | Benchmarking TypeSafe Jev against 15 chat-model configurations on support-ticket classification: latency, tok… | 0 | HTML | 2026-09-20 |
| [RadRebelSam/ai4all-20c-darkpatterns](https://github.com/RadRebelSam/ai4all-20c-darkpatterns) | Detecting manipulative e-commerce website language using supervised machine learning - deployed as a Streamli… | 0 | Python | 2026-09-20 |
| [RadRebelSam/jev-decision-lab](https://github.com/RadRebelSam/jev-decision-lab) | A transparent Next.js benchmark comparing function-only personalization with a function + Jev hybrid. | 0 | Python | 2026-09-21 |
| [RadRebelSam/whichjudge.dev](https://github.com/RadRebelSam/whichjudge.dev) | Replacement matrix for cheap judge / decision models. | 0 | Python | 2026-09-21 |
| [rahiseko-alt/jev-test1](https://github.com/rahiseko-alt/jev-test1) | — | 0 | TypeScript | 2026-09-21 |
| [raitoxlol/hermes-slash-router](https://github.com/raitoxlol/hermes-slash-router) | Unified Hermes Agent + Desktop plugin: TypeSafe Jev routes misspelled, shortened, and meaning-based slash com… | 0 | JavaScript | 2026-09-21 |
| [raj8525/universal-jev](https://github.com/raj8525/universal-jev) | Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents | 0 | JavaScript | 2026-09-19 |
| [Rajeev-SG/jev-tests](https://github.com/Rajeev-SG/jev-tests) | — | 0 | Python | 2026-09-20 |
| [rapidstartup/jevbench](https://github.com/rapidstartup/jevbench) | JevBench public leaderboard site (jevbench.dev) | 0 | JavaScript | 2026-09-20 |
| [rashedInt32/jev-gates](https://github.com/rashedInt32/jev-gates) | Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit … | 0 | JavaScript | 2026-09-20 |
| [rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens) | Do I need to look at what Claude Code just did? A calibrated verdict per stop, judged by TypeSafe Jev. Pairs … | 0 | JavaScript | 2026-09-20 |
| [ravi3594444/jev-agent1](https://github.com/ravi3594444/jev-agent1) | — | 0 | Python | 2026-09-20 |
| [Ravicha2/jev-browser](https://github.com/Ravicha2/jev-browser) | Deterministic browser loop: Jev supplies judgments, code owns control flow | 0 | JavaScript | 2026-09-21 |
| [Ravicha2/transaction-extractor](https://github.com/Ravicha2/transaction-extractor) | — | 0 | Python | 2026-09-20 |
| [rbalch/typesafeai-review](https://github.com/rbalch/typesafeai-review) | Using Typesafe.AI to generate diff reviews. | 0 | Python | 2026-09-21 |
| [rchovatiya88/cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev) | Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One… | 0 | JavaScript | 2026-09-18 |
| [reallygood83/jev-router](https://github.com/reallygood83/jev-router) | — | 0 | Python | 2026-09-21 |
| [RefoundAI/jev-editor-skill](https://github.com/RefoundAI/jev-editor-skill) | Editorial gate skill for Claude Code and other agents. Scores a draft on AI tells, your own voice, editorial … | 0 | Python | 2026-09-21 |
| [rei0623/AFNJP](https://github.com/rei0623/AFNJP) | 海外のAIニュースを一次情報から確認し、出典リンク付きの日本語記事として毎日届けるDiscordコミュニティ「AI Frontier News JP」の公式サイト | 0 | HTML | 2026-09-21 |
| [RemiCarbonne/jev-code-context-router](https://github.com/RemiCarbonne/jev-code-context-router) | — | 0 | Python | 2026-09-19 |
| [renatobardi/jev-o-matic](https://github.com/renatobardi/jev-o-matic) | Lab of Jev | 0 | Python | 2026-09-20 |
| [renatosousa/jev-trader](https://github.com/renatosousa/jev-trader) | — | 0 | Python | 2026-09-18 |
| [resumocast/jev-mcp](https://github.com/resumocast/jev-mcp) | Community experimental MCP server and Pi adapter for bounded TypeSafe Jev judgments | 0 | Go | 2026-09-21 |
| [rexmcintosh/ai-harness](https://github.com/rexmcintosh/ai-harness) | — | 0 | Python | 2026-09-21 |
| [rhelmer/filelathe](https://github.com/rhelmer/filelathe) | — | 0 | TypeScript | 2026-09-21 |
| [rheono/html-jev](https://github.com/rheono/html-jev) | SO-meme HTML judge on TypeSafe Jev | 0 | HTML | 2026-09-21 |
| [RichardoMrMu/jev-mini](https://github.com/RichardoMrMu/jev-mini) | Put Jev's three headline claims on trial on your own GPU. One command, a 0.5B local model: measures constrain… | 0 | Python | 2026-09-21 |
| [rinti/wagtail-jev](https://github.com/rinti/wagtail-jev) | Use jev to classify tags for pages | 0 | Python | 2026-09-21 |
| [rioriost/rspamd-jev](https://github.com/rioriost/rspamd-jev) | TypeSafe Jev shadow-evaluation plugin for Rspamd with optional GPT provider comparison | 0 | Python | 2026-09-21 |
| [riposta/pi-jev](https://github.com/riposta/pi-jev) | a Jev classification layer for the Pi coding agent | 0 | TypeScript | 2026-09-19 |
| [rivianpratama/JeVJ](https://github.com/rivianpratama/JeVJ) | — | 0 | TypeScript | 2026-09-18 |
| [rmakiyama/raincheck](https://github.com/rmakiyama/raincheck) | Every bookmark is a rain check. Find the ones worth redeeming today. | 0 | TypeScript | 2026-09-21 |
| [rnjsxodyd90/jev-relay](https://github.com/rnjsxodyd90/jev-relay) | A typed Jev decision gate, local-voice interpreter workbench, and reproducible Jev vs Qwen research. | 0 | JavaScript | 2026-09-20 |
| [rnldsalili/email-triage-badi](https://github.com/rnldsalili/email-triage-badi) | Personal Gmail triage on Cloudflare Workers with Hono, Jev, Drizzle, and Bun | 0 | JavaScript | 2026-09-20 |
| [Robertzu43/system-one-security-triage](https://github.com/Robertzu43/system-one-security-triage) | Recorded comparison of Jev, Terra, and Opus on 100 synthetic security-triage cases, five passes each, with a … | 0 | TypeScript | 2026-09-21 |
| [robokrunch/jev-physical-ai](https://github.com/robokrunch/jev-physical-ai) | Putting TypeSafe's Jev to work on robots, fleets, and edge hardware — real measured numbers, honestly caveate… | 0 | Python | 2026-09-20 |
| [rockjoel/local-skill-router](https://github.com/rockjoel/local-skill-router) | Local-first skill router for coding agents. Inspired by TypeSafe Jev; optional swappable judge (not an offici… | 0 | Python | 2026-09-19 |
| [roguefort-dev/TrashCompact](https://github.com/roguefort-dev/TrashCompact) | Deterministic transcript cleanup and compaction support using TypeSafe's Jev. | 0 | JavaScript | 2026-09-21 |
| [rolln-ai/axel](https://github.com/rolln-ai/axel) | Open-source webhook ingestion and event delivery platform. The source for Axel Cloud. | 0 | TypeScript | 2026-09-21 |
| [romiluz13/jevmory](https://github.com/romiluz13/jevmory) | Coding-agent memory where every fact is a verbatim quote graded by TypeSafe Jev's calibrated confidence. Loca… | 0 | Python | 2026-09-21 |
| [ross-jill-ws/pi-fast-jev-compaction](https://github.com/ross-jill-ws/pi-fast-jev-compaction) | Fast, verbatim, jev-guided compaction for pi | 0 | TypeScript | 2026-09-20 |
| [Royhu1/jev-poker-trainer](https://github.com/Royhu1/jev-poker-trainer) | A multilingual Texas Hold’em training studio with Jev-powered opponents, live coaching, replay and skill asse… | 0 | TypeScript | 2026-09-21 |
| [royosherove/graphlin](https://github.com/royosherove/graphlin) | Live architecture and activity diagrams for coding agents using JEV. | 0 | JavaScript | 2026-09-21 |
| [RubenVroman/Hearth](https://github.com/RubenVroman/Hearth) | — | 0 | Python | 2026-09-20 |
| [rudrasingh500/jev_minecraft](https://github.com/rudrasingh500/jev_minecraft) | An agent to beat minecraft | 0 | JavaScript | 2026-09-21 |
| [rurasua/dashboard-jev](https://github.com/rurasua/dashboard-jev) | dashboard especial para mejorar probabilidad de eventos geologicos con certeza | 0 | HTML | 2026-09-20 |
| [russleyshaw/typesafe-jev-gate](https://github.com/russleyshaw/typesafe-jev-gate) | Fail-closed Jev policy gate for Hermes Agent tool calls | 0 | Python | 2026-09-20 |
| [rustfuture/reflex-control](https://github.com/rustfuture/reflex-control) | Rust policy engine using TypeSafe Jev and deterministic checks to route AI agent decisions. | 0 | Rust | 2026-09-19 |
| [rvben/werkt](https://github.com/rvben/werkt) | An agent-first, Git-native control plane for code automations. | 0 | Go | 2026-09-21 |
| [ryan-sunny/dbt-assay](https://github.com/ryan-sunny/dbt-assay) | Your dbt project has types nobody declared. assay infers them and finds where they contradict each other. sql… | 0 | Python | 2026-09-21 |
| [RyoyaYahagi/Trader-Jev](https://github.com/RyoyaYahagi/Trader-Jev) | — | 0 | — | 2026-09-21 |
| [ryuchan00/jev_practice](https://github.com/ryuchan00/jev_practice) | Jev (TypeSafe System One) と LLM に同じゲームを打たせて、レイテンシ・コスト・判断の質を比べる練習台 | 0 | Python | 2026-09-21 |
| [s-hiraoku/jev-checkkit](https://github.com/s-hiraoku/jev-checkkit) | — | 0 | TypeScript | 2026-09-21 |
| [s-hiraoku/jev-page-checker](https://github.com/s-hiraoku/jev-page-checker) | — | 0 | TypeScript | 2026-09-21 |
| [S1LV3RJ1NX/openjev](https://github.com/S1LV3RJ1NX/openjev) | Open System One models: typed decisions with calibrated probabilities, trainable on your own data. No text ge… | 0 | Python | 2026-09-21 |
| [s2422114/jev_app](https://github.com/s2422114/jev_app) | — | 0 | — | 2026-09-21 |
| [Sachin-chaurasiya/scam-checker-with-jev](https://github.com/Sachin-chaurasiya/scam-checker-with-jev) | Paste a suspicious text message. Get a straight answer and the reasons behind it. | 0 | TypeScript | 2026-09-21 |
| [sahajamit/jev-lens](https://github.com/sahajamit/jev-lens) | Personal Chrome extension: Jev (TypeSafe) badges X and LinkedIn posts READ / MAYBE / SKIP against my own inte… | 0 | JavaScript | 2026-09-21 |
| [sambhav/jev-explained](https://github.com/sambhav/jev-explained) | — | 0 | HTML | 2026-09-18 |
| [Samge0/jev-arena](https://github.com/Samge0/jev-arena) | Jev模型跟开源方案NanoJev / Laya的对比测试 | 0 | Python | 2026-09-21 |
| [samyung0/capy-notebook](https://github.com/samyung0/capy-notebook) | — | 0 | Python | 2026-09-21 |
| [sandrotaje/pi-jev-concise](https://github.com/sandrotaje/pi-jev-concise) | — | 0 | TypeScript | 2026-09-20 |
| [sanmai/typesafe-ai-php](https://github.com/sanmai/typesafe-ai-php) | Jev for PHP, TypeSafe AI PHP SDK | 0 | PHP | 2026-09-21 |
| [Sannrox/sekai-chisei](https://github.com/Sannrox/sekai-chisei) | Local-first Rust control plane for ontology-driven, governed agent operations: policy, budgets, audit, evalua… | 0 | Rust | 2026-09-21 |
| [sarang-pratham/jev-computer-use](https://github.com/sarang-pratham/jev-computer-use) | — | 0 | Python | 2026-09-21 |
| [SarathChandraBellam/jev-vs-llm-ticket-router](https://github.com/SarathChandraBellam/jev-vs-llm-ticket-router) | Benchmark: TypeSafe Jev vs traditional LLM on support-ticket routing accuracy, latency, and cost | 0 | Python | 2026-09-21 |
| [SashaSkind/beyondgreen](https://github.com/SashaSkind/beyondgreen) | Your tests passed. We check what they missed. | 0 | TypeScript | 2026-09-15 |
| [sava-software/typesafe-client](https://github.com/sava-software/typesafe-client) | Java client for the TypeSafe System One API (Jev): typed questions in, calibrated probabilities out | 0 | Java | 2026-09-18 |
| [scbrown/camayoc](https://github.com/scbrown/camayoc) | 🪢 The knot-keeper — bootstrap ontology, knowledge ingress, and knowledge packs for the quipu stack | 0 | Python | 2026-09-21 |
| [SCBuergel/jev-netprofiler](https://github.com/SCBuergel/jev-netprofiler) | A network profiler usign Jev, educational proof of concept only! | 0 | Python | 2026-09-21 |
| [schalkneethling/jev-lint](https://github.com/schalkneethling/jev-lint) | An experiment with semantic code linting using Jev from TypeSafe AI | 0 | TypeScript | 2026-09-21 |
| [schulxf/browser-qa](https://github.com/schulxf/browser-qa) | Skill de QA visual e funcional para aplicações web. Combina agent-browser, Jev e verificação independente com… | 0 | JavaScript | 2026-09-18 |
| [Schweik7/jev-pacman](https://github.com/Schweik7/jev-pacman) | Pac-Man decision environment for TypeSafe's Jev (System One) model | 0 | Python | 2026-09-20 |
| [scottjoyner/my-jev](https://github.com/scottjoyner/my-jev) | — | 0 | — | 2026-09-21 |
| [scursel/hermes-jev-fastpath](https://github.com/scursel/hermes-jev-fastpath) | Hermes Agent middleware using TypeSafe Jev for fail-open deterministic fast paths before LLM execution | 0 | Python | 2026-09-20 |
| [seamlessux/seamlessux](https://github.com/seamlessux/seamlessux) | Your users are already telling you what is broken. Seamless UX helps you understand it. | 0 | TypeScript | 2026-09-20 |
| [SeanPlusPlus/hellojev](https://github.com/SeanPlusPlus/hellojev) | 👋 jev | 0 | TypeScript | 2026-09-21 |
| [seb4ez/jevguard](https://github.com/seb4ez/jevguard) | Deterministic decision runtime, zero-token caching, and certainty calibrator for TypeSafe AI (Jev). | 0 | Python | 2026-09-21 |
| [seb4ez/jevguard-mcp](https://github.com/seb4ez/jevguard-mcp) | Official Model Context Protocol (MCP) server for JevGuard and TypeSafe AI | 0 | Python | 2026-09-21 |
| [secondfret/mailjay](https://github.com/secondfret/mailjay) | Personal macOS inbox triage app powered by Gmail API and TypeSafe Jev | 0 | Swift | 2026-09-20 |
| [segavvy/mnist-text-input-benchmark](https://github.com/segavvy/mnist-text-input-benchmark) | 手書き数字データセットMNISTのテストデータから、各数字（0〜9）をランダムに10枚ずつ、計100枚抽出した簡易的な評価です。 同じ100枚でJev・GPT-5 nano・GPT-5.6 Lunaの入力表現・精度・費… | 0 | HTML | 2026-09-21 |
| [seoheejung/spendguard-agent](https://github.com/seoheejung/spendguard-agent) | Jev, OpenAI Agent, MCP를 활용해 구매·구독·비용 의사결정을 계산·비교·검증하는 프로젝트 | 0 | Python | 2026-09-19 |
| [SergeiGolos/ask-jev](https://github.com/SergeiGolos/ask-jev) | — | 0 | TypeScript | 2026-09-20 |
| [sfriedowitz/toy-jev](https://github.com/sfriedowitz/toy-jev) | Toy implementation of a Jev-like model. | 0 | Python | 2026-09-20 |
| [sglenon/jev-semantic-reviewer](https://github.com/sglenon/jev-semantic-reviewer) | — | 0 | TypeScript | 2026-09-21 |
| [shaduf-labs/jev-catalog](https://github.com/shaduf-labs/jev-catalog) | Jev use cases, open-source alternatives, real products and current access prices. | 0 | HTML | 2026-09-21 |
| [shailesh-svg/Jev-POC-Lead-Gen](https://github.com/shailesh-svg/Jev-POC-Lead-Gen) | — | 0 | TypeScript | 2026-09-21 |
| [Shalimov04/open-jev](https://github.com/Shalimov04/open-jev) | Distil a prompt into a small, fast, calibrated classifier. Typed decisions (choice/score/noul) with calibrate… | 0 | Python | 2026-09-21 |
| [shank4804/shank4804.github.io](https://github.com/shank4804/shank4804.github.io) | The actual website HTML/CSS files | 0 | HTML | 2026-09-19 |
| [shantanugoel/tetris-ai](https://github.com/shantanugoel/tetris-ai) | Browser Tetris with a first-class AI API: play it with a built-in planning agent, TypeSafe's Jev decision mod… | 0 | JavaScript | 2026-09-18 |
| [Sharkelot/jev-laya-free](https://github.com/Sharkelot/jev-laya-free) | Free local Jev-compatible typed decisions backed by rules or Laya, with a TypeSafe SDK-compatible Python surf… | 0 | Python | 2026-09-21 |
| [sharpninja/jev-codex-blazor](https://github.com/sharpninja/jev-codex-blazor) | Jev emulation layer over Codex CLI using Microsoft Agent Framework and a Blazor chat harness | 0 | C# | 2026-09-21 |
| [shashwatc12/watermelon](https://github.com/shashwatc12/watermelon) | Green on the outside, red on the inside. Jev checks whether a weekly program status update's claimed status m… | 0 | JavaScript | 2026-09-21 |
| [SherlockGy/play-jev](https://github.com/SherlockGy/play-jev) | — | 0 | JavaScript | 2026-09-21 |
| [Sheshiyer/urania-137](https://github.com/Sheshiyer/urania-137) | Graph-first stellar console over the Selemene engine — chat is the threshold, the Folio is the durable readin… | 0 | TypeScript | 2026-09-21 |
| [shimayuz/cath-lab-open](https://github.com/shimayuz/cath-lab-open) | Open-source coronary catheter learning prototype. English/Japanese. Research data under separate terms; Jev P… | 0 | TypeScript | 2026-09-20 |
| [ShingoHiroki/jev-test](https://github.com/ShingoHiroki/jev-test) | — | 0 | TypeScript | 2026-09-20 |
| [ShiqinGuo/jev-hunter](https://github.com/ShiqinGuo/jev-hunter) | JevHunter — AI job application plugin with TypeSafe Jev for job matching. Screen BOSS Zhipin jobs, apply and … | 0 | Python | 2026-09-21 |
| [shivam-raval96/multiagent-jev-monitor](https://github.com/shivam-raval96/multiagent-jev-monitor) | — | 0 | JavaScript | 2026-09-18 |
| [shivamnarkar47/Jev-testcase](https://github.com/shivamnarkar47/Jev-testcase) | Validate execution plans with TypeSafe Jev (raw curl, tunable thresholds, JSON mode) | 0 | Python | 2026-09-20 |
| [shm11C3/jev-checkup](https://github.com/shm11C3/jev-checkup) | — | 0 | TypeScript | 2026-09-21 |
| [Shuhan-Zhang/simtra](https://github.com/Shuhan-Zhang/simtra) | — | 0 | Rust | 2026-09-19 |
| [shunta-furukawa/jev-tick-lab](https://github.com/shunta-furukawa/jev-tick-lab) | A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged f… | 0 | — | 2026-09-19 |
| [si618/explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai) | TypeSafe System One (Jev) evaluated on synthetic FHIR clinical scenarios, with Claude as System Two | 0 | Python | 2026-09-20 |
| [sichengchen/unimeasure](https://github.com/sichengchen/unimeasure) | Imperial/Metric conversion for Chrome. Smart detection with Jev. | 0 | JavaScript | 2026-09-20 |
| [sijiaoh/jevgrep](https://github.com/sijiaoh/jevgrep) | grep lines by what they mean | 0 | Go | 2026-09-20 |
| [silverzzzzz/jev-binaryoption](https://github.com/silverzzzzz/jev-binaryoption) | — | 0 | JavaScript | 2026-09-19 |
| [simplosophy/jev-skill](https://github.com/simplosophy/jev-skill) | — | 0 | Python | 2026-09-21 |
| [sinfiny/jev-feed](https://github.com/sinfiny/jev-feed) | Adaptive public YouTube learning feeds built for focused audiences. | 0 | TypeScript | 2026-09-21 |
| [siren2345/jev-single-decode](https://github.com/siren2345/jev-single-decode) | Jev-compatible choice inference using prefill plus exactly one decode step | 0 | Python | 2026-09-21 |
| [siroccomask/snake-jev](https://github.com/siroccomask/snake-jev) | Snake controlled by parallel Jev assessments, with one API call per game tick. | 0 | Python | 2026-09-19 |
| [sirviejo/jev-tidy-my-desktop](https://github.com/sirviejo/jev-tidy-my-desktop) | Jev Tidy my Desktop — tidies the macOS Desktop with TypeSafe's Jev: screenshots always go to their folder; fo… | 0 | Python | 2026-09-20 |
| [sk8metalme/jev-practice](https://github.com/sk8metalme/jev-practice) | — | 0 | Rust | 2026-09-21 |
| [skiingfalcon/jev-email-cascade](https://github.com/skiingfalcon/jev-email-cascade) | Proves an email-triage cascade: Jev decides via typed questions, a policy routes, gpt-oss handles the leftove… | 0 | Python | 2026-09-20 |
| [smaldd14/qavo](https://github.com/smaldd14/qavo) | A QA agent that drives a real browser with Jev choices | 0 | TypeScript | 2026-09-21 |
| [smalltownrobotics/proxima-1024](https://github.com/smalltownrobotics/proxima-1024) | Open-source generation-ship command simulation with Astra and Jev. | 0 | Python | 2026-09-19 |
| [smammadov1994/Signal98](https://github.com/smammadov1994/Signal98) | A new type of error handling for your project with JEV | 0 | JavaScript | 2026-09-20 |
| [smcronin/jev-the-band](https://github.com/smcronin/jev-the-band) | Five decision models. One improvising jam band. Jev personas, a declarative score, live audio, and a virtual … | 0 | TypeScript | 2026-09-21 |
| [Smotherer007/pi-jev](https://github.com/Smotherer007/pi-jev) | — | 0 | TypeScript | 2026-09-21 |
| [snakerzr/OpenJev](https://github.com/snakerzr/OpenJev) | Open-source self-hosted implementation of System One Decisions API (zero-generation fast classification engin… | 0 | Python | 2026-09-20 |
| [sneldao/stoppage](https://github.com/sneldao/stoppage) | stoppage.sportwarren.com | 0 | JavaScript | 2026-09-20 |
| [soloa715/Valorant-Mc](https://github.com/soloa715/Valorant-Mc) | — | 0 | Java | 2026-09-21 |
| [somarc/da-jev](https://github.com/somarc/da-jev) | — | 0 | JavaScript | 2026-09-18 |
| [SongMarco/jev-jstris](https://github.com/SongMarco/jev-jstris) | Jev chooses Tetris placements; a local controller plays Jstris through keyboard input. | 0 | TypeScript | 2026-09-21 |
| [SophiaSama/Manufacturing-Assistant-Agent-Framework](https://github.com/SophiaSama/Manufacturing-Assistant-Agent-Framework) | A framework for generic RAG in enterprise environment | 0 | Python | 2026-09-21 |
| [SoundBlaster/Jev4Mellea](https://github.com/SoundBlaster/Jev4Mellea) | Jev adapter for Mellea | 0 | Python | 2026-09-21 |
| [SovereignSignal/discuss-dot-watch](https://github.com/SovereignSignal/discuss-dot-watch) | — | 0 | TypeScript | 2026-09-21 |
| [spareilleux/learn](https://github.com/spareilleux/learn) | Learning in public — bilingual (en/fr) courses written as I learn | 0 | MDX | 2026-09-21 |
| [SpecialSouth2004/AutoGPT](https://github.com/SpecialSouth2004/AutoGPT) | — | 0 | Python | 2026-09-21 |
| [spencerlepine/blog](https://github.com/spencerlepine/blog) | Personal developer blog | 0 | Markdown | 2026-09-21 |
| [sperictao/dsh-auto-review-jev](https://github.com/sperictao/dsh-auto-review-jev) | — | 0 | TypeScript | 2026-09-21 |
| [spivi/cloudforge-jev](https://github.com/spivi/cloudforge-jev) | Sidecar: grade a cloudforge student writeup with TypeSafe Jev. Not part of the OSS product. | 0 | Python | 2026-09-18 |
| [Spykoninho/trading-bot-jev](https://github.com/Spykoninho/trading-bot-jev) | Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news | 0 | TypeScript | 2026-09-19 |
| [SqaaSSL/aeat-doc-classifier](https://github.com/SqaaSSL/aeat-doc-classifier) | Spanish AEAT document classification and reviewable PGC account suggestions powered by Jev. MIT. | 0 | TypeScript | 2026-09-21 |
| [Sqhh99/personal-site](https://github.com/Sqhh99/personal-site) | this is my personal website. | 0 | TypeScript | 2026-09-20 |
| [srbryers/model-routing-cards](https://github.com/srbryers/model-routing-cards) | Which model for this task, and whether to believe it. Routing cards with a trust gate that refuses to name a … | 0 | JavaScript | 2026-09-20 |
| [sriannamalai/Jev.UI](https://github.com/sriannamalai/Jev.UI) | Easy to use User Interface for System One's Jev Model interaction. | 0 | TypeScript | 2026-09-21 |
| [Sskift/jev-sts2-agent](https://github.com/Sskift/jev-sts2-agent) | — | 0 | JavaScript | 2026-09-21 |
| [steelwalrus/jev-needs-review](https://github.com/steelwalrus/jev-needs-review) | Classifies PRs as "merge candidate" or "human review" required using Jev's typed decision making. | 0 | TypeScript | 2026-09-20 |
| [STEERIX-home/robo-jev](https://github.com/STEERIX-home/robo-jev) | — | 0 | Python | 2026-09-21 |
| [StefH/typesafe-ai.sdk](https://github.com/StefH/typesafe-ai.sdk) | .NET SDK for TypeSafe AI | 0 | C# | 2026-09-21 |
| [sterlingdigitalp/jevtweet](https://github.com/sterlingdigitalp/jevtweet) | — | 0 | Python | 2026-09-19 |
| [stevenke1981/jev-codex-harness](https://github.com/stevenke1981/jev-codex-harness) | — | 0 | Go | 2026-09-21 |
| [STRML/omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier) | Jev-powered model-judged permission gate for OMP (TypeSafe System One) | 0 | TypeScript | 2026-09-17 |
| [Studio-Sasquatch/typesafe-sdk-elixir](https://github.com/Studio-Sasquatch/typesafe-sdk-elixir) | An unofficial SDK for TypeSafe AI | 0 | Elixir | 2026-09-21 |
| [sub-surface/jev](https://github.com/sub-surface/jev) | — | 0 | Python | 2026-09-19 |
| [sudeshkar/jev-corrective-rag](https://github.com/sudeshkar/jev-corrective-rag) | Corrective RAG where every decision gate is a typed System One model call instead of an LLM judge. 7x fewer L… | 0 | Python | 2026-09-21 |
| [sueszli/qwen27b-jev](https://github.com/sueszli/qwen27b-jev) | logits to multiple-choice questions for Qwen3.8-27B | 0 | Python | 2026-09-19 |
| [SunnyKikiHK/jev-replacement](https://github.com/SunnyKikiHK/jev-replacement) | — | 0 | Python | 2026-09-20 |
| [Sunwood-ai-labs/jev-colab-lab](https://github.com/Sunwood-ai-labs/jev-colab-lab) | Reproducible Google Colab GPU experiments for decision-model inference | 0 | Python | 2026-09-21 |
| [SupremeDreamZ/jev-fastloop](https://github.com/SupremeDreamZ/jev-fastloop) | Cheap fail-open semantic edge layer for Jev (TypeSafe System One): decision service + confidence policy + dec… | 0 | Python | 2026-09-21 |
| [suraj-phanindra/wellposed](https://github.com/suraj-phanindra/wellposed) | Lint your jev requests before they come back confidently wrong. | 0 | JavaScript | 2026-09-18 |
| [surajkushvaha/tic-tac-toe-with-jev](https://github.com/surajkushvaha/tic-tac-toe-with-jev) | — | 0 | TypeScript | 2026-09-20 |
| [surreptakos/claude-dotfiles](https://github.com/surreptakos/claude-dotfiles) | Machine-local half of a Claude Code setup: global rules, skills, hooks, plugin manifests, per-project memory.… | 0 | JavaScript | 2026-09-21 |
| [svilupp/agent-hotwash](https://github.com/svilupp/agent-hotwash) | — | 0 | Python | 2026-09-20 |
| [svsaraf/tswitch](https://github.com/svsaraf/tswitch) | Typesafe switch, score, and bool primitives for Python, powered by TypeSafe AI | 0 | Python | 2026-09-19 |
| [sw-ml-study/demo-decision-model](https://github.com/sw-ml-study/demo-decision-model) | A Jev-or-System-1 inspired typed decision model demo in sw-mlpl | 0 | Rust | 2026-09-21 |
| [swarooppatilx/oxox](https://github.com/swarooppatilx/oxox) | Probably the least useful thing you can build with Jev | 0 | TypeScript | 2026-09-20 |
| [sysone-help/sysone](https://github.com/sysone-help/sysone) | A tiny, zero-dependency TypeScript library for Jev by TypeSafe. Checks, classification and scoring, with a li… | 0 | TypeScript | 2026-09-20 |
| [szocpaul/jev-compaction-prime](https://github.com/szocpaul/jev-compaction-prime) | Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scor… | 0 | Python | 2026-09-20 |
| [T-Lind/accessor](https://github.com/T-Lind/accessor) | Local voice gateway around Codex, Claude Code, and Antigravity | 0 | Rust | 2026-09-21 |
| [tackaaaada/jev-langfuse-trial](https://github.com/tackaaaada/jev-langfuse-trial) | — | 0 | Python | 2026-09-21 |
| [taecontrol/manuvra](https://github.com/taecontrol/manuvra) | macOS CLI for coding agents to observe and control exact Chrome tabs and native windows | 0 | Rust | 2026-09-21 |
| [taisan11/jev-agent](https://github.com/taisan11/jev-agent) | — | 0 | TypeScript | 2026-09-19 |
| [taituo/jev](https://github.com/taituo/jev) | Audited LLM Wiki over RFCs 7519/7515/7516/6749/6750/8725 — Slice 1: reproducible sources, resolvable citation… | 0 | Python | 2026-09-19 |
| [takafumikobayashi/jev-snap-lab](https://github.com/takafumikobayashi/jev-snap-lab) | Tiny inputs. Instant decisions. A small experimental playground for exploring fast, probabilistic decisions w… | 0 | TypeScript | 2026-09-21 |
| [TakashiYoshinaga/Jev-vs-VectorSearch](https://github.com/TakashiYoshinaga/Jev-vs-VectorSearch) | — | 0 | Python | 2026-09-20 |
| [takezou621/jev-mcp](https://github.com/takezou621/jev-mcp) | — | 0 | TypeScript | 2026-09-20 |
| [TakSeBiegam/jevode](https://github.com/TakSeBiegam/jevode) | — | 0 | TypeScript | 2026-09-19 |
| [taku-me/chakuho](https://github.com/taku-me/chakuho) | Jev-compatible System One decision endpoint over a local LLM (1-token logprob decisions) | 0 | Python | 2026-09-21 |
| [Talya1412/jev-harness](https://github.com/Talya1412/jev-harness) | TypeSafe Jev (System One) integrations for OMP, MCP, Claude Code, and Pi — fail-open decision routing, gating… | 0 | TypeScript | 2026-09-20 |
| [tanayvasishtha/jev-lab](https://github.com/tanayvasishtha/jev-lab) | — | 0 | JavaScript | 2026-09-21 |
| [Tango-Tango/ex_typesafe](https://github.com/Tango-Tango/ex_typesafe) | An Elixir SDK for Typesafe's API (https://docs.typesafe.ai/sdk) | 0 | Elixir | 2026-09-21 |
| [tarasyarema/hackspain](https://github.com/tarasyarema/hackspain) | CINTA — Class-agnostic INline Transport Analyzer | 0 | Python | 2026-09-20 |
| [taro1985/dual-process-ai](https://github.com/taro1985/dual-process-ai) | Dual-Process AI: A design pattern combining System 1 (Jev/TypeSafe AI) with System 2 (Gemini) — inspired by K… | 0 | Python | 2026-09-20 |
| [taruo/jev-adblocker](https://github.com/taruo/jev-adblocker) | — | 0 | JavaScript | 2026-09-21 |
| [tatdt622989/blog](https://github.com/tatdt622989/blog) | — | 0 | HTML | 2026-09-18 |
| [taxfree-python/taxfree-python.github.io](https://github.com/taxfree-python/taxfree-python.github.io) | — | 0 | TypeScript | 2026-09-19 |
| [tcgarvin/bobgame](https://github.com/tcgarvin/bobgame) | Vibe coding experiment | 0 | Python | 2026-09-21 |
| [tenfingerseddy/voicebind](https://github.com/tenfingerseddy/voicebind) | Natural voice control, dictation and workspace bookmarks for Omarchy. Local Whisper with optional Jev interpr… | 0 | Python | 2026-09-21 |
| [tensorfish/jrisc](https://github.com/tensorfish/jrisc) | Jev's Reduced Instruction Set | 0 | JavaScript | 2026-09-19 |
| [TentacleCat/JevDice](https://github.com/TentacleCat/JevDice) | A Jev-powered dice and coin CLI | 0 | Rust | 2026-09-20 |
| [Tewoto1/Computer-use-and-control-with-Jev](https://github.com/Tewoto1/Computer-use-and-control-with-Jev) | Jev assisted computer use and control framework, can link to a phone or a display to showcase current use pro… | 0 | Python | 2026-09-20 |
| [teyhouse/jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) | Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets | 0 | Python | 2026-09-18 |
| [tgiridhar/claude-code-jev-smart-router](https://github.com/tgiridhar/claude-code-jev-smart-router) | HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task … | 0 | Python | 2026-09-19 |
| [the-wbs-project/aec-integrations](https://github.com/the-wbs-project/aec-integrations) | — | 0 | TypeScript | 2026-09-21 |
| [themacdonald/BiasGuard](https://github.com/themacdonald/BiasGuard) | Framework for Model Bias Detection & Mitigation | 0 | Python | 2026-09-21 |
| [TheodoreGalanos/agent-memory](https://github.com/TheodoreGalanos/agent-memory) | Agent memory architecture: Rust host, Pi worker pool, judgement runtime with Jev shadow, formation/activation… | 0 | Rust | 2026-09-20 |
| [theosunny/jev_stock](https://github.com/theosunny/jev_stock) | — | 0 | Python | 2026-09-21 |
| [TheWayWithin/jev-bench](https://github.com/TheWayWithin/jev-bench) | Does the cited source actually say it? A 42-claim benchmark: Jev (TypeSafe System One) against GPT-5.4, Claud… | 0 | Python | 2026-09-21 |
| [thijmenkam/jev-benchmarks](https://github.com/thijmenkam/jev-benchmarks) | — | 0 | Python | 2026-09-18 |
| [thirdlf03/swe2-orca-orchestrate](https://github.com/thirdlf03/swe2-orca-orchestrate) | Orca + Devin CLI (SWE-2) multi-agent orchestration harness | 0 | Python | 2026-09-20 |
| [thisisandreeeee/jev-benchmarks](https://github.com/thisisandreeeee/jev-benchmarks) | — | 0 | Python | 2026-09-21 |
| [thisisjorge/jev-control-room](https://github.com/thisisjorge/jev-control-room) | A visual control room for typed AI evaluations, structured decision-making, and confidence-aware policy gatin… | 0 | TypeScript | 2026-09-19 |
| [thisyearnofear/diversify](https://github.com/thisyearnofear/diversify) | — | 0 | TypeScript | 2026-09-21 |
| [thomas-chong/agy-cli-jev-auto-mode](https://github.com/thomas-chong/agy-cli-jev-auto-mode) | — | 0 | JavaScript | 2026-09-21 |
| [timnikolov/jev-system-one-ai-engine](https://github.com/timnikolov/jev-system-one-ai-engine) | — | 0 | JavaScript | 2026-09-21 |
| [tincke10/Jevest](https://github.com/tincke10/Jevest) | Automated PR review pipeline using Jev (TypeSafe AI) as a millisecond decision layer over an LLM reviewer | 0 | TypeScript | 2026-09-20 |
| [TinkerandScribe/gxp](https://github.com/TinkerandScribe/gxp) | GXP — Guided eXecution Protocol: a verification-first, binary-criteria workflow for bounded AI agents. | 0 | Python | 2026-09-19 |
| [tinyhumansai/tinyjevclient](https://github.com/tinyhumansai/tinyjevclient) | An integration with jev by typesafe.ai in Rust | 0 | Rust | 2026-09-20 |
| [tirukovelamanoj/jev-plays-doom](https://github.com/tirukovelamanoj/jev-plays-doom) | A System One model driving the game through structured state, no pixels. | 0 | Python | 2026-09-19 |
| [tkuhemiya/jeveve](https://github.com/tkuhemiya/jeveve) | — | 0 | Python | 2026-09-21 |
| [Toby-Faucher/oarfish](https://github.com/Toby-Faucher/oarfish) | Log-driven alarms for homelabs, with a judgment model where the guesswork used to be. Rust + Drain + Jev + As… | 0 | Rust | 2026-09-20 |
| [Tomdachs/jev-replay-lab](https://github.com/Tomdachs/jev-replay-lab) | Local Jev evaluation workbench: datasets, typed questions, threshold simulation and run comparison | 0 | TypeScript | 2026-09-21 |
| [tomharris/engineer-agent](https://github.com/tomharris/engineer-agent) | A Claude Code plugin that automates senior software engineer work — PR reviews, Slack answers, ticket impleme… | 0 | Shell | 2026-09-20 |
| [tomoya-k31/totsuka](https://github.com/tomoya-k31/totsuka) | AI-driven dev-flow automation — detects task instructions from GitHub Issues, Notion and Slack, then orchestr… | 0 | Rust | 2026-09-21 |
| [Tonours/etabli](https://github.com/Tonours/etabli) | — | 0 | Shell | 2026-09-21 |
| [TonyP-MR/jev-curation-engine](https://github.com/TonyP-MR/jev-curation-engine) | Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions… | 0 | Python | 2026-09-21 |
| [toorop/pi-jev-router](https://github.com/toorop/pi-jev-router) | — | 0 | TypeScript | 2026-09-21 |
| [toorop/veille-by-jev](https://github.com/toorop/veille-by-jev) | — | 0 | Python | 2026-09-18 |
| [TOSUKUi/jev-bridge](https://github.com/TOSUKUi/jev-bridge) | Jev-style /v1/systemone API in front of any OpenAI-compatible LLM server (one-token logprob scoring, MIT) | 0 | Python | 2026-09-21 |
| [totally-tim/jev-gate](https://github.com/totally-tim/jev-gate) | Calibrated PR review gates powered by TypeSafe Jev: a GitHub Action, a local CLI, and an OpenCode plugin | 0 | TypeScript | 2026-09-21 |
| [toufu-cell/jev_mine](https://github.com/toufu-cell/jev_mine) | — | 0 | JavaScript | 2026-09-20 |
| [tpellet/jevify](https://github.com/tpellet/jevify) | grep for meaning: find the error in a 10,000-line log, a commit by description, the command for a task. A Uni… | 0 | Rust | 2026-09-21 |
| [tr1v3r/dsh-jev](https://github.com/tr1v3r/dsh-jev) | jev × DeepSeek Harness: System One decision client, MCP server, per-turn router and effort plugins | 0 | TypeScript | 2026-09-21 |
| [TranBaVinhSon/jev-router](https://github.com/TranBaVinhSon/jev-router) | — | 0 | TypeScript | 2026-09-20 |
| [TreeCityWes/jev_x1](https://github.com/TreeCityWes/jev_x1) | x1.xyz transaction classifier | 0 | JavaScript | 2026-09-19 |
| [treycausey/semantic-find](https://github.com/treycausey/semantic-find) | Local evidence search with optional Jev semantic ranking | 0 | TypeScript | 2026-09-21 |
| [Troy-LL/OpenReach](https://github.com/Troy-LL/OpenReach) | Reach for scientific papers that weren't findable before. | 0 | TypeScript | 2026-09-21 |
| [tsnAnh/pikachu](https://github.com/tsnAnh/pikachu) | Curated Pi coding agent configuration with Jev compaction, LSP, subagents, plan mode, safety tools, and autom… | 0 | TypeScript | 2026-09-21 |
| [ttlequals0/MinusPodJev](https://github.com/ttlequals0/MinusPodJev) | MinusPod Jev Proxy | 0 | Python | 2026-09-21 |
| [tune-77/tune_lease_55](https://github.com/tune-77/tune_lease_55) | SHION — an AI that turns on-the-ground "something feels off" into reusable judgment assets for lease-financin… | 0 | Python | 2026-09-21 |
| [twilwa/pi-typesafe](https://github.com/twilwa/pi-typesafe) | Pi coding-agent extension built on the TypeSafe AI System One API (Jev) | 0 | TypeScript | 2026-09-21 |
| [twwright/jeverything](https://github.com/twwright/jeverything) | Jev engineering skill and source-backed knowledge | 0 | — | 2026-09-19 |
| [tylerfloyd/spec-drift](https://github.com/tylerfloyd/spec-drift) | Jev-backed spec-drift review bot for Pi | 0 | TypeScript | 2026-09-20 |
| [tylervick/jevplays](https://github.com/tylervick/jevplays) | — | 0 | Python | 2026-09-21 |
| [typesend/typesafe_ai](https://github.com/typesend/typesafe_ai) | Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out… | 0 | Elixir | 2026-09-17 |
| [ufx7/jev-testbench](https://github.com/ufx7/jev-testbench) | Black-box Jev test bench + a Claude/LLM-and-Jev collaboration measurement harness | 0 | TypeScript | 2026-09-19 |
| [uh-joan/jev-warning-letter-classifier](https://github.com/uh-joan/jev-warning-letter-classifier) | — | 0 | TypeScript | 2026-09-19 |
| [uist1idrju3i/study-jev](https://github.com/uist1idrju3i/study-jev) | — | 0 | HTML | 2026-09-20 |
| [umgbhalla/jevx](https://github.com/umgbhalla/jevx) | Jev (TypeSafe System One) research: API notes, benchmarks, community experiments, agent-loop patterns | 0 | Python | 2026-09-21 |
| [UnbelievableT/topxai-docs](https://github.com/UnbelievableT/topxai-docs) | TopxAI documentation: one OpenAI- and Anthropic-compatible API for Claude, GPT, Grok, GLM, Kimi and Jev at fi… | 0 | — | 2026-09-19 |
| [uninhibited-scholar/jev-universal](https://github.com/uninhibited-scholar/jev-universal) | Jev structured decisions for Claude, ChatGPT, Kimi Code, ZCode and Codex via MCP | 0 | Python | 2026-09-21 |
| [uspraveen/Jev-Reranker](https://github.com/uspraveen/Jev-Reranker) | A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings | 0 | Python | 2026-09-20 |
| [uzak0209/AI-Research](https://github.com/uzak0209/AI-Research) | 研究トレンドの自動追跡 — 日次で論文を収集し、重複／活用可能性とテーマ候補を報告。アプリ内で参考文献を管理し、.bib / Typst へ自動書き出し。原稿のファクトチェックも行う (設計フェーズ) | 0 | TypeScript | 2026-09-21 |
| [v4fs/awesome-jev-security](https://github.com/v4fs/awesome-jev-security) | Basic triage for security issues using SSVC and Jev | 0 | Python | 2026-09-21 |
| [vafaei-ar/jev-scientific-development](https://github.com/vafaei-ar/jev-scientific-development) | — | 0 | Python | 2026-09-19 |
| [valksor/typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go) | Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not a… | 0 | Go | 2026-09-19 |
| [valksor/typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php) | Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not … | 0 | PHP | 2026-09-19 |
| [vamsikrishna2421/jev-usecases](https://github.com/vamsikrishna2421/jev-usecases) | Jev (TypeSafe AI's System One decision model) use-case catalog: real-world builds, cost math, design patterns… | 0 | — | 2026-09-21 |
| [vayungodara/jev-lint](https://github.com/vayungodara/jev-lint) | Lint a Markdown knowledge base (Obsidian vault or LLM wiki) for contradictions, stale claims, unresolved mark… | 0 | Python | 2026-09-19 |
| [VdustR/gomoku-arena](https://github.com/VdustR/gomoku-arena) | A gomoku board any player can sit at — you, a search algorithm, a model, or an agent over MCP. Free-style and… | 0 | TypeScript | 2026-09-20 |
| [vedang/pi-progress-bar](https://github.com/vedang/pi-progress-bar) | A progress bar to see if work is being done well. | 0 | TypeScript | 2026-09-20 |
| [VennIntelligence/jev-drive](https://github.com/VennIntelligence/jev-drive) | — | 0 | Python | 2026-09-21 |
| [Verhex/deckent-next](https://github.com/Verhex/deckent-next) | Deckent repo v3 | 0 | TypeScript | 2026-09-21 |
| [Verhex/xerify](https://github.com/Verhex/xerify) | Verify before you trust. Cross-provider verification with LLMs and Jev. CLI, library & MCP. | 0 | TypeScript | 2026-09-18 |
| [victortran0904/Jev-Browser-Use](https://github.com/victortran0904/Jev-Browser-Use) | — | 0 | TypeScript | 2026-09-19 |
| [vinsonws/jev-page-tester](https://github.com/vinsonws/jev-page-tester) | — | 0 | TypeScript | 2026-09-21 |
| [vishesh-baghel/typesafe](https://github.com/vishesh-baghel/typesafe) | — | 0 | TypeScript | 2026-09-18 |
| [vishivishvish/jev-typesafeai](https://github.com/vishivishvish/jev-typesafeai) | — | 0 | TypeScript | 2026-09-19 |
| [Visorian/TidyUp](https://github.com/Visorian/TidyUp) | Experimental Jev based Ad Blocker | 0 | TypeScript | 2026-09-20 |
| [vouchington/vouchington](https://github.com/vouchington/vouchington) | — | 0 | TypeScript | 2026-09-21 |
| [voyagerforge-dev/loci](https://github.com/voyagerforge-dev/loci) | FOSS dynamic slotting engine with evidence-aware optimization, rules, constraints, and optional Jev judgment | 0 | Python | 2026-09-21 |
| [vrash/jeval](https://github.com/vrash/jeval) | jeval: open-source evaluations for AI outputs and agents, judged by Jev | 0 | TypeScript | 2026-09-20 |
| [vzornjak/typesafe-decision](https://github.com/vzornjak/typesafe-decision) | Unofficial, advisory TypeSafe Jev decision layer for Minis — fail-closed routing, ranking, verification, and … | 0 | Python | 2026-09-21 |
| [WallerChen/jev-measured](https://github.com/WallerChen/jev-measured) | Measured cost, latency and raw output from the live Jev API (TypeSafe AI System One model) across 8 use cases… | 0 | Python | 2026-09-20 |
| [warmlukecore/warmluke](https://github.com/warmlukecore/warmluke) | — | 0 | TypeScript | 2026-09-21 |
| [waschbaerwerkstatt-tech/jev-review-vorschau](https://github.com/waschbaerwerkstatt-tech/jev-review-vorschau) | Passwortgeschützte Jev-Review-Auswertung; ausschließlich verschlüsselte HTML-Datei | 0 | HTML | 2026-09-19 |
| [waterme7on/jev-paper-trader](https://github.com/waterme7on/jev-paper-trader) | 用 typesafe-ai/jev 做决策引擎的 BTC/ETH 纸面交易台（每 5 秒评估，含买卖点与决策历史） | 0 | JavaScript | 2026-09-21 |
| [wattgod/xc-ski-labs](https://github.com/wattgod/xc-ski-labs) | Nordic Lab — XC ski race database, scoring, and search. Classic & skate. 300+ races worldwide. | 0 | Python | 2026-09-21 |
| [Waxmell114514/awesome-jev-compaction](https://github.com/Waxmell114514/awesome-jev-compaction) | A context compactor that can only score, never write — so an agent's memory can't hold a fact the transcript … | 0 | Python | 2026-09-21 |
| [Waxmell114514/jev-trade](https://github.com/Waxmell114514/jev-trade) | — | 0 | Python | 2026-09-21 |
| [waygatetech/jev-go](https://github.com/waygatetech/jev-go) | An unofficial Go SDK for TypeSafe AI's Jev model | 0 | Go | 2026-09-21 |
| [webNeat/llama-jev](https://github.com/webNeat/llama-jev) | Reproducing jev classifier API on top of llama.cpp | 0 | TypeScript | 2026-09-20 |
| [webstercharly/jev-authorship-check](https://github.com/webstercharly/jev-authorship-check) | A small Jev experiment for classifying text as human, AI-generated, or uncertain | 0 | Python | 2026-09-20 |
| [WhiteK0T/Base-of-knowledge](https://github.com/WhiteK0T/Base-of-knowledge) | — | 0 | Shell | 2026-09-20 |
| [whosydd/pi-web-toolkit](https://github.com/whosydd/pi-web-toolkit) | Single pi extension: Context7 library docs + Exa web search + Sourcegraph code search | 0 | TypeScript | 2026-09-21 |
| [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) | An adversarial evaluation of TypeSafe's jev decision model: nine experiments and 28 predictions fixed before … | 0 | Python | 2026-09-21 |
| [windymelt/ddskk-jev](https://github.com/windymelt/ddskk-jev) | — | 0 | Emacs Lisp | 2026-09-18 |
| [WingManJJH/continuum-core](https://github.com/WingManJJH/continuum-core) | Continuum Core — an event-sourced process-to-agent governance model: editable guardrails enforced as a real g… | 0 | Python | 2026-09-21 |
| [winter-loo/jev-voice-browser](https://github.com/winter-loo/jev-voice-browser) | Voice-controlled browser via Jev, native CDP (port 9229), Doubao Voice Bridge and Web Audio streaming | 0 | JavaScript | 2026-09-21 |
| [Wionerlol/wechat-jev-hud](https://github.com/Wionerlol/wechat-jev-hud) | — | 0 | C# | 2026-09-21 |
| [WiredMind2/jev](https://github.com/WiredMind2/jev) | Independent research notes toward an open Jev-like decision model: public facts, API contract, training and e… | 0 | Python | 2026-09-21 |
| [wizicer/jev_info_site](https://github.com/wizicer/jev_info_site) | Community index of tools, models, and real-world use cases built on Jev. | 0 | Astro | 2026-09-21 |
| [wjdjdakf17/jev-study](https://github.com/wjdjdakf17/jev-study) | Jev(TypeSafe AI System One Model) 스터디 — 타입화된 결정·RLCD·confidence-gated routing을 한국어 노트와 TypeScript 목업으로 정리 | 0 | TypeScript | 2026-09-21 |
| [wmtang2/jevknows](https://github.com/wmtang2/jevknows) | A malicious instruction protection skill and prehook for zcode | 0 | Python | 2026-09-21 |
| [WXH666-bit/jev-tetris-lab](https://github.com/WXH666-bit/jev-tetris-lab) | AI-driven Tetris decision playground with a cosmic UI, provider management, and Jev integration | 0 | TypeScript | 2026-09-21 |
| [wyattjoh/demur](https://github.com/wyattjoh/demur) | A proof-of-concept destructive-command guard for coding agents. | 0 | TypeScript | 2026-09-21 |
| [wylu1037/pi-jev-checkpoints](https://github.com/wylu1037/pi-jev-checkpoints) | — | 0 | TypeScript | 2026-09-21 |
| [WYM22101AI/AI-Framework-](https://github.com/WYM22101AI/AI-Framework-) | Creating AI learning framework for market data training | 0 | Python | 2026-09-21 |
| [xAndreiLi/pi-jev-wiki](https://github.com/xAndreiLi/pi-jev-wiki) | Agent managed wiki for a project's conceptual space, utilizing Jev to ensure legitmate, relevant, and robust … | 0 | TypeScript | 2026-09-20 |
| [xcellect/theia](https://github.com/xcellect/theia) | — | 0 | Python | 2026-09-20 |
| [xiaohu0x/jevhunt](https://github.com/xiaohu0x/jevhunt) | jevhunt project | 0 | HTML | 2026-09-21 |
| [xiaohuaxi/jev-study](https://github.com/xiaohuaxi/jev-study) | Hands-on measurements of TypeSafe's Jev via OpenRouter: integration, Chinese-language behaviour, and game loo… | 0 | Python | 2026-09-21 |
| [Xio-Shark/local-search-engine](https://github.com/Xio-Shark/local-search-engine) | Local code & document retrieval layer built on Tantivy: CJK/code tokenization, query AST, symbol-aware eviden… | 0 | Python | 2026-09-21 |
| [Xopher00/jevdevice](https://github.com/Xopher00/jevdevice) | MCP server that lets an LLM agent control a real Android phone, using TypeSafe's Jev to pick real, runtime-di… | 0 | Python | 2026-09-21 |
| [xpressabhi/jev-browser](https://github.com/xpressabhi/jev-browser) | Jev decides. The harness acts. | 0 | TypeScript | 2026-09-20 |
| [xuboboo/ashare-trader](https://github.com/xuboboo/ashare-trader) | 基于 Jev 的 A 股 T+1 决策台：盘前预选 + 交易时段全程决策 + 本地概率模型 + 严格成本回测 + QMT 桥接（默认不下单）。1 万本金影子盘记录中；策略未证实正期望（README 有全部数据）。 | 0 | TypeScript | 2026-09-21 |
| [Xubqpanda/everything2jev](https://github.com/Xubqpanda/everything2jev) | — | 0 | TypeScript | 2026-09-21 |
| [xxkuboxx/jev-eval](https://github.com/xxkuboxx/jev-eval) | — | 0 | Python | 2026-09-20 |
| [Xy2002/poker-jev-test-bench](https://github.com/Xy2002/poker-jev-test-bench) | Jev test bench — Texas Hold'em edition: live-fire testing of TypeSafe's Jev evaluation model through a React … | 0 | JavaScript | 2026-09-20 |
| [yagi469/playground-Jev](https://github.com/yagi469/playground-Jev) | — | 0 | Python | 2026-09-21 |
| [yama4936/mahjong-agent](https://github.com/yama4936/mahjong-agent) | — | 0 | TypeScript | 2026-09-21 |
| [yandong2023/jev-test](https://github.com/yandong2023/jev-test) | — | 0 | TypeScript | 2026-09-21 |
| [yangzhou-chaofan/awesome-jev-prompt](https://github.com/yangzhou-chaofan/awesome-jev-prompt) | latest top 100 showcases for jev (keep updating) from x / github / latest sources | 0 | JavaScript | 2026-09-20 |
| [yanmad27/ask-jev](https://github.com/yanmad27/ask-jev) | Ask Jev before asking you — a Claude Code plugin that answers AskUserQuestion from conversation context, and … | 0 | JavaScript | 2026-09-21 |
| [yannip1234/codex-jev](https://github.com/yannip1234/codex-jev) | Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client. | 0 | Rust | 2026-09-19 |
| [yesitsfebreeze/pearde](https://github.com/yesitsfebreeze/pearde) | pearde — a PRD board worked by one orchestrator session: specs ahead, dispatches implementers, asks when it m… | 0 | TypeScript | 2026-09-19 |
| [yinlu01/interview-coach](https://github.com/yinlu01/interview-coach) | 模拟面试 Agent：LLM 面试官 + JEV 实时五维测评。基于简历与 JD 出题、智能追问、本地语音转写、复盘报告 | 0 | Python | 2026-09-20 |
| [yldm-tech/loom](https://github.com/yldm-tech/loom) | Generate a landing page from one sentence: an LLM writes the copy, Jev makes the judgement calls, code owns t… | 0 | TypeScript | 2026-09-21 |
| [yn01/jev-stormboard](https://github.com/yn01/jev-stormboard) | Jev × 東京の防災電文 — 気象庁の防災情報XMLをリアルタイムに取り込み、TypeSafe の Jev が「自分にとって何を意味するか」を判定する Streamlit デモ | 0 | Python | 2026-09-20 |
| [yo4e/JevPip](https://github.com/yo4e/JevPip) | GMOのFX/BTC市場データに対応したローカル市場研究ターミナル。ライブチャート、ペーパートレード、バックテスト、安全監督、TypeSafe Jev連携。安全機構を整えたうえで実売買対応予定。 | 0 | Python | 2026-09-21 |
| [yodablocks/commitjev](https://github.com/yodablocks/commitjev) | Reads a commit before a reviewer has to: whether the message matches the diff, whether the edits belong in on… | 0 | Python | 2026-09-20 |
| [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) | Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and inv… | 0 | Python | 2026-09-20 |
| [yoredstorm/zent_rag](https://github.com/yoredstorm/zent_rag) | RAG con IA | 0 | Python | 2026-09-21 |
| [YosAwed/python-jev-if](https://github.com/YosAwed/python-jev-if) | Use TypeSafe Jev yes/no probabilities in Python if conditions. | 0 | Python | 2026-09-21 |
| [yotiosoft/Yapps](https://github.com/yotiosoft/Yapps) | 自作Webアプリ集 | 0 | HTML | 2026-09-21 |
| [yottayoshida/jev-intent-review](https://github.com/yottayoshida/jev-intent-review) | Verify a pull request against the intent that caused it, across the whole repository, with small typed judgme… | 0 | TypeScript | 2026-09-21 |
| [YouHyuksoo/cinema](https://github.com/YouHyuksoo/cinema) | — | 0 | TypeScript | 2026-09-21 |
| [yslinear/cartpole-jev](https://github.com/yslinear/cartpole-jev) | A tug-of-war over one shared actuator — you and TypeSafe's Jev push the same CartPole and the forces add. Phy… | 0 | JavaScript | 2026-09-21 |
| [yteruel31/pi-toolbox](https://github.com/yteruel31/pi-toolbox) | A collection of packages, themes, and extensions for Pi | 0 | TypeScript | 2026-09-21 |
| [yuan-phd/jev-rlcd-research](https://github.com/yuan-phd/jev-rlcd-research) | — | 0 | Python | 2026-09-21 |
| [yuki-dev26/jev-test](https://github.com/yuki-dev26/jev-test) | Jevの検証用 | 0 | JavaScript | 2026-09-19 |
| [yurenju/jev-playground](https://github.com/yurenju/jev-playground) | — | 0 | TypeScript | 2026-09-20 |
| [zahere-dev/sentiment-analysis-with-jev](https://github.com/zahere-dev/sentiment-analysis-with-jev) | — | 0 | HTML | 2026-09-20 |
| [zaichu/m5stack-pc-remote](https://github.com/zaichu/m5stack-pc-remote) | — | 0 | Rust | 2026-09-21 |
| [zanedonkey/jev-pet](https://github.com/zanedonkey/jev-pet) | Telegram group pet — Jev decides when it speaks; an LLM decides what it says. | 0 | TypeScript | 2026-09-21 |
| [zapz-glitch/flowstate-v5](https://github.com/zapz-glitch/flowstate-v5) | Flowstate v5 repo with prod main and integration branches | 0 | TypeScript | 2026-09-21 |
| [zavocc/ground-zero](https://github.com/zavocc/ground-zero) | Eval framework library to evaluate AI hallucinations, correctness, and instruction following, powered by Jev … | 0 | Python | 2026-09-21 |
| [zbloss/jev-plays-pokemon](https://github.com/zbloss/jev-plays-pokemon) | Like Claude Plays Pokemon, but with Jev | 0 | Python | 2026-09-21 |
| [zchee/typesafe-sdk-rust](https://github.com/zchee/typesafe-sdk-rust) | — | 0 | Rust | 2026-09-21 |
| [zebedelu/sudoku-vs-jev](https://github.com/zebedelu/sudoku-vs-jev) | A terminal Sudoku game where TypeSafe's Jev model plays the game, built to probe its decision-making move by … | 0 | Python | 2026-09-20 |
| [ZeroX-01/jev-atlas](https://github.com/ZeroX-01/jev-atlas) | Continuously updated public index of real TypeSafe JEV projects, videos, articles, and open-source demos. | 0 | JavaScript | 2026-09-21 |
| [zhuyansen/x-reply-filter](https://github.com/zhuyansen/x-reply-filter) | Chrome extension: collapse spam, bait, off-topic and AI-filler replies on X. Local rules + TypeSafe Jev, lear… | 0 | JavaScript | 2026-09-21 |
| [zixiang0623/Jev-Openrouter](https://github.com/zixiang0623/Jev-Openrouter) | Vercelに一時的に依存 | 0 | HTML | 2026-09-21 |
| [ziyu/system-one-sdk](https://github.com/ziyu/system-one-sdk) | Unified interface wrapper for system one models | 0 | JavaScript | 2026-09-20 |
| [zlZayn/AI-decision-maker](https://github.com/zlZayn/AI-decision-maker) | AI 只判断数据每列是什么类型，输出一个字符。支持两种引擎：生成式 LLM 与概率引擎 Jev，实测清洗与分类结论一致。 | 0 | Python | 2026-09-21 |
| [zohaibtanwir/jev-inbox-lab](https://github.com/zohaibtanwir/jev-inbox-lab) | Local lab for exploring TypeSafe's Jev model on a frozen personal email corpus | 0 | Python | 2026-09-21 |
| [zojeda/llama-cpp-system-one](https://github.com/zojeda/llama-cpp-system-one) | A Rust implementation of the System One API for structured question answering with DiffusionGemma and llama.c… | 0 | Rust | 2026-09-21 |
| [zong09/cane](https://github.com/zong09/cane) | — | 0 | Python | 2026-09-21 |
## Contributing

Open a pull request. The index is swept automatically, so you do not need to add a project by
hand — but a Featured entry is a human judgment and always welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).
