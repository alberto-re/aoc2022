#!/usr/bin/env python3
# --- Day 3: Rucksack Reorganization ---

from typing import List, Tuple


def split_rucksack(content: str) -> Tuple[str, str]:
    half = len(content) // 2
    return content[:half], content[half:]


assert split_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr", "hcsFMMfFFhFp")


def common_items(compartments: Tuple[str, str]) -> List[str]:
    return list(set(compartments[0]).intersection(set(compartments[1])))


assert common_items(("vJrwpWtwJgWr", "hcsFMMfFFhFp")) == ["p"]


def item_priority(item: str) -> int:
    decimal = ord(item)
    if decimal > 96:
        return decimal - 96
    else:
        return decimal - 38


for priority in [(16, "p"), (38, "L"), (42, "P"), (22, "v"), (20, "t"), (19, "s")]:
    assert item_priority(priority[1]) == priority[0]


def priorities(rucksacks: List[str]) -> List[int]:
    priorities = []
    for rucksack in rucksacks:
        compartments = split_rucksack(rucksack)
        common = common_items(compartments)
        assert len(common) == 1
        priorities.append(item_priority(common[0]))
    return priorities


INPUT_PART1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""

assert priorities(INPUT_PART1.split("\n")) == [16, 38, 42, 22, 20, 19]

INPUT_GROUP1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg\
"""

INPUT_GROUP2 = """\
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""


def find_badge(rucksacks: List[str]) -> str:
    rucksacks_unique_items: List[set] = [set(rucksack) for rucksack in rucksacks]
    for i in range(1, len(rucksacks_unique_items)):
        rucksacks_unique_items[0] = rucksacks_unique_items[0].intersection(
            rucksacks_unique_items[i]
        )
    common: List[str] = list(rucksacks_unique_items[0])
    assert len(common) == 1
    return common[0]


assert find_badge(INPUT_GROUP1.split("\n")) == "r"
assert find_badge(INPUT_GROUP2.split("\n")) == "Z"


def badge_priorities(rucksacks: List[str]) -> List[int]:
    priorities = []
    for i in range(0, len(rucksacks), 3):
        item = find_badge(rucksacks[i : i + 3])
        priorities.append(item_priority(item))
    return priorities


def main():
    with open("input/day03.txt") as f:
        lines = [line.rstrip() for line in f]

    print(f"Part one solution: {sum(priorities(lines))}")
    print(f"Part two solution: {sum(badge_priorities(lines))}")


if __name__ == "__main__":
    main()
