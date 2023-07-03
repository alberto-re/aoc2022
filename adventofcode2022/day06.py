#!/usr/bin/env python3
# --- Day 6: Tuning Trouble ---


def find_marker(buffer: str, distinct_chars: int = 4) -> int:
    for i in range(distinct_chars, len(buffer)):
        if len(set(buffer[i - distinct_chars : i])) == distinct_chars:
            return i
    return 0


def main() -> None:
    with open("input/day06.txt") as f:
        line = f.readline().strip()

    print(f"Part one solution: {find_marker(line)}")
    print(f"Part two solution: {find_marker(line, 14)}")


if __name__ == "__main__":
    main()
