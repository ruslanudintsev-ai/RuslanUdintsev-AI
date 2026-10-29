# AGENTS.md — public portfolio maintenance

This repository is a **public professional portfolio**, not a development or deployment workspace for any of the projects it mentions.

## Scope

- You may edit **only this portfolio repository** when asked to add or improve a case.
- Do not read or copy private source, secrets, logs, raw screenshots or infrastructure details into public files.
- Never create links that imply private repository contents are publicly accessible.
- Do not run, deploy, reconfigure or modify another project while updating this portfolio.
- Do not make unsupported employment, skill, client, product, traffic, profit or reliability claims.

## Sources and checks

1. Re-read the relevant source project's current README/status and the original test evidence.
2. Describe the portfolio owner's **coordination/testing/product** role distinctly from agent-authored implementation.
3. Mark every project **production / staged / experimental / archived / paused** using source-supported wording.
4. Separate **draft → implementation → tested → merged → deployed → observed → measured impact**.
5. For numerical evidence, provide the test/environment/snapshot meaning; never turn QA counts into live metrics.
6. Publish a public proof link only if public access is verified; otherwise say "private evidence available for a sanitized walkthrough."
7. Use the structure in [CASE_TEMPLATE.md](CASE_TEMPLATE.md), update [CASE_STUDIES.md](CASE_STUDIES.md), and adjust navigation on [README.md](README.md) and [README.ru.md](README.ru.md) as needed.
8. Update skills through the canonical [skills/registry.json](skills/registry.json): distinguish personally demonstrated operation (`practical`), delivery via AI coding agents (`agent_assisted`), and learning (`learning`). Do not present learning as experience. Keep [SKILLS.md](SKILLS.md) and [SKILLS.ru.md](SKILLS.ru.md) synchronized.
9. Run `python scripts/check_skills.py` to validate the registry and both language pages before finishing.
10. Review all files for privacy leakage; verify links and Markdown before finalizing.

## Profile navigation

- English landing: `README.md`
- Russian landing: `README.ru.md`
- English project map: `ECOSYSTEM.md`
- Russian project map: `ECOSYSTEM.ru.md`
- Case studies: `CASE_STUDIES.md`
- Verified skills matrix: `SKILLS.md` and `SKILLS.ru.md`
- Canonical machine-readable skills: `skills/registry.json`
- Registry validation: `scripts/check_skills.py`
- Coordination workflow: `AGENT_OPERATIONS.md`
- Evidence and privacy: `EVIDENCE_AND_PRIVACY.md`

## Quality gate

No misleading badges or synthetic statistics. No portfolio additions should imply endorsement by OpenAI, ownership of third-party software, or independent authorship of all AI-generated code.

Use plain-language, precise technical writing. When status is unknown, write **not verified** rather than guessing.
