"""Brute-force reference implementations used only by tests."""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    for i, left in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if left + nums[j] == target:
                return [i, j]
    raise ValueError("no pair sums to target")


def pair_count(nums: list[int], target: int) -> int:
    count = 0
    for i, left in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if left + nums[j] == target:
                count += 1
    return count


def max_profit(prices: list[int]) -> int:
    best = 0
    for i, buy in enumerate(prices):
        for sell in prices[i + 1 :]:
            gain = sell - buy
            if gain > best:
                best = gain
    return best


def contains_duplicate(nums: list[int]) -> bool:
    for i, value in enumerate(nums):
        for other in nums[i + 1 :]:
            if value == other:
                return True
    return False


def product_except_self(nums: list[int]) -> list[int]:
    out: list[int] = []
    for i in range(len(nums)):
        product = 1
        for j, value in enumerate(nums):
            if i != j:
                product *= value
        out.append(product)
    return out


def max_subarray(nums: list[int]) -> int:
    best = nums[0]
    for i in range(len(nums)):
        total = 0
        for value in nums[i:]:
            total += value
            if total > best:
                best = total
    return best
