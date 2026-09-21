from tests.helpers import load_answer


def _fn():
    return load_answer("p0003_longest_substring_without_repeating_characters").length_of_longest_substring


def test_empty() -> None:
    assert _fn()("") == 0


def test_all_unique() -> None:
    assert _fn()("wxyz") == 4


def test_all_same() -> None:
    assert _fn()("aaaa") == 1


def test_repeat_after_window() -> None:
    assert _fn()("abba") == 2


def test_later_slice_wins() -> None:
    assert _fn()("dvdf") == 3


def test_spaces_and_digits() -> None:
    assert _fn()("a 1a") == 3
