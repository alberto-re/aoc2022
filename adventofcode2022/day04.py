#!/usr/bin/env python3
# --- Day 4: Camp Cleanup ---

from typing import List, Tuple


INPUT_PART1 = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8\
"""

def input_lines(input: str) -> List[str]:
    return [line for line in input.split("\n")]


def lines_to_assignment_pairs(lines: List[str]) -> List[Tuple[list, list]]:
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

expected = [([2, 4], [6, 8]), ([2, 3], [4, 5]), ([5, 7], [7, 9]), ([2, 8], [3, 7]), ([6, 6], [4, 6]), ([2, 6], [4, 8])]
pairs = lines_to_assignment_pairs(input_lines(INPUT_PART1))
assert pairs == expected


def is_contained(x: List[int], y: List[int]) -> bool:
    return x[0] >= y[0] and x[1] <= y[1]


assert is_contained([3, 7], [2, 8]) 
assert is_contained([6, 6], [4, 6]) 


def is_contained_or_contains(x: List[int], y: List[int]) -> bool:
    return is_contained(x, y) or is_contained(y, x)


assert is_contained_or_contains([2, 8], [3, 7]) 
assert is_contained_or_contains([6, 6], [4, 6]) 

assert sum([is_contained_or_contains(pair[0], pair[1]) for pair in pairs]) == 2

def overlaps(x: List[int], y: List[int]) -> bool:
    if x[0] <= y[0]:
        return y[0] >= x[0] and y[0] <= x[1]
    else:
        return x[0] >= y[0] and x[0] <= y[1]


assert overlaps([5,7], [7,9])
assert overlaps([2,8], [3,7])
assert overlaps([6,6], [4,6])
assert overlaps([2,6], [4,8])

def main():
    with open("input/day04.txt") as f:
        lines = [line.rstrip() for line in f]

    pairs = lines_to_assignment_pairs(lines)

    pairs_to_reconsider = sum([is_contained_or_contains(pair[0], pair[1]) for pair in pairs])
    print(f"Part one solution: {pairs_to_reconsider}")
    pairs_overlapping = sum([overlaps(pair[0], pair[1]) for pair in pairs])
    print(f"Part two solution: {pairs_overlapping}")


if __name__ == "__main__":
    main()
