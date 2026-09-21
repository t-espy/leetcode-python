def max_profit(prices: list[int]) -> int:
    lowest = prices[0]
    best = 0
    for price in prices[1:]:
        gain = price - lowest
        if gain > best:
            best = gain
        if price < lowest:
            lowest = price
    return best
