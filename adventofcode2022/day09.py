#!/usr/bin/env python3
# --- Day 9: Rope Bridge ---

from dataclasses import dataclass


@dataclass
class Knot:
    x: int
    y: int

    def touches(self, knot: "Knot") -> bool:
        return abs(self.x - knot.x) <= 1 and abs(self.y - knot.y) <= 1

    def move_towards(self, knot: "Knot") -> None:
        if self.x < knot.x:
            self.x += 1
        if self.x > knot.x:
            self.x -= 1
        if self.y < knot.y:
            self.y += 1
        if self.y > knot.y:
            self.y -= 1


assert Knot(1, 1).touches(Knot(1, 1))
assert Knot(1, 1).touches(Knot(2, 2))
assert not Knot(1, 1).touches(Knot(1, 3))

knot = Knot(1, 1)
knot.move_towards(Knot(3, 1))
assert knot.x == 2 and knot.y == 1
knot.move_towards(Knot(2, 3))
assert knot.x == 2 and knot.y == 2
knot.move_towards(Knot(4, 4))
assert knot.x == 3 and knot.y == 3


class Rope:
    def __init__(self, knots: list[Knot]):
        self.knots = knots

    @property
    def head(self) -> Knot:
        return self.knots[0]

    @property
    def tail(self) -> Knot:
        return self.knots[-1]

    def move_head(self, xd: int, yd: int) -> None:
        self.knots[0].x += xd
        self.knots[0].y += yd

        for i in range(1, len(self.knots)):
            if not self.knots[i].touches(self.knots[i - 1]):
                self.knots[i].move_towards(self.knots[i - 1])

    def apply_motions(self, motions: list[tuple[str, int]]) -> list[tuple[int, int]]:
        path = []
        for direction, quantity in motions:
            if direction == "U":
                delta = (0, -1)
            elif direction == "D":
                delta = (0, 1)
            elif direction == "L":
                delta = (-1, 0)
            else:
                delta = (1, 0)
            for _ in range(quantity):
                self.move_head(*delta)
                path.append((self.tail.x, self.tail.y))
        return path


# ....     .....    .....
# .TH.. -> .T.H. -> ..TH.
# .....    .....    .....
rope = Rope([Knot(2, 1), Knot(1, 1)])
rope.move_head(1, 0)
assert rope.head.x == 3 and rope.head.y == 1, f"{rope.head}"
assert rope.tail.x == 2 and rope.tail.y == 1, f"{rope.tail}"

# ...    ...    ...
# .T.    .T.    ...
# .H. -> ... -> .T.
# ...    .H.    .H.
# ...    ...    ...
rope = Rope([Knot(1, 2), Knot(1, 1)])
rope.move_head(0, 1)
assert rope.head.x == 1 and rope.head.y == 3
assert rope.tail.x == 1 and rope.tail.y == 2

# .....    .....    .....
# .....    ..H..    ..H..
# ..H.. -> ..... -> ..T..
# .T...    .T...    .....
# .....    .....    .....
rope = Rope([Knot(2, 2), Knot(1, 3)])
rope.move_head(0, -1)
assert rope.head.x == 2 and rope.head.y == 1
assert rope.tail.x == 2 and rope.tail.y == 2

# .....    .....    .....
# .....    .....    .....
# ..H.. -> ...H. -> ..TH.
# .T...    .T...    .....
# .....    .....    .....
rope = Rope([Knot(2, 2), Knot(1, 3)])
rope.move_head(1, 0)
assert rope.head.x == 3 and rope.head.y == 2
assert rope.tail.x == 2 and rope.tail.y == 2

INPUT_PART1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


def parse_motions(text: str) -> list[tuple[str, int]]:
    motions = []
    for line in text.strip().splitlines():
        direction, quantity = line.split()
        motions.append((direction, int(quantity)))
    return motions


exp_motions = [
    ("R", 4),
    ("U", 4),
    ("L", 3),
    ("D", 1),
    ("R", 4),
    ("D", 1),
    ("L", 5),
    ("R", 2),
]
motions = parse_motions(INPUT_PART1)
assert motions == exp_motions

rope = Rope([Knot(0, 0), Knot(0, 0)])
path = rope.apply_motions(motions)
assert len(set(path)) == 13


def main() -> None:
    with open("input/day09.txt") as f:
        motions = parse_motions(f.read())

    rope = Rope([Knot(0, 0), Knot(0, 0)])
    path = rope.apply_motions(motions)
    print(f"Part one solution: {len(set(path))}")

    rope = Rope([Knot(0, 0) for _ in range(10)])
    path = rope.apply_motions(motions)
    print(f"Part two solution: {len(set(path))}")


if __name__ == "__main__":
    main()
