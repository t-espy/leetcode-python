def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    unreachable = amount + 1
    fewest = [unreachable] * (amount + 1)
    fewest[0] = 0
    for coin in coins:
        for total in range(coin, amount + 1):
            candidate = fewest[total - coin] + 1
            if candidate < fewest[total]:
                fewest[total] = candidate
    return fewest[amount] if fewest[amount] != unreachable else -1
