#!/usr/bin/env python3
# --- Day 4: Camp Cleanup ---


def input_lines(input: str) -> list[str]:
    return [line for line in input.split("\n")]


def lines_to_assignment_pairs(lines: list[str]) -> list[tuple[list, list]]:
    pairs = []
    for line in lines:
        assignments = line.split(",")
        assert len(assignments) == 2
        pair0 = list(map(int, assignments[0].split("-")))
        assert len(pair0) == 2
        pair1 = list(map(int, assignments[1].split("-")))
        assert len(pair1) == 2
        pairs.append((pair0, pair1))
    return pairs


def is_contained(x: list[int], y: list[int]) -> bool:
    return x[0] >= y[0] and x[1] <= y[1]


def is_contained_or_contains(x: list[int], y: list[int]) -> bool:
    return is_contained(x, y) or is_contained(y, x)


def overlaps(x: list[int], y: list[int]) -> bool:
    if x[0] <= y[0]:
        return y[0] >= x[0] and y[0] <= x[1]
    else:
        return x[0] >= y[0] and x[0] <= y[1]


def main() -> None:
    with open("input/day04.txt") as f:
        lines = [line.rstrip() for line in f]

    pairs = lines_to_assignment_pairs(lines)

    pairs_to_reconsider = sum(
        [is_contained_or_contains(pair[0], pair[1]) for pair in pairs]
    )
    print(f"Part one solution: {pairs_to_reconsider}")
    pairs_overlapping = sum([overlaps(pair[0], pair[1]) for pair in pairs])
    print(f"Part two solution: {pairs_overlapping}")


if __name__ == "__main__":
    main()
