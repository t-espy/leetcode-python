# Plan

Spend cap for this first build: about $40 of measured ratchetloop cost.

## Done when

1. Public repo `t-espy/leetcode-python` holds this tree.
2. `catalog/blind75.json` lists 75 identifiers, 6 premium skipped, 69 free
   pending or solved.
3. `python -m leetcode_python list` prints the set from the catalog.
4. Five Array answers pass `tests/problems/` and have writeups.
5. Full `pytest -q` is green.
6. Nothing in git is a copied LeetCode statement.

## Stages

1. **Seed (this commit).** Research, design, catalog JSON, original
   prompts and tests for the first five, hygiene tests. Catalog tests pass.
2. **bootstrap** (`tasks/bootstrap.yaml`). Catalog loader, CLI, answer
   loader. Check: catalog and hygiene tests.
3. **answers-batch-1** (`tasks/answers-batch-1.yaml`). Five solutions and
   five writeups. Check: full pytest.
4. **Later batches.** One task per five free problems, same shape, until
   the 69 are solved. Out of this spend cap.

## Merge

After ACCEPT, fast-forward `main` to `ratchetloop/<task_key>` and push.
