#!/usr/bin/env python3
# --- Day 2: Rock Paper Scissors ---

oppo = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

you = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

score_shape = {"rock": 1, "paper": 2, "scissors": 3}

score_outcome = {"lost": 0, "draw": 3, "won": 6}


def guess_play(lines: list[str]) -> list[str]:
    choice_to_symbol = {v: k for k, v in you.items()}
    lose = {v: k for k, v in wins.items()}

    plays = []
    for line in lines:
        x, y = line.split()
        if y == "X":
            y = choice_to_symbol[wins[oppo[x]]]
        elif y == "Y":
            y = choice_to_symbol[oppo[x]]
        elif y == "Z":
            y = choice_to_symbol[lose[oppo[x]]]
        plays.append(f"{x} {y}")
    return plays


def total_score(lines: list[str]) -> int:
    score = 0
    for line in lines:
        x, y = line.split()
        x, y = oppo[x], you[y]

        score += score_shape[y]

        if x == y:
            score += score_outcome["draw"]
        else:
            if wins[y] == x:
                score += score_outcome["won"]
            else:
                score += score_outcome["lost"]
    return score


def main() -> None:
    with open("input/day02.txt") as f:
        lines = [line for line in f]

    print(f"Part one solution: {total_score(lines)}")
    print(f"Part two solution: {total_score(guess_play(lines))}")


if __name__ == "__main__":
    main()
