from adventofcode2022.day07 import parse_output

INPUT_PART1 = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_parse_output():
    exp_sizes = {
        "/": 48381165,
        "//d": 24933642,
        "//a": 94853,
        "//a/e": 584,
    }
    calc_sizes = parse_output(INPUT_PART1.strip().split("\n"))
    assert calc_sizes == exp_sizes
    assert sum([x for x in calc_sizes.values() if x <= 100000]) == 95437
