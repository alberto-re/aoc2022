#!/usr/bin/env python3
# --- Day 1: Calorie Counting ---


def calories_per_elf(lines: list[str]) -> list[int]:
    aggr = [0]
    for line in lines:
        try:
            aggr[-1] += int(line)
        except ValueError:
            aggr.append(0)
    return aggr


def main():
    with open("input/day01.txt") as f:
        lines = [line for line in f]

    print(f"Part one solution: {max(calories_per_elf(lines))}")
    print(
        f"Part two solution: {sum(sorted(calories_per_elf(lines), reverse=True)[:3])}"
    )


if __name__ == "__main__":
    main()
