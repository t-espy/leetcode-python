from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = ROOT / "venv" / "bin" / "python"
ENV = {**os.environ, "PYTHONPATH": str(ROOT / "src")}


def _run(command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(PYTHON), "-m", "leetcode_python", command],
        cwd=ROOT,
        env=ENV,
        capture_output=True,
        text=True,
        check=False,
    )


def test_list_prints_seventy_five_problem_rows() -> None:
    proc = _run("list")
    assert proc.returncode == 0, proc.stderr
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    assert len(lines) == 75
    first = lines[0].split()
    assert len(first) == 5


def test_status_counts_cover_the_catalog() -> None:
    proc = _run("status")
    assert proc.returncode == 0, proc.stderr
    fields = dict(part.split("=", 1) for part in proc.stdout.split())
    pending = int(fields["pending"])
    solved = int(fields["solved"])
    skipped = int(fields["skipped_premium"])
    assert skipped == 6
    assert pending + solved + skipped == 75
    assert solved >= 5
