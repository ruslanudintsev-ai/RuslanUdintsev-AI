# Professional skill system — AI Agent Operations

[Portfolio](README.md) · [Case studies](CASE_STUDIES.md) · [Agent workflow](AGENT_OPERATIONS.md) · [Machine-readable registry](skills/registry.json)

**My strongest skills are in operating AI-assisted work, not independently writing every system component.** An agent-generated implementation does not automatically prove personal engineering mastery. Snapshot: **29 October 2026**.

## Skill levels

- **Hands-on operational (practical)** — I perform this as an owner/operator: scope work, verify results and make decisions.
- **AI-assisted delivery (agent_assisted)** — Implemented in agent-assisted projects. I can describe scope and validation, but not claim independent implementation expertise.
- **Learning / not independently evidenced (learning)** — An explicit learning goal without verified independent professional delivery.

## Skills inventory

### AI agent operations

| Skill | Level | What I've done / limitations | Evidence |
| --- | --- | --- | --- |
| **Agent task briefing** | Hands-on operational | Task scope, acceptance criteria and evidence requirements for Codex | [case](AGENT_OPERATIONS.md) · [case](CASE_STUDIES.md) |
| **Multi-agent workstream coordination** | Hands-on operational | Separated DATA / DESIGN workstreams, dependencies and conflict control | [case](CASE_STUDIES.md) |
| **GitHub Issues, PRs and branch discipline** | Hands-on operational | Tracking tasks, PRs and changes; implementation may be agent-authored | [case](AGENT_OPERATIONS.md) |
| **CI and test-evidence review** | Hands-on operational | Reviewing SHA-specific checks and keeping merge separate from deploy | [case](AGENT_OPERATIONS.md) · [case](CASE_STUDIES.md) |
| **Release gates and rollback planning** | Hands-on operational | Approval boundaries for risky actions and rollback-aware decisions | [case](AGENT_OPERATIONS.md) |
| **Prompt/task iteration** | Hands-on operational | Iterating on agent tasks based on errors and QA results | [case](CASE_STUDIES.md) |

### LLM products and integrations

| Skill | Level | What I've done / limitations | Evidence |
| --- | --- | --- | --- |
| **LLM product flow design** | Hands-on operational | Product planning for input → structure → validation → output | [case](CASE_STUDIES.md) |
| **LLM cost-safety rules** | Hands-on operational | Opt-in paid API requests, fake-mode and limits | [case](CASE_STUDIES.md) |
| **LLM API integrations: OpenRouter / DeepSeek** | AI-assisted delivery | Integrated in agent-built Telegram prototypes; independent backend implementation not claimed | [case](CASE_STUDIES.md) |
| **Structured LLM outputs and validation** | AI-assisted delivery | Structured JSON contracts and generation validation in bot prototypes | [case](CASE_STUDIES.md) |
| **AI Telegram bot workflows** | AI-assisted delivery | Music bot fake-mode E2E and reply bot MVP with payment safeguards | [case](CASE_STUDIES.md) · [case](ECOSYSTEM.md) |
| **Retries, idempotency and balance handling** | AI-assisted delivery | Agent-implemented functions tested in prototype scenarios | [case](CASE_STUDIES.md) |
| **External service/tool integration** | AI-assisted delivery | Telegram/API/GitHub workflows; autonomy varies by project | [case](ECOSYSTEM.md) · [case](AGENT_OPERATIONS.md) |

### QA, infrastructure and release safety

| Skill | Level | What I've done / limitations | Evidence |
| --- | --- | --- | --- |
| **HTTPS/Nginx incident investigation** | Hands-on operational | Public field report on iPhone, HTTP/2 tests and causal uncertainty | [public proof](https://github.com/ruslanudintsev-ai/ios-cellular-nginx-http2-fix) |
| **Mobile/browser verification** | Hands-on operational | Checking site behavior across devices and networks | [case](CASE_STUDIES.md) |
| **Test/staging/production status discipline** | Hands-on operational | Explicit environments and honest status reporting | [case](AGENT_OPERATIONS.md) |
| **GitHub Actions CI/CD pipelines** | AI-assisted delivery | Review CI results; technical workflow implementations are agent-assisted | [case](CASE_STUDIES.md) |
| **Docker, Cloudflare and deployment environments** | AI-assisted delivery | Agent-assisted project operations; not claiming DevOps engineer proficiency | [case](ECOSYSTEM.md) |
| **Laravel / Django / Astro web stacks** | AI-assisted delivery | Scoping and acceptance across agent-built stacks | [case](CASE_STUDIES.md) · [case](ECOSYSTEM.md) |

### Product, data and research

| Skill | Level | What I've done / limitations | Evidence |
| --- | --- | --- | --- |
| **Source provenance and factual checks** | Hands-on operational | Keeping reported data separate from verified data before publication | [case](CASE_STUDIES.md) |
| **Technical SEO and large-catalogue QA** | Hands-on operational | Sitemaps, canonicals, routes and indexing safeguards | [case](CASE_STUDIES.md) |
| **Product ownership and prioritization** | Hands-on operational | Cost-aware prioritization and explicit stopping decisions | [case](ECOSYSTEM.md) |
| **Research discipline and stop rules** | Hands-on operational | Stopping experimental research without reliable positive evidence | [case](CASE_STUDIES.md) |
| **Reinforcement learning: DQN/Rainbow exposure** | AI-assisted delivery | Educational experiments, not independent ML engineering expertise | [public proof](https://github.com/ruslanudintsev-ai/dqn-beginner-rainbow-trading) |

### Technical growth

| Skill | Level | What I've done / limitations | Evidence |
| --- | --- | --- | --- |
| **Independent Python and backend implementation** | Learning / not independently evidenced | Learning to read, debug and implement without full agent delegation | — |
| **RAG and vector search** | Learning / not independently evidenced | No verified completed RAG implementation | — |
| **LangChain** | Learning / not independently evidenced | No verified production experience | — |
| **LangGraph** | Learning / not independently evidenced | Not used in the music workflow; no hands-on claim | — |
| **ATS / recruiting platform integrations** | Learning / not independently evidenced | Can scope such a project; no completed ATS integration | — |
| **Independent ML/Data Science engineering** | Learning / not independently evidenced | Some educational experiments; independent ML system delivery not verified | — |

## Promotion rules

1. Try a skill in a real, scoped project and describe my personal contribution.
2. Record outcome, tests, limitations and verifiable evidence.
3. Upgrade only on corroborated personal practice; agent-authored implementation stays `agent_assisted` until independent engineering skill is demonstrated.
4. Update `skills/registry.json`, both skills pages and profile navigation.
5. Validate with `python scripts/check_skills.py`.

**Important:** RAG, LangChain, LangGraph, ATS integration and independent ML engineering are learning targets, not skills I claim to have delivered professionally.
