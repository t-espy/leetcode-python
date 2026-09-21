# Design

A local factory that catalogs the Blind 75 identifiers, writes original
Python solutions into `answers/`, proves them with original pytest files,
and stores original writeups in `docs/solutions/`.

## Layout

| Path | Role |
| --- | --- |
| `catalog/blind75.json` | Public identifiers and status. Source of truth for the set. |
| `prompts/` | Original restatements and signatures for a batch. Our text. |
| `answers/` | One Python module per solved free problem. |
| `docs/solutions/` | One original writeup per solved problem. |
| `src/leetcode_python/` | Catalog loader, answer loader, CLI. |
| `tests/` | Hygiene plus per-problem tests. |
| `tasks/` | ratchetloop task files. One change per run. |

## Data rules

- Catalog keys are the identifier set in `research/TOS_AND_COPYRIGHT.md`.
- `paid_only: true` implies `status: skipped_premium` and `answer_file: null`.
- A solved free problem has `status: solved` and an `answers/` file named
  by `answer_file`.
- Answer modules expose the names in the matching `prompts/` file.

## Runtime

Python 3.12, pytest, `PYTHONPATH=src`. No third-party package in product
code. The CLI is `python -m leetcode_python`.

Checks never open a network socket. A hygiene test fails the suite if a
catalog entry grows a statement field, or if an answer file contains
LeetCode HTML markers.

## ratchetloop

`ratchetloop run` writes code on `ratchetloop/<task_key>`. A person merges
and pushes. The pipeline does not talk to LeetCode. Briefs name the prompt
files and the tests that must go green.
