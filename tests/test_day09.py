from adventofcode2022.day09 import Knot, Rope, parse_motions


def test_knot_touches():
    assert Knot(1, 1).touches(Knot(1, 1))
    assert Knot(1, 1).touches(Knot(2, 2))
    assert not Knot(1, 1).touches(Knot(1, 3))


def test_knot_towards():
    knot = Knot(1, 1)
    knot.move_towards(Knot(3, 1))
    assert knot.x == 2 and knot.y == 1
    knot.move_towards(Knot(2, 3))
    assert knot.x == 2 and knot.y == 2
    knot.move_towards(Knot(4, 4))
    assert knot.x == 3 and knot.y == 3


def test_knot_move_head():
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


def test_parse_motions():
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


def test_rope_apply_motions():
    motions = parse_motions(INPUT_PART1)
    rope = Rope([Knot(0, 0), Knot(0, 0)])
    path = rope.apply_motions(motions)
    assert len(set(path)) == 13
