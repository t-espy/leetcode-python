from tests.helpers import load_answer


def _fn():
    return load_answer("p0322_coin_change").coin_change


def test_zero_amount() -> None:
    assert _fn()([2, 5], 0) == 0


def test_exact_one_coin() -> None:
    assert _fn()([3, 7], 7) == 1


def test_needs_several() -> None:
    assert _fn()([1, 4, 6], 8) == 2


def test_impossible() -> None:
    assert _fn()([4, 6], 5) == -1


def test_empty_denoms() -> None:
    assert _fn()([], 3) == -1
    assert _fn()([], 0) == 0


def test_greedy_is_wrong() -> None:
    assert _fn()([1, 3, 4], 6) == 2
