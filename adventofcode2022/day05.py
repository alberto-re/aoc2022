#!/usr/bin/env python3
# --- Day 5: Supply Stacks ---

from copy import deepcopy


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


def main() -> None:
    with open("input/day05.txt") as f:
        lines = [line.rstrip() for line in f]

    stacks, procedures = split_input(lines)
    moved = move_stacks(parse_stacks(stacks), procedures)
    print(f"Part one solution: {''.join([stack[-1] for stack in moved])}")
    moved = move_stacks(parse_stacks(stacks), procedures, retain=True)
    print(f"Part two solution: {''.join([stack[-1] for stack in moved])}")


if __name__ == "__main__":
    main()
