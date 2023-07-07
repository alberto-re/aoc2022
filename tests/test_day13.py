from adventofcode2022.day13 import parse_packet, parse_packets, compare_packets

EXAMPLE_INPUT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]\
"""


def test_parse_packet():
    assert parse_packet("[1,1,3,1,1]") == [1, 1, 3, 1, 1]
    assert parse_packet("[9]") == [9]
    assert parse_packet("[[8,7,6]]") == [[8, 7, 6]]
    assert parse_packet("[[4,4],4,4]") == [[4, 4], 4, 4]
    assert parse_packet("[]") == []
    assert parse_packet(
        "[[[5,[10,6],5,1,6],4],[[9,[7,4,7],6,[],7],[[9,6,0,10],7,[8,5,5,2,7],[7,10,5,6]]]]"
    ) == [
        [[5, [10, 6], 5, 1, 6], 4],
        [[9, [7, 4, 7], 6, [], 7], [[9, 6, 0, 10], 7, [8, 5, 5, 2, 7], [7, 10, 5, 6]]],
    ]


def test_parse_packets():
    pairs = parse_packets(EXAMPLE_INPUT)
    assert pairs == [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        ([[1], [2, 3, 4]], [[1], 4]),
        ([9], [[8, 7, 6]]),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        ([7, 7, 7, 7], [7, 7, 7]),
        ([], [3]),
        ([[[]]], [[]]),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    ]


def test_compare_packets():
    assert compare_packets([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) < 0
    assert compare_packets([[1], [2, 3, 4]], [[1], 4]) < 0
    assert compare_packets([9], [[8, 7, 6]]) > 0
    assert compare_packets([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) < 0
    assert compare_packets([7, 7, 7, 7], [7, 7, 7]) > 0
    assert compare_packets([], [[3]]) < 0
    assert compare_packets([[[]]], [[]]) > 0
    assert (
        compare_packets(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
        )
        > 0
    )


def test_indices():
    pairs = parse_packets(EXAMPLE_INPUT)
    indices = []
    for idx, (left, right) in enumerate(pairs):
        if compare_packets(left, right) < 0:
            indices.append(idx + 1)
    assert indices == [1, 2, 4, 6]
