# Ruslan Udintsev

**AI Agent Operations · AI-assisted Development Coordination · Product & QA**

I coordinate AI coding agents to move real software projects from requirements to tested outcomes. My focus is on **task decomposition, multi-agent coordination, GitHub workflows, quality gates, release safety, and practical product decisions**.

I work hands-on with ChatGPT, Codex, Gemini and developer tooling. I am not claiming to be a senior software engineer or the sole author of agent-generated code: my role is to **define the work, steer execution, verify evidence, and take responsibility for decisions**.

**Open to:** AI Agent Operator, Junior AI Automation Specialist, AI-assisted QA, and AI Development Coordinator opportunities (remote / project-based).

[Русская версия](README.ru.md) · [Detailed case studies](CASE_STUDIES.md) · [GitHub profile](https://github.com/ruslanudintsev-ai)

---

## What I do

- **Coordinate multiple agents:** divide work by responsibility, establish boundaries, manage task dependencies and follow-ups.
- **Operate GitHub workflows:** track issues, branches, pull requests, CI results, reviews, and release readiness.
- **Turn vague requests into testable work:** document acceptance criteria, evidence requirements, rollback conditions and blockers.
- **Investigate real problems:** reproduce failures, compare hypotheses and verify changes in the actual environment.
- **Stay evidence-driven:** distinguish a successful build from deployment, and a draft from a published product.

## Selected work

### 1. Multi-agent operations for a Laravel web product

Coordinated two parallel Codex workstreams on **1creditonline.ru**: one focused on data/import reliability, the other on design/UI quality. A separate dispatch workflow tracked PRs, CI status and cross-team constraints.

**My contribution:** orchestration model, prioritization, scope boundaries, review of results and safe release decisions — not a claim to have individually authored the underlying Laravel implementation.

**Tools / concepts:** Codex, GitHub Issues & PRs, GitHub Actions, Laravel, CI checks, deployment safeguards.

### 2. Production troubleshooting: iPhone cellular access and Nginx

Investigated a real production issue where an HTTPS website behaved differently over cellular data versus Wi-Fi/VPN. A controlled change enabling HTTP/2 was followed by a successful load on the affected iPhone. The exact low-level cause remains unproven.

**Public evidence:** [Technical case study, with diagnostic steps, uncertainty and rollback](https://github.com/ruslanudintsev-ai/ios-cellular-nginx-http2-fix).

**My contribution:** problem reporting, hands-on device verification, hypothesis testing and documenting the observed outcome.

### 3. Recovery QA for a large Django / SEO catalogue

Coordinated recovery validation for an existing insurance catalogue spanning **83 regions, 1,102 cities and 196 vehicle models**. The documented recovery build rendered **217,184 HTML routes** and verified a **216,076-URL sitemap contract**.

These are **recovery / testing figures**, not claims of search traffic, production deployment or successful indexing.

**My contribution:** requirements, scope control, QA acceptance and separating source recovery from production rollout.

### 4. Editorial automation and source-quality workflows

Working on **KursoPilot**, an educational-course comparison product, and other content experiments involving template design, source attribution, QA, duplicate controls, and publication gates. These are **works in progress**; I do not present unpublished pilots as launched products.

### 5. Product feedback for OpenAI Codex

Contributed a concrete user workflow to a public feature request for native **ChatGPT ↔ Codex bidirectional agent delegation**, based on hands-on testing of Grok Bot → Cursor.

[Read the public GitHub comment](https://github.com/openai/codex/issues/40142#issuecomment-6492738160).

---

## How I coordinate agent work

```text
Goal and constraints
       ↓
Task breakdown + agent assignments
       ↓
Implementation in isolated branches/worktrees
       ↓
PR + automated tests + human-readable evidence
       ↓
Review failures, clarify requirements, iterate
       ↓
Release decision and post-release verification
```

**Operating principle:** an AI-generated change is not a verified result. I look for reproducible tests, an auditable diff, explicit limitations, and an appropriate approval boundary before production actions.

## Tools and learning

**Regular workflow:** ChatGPT, Codex, Gemini, GitHub, Issues/PRs, GitHub Actions, CI reporting, browser checks, documentation, SEO diagnostics.

**Project exposure:** Laravel, Django, Astro/TypeScript, Nginx, Docker, Cloudflare, APIs and automation tools.

**Currently developing:** independent Python scripting, reading/debugging code, API integration, software test design and agent orchestration architecture. *Exposure to a tool is not represented as expert proficiency.*

## Collaboration

If you need someone who can translate product goals into effective AI-agent tasks, keep multiple workstreams organized and insist on verifiable outcomes, I would be happy to discuss a practical trial project.

**Contact:** [GitHub profile](https://github.com/ruslanudintsev-ai) · [Open an issue in this portfolio repository](https://github.com/ruslanudintsev-ai/test/issues)

*Private production repositories, infrastructure details, secrets, customer data, and internal reports are intentionally excluded. Additional non-sensitive examples can be shared selectively.*

_Last reviewed: October 2026._
