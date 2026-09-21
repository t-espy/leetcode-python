"""Compare solved answers to independent brute-force oracles.

Inputs are either fixed edge cases or values from random.Random with a
pinned seed, so the suite is deterministic.
"""

from __future__ import annotations

import random

from tests import oracles
from tests.helpers import build_tree, load_answer

SEED = 20260921
RANDOM_CASES = 80


def _rng() -> random.Random:
    return random.Random(SEED)


def test_two_sum_matches_oracle_on_unique_pairs() -> None:
    fn = load_answer("p0001_two_sum").two_sum
    cases = [
        ([1, 4, 9], 13),
        ([8, 2, 8], 16),
        ([-5, 10, 0], 5),
        ([3, 3], 6),
        ([0, 7], 7),
        ([-3, -1, 8], 5),
    ]
    rng = _rng()
    attempts = 0
    while len(cases) < RANDOM_CASES and attempts < 20_000:
        attempts += 1
        n = rng.randint(2, 10)
        nums = [rng.randint(-20, 20) for _ in range(n)]
        i, j = rng.sample(range(n), 2)
        target = nums[i] + nums[j]
        if oracles.pair_count(nums, target) != 1:
            continue
        cases.append((nums, target))
    assert len(cases) >= RANDOM_CASES
    for nums, target in cases:
        assert sorted(fn(list(nums), target)) == sorted(oracles.two_sum(nums, target))


def test_max_profit_matches_oracle() -> None:
    fn = load_answer("p0121_best_time_to_buy_and_sell_stock").max_profit
    cases = [
        [9, 8, 7],
        [1, 2, 3, 4],
        [2, 10, 1, 9],
        [5],
        [3, 3, 3],
        [0, 0],
        [-4, -1, -3],
        [4, -2, 6],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        n = rng.randint(1, 12)
        cases.append([rng.randint(-15, 25) for _ in range(n)])
    for prices in cases:
        assert fn(list(prices)) == oracles.max_profit(prices)


def test_contains_duplicate_matches_oracle() -> None:
    fn = load_answer("p0217_contains_duplicate").contains_duplicate
    cases = [
        [],
        [0],
        [1, 2, 3],
        [1, 2, 1],
        [7, 7],
        [-1, 0, -1],
        [0, 0, 1],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        n = rng.randint(0, 12)
        cases.append([rng.randint(-8, 8) for _ in range(n)])
    for nums in cases:
        assert fn(list(nums)) is oracles.contains_duplicate(nums)


def test_product_except_self_matches_oracle() -> None:
    fn = load_answer("p0238_product_of_array_except_self").product_except_self
    cases = [
        [2, 3, 5],
        [1, 1, 1],
        [0, 4, 5],
        [0, 0, 3],
        [-1, 2, -3],
        [4, 0],
        [-2, -2, -2],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        n = rng.randint(2, 8)
        cases.append([rng.randint(-6, 6) for _ in range(n)])
    for nums in cases:
        assert fn(list(nums)) == oracles.product_except_self(nums)


def test_max_subarray_matches_oracle() -> None:
    fn = load_answer("p0053_maximum_subarray").max_subarray
    cases = [
        [1, 2, 3],
        [-2, -1, -3],
        [5, -1, 5],
        [0, -1, 0],
        [4],
        [-5, 4, -1, 2, 1, -5],
        [0],
        [-7],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        n = rng.randint(1, 12)
        cases.append([rng.randint(-12, 12) for _ in range(n)])
    for nums in cases:
        assert fn(list(nums)) == oracles.max_subarray(nums)


def test_num_islands_matches_oracle() -> None:
    fn = load_answer("p0200_number_of_islands").num_islands
    cases = [
        [],
        [[]],
        [[0]],
        [[1]],
        [[1, 0, 1]],
        [[1, 0], [0, 1]],
        [[1, 1, 0], [1, 0, 0], [0, 0, 1]],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        cases.append([[rng.choice((0, 1)) for _ in range(cols)] for _ in range(rows)])
    for grid in cases:
        copy_a = [row[:] for row in grid]
        copy_b = [row[:] for row in grid]
        assert fn(copy_a) == oracles.num_islands(copy_b)


def test_is_valid_bst_matches_oracle() -> None:
    mod = load_answer("p0098_validate_binary_search_tree")
    cases = [
        None,
        [4],
        [4, 2, 6],
        [4, 5, 6],
        [5, 3, 8, None, None, 4, 9],
        [2, 2, 3],
        [2, 1, 2],
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        size = rng.randint(1, 7)
        values: list[int | None] = []
        for index in range(size):
            if index > 0 and rng.random() < 0.25:
                values.append(None)
            else:
                values.append(rng.randint(-8, 8))
        cases.append(values)
    for spec in cases:
        if spec is None:
            root_a = None
            root_b = None
        else:
            root_a = build_tree(mod.TreeNode, spec)
            root_b = build_tree(mod.TreeNode, spec)
        assert mod.is_valid_bst(root_a) is oracles.is_valid_bst(root_b)


def test_longest_substring_matches_oracle() -> None:
    fn = load_answer(
        "p0003_longest_substring_without_repeating_characters"
    ).length_of_longest_substring
    cases = ["", "wxyz", "aaaa", "abba", "dvdf", "a 1a", " "]
    rng = _rng()
    alphabet = "ab cde12"
    for _ in range(RANDOM_CASES):
        n = rng.randint(0, 16)
        cases.append("".join(rng.choice(alphabet) for _ in range(n)))
    for text in cases:
        assert fn(text) == oracles.length_of_longest_substring(text)


def test_coin_change_matches_oracle() -> None:
    fn = load_answer("p0322_coin_change").coin_change
    cases = [
        ([2, 5], 0),
        ([3, 7], 7),
        ([1, 4, 6], 8),
        ([4, 6], 5),
        ([], 3),
        ([], 0),
        ([1, 3, 4], 6),
    ]
    rng = _rng()
    denoms = [1, 2, 3, 4, 5, 7]
    for _ in range(RANDOM_CASES):
        n = rng.randint(0, 4)
        coins = [denoms[rng.randrange(len(denoms))] for _ in range(n)]
        amount = rng.randint(0, 20)
        cases.append((coins, amount))
    for coins, amount in cases:
        assert fn(list(coins), amount) == oracles.coin_change(coins, amount)


def test_top_k_frequent_matches_oracle() -> None:
    fn = load_answer("p0347_top_k_frequent_elements").top_k_frequent
    unique_freq_cases = [
        ([4, 4, 5, 5, 5, 6], 2),
        ([9, 8, 9], 2),
        ([3, 3, 3], 1),
        ([-1, -1, 2, 2, 2, 0], 2),
    ]
    rng = _rng()
    for _ in range(RANDOM_CASES):
        distinct = rng.randint(1, 6)
        nums: list[int] = []
        for i in range(distinct):
            nums.extend([i - 2] * (i + 1))
        rng.shuffle(nums)
        k = rng.randint(1, distinct)
        unique_freq_cases.append((nums, k))
    for nums, k in unique_freq_cases:
        got = fn(list(nums), k)
        assert set(got) == set(oracles.top_k_frequent(nums, k))
        assert oracles.is_valid_top_k(nums, k, got)
    # Tied cutoff: any valid top-k set is accepted.
    tied = [7, 7, 8, 8, 9]
    got = fn(tied, 2)
    assert oracles.is_valid_top_k(tied, 2, got)
