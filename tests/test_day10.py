from adventofcode2022.day10 import parse_input, CPU

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


def test_parse_input():
    program_small = parse_input(SMALL_INPUT_PART1)
    assert program_small == [("noop", None), ("addx", 3), ("addx", -5)]


def test_cpu_run_small():
    program_small = parse_input(SMALL_INPUT_PART1)
    cpu = CPU()
    cpu.run(program_small)

    assert cpu.xhist[0] == 1
    assert cpu.xhist[1] == 1
    assert cpu.xhist[2] == 1
    assert cpu.xhist[3] == 1
    assert cpu.xhist[4] == 4
    assert cpu.xhist[5] == 4
    assert cpu.x == -1


def test_cpu_run_large():
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
