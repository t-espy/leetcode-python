# leetcode-python

[![CI](https://github.com/t-espy/leetcode-python/actions/workflows/ci.yml/badge.svg)](https://github.com/t-espy/leetcode-python/actions/workflows/ci.yml)

Original Python solutions and writeups for the Blind 75 interview set.
Each catalog row links to the corresponding page on leetcode.com. The
repo holds our code, our tests, and our notes.

Solved implementations are checked against independent brute-force
reference oracles on a seeded set of small inputs (duplicates, negatives,
zeros, empty and singleton lists where the contract allows them).

LeetCode is a trademark of LeetCode. This project is independent. See
`NOTICE` and `research/TOS_AND_COPYRIGHT.md`.

## Status

| Set | Rows | Premium skipped | Solved |
| --- | --- | --- | --- |
| Blind 75 | 75 | 6 | 5 |

## Setup

```bash
/usr/bin/python3 -m venv venv
venv/bin/pip install -e '.[dev]'
PYTHONPATH=src venv/bin/python -m pytest -q
PYTHONPATH=src venv/bin/python -m leetcode_python list
```

GitHub Actions runs the same pytest suite on every push and pull request
(Python 3.12).

## Layout

- `catalog/blind75.json` — identifiers and status
- `prompts/` — original restatements for a solve batch
- `answers/` — Python modules
- `docs/solutions/` — writeups
- `tasks/` — ratchetloop task files
- `docs/RATCHETLOOP.md` — full description of the pipeline that writes the code

## Legal fence

The tree does not fetch LeetCode pages, APIs, or GraphQL, and it does not
submit code to their judge. Premium items stay skipped. Tests are original.
