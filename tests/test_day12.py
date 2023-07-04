from adventofcode2022.day12 import (
    heightmap_from_text,
    elevation,
    valid_moves,
    find_shortest_path,
)

EXAMPLE_INPUT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi\
"""


def test_heightmap_from_text():
    hmap, start, end = heightmap_from_text(EXAMPLE_INPUT)
    assert start == (0, 0)
    assert end == (5, 2)
    assert hmap == [
        ["a", "a", "b", "q", "p", "o", "n", "m"],
        ["a", "b", "c", "r", "y", "x", "x", "l"],
        ["a", "c", "c", "s", "z", "z", "x", "k"],
        ["a", "c", "c", "t", "u", "v", "w", "j"],
        ["a", "b", "d", "e", "f", "g", "h", "i"],
    ]


def test_elevation():
    assert elevation("a") == 97
    assert elevation("g") == 103
    assert elevation("z") == 122


def test_valid_moves():
    hmap, _, _ = heightmap_from_text(EXAMPLE_INPUT)
    assert valid_moves(hmap, (1, 1)) == [
        (1, 0),
        (2, 1),
        (1, 2),
        (0, 1),
    ]
    assert valid_moves(hmap, (0, 0)) == [(1, 0), (0, 1)]
    assert valid_moves(hmap, (2, 1)) == [(2, 0), (2, 2), (1, 1)]


def test_find_shortest_path():
    hmap, start, end = heightmap_from_text(EXAMPLE_INPUT)
    path = find_shortest_path(hmap, start, end)
    assert len(path) == 31
