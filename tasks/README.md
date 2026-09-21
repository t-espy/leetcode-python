# tasks/

Code changes go through `ratchetloop run`. The pipeline itself is
described in `docs/RATCHETLOOP.md`.

    ~/opt/ratchetloop/current/deploy/ratchetloop run tasks/<task_key>.yaml --detach \
        --policy /home/tespy/opt/ratchetloop/current/WORKFLOW.md
    ~/opt/ratchetloop/current/deploy/ratchetloop status <task_key>

A person merges `ratchetloop/<task_key>` into `main` after ACCEPT.

Briefs must keep the legal fence in `research/TOS_AND_COPYRIGHT.md`:
identifiers and original work only; no LeetCode fetch or submit.
