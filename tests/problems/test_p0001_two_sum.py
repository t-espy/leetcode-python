from tests.helpers import load_answer


def _fn():
    return load_answer("p0001_two_sum").two_sum


def test_pair_in_the_middle() -> None:
    got = sorted(_fn()([1, 4, 9], 13))
    assert got == [1, 2]


def test_same_value_different_indices() -> None:
    got = sorted(_fn()([8, 2, 8], 16))
    assert got == [0, 2]


def test_negative_addend() -> None:
    got = sorted(_fn()([-5, 10, 0], 5))
    assert got == [0, 1]


def test_large_magnitudes() -> None:
    got = sorted(_fn()([1_000_000, 1, 999_999], 1_000_000))
    assert got == [1, 2]


def test_two_equal_halves() -> None:
    got = sorted(_fn()([3, 3], 6))
    assert got == [0, 1]
