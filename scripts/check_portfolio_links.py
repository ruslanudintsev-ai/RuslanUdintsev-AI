#!/usr/bin/env python3
"""Check local portfolio Markdown navigation and avoid linking private repos.

Static-only: does not make network calls or assert that external links resolve.
"""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    "README.md", "README.ru.md",
    "HIRE_ME.md", "HIRE_ME.ru.md", "PROFILE_README.md",
    "ECOSYSTEM.md", "ECOSYSTEM.ru.md",
    "CASE_STUDIES.md", "AGENT_OPERATIONS.md",
    "docs/EVIDENCE_INDEX.md", "docs/EVIDENCE_INDEX.ru.md",
    "docs/CASE_MULTI_AGENT_GITHUB.md",
    "docs/INDEPENDENT_AGENT_REVIEW.md", "docs/INDEPENDENT_AGENT_REVIEW.ru.md",
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)")
PUBLIC_OWNER_REPOS = {
    "RuslanUdintsev-AI",
    "ios-cellular-nginx-http2-fix",
    "dqn-beginner-rainbow-trading",
    "opalubka",
}


def main():
    for page_name in PAGES:
        source = ROOT / page_name
        text = source.read_text(encoding="utf-8")
        for destination in MARKDOWN_LINK.findall(text):
            if destination.startswith("#"):
                continue
            parsed = urlsplit(destination)
            if parsed.scheme in {"http", "https"}:
                if parsed.netloc.lower() == "github.com":
                    parts = parsed.path.strip("/").split("/")
                    if len(parts) > 1 and parts[0].lower() == "ruslanudintsev-ai":
                        assert parts[1] in PUBLIC_OWNER_REPOS, (
                            f"{page_name}: linked repository may be private: {parts[1]}"
                        )
                continue
            if parsed.scheme or destination.startswith("//"):
                continue
            local = (source.parent / unquote(parsed.path)).resolve()
            assert local.is_relative_to(ROOT.resolve()), (
                f"{page_name}: link escapes portfolio directory: {destination}"
            )
            assert local.is_file(), (
                f"{page_name}: broken local link: {destination}"
            )
    assert "HIRE_ME.md" in (ROOT / "README.md").read_text(encoding="utf-8")
    assert "HIRE_ME.ru.md" in (ROOT / "README.ru.md").read_text(encoding="utf-8")
    assert "HIRE_ME.ru.md" in (ROOT / "HIRE_ME.md").read_text(encoding="utf-8")
    assert "HIRE_ME.md" in (ROOT / "HIRE_ME.ru.md").read_text(encoding="utf-8")
    # A growing case library must not leave stale numeric promises in the landing pages.
    cases = re.findall(
        r"^## Case (\d{2}) — ",
        (ROOT / "CASE_STUDIES.md").read_text(encoding="utf-8"),
        flags=re.MULTILINE,
    )
    assert cases == [f"{i:02d}" for i in range(1, len(cases) + 1)], (
        f"Case index numbering must be consecutive: {cases}"
    )
    assert len(cases) >= 1
    assert f"{len(cases)} case studies" in (ROOT / "README.md").read_text(encoding="utf-8")
    assert f"{len(cases)} кейсов" in (ROOT / "README.ru.md").read_text(encoding="utf-8")
    assert "docs/EVIDENCE_INDEX.md" in (ROOT / "README.md").read_text(encoding="utf-8")
    assert "docs/EVIDENCE_INDEX.ru.md" in (ROOT / "README.ru.md").read_text(encoding="utf-8")
    print(f"OK: {len(cases)} consecutive cases, matching EN/RU entry points")

    print(f"OK: checked internal links and public-repo references in {len(PAGES)} pages")
    print("External link availability and private evidence were not independently verified.")


if __name__ == "__main__":
    main()
