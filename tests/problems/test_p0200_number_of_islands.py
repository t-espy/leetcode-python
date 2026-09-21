from tests.helpers import load_answer


def _fn():
    return load_answer("p0200_number_of_islands").num_islands


def _run(grid: list[list[int]]) -> int:
    return _fn()([row[:] for row in grid])


def test_empty() -> None:
    assert _run([]) == 0
    assert _run([[]]) == 0


def test_all_water() -> None:
    assert _run([[0, 0], [0, 0]]) == 0


def test_single_land() -> None:
    assert _run([[1]]) == 1


def test_two_separate() -> None:
    assert _run([[1, 0, 1]]) == 2


def test_connected_plus_one() -> None:
    grid = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ]
    assert _run(grid) == 2


def test_no_diagonal_join() -> None:
    grid = [
        [1, 0],
        [0, 1],
    ]
    assert _run(grid) == 2
