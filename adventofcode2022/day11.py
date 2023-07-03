#!/usr/bin/env python3
# --- Day 11: Monkey in the Middle ---
from typing import Callable
import re
import operator
import math


class Monkey:
    def __init__(
        self,
        idx: int,
        items: list[int],
        operation: Callable,
        test: tuple[int, int, int],
    ) -> None:
        self._idx = idx
        self._items = items
        self._operation = operation
        self._test = test
        self._inspect_count = 0

    @staticmethod
    def from_text(text: str) -> "Monkey":
        pattern = """\
Monkey (\d+):
  Starting items: (.+)
  Operation: new = (.+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)\
"""

        op_impl = {
            "*": operator.mul,
            "/": operator.truediv,
            "+": operator.add,
            "-": operator.sub,
        }

        match = re.search(pattern, text, re.MULTILINE)
        assert match is not None
        idx = int(match.group(1))
        items = list(map(int, match.group(2).split(", ")))
        x, op, y = match.group(3).split()
        match x, y:
            case "old", "old":

                def operation(old: int) -> int:
                    return op_impl[op](old, old)

            case "old", x:

                def operation(old: int) -> int:
                    return op_impl[op](old, int(x))

            case x, _:

                def operation(old: int) -> int:
                    return op_impl[op](int(x), old)

            case x, y:

                def operation(old: int) -> int:
                    return op_impl[op](int(x), int(y))

        div_by = int(match.group(4))
        div_if_true = int(match.group(5))
        div_if_false = int(match.group(6))
        return Monkey(idx, items, operation, (div_by, div_if_true, div_if_false))

    @property
    def items(self) -> list[int]:
        return self._items

    @property
    def test(self) -> tuple[int, int, int]:
        return self._test

    @property
    def inspect_count(self) -> int:
        return self._inspect_count

    def inspect(self, item_index: int) -> int:
        self._inspect_count += 1
        return self._operation(self._items[item_index])

    def decide(self, worry: int) -> int:
        return self._test[1] if worry % self._test[0] == 0 else self._test[2]

    def take(self, item: int) -> None:
        self._items.append(item)


def parse_input(puzzle_input: str) -> list[Monkey]:
    monkeys = []
    input_lines = puzzle_input.splitlines()
    for linen in range(0, len(input_lines), 7):
        monkey_text = "\n".join(input_lines[linen : linen + 7])
        monkey = Monkey.from_text(monkey_text)
        monkeys.append(monkey)
    return monkeys


def do_round(monkeys: list[Monkey], very_worried: bool = False) -> None:
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.test[0]

    for monkey in monkeys:
        thrown = []
        for idx in range(len(monkey.items)):
            worry = monkey.inspect(idx)
            if very_worried:
                worry = worry % modulo
            if not very_worried:
                worry = math.floor(worry / 3)
            dest = monkey.decide(worry)
            thrown.append(idx)
            monkeys[dest].take(worry)

        monkey._items = [
            monkey._items[x] for x in range(len(monkey._items)) if x not in thrown
        ]


def monkey_business(monkeys: list[Monkey]) -> int:
    inspections = sorted([x.inspect_count for x in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def main() -> None:
    with open("input/day11.txt") as f:
        monkeys = parse_input(f.read())

    for _ in range(20):
        do_round(monkeys)

    print(f"Part one solution: {monkey_business(monkeys)}")

    with open("input/day11.txt") as f:
        monkeys = parse_input(f.read())

    for _ in range(10000):
        do_round(monkeys, very_worried=True)

    print(f"Part two solution: {monkey_business(monkeys)}")


if __name__ == "__main__":
    main()
