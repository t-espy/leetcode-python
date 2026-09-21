# Top K Frequent Elements

Catalog: id 347, slug `top-k-frequent-elements`.
Answer file: `answers/p0347_top_k_frequent_elements.py`
Writeup: `docs/solutions/p0347_top_k_frequent_elements.md`

## Contract

`top_k_frequent(nums: list[int], k: int) -> list[int]`

Return `k` distinct values from `nums` whose frequencies are the highest.
`nums` is non-empty. `1 <= k <=` the number of distinct values. Order of
the returned list does not matter. When several values share the cutoff
frequency, any of those tied values may be chosen so that the returned
set is a valid top-k.

## Original checks

`tests/problems/test_p0347_top_k_frequent_elements.py`

## Writeup

Original approach, time, extra space.
