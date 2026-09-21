# Coin Change

Let `fewest[x]` be the fewest coins that sum to `x`. Start with
`fewest[0] = 0` and every positive total unreachable. For each denomination,
walk totals from that coin up to the amount and try adding one more coin
onto `fewest[total - coin]`. Unlimited uses of a coin fall out of that inner
loop. If the amount stays unreachable, return -1; amount 0 is already 0.

Time: O(len(coins) * amount).
Extra space: O(amount) for the table.
