import pytest

from adventofcode2022.day03 import (
    split_rucksack,
    common_items,
    item_priority,
    priorities,
    find_badge,
)


def test_split_rucksack():
    assert split_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp") == (
        "vJrwpWtwJgWr",
        "hcsFMMfFFhFp",
    )


def test_common_items():
    assert common_items(("vJrwpWtwJgWr", "hcsFMMfFFhFp")) == ["p"]


@pytest.mark.parametrize(
    "input_item,exp_priority",
    [("p", 16), ("L", 38), ("P", 42), ("v", 22), ("t", 20), ("s", 19)],
)
def test_item_priority(input_item, exp_priority):
    assert item_priority(input_item) == exp_priority


INPUT_PART1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""


def test_priorities():
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


def test_find_badge():
    assert find_badge(INPUT_GROUP1.split("\n")) == "r"
    assert find_badge(INPUT_GROUP2.split("\n")) == "Z"
