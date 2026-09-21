---
idea_key: remaining-free
repo: /home/tespy/projects/leetcode-python
base_branch: main
setup:
  - "ln -s /home/tespy/projects/leetcode-python/venv venv"
checks:
  - "venv/bin/python -m pytest -q"
max_phases: 6
cost_budget_usd: 40
wall_budget_s: 21600
---
Continue solving the remaining free Blind 75 rows the same way as
answers-batch-1: original prompts, original tests, original answers,
original writeups, catalog status updates. Skip the six premium rows.
Do not fetch or submit to LeetCode. This idea is parked until batch 1
is on main; later work is one `ratchetloop run` task per five problems
rather than a single idea, because a 69-problem idea exceeds max_phases.
