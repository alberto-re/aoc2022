from adventofcode2022.day04 import (
    input_lines,
    lines_to_assignment_pairs,
    is_contained,
    is_contained_or_contains,
    overlaps,
)

INPUT_PART1 = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8\
"""


def test_lines_to_assignment_pairs():
    expected = [
        ([2, 4], [6, 8]),
        ([2, 3], [4, 5]),
        ([5, 7], [7, 9]),
        ([2, 8], [3, 7]),
        ([6, 6], [4, 6]),
        ([2, 6], [4, 8]),
    ]
    pairs = lines_to_assignment_pairs(input_lines(INPUT_PART1))
    assert pairs == expected


def test_is_contained():
    assert is_contained([3, 7], [2, 8])
    assert is_contained([6, 6], [4, 6])


def test_is_contained_or_contains():
    assert is_contained_or_contains([2, 8], [3, 7])
    assert is_contained_or_contains([6, 6], [4, 6])


def test_overlaps():
    assert overlaps([5, 7], [7, 9])
    assert overlaps([2, 8], [3, 7])
    assert overlaps([6, 6], [4, 6])
    assert overlaps([2, 6], [4, 8])
