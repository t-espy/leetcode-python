from tests.helpers import build_tree, load_answer


def _mod():
    return load_answer("p0098_validate_binary_search_tree")


def _fn(values: list):
    mod = _mod()
    return mod.is_valid_bst(build_tree(mod.TreeNode, values))


def test_empty() -> None:
    assert _mod().is_valid_bst(None) is True


def test_singleton() -> None:
    assert _fn([4]) is True


def test_simple_valid() -> None:
    assert _fn([4, 2, 6]) is True


def test_immediate_left_too_big() -> None:
    assert _fn([4, 5, 6]) is False


def test_deep_right_violates_root() -> None:
    # 4 sits in the right subtree of 5 but is smaller than 5.
    assert _fn([5, 3, 8, None, None, 4, 9]) is False


def test_duplicates_invalid() -> None:
    assert _fn([2, 2, 3]) is False
    assert _fn([2, 1, 2]) is False
