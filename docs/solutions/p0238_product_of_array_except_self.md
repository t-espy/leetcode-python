# Product of Array Except Self

Fill the output with prefix products so `out[i]` is the product of
`nums[0..i-1]`. Then walk right to left, multiplying each `out[i]` by a
running suffix product of `nums[i+1..]`. Zeros fall out naturally: a single
zero zeros every other slot, and two zeros zero the whole result. Division
is unused.

Time: O(n) for the two linear passes.
Extra space: O(1) besides the output list, which holds the prefixes in place.
