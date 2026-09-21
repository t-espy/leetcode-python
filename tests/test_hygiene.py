from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Markers of pasted LeetCode HTML or boilerplate. Original writeups do not
# need these strings.
FORBIDDEN = (
    "example 1:",
    "example 2:",
    "follow up:",
    "leetcode-cdn",
    "<div class=\"question",
    "data-cy=\"question-title\"",
)


def test_answers_and_writeups_are_original_prose() -> None:
    roots = [ROOT / "answers", ROOT / "docs" / "solutions"]
    hits: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in {".py", ".md"}:
                continue
            text = path.read_text(encoding="utf-8").lower()
            for needle in FORBIDDEN:
                if needle in text:
                    hits.append(f"{path.relative_to(ROOT)}: {needle}")
    assert hits == []
