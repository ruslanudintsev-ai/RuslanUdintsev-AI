# Portfolio evidence, accuracy and privacy rules

[Portfolio](README.md) · [Case studies](CASE_STUDIES.md) · [Ecosystem](ECOSYSTEM.md)

**Purpose:** make a public professional portfolio credible, independently inspectable where possible, and safe for private products.

## What counts as evidence

| Level | Typical evidence | Acceptable claim |
| --- | --- | --- |
| Public and reproducible | Public README, commit or issue, documented test steps | Verifiable public artifact with stated limitations |
| Private but internally documented | Scoped task / PR / CI run / QA report | Work is described at a high level; source is not linked as though public |
| Operator observation | Repeated device/browser tests, before/after description | Observation only; cause may remain uncertain |
| Prototype / staging | Local smoke, preview URL, fake-mode or sandbox tests | Prototype/staging success, **not** production availability |
| Hypothesis | Proposal, research note or unverified idea | Research direction only, **not** a result |

## Publication checklist

- Give my **actual role**: product owner, AI-agent coordinator, tester or researcher; distinguish AI-written code from manually written code.
- State the exact **environment and date** whenever a result depends on them.
- Preserve the difference between an issued task, green CI, merge, deploy and measured business impact.
- Do not invent stars, clients, revenue, traffic, uptime, job titles, years of professional employment or performance gains.
- Do not claim a model is accurate, profitable or production-ready without independent supporting evidence.
- Mark paused projects as paused; mark experiments as experiments.
- Remove credentials, tokens, IP addresses, internal paths, production logs, customer information, unpublished pricing, personal data and sensitive security details.
- Do not publish copied internal notes/screenshots without a deliberate sanitization review.
- Never treat a private GitHub repo link as a public demonstration; provide a redacted walkthrough only where appropriate.
- Treat external/third-party tools as credited collaborators; do not claim personal implementation of their code.

## Change procedure for this repository

1. Verify a project’s current status from its own source of truth.
2. Add or update a case with: **problem → my role → approach → evidence → result → limits**.
3. Check that public links resolve without private access.
4. Review files for sensitive strings and accidental private paths.
5. Commit portfolio-only edits; do not make changes to production repositories as part of a portfolio update.
6. Recheck root navigation in both English and Russian.

**Snapshot date:** 29 October 2026. Portfolio pages are historical summaries unless updated; they are not live status dashboards.

**Contact:** [GitHub profile](https://github.com/ruslanudintsev-ai).
