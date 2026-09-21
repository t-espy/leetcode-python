from tests.helpers import load_answer


def _fn():
    return load_answer("p0053_maximum_subarray").max_subarray


def test_all_positive() -> None:
    assert _fn()([1, 2, 3]) == 6


def test_all_negative() -> None:
    assert _fn()([-2, -1, -3]) == -1


def test_wraps_a_dip() -> None:
    assert _fn()([5, -1, 5]) == 9


def test_zeros() -> None:
    assert _fn()([0, -1, 0]) == 0


def test_singleton() -> None:
    assert _fn()([4]) == 4


def test_mixed_run() -> None:
    assert _fn()([-5, 4, -1, 2, 1, -5]) == 6
