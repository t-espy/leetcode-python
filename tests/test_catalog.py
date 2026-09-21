from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "blind75.json"

ALLOWED = {
    "id",
    "title",
    "slug",
    "difficulty",
    "category",
    "url",
    "paid_only",
    "status",
    "answer_file",
    "skip_reason",
}

STATEMENT_KEYS = {
    "description",
    "content",
    "body",
    "statement",
    "examples",
    "editorial",
    "constraints",
    "code_snippet",
}


def _doc() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def test_blind75_has_seventy_five_problems() -> None:
    problems = _doc()["problems"]
    assert len(problems) == 75


def test_slugs_and_ids_are_unique() -> None:
    problems = _doc()["problems"]
    slugs = [p["slug"] for p in problems]
    ids = [p["id"] for p in problems]
    assert len(set(slugs)) == 75
    assert len(set(ids)) == 75


def test_six_premium_rows_are_skipped() -> None:
    paid = [p for p in _doc()["problems"] if p["paid_only"]]
    assert len(paid) == 6
    for p in paid:
        assert p["status"] == "skipped_premium"
        assert p["answer_file"] is None
        assert p["skip_reason"] == "leetcode_premium"


def test_free_rows_name_an_answer_file() -> None:
    for p in _doc()["problems"]:
        if p["paid_only"]:
            continue
        assert p["answer_file"]
        assert p["answer_file"].startswith("p")
        assert p["answer_file"].endswith(".py")


def test_urls_are_official_problem_links() -> None:
    for p in _doc()["problems"]:
        assert p["url"] == f"https://leetcode.com/problems/{p['slug']}/"


def test_catalog_holds_identifiers_only() -> None:
    for p in _doc()["problems"]:
        extra = set(p) - ALLOWED
        assert not extra, extra
        assert STATEMENT_KEYS.isdisjoint(p)
