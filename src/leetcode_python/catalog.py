"""Load catalog/blind75.json identifiers from the repo root."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "catalog" / "blind75.json"


def load_catalog(path: Path | None = None) -> dict[str, Any]:
    target = path or CATALOG_PATH
    return json.loads(target.read_text(encoding="utf-8"))


def problems(doc: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    data = doc if doc is not None else load_catalog()
    return list(data["problems"])


def status_counts(rows: list[dict[str, Any]] | None = None) -> dict[str, int]:
    items = rows if rows is not None else problems()
    counts = {"pending": 0, "solved": 0, "skipped_premium": 0}
    for row in items:
        status = row["status"]
        if status in counts:
            counts[status] += 1
    return counts
