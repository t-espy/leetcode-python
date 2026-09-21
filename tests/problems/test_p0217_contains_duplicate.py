from tests.helpers import load_answer


def _fn():
    return load_answer("p0217_contains_duplicate").contains_duplicate


def test_all_unique() -> None:
    assert _fn()([1, 2, 3]) is False


def test_repeat() -> None:
    assert _fn()([1, 2, 1]) is True


def test_empty() -> None:
    assert _fn()([]) is False


def test_singleton() -> None:
    assert _fn()([0]) is False


def test_pair_of_equals() -> None:
    assert _fn()([7, 7]) is True
