# Maximum Subarray

Track the best sum that ends at the current index. If the sum so far is
negative, start a new slice at the current value; otherwise extend. The
global maximum of those ending sums is the answer. A fully negative input
selects the largest single element because a new slice starts at every
step.

Time: O(n) for one pass.
Extra space: O(1) for the running and best sums.

Enumerating every slice is cubic (or quadratic with prefix sums) and was
dropped in favor of this linear scan.
