#!/usr/bin/env python3
# --- Day 12: Hill Climbing Algorithm ---

from collections import deque

Heightmap = list[list[str]]
Position = tuple[int, int]


def heightmap_from_text(
    text: str,
) -> tuple[Heightmap, Position, Position]:
    hmap = []
    start, end = (0, 0), (0, 0)
    for rowidx, row in enumerate(text.strip().split("\n")):
        row_vals = []
        for colidx, value in enumerate(row):
            if value == "S":
                start = (colidx, rowidx)
                value = "a"
            if value == "E":
                end = (colidx, rowidx)
                value = "z"
            row_vals.append(value)
        hmap.append(row_vals)
    return hmap, start, end


def elevation(area: str) -> int:
    return ord(area)


def valid_moves(hmap: Heightmap, pos: Position) -> list[Position]:
    candidates = []
    width = len(hmap[0])
    height = len(hmap)
    curr_elevation = elevation(hmap[pos[1]][pos[0]])
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        dpos = (pos[0] + dx, pos[1] + dy)
        if dpos[0] < 0 or dpos[0] > width - 1 or dpos[1] < 0 or dpos[1] > height - 1:
            continue
        dest_elevation = elevation(hmap[dpos[1]][dpos[0]])
        if dest_elevation > curr_elevation + 1:
            continue
        candidates.append(dpos)
    return candidates


def find_shortest_path(
    hmap: Heightmap, start: Position, end: Position
) -> list[Position] | None:
    frontier: deque[tuple] = deque([(start, [])])
    visited = []

    while len(frontier) > 0:
        pos, path = frontier.popleft()
        if pos in visited:
            continue
        visited.append(pos)
        if pos == end:
            return path
        candidates = valid_moves(hmap, pos)
        for pos in candidates:
            if pos not in visited:
                frontier.append((pos, path + [pos]))
    return None


def main() -> None:
    with open("input/day12.txt") as f:
        hmap, start, end = heightmap_from_text(f.read())

    path = find_shortest_path(hmap, start, end)
    assert path is not None
    print(f"Part one solution: {len(path)}")

    global_minlen = None
    for rowidx, row in enumerate(hmap):
        for colidx, area in enumerate(row):
            if area == "a":
                start = (colidx, rowidx)
                path = find_shortest_path(hmap, start, end)
                if path is None:
                    continue
                if global_minlen is None or len(path) < global_minlen:
                    global_minlen = len(path)

    print(f"Part two solution: {global_minlen}")


if __name__ == "__main__":
    main()
