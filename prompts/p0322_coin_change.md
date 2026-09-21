# Coin Change

Catalog: id 322, slug `coin-change`.
Answer file: `answers/p0322_coin_change.py`
Writeup: `docs/solutions/p0322_coin_change.md`

## Contract

`coin_change(coins: list[int], amount: int) -> int`

`coins` is a list of positive denominations. Each denomination may be
used any number of times. Return the fewest coins that sum to `amount`.
Return `-1` when `amount` cannot be formed. `amount` is a non-negative
integer; `amount == 0` returns 0.

## Original checks

`tests/problems/test_p0322_coin_change.py`

## Writeup

Original approach, time, extra space.
