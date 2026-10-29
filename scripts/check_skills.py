#!/usr/bin/env python3
"""Validate the public skills registry against the portfolio's disclosure rules.

Run: python scripts/check_skills.py
Standard library only. This validates structured claims and public link hygiene;
it does NOT independently verify private project evidence or competence.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "skills" / "registry.json"
LEVELS = {"practical", "agent_assisted", "learning"}
SLUG = re.compile(r"^[a-z][a-z0-9-]*$")
PRIVATE_LINK = re.compile(r"https?://github[.]com/ruslanudintsev-ai/([^/#)]+)")
PUBLIC_REPOS = {"ios-cellular-nginx-http2-fix", "dqn-beginner-rainbow-trading", "RuslanUdintsev-AI", "opalubka"}

def main():
    registry = json.loads(PATH.read_text(encoding="utf-8"))
    assert registry.get("schema_version") == 1, "unsupported schema"
    groups = {g["id"] for g in registry["categories"]}
    assert len(groups) == len(registry["categories"]), "duplicate categories"
    ids = set()
    for skill in registry["skills"]:
        sid = skill["id"]
        assert SLUG.fullmatch(sid) and sid not in ids, f"invalid/duplicate skill id: {sid}"
        ids.add(sid)
        assert skill["category"] in groups, f"unknown category for {sid}"
        assert skill["level"] in LEVELS, f"unknown level for {sid}"
        for field in ("title_ru", "title_en", "example_ru", "example_en"):
            assert isinstance(skill[field], str) and skill[field].strip(), f"missing {field}: {sid}"
        evidence = skill["evidence"]
        assert isinstance(evidence, list), f"bad evidence: {sid}"
        if skill["level"] != "learning":
            assert evidence, f"no evidence: {sid}"
        for item in evidence:
            assert isinstance(item, str), f"bad evidence item: {sid}"
            if item.startswith("https://"):
                match = PRIVATE_LINK.search(item)
                assert not match or match.group(1) in PUBLIC_REPOS, f"potential private repo exposure: {sid}"
            else:
                assert (ROOT / item).is_file(), f"missing local evidence: {item}"
    assert (ROOT / "SKILLS.md").is_file()
    assert (ROOT / "SKILLS.ru.md").is_file()
    print(f"OK: {len(ids)} skills; {len(groups)} categories; structural and link-hygiene validation passed")
    print("Reminder: this is not an independent skills verification.")

if __name__ == "__main__":
    main()
