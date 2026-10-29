#!/usr/bin/env python3
"""Offline PR/CI evidence triage demo — advisory only, never deploys anything.

All input is synthetic or manually approved JSON; no GitHub token or network.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


_SHA = re.compile(r"[0-9a-fA-F]{40}\Z")
_VALID_STATUSES = {"completed", "queued", "in_progress"}
_VALID_CONCLUSIONS = {"success", "failure", "cancelled", "timed_out", "skipped"}


class InvalidSnapshot(ValueError):
    """A snapshot cannot be evaluated safely."""


def _required_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InvalidSnapshot(f"{label} must be a non-empty string")
    return value.strip()


def _safe_repo_path(value: Any, label: str, *, prefix: bool = False) -> str:
    path = _required_text(value, label)
    if (
        path.startswith("/")
        or "\\" in path
        or any(piece in {"", ".", ".."} for piece in path.rstrip("/").split("/"))
        or (prefix and not path.endswith("/"))
        or (not prefix and path.endswith("/"))
    ):
        raise InvalidSnapshot(f"{label} must be a relative repository path")
    return path


def analyze(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic observations, never a deployment authorization."""
    if not isinstance(snapshot, dict):
        raise InvalidSnapshot("snapshot must be a JSON object")
    sha = _required_text(snapshot.get("commit"), "commit")
    if _SHA.fullmatch(sha) is None:
        raise InvalidSnapshot("commit must be a full 40-character hexadecimal SHA")
    actor = _required_text(snapshot.get("actor"), "actor")
    pr = snapshot.get("pr_number")
    if type(pr) is not int or pr < 1:
        raise InvalidSnapshot("pr_number must be a positive integer")

    prefixes = snapshot.get("allowed_paths")
    changed = snapshot.get("changed_files")
    if not isinstance(prefixes, list) or not prefixes:
        raise InvalidSnapshot("allowed_paths must be a non-empty list")
    if not isinstance(changed, list) or not changed:
        raise InvalidSnapshot("changed_files must be a non-empty list")
    prefixes = [_safe_repo_path(p, "allowed_paths[]", prefix=True) for p in prefixes]
    changed = [_safe_repo_path(p, "changed_files[]") for p in changed]
    outside_scope = sorted({p for p in changed if not any(p.startswith(root) for root in prefixes)})

    checks = snapshot.get("checks")
    if not isinstance(checks, list) or not checks:
        raise InvalidSnapshot("checks must be a non-empty list of expected CI jobs")
    check_states: list[tuple[str, str, str | None]] = []
    names: set[str] = set()
    for i, entry in enumerate(checks):
        if not isinstance(entry, dict):
            raise InvalidSnapshot(f"checks[{i}] must be an object")
        name = _required_text(entry.get("name"), f"checks[{i}].name")
        status = _required_text(entry.get("status"), f"checks[{i}].status")
        conclusion = entry.get("conclusion")
        if name in names:
            raise InvalidSnapshot(f"duplicate CI check: {name}")
        names.add(name)
        if status not in _VALID_STATUSES:
            raise InvalidSnapshot(f"unsupported CI status for {name}")
        if conclusion is not None and conclusion not in _VALID_CONCLUSIONS:
            raise InvalidSnapshot(f"unsupported CI conclusion for {name}")
        if status != "completed" and conclusion is not None:
            raise InvalidSnapshot(f"unfinished check cannot have a conclusion: {name}")
        if status == "completed" and conclusion is None:
            raise InvalidSnapshot(f"completed check has no conclusion: {name}")
        check_states.append((name, status, conclusion))

    events = snapshot.get("events", [])
    if not isinstance(events, list):
        raise InvalidSnapshot("events must be a list")
    own_echoes = 0
    external_events = 0
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            raise InvalidSnapshot(f"events[{i}] must be an object")
        author = _required_text(event.get("author"), f"events[{i}].author")
        kind = _required_text(event.get("kind"), f"events[{i}].kind")
        if kind != "comment":
            raise InvalidSnapshot("this demo only evaluates comment notifications")
        if author.casefold() == actor.casefold():
            own_echoes += 1
        else:
            external_events += 1

    blocking = []
    if outside_scope:
        blocking.append("Files outside the allowed PR scope")
    bad_checks = sorted(
        name for name, status, conclusion in check_states
        if status != "completed" or conclusion != "success"
    )
    if bad_checks:
        blocking.append("Required CI checks not successful")
    decision = "BLOCKED" if blocking else "HUMAN_REVIEW_REQUIRED"

    return {
        "pr_number": pr,
        "commit": sha.lower(),
        "decision": decision,
        "outside_scope": outside_scope,
        "ci_not_successful": bad_checks,
        "ci_checked": len(check_states),
        "ignored_own_comment_echoes": own_echoes,
        "external_comments_to_review": external_events,
        "blocking_reasons": blocking,
        "notice": "Advisory offline assessment; never authorizes merge or deployment.",
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Make a concise report without copying comment text or secrets."""
    lines = [
        "# AI-assisted PR readiness — offline demonstration",
        "",
        f"- Pull request: #{result['pr_number']}",
        f"- Exact commit: `{result['commit']}`",
        f"- Result: **{result['decision']}**",
        f"- CI jobs considered: {result['ci_checked']}",
        f"- Self-authored comment notifications skipped: {result['ignored_own_comment_echoes']}",
        f"- Other comment notifications for human review: {result['external_comments_to_review']}",
        "",
    ]
    if result["outside_scope"]:
        lines.append("## Files outside the agreed scope")
        lines.extend(f"- `{p}`" for p in result["outside_scope"])
        lines.append("")
    if result["ci_not_successful"]:
        lines.append("## CI jobs requiring attention")
        lines.extend(f"- `{name}`" for name in result["ci_not_successful"])
        lines.append("")
    lines.extend([
        "## Release boundary",
        "",
        "**This report is NOT approval to merge or deploy.**",
        "A human must review original PR changes, complete CI coverage, security and the deployment plan.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Local approved JSON snapshot")
    parser.add_argument("--output", type=Path, help="Optional Markdown report destination")
    args = parser.parse_args()
    try:
        report = render_markdown(analyze(json.loads(args.input.read_text(encoding="utf-8"))))
    except (InvalidSnapshot, json.JSONDecodeError, OSError) as exc:
        parser.error(str(exc))
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
