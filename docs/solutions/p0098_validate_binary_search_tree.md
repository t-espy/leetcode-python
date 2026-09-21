# Validate Binary Search Tree

Recurse with a strict open interval that a node must sit inside. The left
child inherits `(lo, node.val)` and the right child inherits `(node.val, hi)`.
That interval carries ancestor bounds, so a deep descendant cannot sneak
past a grandparent. Equal values fail the strict inequalities. A missing
root is valid.

Time: O(n) for one visit per node.
Extra space: O(h) recursion depth for a tree of height h.
