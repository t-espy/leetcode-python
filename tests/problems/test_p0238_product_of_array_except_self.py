from tests.helpers import load_answer


def _fn():
    return load_answer("p0238_product_of_array_except_self").product_except_self


def test_three_positives() -> None:
    assert _fn()([2, 3, 5]) == [15, 10, 6]


def test_ones() -> None:
    assert _fn()([1, 1, 1]) == [1, 1, 1]


def test_one_zero() -> None:
    assert _fn()([0, 4, 5]) == [20, 0, 0]


def test_two_zeros() -> None:
    assert _fn()([0, 0, 3]) == [0, 0, 0]


def test_negatives() -> None:
    assert _fn()([-1, 2, -3]) == [-6, 3, -2]
