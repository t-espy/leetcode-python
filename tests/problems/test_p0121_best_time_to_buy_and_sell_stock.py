from tests.helpers import load_answer


def _fn():
    return load_answer("p0121_best_time_to_buy_and_sell_stock").max_profit


def test_strictly_falling() -> None:
    assert _fn()([9, 8, 7]) == 0


def test_strictly_rising() -> None:
    assert _fn()([1, 2, 3, 4]) == 3


def test_dip_then_peak() -> None:
    assert _fn()([2, 10, 1, 9]) == 8


def test_single_day() -> None:
    assert _fn()([5]) == 0


def test_flat() -> None:
    assert _fn()([3, 3, 3]) == 0
