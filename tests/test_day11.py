from adventofcode2022.day11 import Monkey, parse_input, do_round, monkey_business

EXAMPLE_INPUT_PART1 = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


MONKEY_TEXT_EXAMPLE_0 = "\n".join(EXAMPLE_INPUT_PART1.splitlines()[:6])
MONKEY_TEXT_EXAMPLE_1 = "\n".join(EXAMPLE_INPUT_PART1.splitlines()[7:14])


def test_monkey_from_text():
    monkey0 = Monkey.from_text(MONKEY_TEXT_EXAMPLE_0)
    monkey1 = Monkey.from_text(MONKEY_TEXT_EXAMPLE_1)
    assert monkey0.items == [79, 98]
    assert monkey1.items == [54, 65, 75, 74]


def test_monkey_inspect():
    monkey0 = Monkey.from_text(MONKEY_TEXT_EXAMPLE_0)
    monkey1 = Monkey.from_text(MONKEY_TEXT_EXAMPLE_1)
    assert monkey0.inspect(0) == 1501
    assert monkey0.inspect(1) == 1862
    assert monkey1.inspect(0) == 60
    assert monkey1.inspect(1) == 71
    assert monkey1.inspect(2) == 81
    assert monkey1.inspect(3) == 80


def test_monkey_decide():
    monkey0 = Monkey.from_text(MONKEY_TEXT_EXAMPLE_0)
    assert monkey0.decide(500) == 3
    assert monkey0.decide(620) == 3


def test_parse_input():
    monkeys = parse_input(EXAMPLE_INPUT_PART1)
    assert len(monkeys) == 4


def test_do_round():
    monkeys = parse_input(EXAMPLE_INPUT_PART1)
    for _ in range(20):
        do_round(monkeys)
    assert monkey_business(monkeys) == 10605


def test_do_round_part2():
    monkeys = parse_input(EXAMPLE_INPUT_PART1)

    do_round(monkeys, very_worried=True)
    assert monkey_business(monkeys) == 4 * 6

    for _ in range(19):
        do_round(monkeys, very_worried=True)
    assert monkey_business(monkeys) == 103 * 99

    for _ in range(980):
        do_round(monkeys, very_worried=True)
    assert monkey_business(monkeys) == 5204 * 5192

    for _ in range(9000):
        do_round(monkeys, very_worried=True)
    assert monkey_business(monkeys) == 52166 * 52013
