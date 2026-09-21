# Validate Binary Search Tree

Catalog: id 98, slug `validate-binary-search-tree`.
Answer file: `answers/p0098_validate_binary_search_tree.py`
Writeup: `docs/solutions/p0098_validate_binary_search_tree.md`

## Contract

Define `TreeNode` with `__init__(self, val=0, left=None, right=None)`.

`is_valid_bst(root: TreeNode | None) -> bool`

A tree is a valid BST when every node in the left subtree is strictly
less than the node, every node in the right subtree is strictly greater,
and both subtrees are valid BSTs. `None` is valid. Duplicate values are
invalid. Checking only a node against its two children is not enough:
a deep descendant can still violate the ancestor bound.

## Original checks

`tests/problems/test_p0098_validate_binary_search_tree.py`

## Writeup

Original approach, time, extra space.
