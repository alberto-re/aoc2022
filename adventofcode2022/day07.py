#!/usr/bin/env python3
# --- Day 7: No Space Left On Device ---

from typing import List, DefaultDict
from collections import defaultdict

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

def parse_output(lines: List[str]) -> DefaultDict[str, int]:
    pos = 0
    cwd = ["/"]
    curcmd = ""
    dirsize: DefaultDict[str, int] = defaultdict(int)
    while pos < len(lines):
        line = lines[pos]
        if line.startswith("$"):
            parts = line.split()
            _, cmd = parts[0], parts[1]
            curcmd = cmd
            if cmd == "cd":
                arg = parts[2]
                if arg == "/":
                    cwd = [arg]
                elif arg == "..":
                    cwd.pop()
                else:
                    cwd.append(arg)
            elif cmd == "ls":
                pass
            else:
                raise ValueError(f"Unknown command: {cmd}")
        else:
            if curcmd == "ls":
                if line.startswith("dir"):
                    pass
                else:
                    size, _ = line.split()
                    for i in range(len(cwd)):
                        dirsize["/".join(cwd[0:i+1])] += int(size)
        pos += 1
    return dirsize

exp_sizes = {
    "/": 48381165,
    "//d": 24933642,
    "//a": 94853,
    "//a/e": 584,
}
calc_sizes = parse_output(INPUT_PART1.strip().split("\n"))
assert calc_sizes == exp_sizes

assert sum([x for x in calc_sizes.values() if x <= 100000]) == 95437

def main():
    with open("input/day07.txt") as f:
        lines = [line.rstrip() for line in f]

    calc_sizes = parse_output(lines)
    sum_sizes = sum([x for x in calc_sizes.values() if x <= 100000])
    print(f"Part one solution: {sum_sizes}")

    total_disk_used = calc_sizes["/"]
    disk_to_free = 30000000 - (70000000 - total_disk_used)

    smallest_size_enough = total_disk_used
    for size in sorted(calc_sizes.values()):
        if size >= disk_to_free and size < smallest_size_enough:
            smallest_size_enough = size

    print(f"Part two solution: {smallest_size_enough}")


if __name__ == "__main__":
    main()
