"""Compare solved answers to independent brute-force oracles.

Inputs are either fixed edge cases or values from random.Random with a
pinned seed, so the suite is deterministic.
"""

from __future__ import annotations

import random

from tests import oracles
from tests.helpers import load_answer

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
