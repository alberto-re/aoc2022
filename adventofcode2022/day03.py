#!/usr/bin/env python3
# --- Day 3: Rucksack Reorganization ---


def split_rucksack(content: str) -> tuple[str, str]:
    half = len(content) // 2
    return content[:half], content[half:]


def common_items(compartments: tuple[str, str]) -> list[str]:
    return list(set(compartments[0]).intersection(set(compartments[1])))


def item_priority(item: str) -> int:
    decimal = ord(item)
    if decimal > 96:
        return decimal - 96
    else:
        return decimal - 38


def priorities(rucksacks: list[str]) -> list[int]:
    priorities = []
    for rucksack in rucksacks:
        compartments = split_rucksack(rucksack)
        common = common_items(compartments)
        assert len(common) == 1
        priorities.append(item_priority(common[0]))
    return priorities


def find_badge(rucksacks: list[str]) -> str:
    rucksacks_unique_items: list[set] = [set(rucksack) for rucksack in rucksacks]
    for i in range(1, len(rucksacks_unique_items)):
        rucksacks_unique_items[0] = rucksacks_unique_items[0].intersection(
            rucksacks_unique_items[i]
        )
    common: list[str] = list(rucksacks_unique_items[0])
    assert len(common) == 1
    return common[0]


def badge_priorities(rucksacks: list[str]) -> list[int]:
    priorities = []
    for i in range(0, len(rucksacks), 3):
        item = find_badge(rucksacks[i : i + 3])
        priorities.append(item_priority(item))
    return priorities


def main() -> None:
    with open("input/day03.txt") as f:
        lines = [line.rstrip() for line in f]

    print(f"Part one solution: {sum(priorities(lines))}")
    print(f"Part two solution: {sum(badge_priorities(lines))}")


if __name__ == "__main__":
    main()
