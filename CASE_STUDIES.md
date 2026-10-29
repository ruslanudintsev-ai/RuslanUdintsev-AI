# Case studies: real AI-agent operations

[Profile](README.md) · [Русский профиль](README.ru.md) · [Ecosystem](ECOSYSTEM.md) · [Agent workflow](AGENT_OPERATIONS.md)

> **How to read this page:** I coordinate AI-assisted projects as the owner/operator. Coding agents authored substantial portions of implementation. Each case states my role, the checked outcome and the evidence boundary. Private repository references below are **not public links**. Descriptions are sanitized for a public portfolio. Snapshot: 29 October 2026.

## Case 01 — Operating two Codex agents on one Laravel product

**Problem.** A production web product needed simultaneous data/import reliability work and UI improvements. Parallel agent changes risked conflicts, unclear ownership and unsafe changes to production data.

**My role.** Product owner and AI-agent coordinator: defined separate DATA and DESIGN responsibilities, prioritization, acceptance criteria, safety rules and review of PR/CI outcomes.

**Approach.**
- **DATA agent:** data sources, parser, importer and correctness checks.
- **DESIGN agent:** Blade/CSS, responsive UX, interface and visual tests.
- **Coordination layer:** GitHub tasks and handoffs, cross-scope review, CI status, blockers and integration decisions.
- Separate branches/worktrees; production data writes require narrower permission, backup, dry run and verification.

**Observed outcome.** The parallel operating model and task boundaries were recorded and used for work in the Laravel workspace. This is evidence of coordination, **not** a claim that all agents autonomously exchange messages in a normal ChatGPT thread.

**Evidence.** Private project README, role-specific issues, PR/CI history (available only in a sanitized walkthrough).

**Limit.** No unsupported claim of business impact, full self-written code or all tasks already deployed.

## Case 02 — Debugging a real iPhone / Nginx production incident

**Problem.** The same HTTPS site sometimes failed to render on Safari over iPhone mobile data, while Wi-Fi/VPN access behaved differently.

**My role.** Field tester and investigation coordinator: tested the affected device, reported outcomes, separated inconsistent observations and verified production behavior after a small configuration change.

**Approach.** Eliminated or examined alternative explanations including host routing, static responses, JavaScript, compression, TLS and connection behavior; tested an HTTP/2-enabled diagnostic virtual host, then an explicitly scoped production change.

**Observed outcome.** Enabling HTTP/2 on production HTTPS hosts was followed by a successful load on the same affected iPhone over mobile data. HTTP/1.1 fallback remained available.

**Public evidence.** [Documented case study](https://github.com/ruslanudintsev-ai/ios-cellular-nginx-http2-fix), including [Russian translation](https://github.com/ruslanudintsev-ai/ios-cellular-nginx-http2-fix/blob/main/README.ru.md).

**Limit.** The root cause was **not proven**; Nginx reload and network/browser state could have contributed. One successful test is not universal long-term validation.

## Case 03 — Large Django catalogue: reconstruction and static-build QA

**Problem.** A lost/local Django static generator had to be reconstructed from surviving artifacts without treating a recovery test as permission to alter production.

**My role.** Requirements, agent steering, QA acceptance and the separation of recovery validation from rollout decisions.

**Verified recovery scope (recorded in project documentation):**

| Metric | Recovery QA result |
| --- | ---: |
| Regions | 83 |
| Cities | 1,102 |
| Vehicle models | 196 |
| Rendered HTML routes | 217,184 |
| Unique sitemap URLs verified | 216,076 |

**Approach.** Django source reconstruction → deterministic static render → regression tests → sitemap-to-file, canonical, grammar and representative user-flow verification.

**Observed outcome.** A recovery artifact was generated and validated against the documented route/sitemap contract.

**Evidence.** Private test results and recovery reports; counts are included here for scope, not as public GitHub artifacts.

**Limit.** **Not** a claim that 217,184 pages were deployed, indexed or useful to search engines. A separate release and SEO strategy are needed.

## Case 04 — Editorial automation without invented source facts

**Problem.** Large-scale AI-assisted publishing can create unverifiable course claims, inconsistent prices, duplicate pages and misleading publication statuses.

**My role.** Product requirements, QA rules, editorial approval criteria and review of agent-produced records.

**Approach.** Separate external-source reported facts from verified facts; keep original snapshots and source lineage, require editorial gates, ensure taxonomy research is not automatically treated as published pages.

**Observed outcome.** KursoPilot has defined an Astro/TypeScript workflow with source capture rules and a publication quality gate. Related catalogue experiments maintain explicit historical-price/freshness caveats.

**Evidence.** Private project documentation and CI/QA contracts.

**Limit.** This case covers the editorial/source workflow. Individual course-page publication and search-engine indexing were **not** established; a later, limited site release is recorded separately in [Case 10](#case-10--kursopilot-agent-assisted-public-release-of-a-course-catalogue).

## Case 05 — AI Telegram product: cost, privacy and safe experimentation

**Problem.** Calling paid AI/music APIs without limits can waste money while a product is still unvalidated. User-facing bots also need reliable retries, privacy and delivery behavior.

**My role.** Product choices and cost constraints; coordinating the agent-built planning, validation, delivery, feedback and safe test path.

**Approach.**
- One structured story-planning pass with strict validation.
- Deterministic compilation / adapter for audio generation.
- Development fake mode with deterministic local artifacts and **paid music requests off by default**.
- End-to-end checks for delivery, feedback, replay/idempotency and privacy.
- Live paid-music quality evaluation deferred until a separate explicit decision.

**Observed outcome.** The music-gift Telegram workflow passed end-to-end **fake-mode acceptance**; no paid music-generation acceptance is claimed.

**Evidence.** Private product README and recorded acceptance reports.

**Limit.** Fake-mode is not evidence of real music quality or commercial launch. The developer tools and model providers are credited as implementation components.

## Case 06 — Research discipline: knowing when to stop

**Problem.** AI-supported trading experiments are vulnerable to overfitting, exaggerated performance and endless spending without a reliable signal.

**My role.** Project oversight, decision to pause and insistence on data, baseline and failure reporting.

**Recorded historical cohort:**

```text
127 candidate trigger ideas
→ 13 triggers fired
→ 10 confirmed
→ 6 entry evaluations
→ 0 entries
```

**Observed outcome.** The LLM trading research project was **frozen** after evidence failed to establish a repeatable edge. Related FinRL/Mamba work was also paused under explicit cost controls.

**Evidence.** Private research retrospective, findings and experiment records. Separately, an [educational public DQN repo](https://github.com/ruslanudintsev-ai/dqn-beginner-rainbow-trading) demonstrates baseline comparison exercises.

**Limit.** No claim of profitability, broker access, validated forecasts or a deployable strategy.

## Case 07 — Managing a multi-project AI development portfolio

**Problem.** Work across many repositories becomes difficult to coordinate when instructions, status reports and agent decisions are scattered.

**My role.** Portfolio owner: keep priorities and product rules clear, align research with actual user outcomes, organize task queues and decide where attention is worth spending.

**Approach.** Separate project repositories from cross-project decisions, use GitHub Issues/PRs and an aggregated board, keep research/source evidence outside code where appropriate, and use a simple priority and status vocabulary.

**Observed outcome.** A portfolio-level operating model coordinates multiple products and experiments. A prior reviewed sample covered **26 repositories**; the connected account listed **36 accessible repositories on 29 October 2026**, with recently recovered research repos not individually revalidated. The count is not an outcome metric.

**Evidence.** GitHub account inventory and private portfolio operating documentation.

**Limit.** Repo count is **not** a proxy for independent software engineering experience, revenue, or fully autonomous agents.

## Case 08 — Improving the developer workflow through product feedback

**Problem.** Moving work between ChatGPT and Codex frequently requires the person to manually carry task prompts, results and blockers between interfaces.

**My role.** Hands-on tool evaluator and product-feedback contributor.

**Approach.** Tested a real Grok → Grok Bot → Cursor example, documented what made it useful and proposed ongoing permission-scoped, bidirectional ChatGPT ↔ Codex delegation rather than a one-off prompt handoff.

**Observed outcome.** The user workflow and proposal were **published as a comment** in an existing OpenAI Codex feature issue.

**Public evidence.** [OpenAI Codex #40142 — feature request comment](https://github.com/openai/codex/issues/40142#issuecomment-6492738160).

**Limit.** Public feedback is **not** evidence of endorsement, roadmap inclusion or employment by OpenAI.

## Case 09 — Historical pet-food websites with automated content population (owner-reported)

**Products.** Two historical pet-food content websites: `korm-dlya-zhivotnyh.ru` and `luchshiekormadlyasobak.ru`. This is a **past / discontinued direction**, not an active deployment or a newly launched business.

**Problem.** Maintaining niche content sites manually (topics, articles, updates and internal linking) does not scale well for an independent publisher.

**My role.** Site owner and operator. I report that an **automatic site-content filling workflow was used** in this earlier project. The exact scripts, platform/plugin configuration, implementation authorship and automation coverage have not yet been independently recovered, so this is clearly an **owner-reported historical workflow**.

**Evidence and distinction.** Historical articles and category/ranking pages from September 2024 are documented in private project research. A later master planning document specified an **aspirational, broader** autopilot: sources/feeds → normalization → content generation/updating → WordPress/API publishing → internal links → search monitoring → reporting. **That proposed end-to-end architecture must not be represented as fully implemented historically.** No matching source repository or reproducible implementation proof is currently available on GitHub.

**Learning.** This was an early practical encounter with automated content operations, editorial scale and the need to balance automation against content quality, provenance and actual search/affiliate economics.

**Limitations.** Past automation is based on the owner's firsthand report; exact throughput, technologies, degree of autonomy and traffic/revenue effect are **not verified**. These domains should not be presented as active products, and no claim is made that AI/LLMs powered the original automation. No new development or domain renewal is implied.

---

## Hiring-relevant capabilities

**Hands-on operations:** agent task delegation, scope and responsibility boundaries, GitHub Issue/PR/CI coordination, release-state verification, incident triage, product QA, API cost gates, and clear documentation.

**Developing skills:** independent Python development, API architecture, debugging and rigorous reliability measurement.

**Privacy and credibility:** private source code, credentials, internal URLs, raw logs and customer data are not reproduced. See [evidence & privacy rules](EVIDENCE_AND_PRIVACY.md).

Want a practical test? A suitable interview exercise is a **read-only audit of a sample repository followed by a scoped AI-agent task brief, QA evidence checklist and proposed follow-up**, rather than a claim to implement an entire product unaided.

## Case 10 — KursoPilot: agent-assisted public release of a course catalogue

**Product:** [KursoPilot](https://kursopilot.ru/) — course search and comparison for Russian-language users, built with Astro and TypeScript. The source repository is private.

**Problem.** Turn research, scattered course records and product requirements into a usable online catalogue while controlling source accuracy, AI-assisted content generation, mobile experience and release safety.

**My role.** Product owner and AI-agent coordinator: set priorities and user needs, defined what the catalogue and editorial landing pages should do, separated workstreams and required test evidence and an explicit approval before public release. Coding agents completed substantial technical work.

**Agent workflow.** Gemini handled catalogue/UI and release execution; Codex maintained CI/runner and technical checks; ChatGPT helped coordinate editorial and release constraints. Publication decisions, scope and risk acceptance stayed with the owner. This is **AI-assisted operation with human oversight**, not proof of a fully autonomous production company.

**Recorded release outcome (operator-reported, 28 October 2026):**
- A constrained public release was reported as `DEPLOY_OK` on exact build SHA `40ab09886913dd2822ea3cd785710ef4fa8df496`.
- **10 editorial/navigation URLs** were marked eligible for indexing; **29 other routes** remained `noindex`.
- Post-deploy smoke checks were reported **16/16 PASS**; CI on the release candidate was reported successful.
- A separate local browser report covered Chromium at 320/390/1440 px; iOS/WebKit was not covered.

**Evidence.** Internal release issue and operational smoke report in the **private** product repository; counts are reported here with date and environment, not linked as though publicly inspectable. The product URL is a public-facing address, but independent external HTTP verification from this portfolio review environment was unavailable.

**Limits.** `INDEXING_ELIGIBLE` does **not** mean indexed; Google/Yandex index coverage, organic traffic, completed sales, affiliate commissions, independent uptime and full automatic ingestion at real-world scale are **not established** by this evidence. A prior local 1,000-record synthetic import test, if any, would not prove 1,000 live verified courses. Individual auto-generated course pages are not mass-indexed by this release. The product continues to evolve.

## Case 11 — GitHub-mediated coordination of Codex, Grok and Cursor

**Problem.** Several AI coding/review tools contributed to one private Django/SEO workflow. Without explicit task scope, CI evidence and distinct release decisions, bot comments could turn into duplicated actions, unrelated bugs could expand a PR and green tests could be mistaken for production readiness.

**My role.** Owner and coordinator: define work boundaries, inspect review findings, confirm an exact commit's checks, separate follow-up scope and keep merge/deploy decisions independent of agent-generated text.

**Observed example (29 October 2026).** A review found a potential **false-positive sitemap validation** in a private PR. The agent-authored revision introduced XML parsing, exact expected-inventory checks and regression cases. **Three CI workflows succeeded on the corrected commit**, while the PR stayed unmerged/undeployed. A separate client-side link-building concern was isolated in a different draft PR. A supplied screenshot also showed an agent **identifying one notification as an echo of its own comment** and not treating it as new work.

**Operating model.** GitHub Issues, PRs, comments, commit SHAs and CI results are the common **asynchronous coordination record**. These observations do not prove direct machine-to-machine chat, persistent autonomy or a general-purpose anti-loop guarantee.

**Public walkthrough and diagrams.** [Two Mermaid diagrams, evidence limits and sanitized case](docs/CASE_MULTI_AGENT_GITHUB.md).

**Evidence.** Owner-visible screenshot and private GitHub PR/CI records; private code, links, screenshots and infrastructure are deliberately not reproduced in this public portfolio.

**Limit.** AI agents authored major code changes; this is a coordination/QA example, not proof of self-written backend engineering, public deployment, financial benefit or zero-human operation.
