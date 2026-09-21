import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    heap: list[tuple[int, int]] = []
    for value, freq in counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, value))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, value))
    return [value for _, value in heap]
