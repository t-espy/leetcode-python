# Number of Islands

Catalog: id 200, slug `number-of-islands`.
Answer file: `answers/p0200_number_of_islands.py`
Writeup: `docs/solutions/p0200_number_of_islands.md`

## Contract

`num_islands(grid: list[list[int]]) -> int`

`grid` is a rectangular map. `1` is land, `0` is water. An island is a
maximal 4-connected group of land cells (up, down, left, right; no
diagonals). Return how many islands there are. An empty grid, or a grid
with no rows, is 0. The function may overwrite `grid`.

## Original checks

`tests/problems/test_p0200_number_of_islands.py`

## Writeup

Original approach, time, extra space.
