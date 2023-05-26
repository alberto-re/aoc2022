#!/usr/bin/env python3
# --- Day 5: Supply Stacks ---

from copy import deepcopy

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


def input_lines(input: str) -> list[str]:
    return [line for line in input.split("\n")]


def split_input(lines: list[str]) -> tuple[list[str], list[str]]:
    stacks = []
    procedures = []
    empty_line_seen = False
    for line in lines:
        if line == "":
            empty_line_seen = True
            continue
        if not empty_line_seen:
            stacks.append(line)
        else:
            procedures.append(line)
    return stacks, procedures


stacks_text, procedures = split_input(input_lines(INPUT_PART1))
assert len(stacks_text) == 4
assert len(procedures) == 4


def parse_stacks(lines: list[str]) -> list[list[str]]:
    lines.reverse()
    cols = lines.pop(0)
    stacks: list[list[str]] = [[] for _ in range(max(map(int, cols.split())))]
    for line in lines:
        for i in range(len(stacks)):
            try:
                char_at_col = line[i * 4 + 1]
                if char_at_col != " ":
                    stacks[i].append(char_at_col)
            except IndexError:
                continue
    return stacks


stacks = parse_stacks(stacks_text)
assert stacks == [["Z", "N"], ["M", "C", "D"], ["P"]]


def move_stacks(
    stacks: list[list[str]], procedures: list[str], retain: bool = False
) -> list[list[str]]:
    result = deepcopy(stacks)
    for move in procedures:
        parts = move.split()
        qty, origin, dest = int(parts[1]), int(parts[3]), int(parts[5])
        tmp = []
        for _ in range(qty):
            tmp.append(result[origin - 1].pop())
        for _ in range(len(tmp)):
            if retain:
                result[dest - 1].append(tmp.pop())
            else:
                result[dest - 1].append(tmp.pop(0))
    return result


moved = move_stacks(stacks, procedures)
assert "".join([stack[-1] for stack in moved]) == "CMZ"
moved = move_stacks(stacks, procedures, retain=True)
assert "".join([stack[-1] for stack in moved]) == "MCD"


def main():
    with open("input/day05.txt") as f:
        lines = [line.rstrip() for line in f]

    stacks, procedures = split_input(lines)
    stacks = parse_stacks(stacks)
    moved = move_stacks(stacks, procedures)
    print(f"Part one solution: {''.join([stack[-1] for stack in moved])}")
    moved = move_stacks(stacks, procedures, retain=True)
    print(f"Part two solution: {''.join([stack[-1] for stack in moved])}")


if __name__ == "__main__":
    main()
