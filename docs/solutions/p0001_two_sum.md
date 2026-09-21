# Two Sum

Walk the list once while recording each value's latest index in a dictionary.
For the current index `i`, look up `target - nums[i]`. If that complement is
already stored, the stored index and `i` are the pair. Because each value is
written after the lookup, an index is never paired with itself.

Time: O(n) for one pass and constant-time map operations.
Extra space: O(n) for the value-to-index map.

A nested loop over every pair also works but is quadratic and was discarded
once the map lookup was available.
