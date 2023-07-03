#!/usr/bin/env python3
# --- Day 10: Cathode-Ray Tube ---


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
