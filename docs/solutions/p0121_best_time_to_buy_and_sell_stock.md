# Best Time to Buy and Sell Stock

Scan prices from left to right. Keep the lowest price seen so far (the best
buy day that still precedes the current day) and the largest difference
between the current price and that low. A strictly falling or flat series
leaves the difference at zero.

Time: O(n) for a single pass.
Extra space: O(1) for the running low and best profit.

Recording every valley and peak separately is unnecessary; the running
minimum already encodes the best buy for any later sell.
