# ratchetloop

This project’s code is written by **ratchetloop**, a local command-line
pipeline (pin `~/opt/ratchetloop/current`, source `~/projects/ratchetloop`).
A task file or an idea paragraph goes in; a coding agent changes an isolated
git worktree; deterministic checks run; a second agent from a different
model family reviews the diff. The output is a git branch, a disposition,
and a run directory. A person merges, pushes, and deploys.

Authority for the shapes below is the pinned runtime’s
`docs/CONTRACT.md` at `~/opt/ratchetloop/current`. Callers use
`docs/CALLERS.md`. This page is the description that lives with
leetcode-python.

## Product

A person or program has a bounded change for a git repository — code, or the
plan or design the next code change will follow — and wants it made by an
agent, checked by commands that exit 0 or not, and judged by an independent
reviewer, without trusting what the agents say about themselves.

There is no database, daemon, queue, web UI, or lab-manager dependency. A
caller writes a file, runs a command, and reads `result.json`.

Workers are headless CLIs with structured output: grok, codex, claude, and
copilot. Each can code and each can review. Verdicts come from the worker’s
final JSON object only. Logs, summaries, and narration never turn a failure
into a pass.

## The run loop

```text
caller
  │  tasks/<task_key>.yaml
  ▼
admit → worktree → coder → scope → checks → commit → review
                     ▲                              │
                     └──── findings (≤ 1 revise) ───┘
                                      │
                               disposition
                                      │
              run dir (events, briefs, result.json)
              git branch ratchetloop/<task_key>
```

1. **Admit.** Validate the task file, the policy, the provider CLIs, and
   the repository. Refuse unknown keys, empty checks on a `code` task, a
   check that only greps source, a missing `base_branch`, or a live run of
   the same `task_key`. `--check` stops here and exits 0 when the task
   would be admitted.
2. **Worktree.** Create a git worktree on `ratchetloop/<task_key>` from
   `base_branch`. The primary checkout is left alone. Run `setup` commands
   there (this repo links `venv`). Paths setup leaves are never staged.
3. **Coder.** A worker CLI edits the worktree. Git transport is disabled
   for the worker. The worker cannot commit or push.
4. **Scope.** The change must stay inside `allowed_paths` when that list
   is set, and must leave git config and hooks untouched.
5. **Checks.** The task’s shell commands run with an explicit environment
   (`HOME`, `USER`, locale, `PATH` without ratchetloop’s own venv, plus
   the task’s `env`). All must exit 0. Red checks get one fix launch; still
   red ends FAILED `checks_failed` with nothing committed from that round.
6. **Commit.** The pipeline stages only the worker’s paths and commits on
   the task branch.
7. **Review.** A read-only worker from a different **model family** (xAI,
   Anthropic, OpenAI, Google, Microsoft, Moonshot — compared on the model
   the stream reports it actually used) returns `APPROVE` or
   `REQUEST_CHANGES`. A reviewer that writes anything invalidates its
   review. Two rounds at most; round 2 is a fix-check of round-1 findings.
8. **Result.** `result.json` is written on every exit path. Exit code names
   the disposition.

`kind: doc` uses the same loop for a plan or design that will be the next
build contract. Built-in doc checks: every changed file is inside
`allowed_paths`, at least one file changed, relative markdown links
resolve. Content is the reviewer’s job. A doc ACCEPT means reviewed.

## Commands

Callers launch the **pinned** binary, never a checkout venv:

```text
~/opt/ratchetloop/current/deploy/ratchetloop <subcommand> …
```

The launcher runs `<opt>/current/.venv/bin/ratchetloop` with
`PYTHONSAFEPATH=1`. `RATCHETLOOP_OPT` moves the opt root (default
`~/opt/ratchetloop`). A person pins, promotes, and rolls back with
`deploy/pin.sh`, `deploy/promote.sh --approved-by NAME`, and
`deploy/rollback.sh`.

| Command | Role |
| --- | --- |
| `run TASK.yaml` | One task to a disposition |
| `run TASK.yaml --check` | Admit only |
| `run TASK.yaml --detach` | Admit in the foreground, then continue in a new session; prints pid, run dir, log |
| `run TASK.yaml --continue` | Resume a non-ACCEPT or dead run of the same `task_key` |
| `build IDEA.md` | Design, plan, then one code stage per planned phase |
| `build IDEA.md --gate plan` | Pause after the plan for `approve` |
| `build IDEA.md --continue` | Resume the idea at the first unaccepted stage |
| `approve IDEA_KEY` | Release a plan gate |
| `review TASK.yaml --branch B` | One review round on an existing branch against a base |
| `status TASK_KEY` | Latest `result.json`, or a live run’s last event |
| `stats [--since DATE] [--repo PATH] [--json]` | Usage and velocity summed from result files |
| `trees` | List preserved worktrees; `--discard PATH --yes` force-removes one |

`--policy FILE` names the model-ladder file (this repo uses
`/home/tespy/opt/ratchetloop/current/WORKFLOW.md`). `--coder` and
`--reviewer` override providers (`grok`, `codex`, `claude`, `copilot`).

`--detach` survives a closed terminal. A systemd unit that must keep the
child alive uses `systemd-run --user --scope` or `KillMode=process`.

## Task file

YAML, one task per file, under `tasks/` in this repo. Unknown keys are
refused. `CONTRACT.md` §2 is the field list.

| Key | Required | Meaning |
| --- | --- | --- |
| `task_key` | yes | `[a-z0-9][a-z0-9-]{0,62}`; names branch `ratchetloop/<task_key>` and the run folder |
| `kind` | no | `code` (default) or `doc` |
| `repo` | yes | Path to the target git repository |
| `objective` or `brief_file` | one of | The change, in prose, or a markdown brief |
| `acceptance_criteria` | yes | Non-empty list of checkable strings |
| `checks` | `code`: yes | Non-empty list of shell commands; all must exit 0 |
| `base_branch` | no | Default `master`; this repo sets `main` |
| `setup` | no | Commands in the worktree before the coder (link `venv`) |
| `allowed_paths` | `doc`: yes | Path prefixes the change may touch |
| `coder` / `reviewer` | no | Provider override; reviewer family must differ from every coder of the task |
| `tier` | no | `light`, `standard`, `heavy` — starting rung on the model ladder |
| `max_review_rounds` | no | 1 or 2; default 2 |
| `env` | no | Extra variables for `setup` and `checks` only |
| `wall_budget_s` | no | Default 7200 |
| `cost_budget_usd` | no | Default 25; measured spend only |

This repository’s tasks also set `PYTHONPATH: src` in `env` so a linked
editable venv still imports the **worktree** package.

After ACCEPT, a further change is a new `task_key`. `--continue` is for a
run that ended short of ACCEPT or died. It reuses the task branch and
worktree, starts from the base commit the latest run recorded, adopts
uncommitted worker files a dead run left, and feeds the last
REQUEST_CHANGES findings to the coder.

## Idea mode

`ratchetloop build IDEA.md` takes markdown with YAML front matter
(`idea_key`, `repo`, optional `checks`, `setup`, `max_phases` default 6,
budgets) and a paragraph of intent.

1. **Plan** — a `doc` task `<idea_key>--plan` writes `docs/DESIGN.md` and
   `docs/PLAN.md`. The plan contains exactly one fenced `yaml` block of
   phases (`key`, `objective`, `acceptance_criteria`, `checks`). The
   pipeline’s own `check-plan` must validate that block as runnable tasks.
2. **Gate** — only with `--gate plan`: the idea stops PAUSED until
   `approve IDEA_KEY`.
3. **Phases** — one `code` task per phase, in order, each on
   `ratchetloop/<idea_key>--<phase>`. After ACCEPT the idea branch
   `ratchetloop/<idea_key>` fast-forwards to that head. A person merges
   the idea branch.

A failed stage stops the chain. `max_phases` is 6, which is why this
repo solves Blind 75 as a sequence of `run` batches rather than one idea
covering all 69 free rows. `ideas/remaining-free.md` records that choice.

Inside an idea, a code stage that exhausts review rounds with green checks
and no blocking finding can **carry** residual findings into the next
phase (`on_rounds_exhausted: carry`, the default). A stand-alone `run`
still ends HUMAN_REVIEW in that case.

## Isolation and review

- Each run has its own worktree under `~/var/ratchetloop/worktrees/<repo digest>/<task_key>`.
- Workers cannot use git remotes (`protocol.allow=never`).
- The pipeline alone commits, and only the paths it verified.
- Reviewer ≠ coder, compared by model family. Copilot runs several
  families, so a copilot reviewer on a Claude model does not independently
  judge a claude coder. `--model auto` is refused because its family
  cannot be known.
- Two review rounds at most on a stand-alone task.

## Dispositions

| Disposition | Exit | When |
| --- | --- | --- |
| ACCEPT | 0 | Checks green at the reviewed HEAD and the reviewer says APPROVE |
| HUMAN_REVIEW | 3 | Review rounds exhausted, or the coder blocked |
| FAILED | 4 | Checks, scope, reviewer wrote, invalid result, quota, budget, setup, no change, crash, abandoned, … |
| STOPPED | 5 | `STOP` sentinel or SIGTERM/SIGINT to the pipeline |
| (refused) | 2 | Bad task, args, policy, or missing CLI; no run directory |

ACCEPT requires the checks event and the review event to name the same
`head_sha`.

## Run records

`<runs_root>/<task_key>/<run_id>/` (default `~/var/ratchetloop/runs`,
override `RATCHETLOOP_RUNS_ROOT`):

- `task.yaml` as admitted
- `events.jsonl` — one JSON object per step, flushed before the next step
- `brief.coder.N.md` / `brief.reviewer.N.md` — exact text sent
- worker logs, `checks.N.log`, `diff.N.patch`
- `result.json` — disposition, usage (tokens, cost, `usage_source`),
  velocity (lines, tests added, review rounds, findings)

Read the verdict from `result.json` or `ratchetloop status KEY`. Spend
reporting is `ratchetloop stats`. Codex launches that report tokens but
no dollars count in `launches_without_cost`; `cost_budget_usd` counts
measured spend; wall time still bounds the rest.

## Stop

- `<runs_root>/STOP` — every run, at the next step boundary
- `<run dir>/STOP` — that run
- SIGTERM/SIGINT to `ratchetloop run` — STOPPED `killed`, result written
- SIGKILL — the next run of the task marks the dead one abandoned and
  reaps leftover process groups in its worktree

`--continue` after the sentinel is gone adopts what the run left.

## Policy (model ladders)

The first fenced `yaml` block of `WORKFLOW.md`: `ladders` per provider
(cheapest rung first), `tier_start`, `default_tier` per role,
`review_light_max_lines`, `review_heavy_min_lines`. A failed earlier run
of the same task (blocked, invalid, protocol error, or red checks) climbs
one rung; quota failures do not.

Path: `--policy`, else `RATCHETLOOP_POLICY`, else
`~/.config/ratchetloop/WORKFLOW.md`. A missing named file or a malformed
block refuses the run. With no policy file at all, each CLI uses its own
default model.

## How this repository uses it

Pin and policy on this machine:

```bash
~/opt/ratchetloop/current/deploy/ratchetloop run tasks/<task_key>.yaml --detach \
    --policy /home/tespy/opt/ratchetloop/current/WORKFLOW.md
~/opt/ratchetloop/current/deploy/ratchetloop status <task_key>
```

`tasks/README.md` is the short operator card. `tasks/TEMPLATE.yaml` is
the next five-problem batch. `tasks/bootstrap.yaml` and
`tasks/answers-batch-1.yaml` are the first two accepted runs.

Conventions here:

- Coder `grok`, reviewer `claude` (families xAI and Anthropic).
- `base_branch: main`.
- `setup` links this checkout’s `venv` into the worktree.
- `env.PYTHONPATH: src`.
- Checks are pytest (and the CLI for bootstrap). Hygiene tests fail a
  paste of LeetCode HTML markers.
- `allowed_paths` keep a solve batch inside `answers/`, `docs/solutions/`,
  and `catalog/blind75.json`.
- Briefs point at `prompts/` and `research/TOS_AND_COPYRIGHT.md`. The
  pipeline does not fetch or submit to LeetCode.

After ACCEPT, merge `ratchetloop/<task_key>` into `main` and push. The
pipeline does not do that step.

### First runs on this repo (2026-09-21)

| Task | Disposition | Head | Measured cost |
| --- | --- | --- | --- |
| `bootstrap` | ACCEPT | CLI, catalog loader, `tests/test_cli.py` | $0.16 |
| `answers-batch-1` | ACCEPT | five Array answers and writeups | $0.23 |

Those branches were merged to `main` by a person and pushed to
`https://github.com/t-espy/leetcode-python`.
