# Contains Duplicate

Insert values into a set while scanning. If a value is already present,
return True immediately. An empty list or a list of distinct values never
hits that branch and returns False.

Time: O(n) expected for n insertions and lookups.
Extra space: O(n) for the set in the all-unique case.

Sorting and then comparing neighbors uses less extra memory but costs
O(n log n) and was not needed here.
