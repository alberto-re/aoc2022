#!/usr/bin/env python3
# --- Day 10: Cathode-Ray Tube ---

SMALL_INPUT_PART1 = """
noop
addx 3
addx -5
"""

LARGE_INPUT_PART1 = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


def parse_input(input: str) -> list[tuple[str, int | None]]:
    instr: list[tuple[str, int | None]] = []
    for line in input.strip().splitlines():
        parts = line.split()
        if parts[0] == "noop":
            instr.append(("noop", None))
        elif parts[0] == "addx":
            instr.append(("addx", int(parts[1])))
        else:
            raise ValueError(f"Unknown instruction {parts[0]}")
    return instr


program_small = parse_input(SMALL_INPUT_PART1)
assert program_small == [("noop", None), ("addx", 3), ("addx", -5)]


class CPU:
    def __init__(self) -> None:
        self._x: int = 1
        self._xhist: list[int] = [1]
        self._cycle: int = 0

    @property
    def x(self) -> int:
        return self._x

    @property
    def xhist(self) -> list[int]:
        return self._xhist

    def run(self, program: list[tuple[str, int | None]]) -> None:
        queue = []
        for instr, arg in program:
            if instr == "noop":
                queue.append((instr, arg))
            elif instr == "addx":
                queue.append(("noop", None))
                queue.append((instr, arg))
            else:
                raise ValueError(f"Unknown instruction {instr}")
        for instr, arg in queue:
            self._cycle += 1
            self._xhist.append(self._x)
            if instr == "noop":
                continue
            else:
                self._x += arg if arg is not None else 0


cpu = CPU()
cpu.run(program_small)

assert cpu.xhist[0] == 1
assert cpu.xhist[1] == 1
assert cpu.xhist[2] == 1
assert cpu.xhist[3] == 1
assert cpu.xhist[4] == 4
assert cpu.xhist[5] == 4
assert cpu.x == -1

program_large = parse_input(LARGE_INPUT_PART1)

cpu = CPU()
cpu.run(program_large)

assert cpu.xhist[20] * 20 == 420
assert cpu.xhist[60] * 60 == 1140
assert cpu.xhist[100] * 100 == 1800
assert cpu.xhist[140] * 140 == 2940
assert cpu.xhist[180] * 180 == 2880
assert cpu.xhist[220] * 220 == 3960

assert sum(cpu.xhist[x] * x for x in [20, 60, 100, 140, 180, 220]) == 13140


def main() -> None:
    with open("input/day10.txt") as f:
        program = parse_input(f.read())

    cpu = CPU()
    cpu.run(program)
    signals_strength_sum = sum(cpu.xhist[x] * x for x in [20, 60, 100, 140, 180, 220])

    print(f"Part one solution: {signals_strength_sum}")

    print("Part two solution:")
    for cycle, x in enumerate(cpu.xhist[1:]):
        col = cycle % 40
        pixel = "#" if abs(col - x) < 2 else "."
        print(pixel, end="" if col < 39 else "\n")


if __name__ == "__main__":
    main()
