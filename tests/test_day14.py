from adventofcode2022.day14 import path_from_text, Cave

EXAMPLE_INPUT = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9\
"""


def test_parse_path():
    paths = [path_from_text(x) for x in EXAMPLE_INPUT.splitlines()]
    assert paths == [
        [(498, 4), (498, 6), (496, 6)],
        [(503, 4), (502, 4), (502, 9), (494, 9)],
    ]


def test_cave_add_path():
    cave = Cave()
    cave.add_path([(498, 4), (498, 6), (496, 6)])
    assert cave.is_tile_blocked((498, 4))
    assert cave.is_tile_blocked((498, 5))
    assert cave.is_tile_blocked((498, 6))
    assert cave.is_tile_blocked((497, 6))
    assert cave.is_tile_blocked((496, 6))
    assert not cave.is_tile_blocked((495, 6))
    assert not cave.is_tile_blocked((498, 3))
    assert not cave.is_tile_blocked((498, 7))
    assert cave.bottom == 6
    cave.add_path([(503, 4), (502, 4), (502, 9), (494, 9)])
    assert cave.bottom == 9
    assert cave.floor == 11


def test_cave_produce_sand():
    cave = Cave()
    cave.add_path([(498, 4), (498, 6), (496, 6)])
    cave.add_path([(503, 4), (502, 4), (502, 9), (494, 9)])
    for _ in range(24):
        assert cave.produce_sand()
    assert not cave.produce_sand()


def test_cave_produce_sand_with_floor():
    cave = Cave(has_floor=True)
    cave.add_path([(498, 4), (498, 6), (496, 6)])
    cave.add_path([(503, 4), (502, 4), (502, 9), (494, 9)])
    n_units = 0
    while not cave.is_source_blocked():
        cave.produce_sand()
        n_units += 1
    assert n_units + 1 == 93
