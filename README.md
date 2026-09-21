# Python Algorithm Interview Work Sample

[![CI](https://github.com/t-espy/leetcode-python/actions/workflows/ci.yml/badge.svg)](https://github.com/t-espy/leetcode-python/actions/workflows/ci.yml)

This repository is a public, reproducible software-engineering work sample built around a representative subset of the Blind 75 interview curriculum. Its purpose is to demonstrate algorithmic reasoning, implementation quality, automated validation, and a modern AI-assisted development process rather than completion of every problem in the set.

Each completed problem includes an original Python implementation, focused unit tests, an algorithm and complexity writeup, and deterministic validation against an independent brute-force or reference implementation where practical.

## Development and validation

The implementations are produced through **ratchetloop**, an AI-assisted software-development pipeline that I also designed and built. Ratchetloop takes a bounded task or design, gives it to a coding agent in an isolated git worktree, runs deterministic checks, and sends the resulting diff to an independent reviewer from a different model family. A human controls merge and publication.

For this repository, the workflow is:

```text
problem spec
    ↓
AI implementation
    ↓
unit tests
    ↓
deterministic reference-oracle tests
    ↓
repository integrity checks
    ↓
independent cross-model review
    ↓
human merge
    ↓
GitHub Actions
```

The full ratchetloop workflow, controls, task format, review loop, and run records are documented in [docs/RATCHETLOOP.md](docs/RATCHETLOOP.md).

Solved implementations are checked against deterministic reference implementations using fixed edge cases and seeded generated inputs. GitHub Actions runs the full pytest suite on Python 3.12 for every push and pull request.

## Representative coverage

Ten intentionally selected problems are implemented. The goal is representative coverage of common interview algorithm patterns, not completion of the full Blind 75 set. Six premium Blind 75 problems remain excluded.

| Pattern | Representative problem |
| --- | --- |
| Hashing | Two Sum; Contains Duplicate |
| Linear state | Best Time to Buy and Sell Stock |
| Prefix / suffix | Product of Array Except Self |
| Dynamic programming | Maximum Subarray; Coin Change |
| Sliding window | Longest Substring Without Repeating Characters |
| Graph traversal | Number of Islands |
| Tree recursion | Validate Binary Search Tree |
| Heap / frequency | Top K Frequent Elements |

## Setup

```bash
/usr/bin/python3 -m venv venv
venv/bin/pip install -e '.[dev]'
PYTHONPATH=src venv/bin/python -m pytest -q
PYTHONPATH=src venv/bin/python -m leetcode_python list
```

## Layout

- `catalog/blind75.json` — public problem identifiers and solution status
- `prompts/` — original problem restatements used as solve specifications
- `answers/` — Python implementations
- `tests/problems/` — focused unit tests
- `tests/test_oracles.py` and `tests/oracles.py` — deterministic reference-oracle validation
- `docs/solutions/` — algorithm and complexity writeups
- `tasks/` — ratchetloop task definitions
- `docs/RATCHETLOOP.md` — ratchetloop architecture and workflow used to produce the code

## Legal fence

LeetCode is a trademark of LeetCode. This project is independent.

The repository does not fetch LeetCode pages, APIs, or GraphQL endpoints and does not submit code to LeetCode's judge. Problem statements, examples, constraints, editorials, and hidden tests are not copied into the repository. Premium items remain excluded. Tests and writeups are original.

See [NOTICE](NOTICE) and [research/TOS_AND_COPYRIGHT.md](research/TOS_AND_COPYRIGHT.md).
