#!/usr/bin/env python3
# --- Day 14: Regolith Reservoir ---
from typing import TypeAlias, DefaultDict
from collections import defaultdict
from enum import Enum

XY: TypeAlias = tuple[int, int]
Path: TypeAlias = list[XY]


class Tile(Enum):
    rock = "#"
    sand = "o"
    air = "."


class Cave:
    def __init__(self, has_floor: bool = False) -> None:
        self._grid: DefaultDict[XY, Tile] = defaultdict(lambda: Tile.air)
        self._bottom: int = 0
        self._has_floor = has_floor

    @property
    def bottom(self) -> int:
        return self._bottom

    @property
    def floor(self) -> int:
        return self._bottom + 2

    def add_block(self, xy: XY, tile: Tile) -> None:
        self._grid[xy] = tile

    def add_path(self, path: list[XY]) -> None:
        for idx in range(len(path) - 1):
            from_xy = path[idx]
            to_xy = path[idx + 1]
            if from_xy[0] == to_xy[0]:
                x = from_xy[0]
                if from_xy[1] < to_xy[1]:
                    for y in range(from_xy[1], to_xy[1] + 1):
                        self.add_block((x, y), Tile.rock)
                        if y > self._bottom:
                            self._bottom = y
                else:
                    for y in range(to_xy[1], from_xy[1] + 1):
                        self.add_block((x, y), Tile.rock)
                        if y > self._bottom:
                            self._bottom = y
            elif from_xy[1] == to_xy[1]:
                y = from_xy[1]
                if from_xy[0] < to_xy[0]:
                    for x in range(from_xy[0], to_xy[0] + 1):
                        self.add_block((x, y), Tile.rock)
                        if y > self._bottom:
                            self._bottom = y
                else:
                    for x in range(to_xy[0], from_xy[0] + 1):
                        self.add_block((x, y), Tile.rock)
                        if y > self._bottom:
                            self._bottom = y
            else:
                raise ValueError("Segment {} -> {} is neither horizontal nor vertical")

    def is_tile_blocked(self, xy: XY) -> bool:
        if self._has_floor and xy[1] == self.floor:
            return True
        return self._grid[xy] in [Tile.rock, Tile.sand]

    def is_source_blocked(self) -> bool:
        return (
            self.is_tile_blocked((500, 1))
            and self.is_tile_blocked((499, 1))
            and self.is_tile_blocked((501, 1))
        )

    def produce_sand(self) -> bool:
        x, y = 500, 0
        bottom = self.floor if self._has_floor else self.bottom
        while y < bottom:
            if not self.is_tile_blocked((x, y + 1)):
                y += 1
            elif not self.is_tile_blocked((x - 1, y + 1)):
                x -= 1
                y += 1
            elif not self.is_tile_blocked((x + 1, y + 1)):
                x += 1
                y += 1
            else:
                self.add_block((x, y), Tile.sand)
                return True
        return False


def path_from_text(text: str) -> Path:
    path = []
    for xy in text.split(" -> "):
        x, y = xy.split(",")
        path.append((int(x), int(y)))
    return path


def main() -> None:
    with open("input/day14.txt") as f:
        paths = [path_from_text(x) for x in f.read().splitlines()]

    cave = Cave()
    for path in paths:
        cave.add_path(path)

    n_units = 0
    while cave.produce_sand():
        n_units += 1

    print(f"Part one solution: {n_units}")

    cave = Cave(has_floor=True)
    for path in paths:
        cave.add_path(path)
    n_units = 0
    while not cave.is_source_blocked():
        cave.produce_sand()
        n_units += 1
    print(f"Part two solution: {n_units + 1}")


if __name__ == "__main__":
    main()
