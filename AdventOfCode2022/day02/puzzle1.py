def round_score(strategy):
    choices = {"A": "rock", "B": "paper", "C": "scissors",
               "X": "rock", "Y": "paper", "Z": "scissors"
               }
    shape_score = {"rock": 1, "paper": 2, "scissors": 3}
    ends_score = {"loss": 0, "draw": 3, "win": 6}

    pl1, pl2 = strategy.split()
    # draw
    if choices[pl1] == choices[pl2]:
        return ends_score["draw"] + shape_score[choices[pl2]]
    # win
    if (
        choices[pl1] == "rock" and choices[pl2] == "paper"
        or choices[pl1] == "paper" and choices[pl2] == "scissors"
        or choices[pl1] == "scissors" and choices[pl2] == "rock"
    ):
        return ends_score["win"] + shape_score[choices[pl2]]
    # loss
    if (
        choices[pl1] == "rock" and choices[pl2] == "scissors"
        or choices[pl1] == "paper" and choices[pl2] == "rock"
        or choices[pl1] == "scissors" and choices[pl2] == "paper"
    ):
        return ends_score["loss"] + shape_score[choices[pl2]]


path = "AdventOfCode2022/day02/input.txt"

strategies = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        strategies.append(line.strip())

score = 0
for s in strategies:
    score += round_score(s)

print("Puzzle1 = ", score)
