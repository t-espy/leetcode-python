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


def num_islands(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    seen = [row[:] for row in grid]
    rows, cols = len(seen), len(seen[0])

    def flood(r: int, c: int) -> None:
        if r < 0 or c < 0 or r >= rows or c >= cols or seen[r][c] != 1:
            return
        seen[r][c] = 0
        flood(r + 1, c)
        flood(r - 1, c)
        flood(r, c + 1)
        flood(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if seen[r][c] == 1:
                count += 1
                flood(r, c)
    return count


def is_valid_bst(root) -> bool:
    values: list[int] = []

    def walk(node) -> None:
        if node is None:
            return
        walk(node.left)
        values.append(node.val)
        walk(node.right)

    walk(root)
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))


def length_of_longest_substring(s: str) -> int:
    best = 0
    for i in range(len(s)):
        seen: set[str] = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            length = j - i + 1
            if length > best:
                best = length
    return best


def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    denoms = tuple(sorted({c for c in coins if c > 0}))
    inf = amount + 1
    memo = {0: 0}

    def fewest(rest: int) -> int:
        if rest in memo:
            return memo[rest]
        best = inf
        for coin in denoms:
            if coin <= rest:
                candidate = fewest(rest - coin)
                if candidate + 1 < best:
                    best = candidate + 1
        memo[rest] = best
        return best

    answer = fewest(amount)
    return -1 if answer >= inf else answer


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    ranked = sorted(counts, key=lambda value: (-counts[value], value))
    return ranked[:k]


def is_valid_top_k(nums: list[int], k: int, got: list[int]) -> bool:
    if len(got) != k or len(set(got)) != k:
        return False
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    if any(value not in counts for value in got):
        return False
    selected = min(counts[value] for value in got)
    rest = [counts[value] for value in counts if value not in set(got)]
    return not rest or selected >= max(rest)
