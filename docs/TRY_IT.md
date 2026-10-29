# Try the portfolio in 5 minutes — a reproducible PR/CI demo

**A small hands-on exercise for evaluating AI Agent Operations, not a production tool.**

[Главная RU](../README.ru.md) · [Русская инструкция](TRY_IT.ru.md) · [Source and limitations](../examples/pr-evidence-gate/README.md) · [Evidence index](EVIDENCE_INDEX.md)

## What you can verify for yourself

An AI-agent coordinator should not equate **green tests** with **permission to ship**. This public, AI-assisted Python example reads two **entirely fictional** PR snapshots and checks exact commit format, changed-file scope, required CI status and duplicate notifications from the actor.

| Synthetic snapshot | What it contains | Expected result |
| --- | --- | --- |
| `sample-approved.json` | Two successful checks, changes under permitted paths, one self-authored comment | `HUMAN_REVIEW_REQUIRED` — green CI still requires an owner |
| `sample-blocked.json` | A deployment file outside the allowed scope and an unfinished CI check | `BLOCKED` — no release recommendation |

The inputs are *manually supplied local JSON*, not a live GitHub API feed. There is no access to secrets, private repos, real PRs or external AI models.

## Run it yourself

Install Python **3.12+** and, from a terminal:

```bash
git clone https://github.com/ruslanudintsev-ai/RuslanUdintsev-AI.git
cd RuslanUdintsev-AI
python examples/pr-evidence-gate/triage.py --input examples/pr-evidence-gate/sample-approved.json
python examples/pr-evidence-gate/triage.py --input examples/pr-evidence-gate/sample-blocked.json
python -m unittest discover -s examples/pr-evidence-gate/tests -v
```

Expected observations: the first report says **HUMAN_REVIEW_REQUIRED**, the second **BLOCKED**, and **13 unit tests** are collected and pass. Run status should be checked on the **exact commit** you clone; a previous CI run is not proof of your local execution.

You can also inspect the public [GitHub Actions workflow](../.github/workflows/skills-check.yml) and its [runs](https://github.com/ruslanudintsev-ai/RuslanUdintsev-AI/actions/workflows/skills-check.yml), but a successful GitHub Actions run alone does not verify a live release.

## Explore one change

To see why **scope boundaries matter**, open `examples/pr-evidence-gate/sample-approved.json` in your **local clone** and add a fictional file such as `deployment/prod.yml` to `changed_files`. Rerun the first command. The decision should become `BLOCKED` because the file is outside `docs/` and `src/seo/`. Do not commit or push your local experiment unless you want to.

## What this proves — and what it cannot

**Inspectable public proof:** the synthetic fixtures, source code, test cases, runnable commands, and recorded CI outcomes. The developer/owner made an explicit human release gate part of the task and reviews the resulting evidence.

**Not established:** correctness of any real PR or external GitHub check, the completeness of a real CI inventory, security of a production deploy, prevention of all agent loops, independent manual authorship of the Python code, or commercial ROI.

## What I do in a larger real workflow

I write scope and acceptance criteria, split the builder and reviewer roles, ask for evidence from an exact GitHub SHA, challenge inconsistent results, commission revisions and retain the **human merge/deployment decision**.

See the [independent builder/reviewer QA practice](INDEPENDENT_AGENT_REVIEW.md) and [full case library](../CASE_STUDIES.md). Evidence from private systems stays private, and any public description is sanitized.

**A practical demonstration is more useful than a claim of expertise.** This exercise can be inspected without contacting me, signing in to an external service or spending money.
