# Selected case studies

[Main portfolio](README.md) · [Русская версия](README.ru.md)

These examples describe **product ownership, agent coordination, field testing and QA**. Much of the implementation was carried out using AI coding agents. Private repositories are not exposed as if they were public.

## Case A — Parallel Codex coordination for 1creditonline.ru

**Problem:** a Laravel product had simultaneous needs in data/import reliability and interface design. Mixing workstreams risked conflicting changes and unclear release responsibility.

**Approach:**
1. Separate responsibilities into a **DATA** and **DESIGN** workstream.
2. Track tasks through GitHub Issues and pull requests, with a coordination/dispatch layer.
3. Require isolated branches/worktrees, focused tests and CI status before combining changes.
4. Distinguish branch, merged code and actual production state.
5. Escalate sensitive database and deployment operations through stricter approval gates.

**My role:** owner / AI-agent coordinator; scope definition, prioritization, oversight and acceptance.

**Outcome:** an established operating model for two concurrent coding agents, documented internally. No unverified claim of financial or conversion impact.

**Evidence:** private project README and task history, which can be demonstrated selectively without granting access to credentials or customer data.

## Case B — HTTPS access incident on iPhone (public)

**Problem:** Safari on an iPhone intermittently failed to display a production site over cellular data while Wi-Fi and VPN tests behaved differently.

**Approach:** investigate host and static responses, JavaScript, compression, TLS and proxy behavior; compare behavior with and without HTTP/2; verify the same device and production hostname after a scoped Nginx configuration change.

**Observed outcome:** enabling HTTP/2 on production HTTPS virtual hosts was followed by an immediate successful load via cellular data on the affected iPhone. HTTP/1.1 fallback remained available.

**Important limits:** this is a field observation, not a controlled proof of a protocol bug or long-term universal fix. An Nginx reload may also have influenced connection state.

**My role:** hands-on verification on the affected device, investigation coordination, documenting limitations and outcome.

**Public proof:** [Case study and supporting diagnostics](https://github.com/ruslanudintsev-ai/ios-cellular-nginx-http2-fix).

## Case C — Django catalogue recovery and QA

**Problem:** an existing catalogue generator had to be reconstructed and validated without treating an exploratory build as authorization to deploy.

**Documented test scope:**
- 83 regions
- 1,102 cities
- 196 vehicle models
- 217,184 rendered HTML routes in the recovery artifact
- 216,076 unique sitemap URLs verified in the recovery contract

**Approach:** reconstructed Django → deterministic static render → automated route, sitemap, canonical and language QA → separate release decision.

**My role:** steering the recovery requirements, prioritizing correctness, checking QA evidence and keeping production changes separate.

**Important limit:** these numbers describe a recovery build, **not** live traffic, search indexing or published page count.

**Evidence:** private repository documentation and test reports.

## Case D — Source-quality and editorial automation (in progress)

**Products:** KursoPilot and content-template experiments.

**Problem:** AI can produce content at scale, but copied or unsupported claims, inconsistent data, duplicate URLs and unchecked publication can reduce usefulness.

**Approach:** source lineage, verified-vs-reported distinctions, reusable templates, QA controls, publication gates and explicit rollback plans.

**My role:** product requirements and review of agent-delivered work.

**Status:** active experiments; no claim that every pilot is publicly launched, indexed or monetized.

## Case E — Product feedback based on a competitive workflow

**Observation:** in a normal Grok conversation, a bot could delegate to Cursor and return agent progress/results without manually copy-pasting between products.

**Proposal:** a native, permission-scoped ChatGPT ↔ Codex delegation channel with continuing bidirectional coordination.

**Public proof:** [OpenAI Codex issue #40142 — my comment](https://github.com/openai/codex/issues/40142#issuecomment-6492738160).

## Skills demonstrated across the cases

- Translating goals into agent-ready tasks
- Delegation, responsibility boundaries and follow-up coordination
- GitHub Issues, PRs, CI and test-result interpretation
- Reproducibility, evidence quality and accurate status reporting
- Safer operational decisions around production and private data
- User-focused product feedback grounded in actual experiments

**What I am still improving:** writing and debugging code independently, API design, Python fluency and evaluation techniques for AI-agent reliability.

**Privacy:** no internal IPs, credentials, financial data, customer records or unrestricted private repository links are included here.
