def round_outcome(strategy):
    choices = {"A": "rock", "B": "paper", "C": "scissors"}
    ends = {"X": "loss", "Y": "draw", "Z": "win"}
    shape_score = {"rock": 1, "paper": 2, "scissors": 3}
    ends_score = {"loss": 0, "draw": 3, "win": 6}

    opponent, myself = strategy.split()
    # draw = I have to have the same as my opponent
    if ends[myself] == "draw":
        return ends_score[ends[myself]] + shape_score[choices[opponent]]
    # win
    if ends[myself] == "win":
        if choices[opponent] == "rock":
            return ends_score[ends[myself]] + shape_score["paper"]
        if choices[opponent] == "paper":
            return ends_score[ends[myself]] + shape_score["scissors"]
        if choices[opponent] == "scissors":
            return ends_score[ends[myself]] + shape_score["rock"]
    # loss
    if ends[myself] == "loss":
        if choices[opponent] == "rock":
            return ends_score[ends[myself]] + shape_score["scissors"]
        if choices[opponent] == "paper":
            return ends_score[ends[myself]] + shape_score["rock"]
        if choices[opponent] == "scissors":
            return ends_score[ends[myself]] + shape_score["paper"]


path = "AdventOfCode2022/day02/input.txt"

strategies = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        strategies.append(line.strip())

score = 0
for s in strategies:
    score += round_outcome(s)

print("Puzzle 2 =", score)
