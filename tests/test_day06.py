from adventofcode2022.day06 import find_marker

INPUT_PART1 = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
}


def test_find_marker():
    for key, value in INPUT_PART1.items():
        assert find_marker(key) == value, f"Expected {value} but got {find_marker(key)}"
