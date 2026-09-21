"""Every solved catalog row has an answer module and a writeup."""

from __future__ import annotations

import json
from pathlib import Path

from tests.helpers import load_answer

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "blind75.json"
ANSWERS = ROOT / "answers"
WRITEUPS = ROOT / "docs" / "solutions"


def _problems() -> list[dict]:
    return json.loads(CATALOG.read_text(encoding="utf-8"))["problems"]


def test_solved_rows_have_answer_and_writeup() -> None:
    missing: list[str] = []
    for row in _problems():
        if row["status"] != "solved":
            continue
        name = row["answer_file"]
        assert name, row["slug"]
        stem = Path(name).stem
        answer = ANSWERS / name
        writeup = WRITEUPS / f"{stem}.md"
        if not answer.is_file():
            missing.append(f"answer {answer.relative_to(ROOT)}")
        if not writeup.is_file() or not writeup.read_text(encoding="utf-8").strip():
            missing.append(f"writeup {writeup.relative_to(ROOT)}")
        else:
            load_answer(stem)
    assert missing == []


def test_pending_and_premium_rows_are_not_marked_solved() -> None:
    for row in _problems():
        if row["paid_only"]:
            assert row["status"] == "skipped_premium"
            assert row["answer_file"] is None
        elif row["status"] == "pending":
            assert row["answer_file"]
            assert not (ANSWERS / row["answer_file"]).exists()
