#!/usr/bin/env python3
# --- Day 8: Treetop Tree House ---

INPUT_PART1 = """
30373
25512
65332
33549
35390
"""


def parse_input(input: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in input.strip().splitlines()]


expected_grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]
example_grid = parse_input(INPUT_PART1)
assert example_grid == expected_grid, f"Expected {expected_grid}, got {example_grid}"


def count_visible_trees(grid: list[list[int]]) -> int:
    count = len(grid[0]) * 2 + (len(grid) - 2) * 2
    for m in range(1, len(grid) - 1):
        for n in range(1, len(grid[0]) - 1):
            height = grid[m][n]
            if all([grid[i][n] < height for i in range(m - 1, -1, -1)]):
                count += 1
                continue
            if all([grid[i][n] < height for i in range(m + 1, len(grid))]):
                count += 1
                continue
            if all([grid[m][i] < height for i in range(n - 1, -1, -1)]):
                count += 1
                continue
            if all([grid[m][i] < height for i in range(n + 1, len(grid[0]))]):
                count += 1
                continue
    return count


n_visible_trees = count_visible_trees(example_grid)
assert n_visible_trees == 21, f"Expected 21, got {n_visible_trees}"


def viewing_distance(grid: list[list[int]], pos: tuple[int, int]) -> list[int]:
    view = [0, 0, 0, 0]
    n, m = pos
    height = grid[m][n]
    for i in range(m - 1, -1, -1):
        view[0] += 1
        if grid[i][n] >= height:
            break
    for i in range(m + 1, len(grid)):
        view[1] += 1
        if grid[i][n] >= height:
            break
    for i in range(n - 1, -1, -1):
        view[2] += 1
        if grid[m][i] >= height:
            break
    for i in range(n + 1, len(grid[0])):
        view[3] += 1
        if grid[m][i] >= height:
            break
    return view


def scenic_score(view: list[int]) -> int:
    result = 1
    for x in view:
        result = result * x
    return result


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


def main() -> None:
    with open("input/day08.txt") as f:
        grid = parse_input(f.read())

    print(f"Part one solution: {count_visible_trees(grid)}")

    highest_scenic_score = max(
        [
            scenic_score(viewing_distance(grid, (n, m)))
            for m in range(len(grid))
            for n in range(len(grid[0]))
        ]
    )
    print(f"Part two solution: {highest_scenic_score}")


if __name__ == "__main__":
    main()
