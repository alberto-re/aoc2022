from adventofcode2022.day05 import split_input, input_lines, parse_stacks, move_stacks

INPUT_PART1 = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2\
"""


def test_is_contained_or_contains():
    stacks_text, procedures = split_input(input_lines(INPUT_PART1))
    assert len(stacks_text) == 4
    assert len(procedures) == 4


def test_parse_stacks():
    stacks_text, procedures = split_input(input_lines(INPUT_PART1))
    stacks = parse_stacks(stacks_text)
    assert stacks == [["Z", "N"], ["M", "C", "D"], ["P"]]


def test_move_stacks():
    stacks_text, procedures = split_input(input_lines(INPUT_PART1))
    stacks = parse_stacks(stacks_text)
    moved = move_stacks(stacks, procedures)
    assert "".join([stack[-1] for stack in moved]) == "CMZ"
    moved = move_stacks(stacks, procedures, retain=True)
    assert "".join([stack[-1] for stack in moved]) == "MCD"
