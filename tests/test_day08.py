from adventofcode2022.day08 import (
    parse_input,
    count_visible_trees,
    scenic_score,
    viewing_distance,
)

INPUT_PART1 = """
30373
25512
65332
33549
35390
"""


def test_parse_output():
    expected_grid = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
    example_grid = parse_input(INPUT_PART1)
    assert (
        example_grid == expected_grid
    ), f"Expected {expected_grid}, got {example_grid}"


def test_count_visible_trees():
    example_grid = parse_input(INPUT_PART1)
    n_visible_trees = count_visible_trees(example_grid)
    assert n_visible_trees == 21, f"Expected 21, got {n_visible_trees}"


def test_scenic_score():
    example_grid = parse_input(INPUT_PART1)
    distances = viewing_distance(example_grid, (2, 1))
    assert scenic_score(distances) == scenic_score(
        [1, 1, 2, 2]
    ), f"Expected 4, got {distances}"

    distances = viewing_distance(example_grid, (2, 3))
    assert scenic_score(distances) == scenic_score(
        [2, 2, 1, 2]
    ), f"Expected 8, got {distances}"

    distances = viewing_distance(example_grid, (0, 0))
    assert scenic_score(distances) == scenic_score(
        [0, 0, 2, 2]
    ), f"Expected 4, got {distances}"
