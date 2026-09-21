from tests.helpers import load_answer


def _fn():
    return load_answer("p0347_top_k_frequent_elements").top_k_frequent


def test_unique_frequencies() -> None:
    got = set(_fn()([4, 4, 5, 5, 5, 6], 2))
    assert got == {5, 4}


def test_k_equals_distinct() -> None:
    got = set(_fn()([9, 8, 9], 2))
    assert got == {9, 8}


def test_single_value() -> None:
    assert _fn()([3, 3, 3], 1) == [3]


def test_negatives() -> None:
    got = set(_fn()([-1, -1, 2, 2, 2, 0], 2))
    assert got == {2, -1}
