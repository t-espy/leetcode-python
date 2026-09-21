def max_subarray(nums: list[int]) -> int:
    best = nums[0]
    running = nums[0]
    for value in nums[1:]:
        running = value if running < 0 else running + value
        if running > best:
            best = running
    return best
