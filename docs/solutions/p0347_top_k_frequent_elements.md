# Top K Frequent Elements

Count each distinct value, then keep a min-heap of size `k` keyed by
frequency. A new value enters while the heap is short, or replaces the
current minimum when its frequency is strictly larger. The heap then holds
`k` values whose counts are at least as high as every leftover value. Ties
at the cutoff keep whichever of the tied values already sat in the heap.

Time: O(n + d log k) to count n items and heap-update d distinct values.
Extra space: O(d) for the counts and O(k) for the heap.
