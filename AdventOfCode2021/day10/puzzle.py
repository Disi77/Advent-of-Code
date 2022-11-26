def where_is_corrupted(line):
    open = "([{<"
    close = ")]}>"
    temp = ""
    for i, char in enumerate(line):
        if char in open:
            temp += char
        else:
            if open.index(temp[-1]) == close.index(char):
                temp = temp[:-1]
            else:
                return i
    return -1


def find_missing_brackets(line):
    open = "([{<"
    close = ")]}>"
    temp = ""
    for char in line:
        if char in open:
            temp += char
        else:
            if open.index(temp[-1]) == close.index(char):
                temp = temp[:-1]
            else:
                return ""

    missing_brackets = ""
    for b in temp[::-1]:
        index = open.index(b)
        missing_brackets += close[index]
    return missing_brackets


def calculate_score(brackets):
    score_points = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for b in brackets:
        score = score * 5 + score_points[b]
    return score


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            puzzle_input.append(line.strip())
    return puzzle_input


#Puzzle input
puzzle_input = get_puzzle_input()


#Puzzle 1
score_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
result = 0
for line in puzzle_input:
    i = where_is_corrupted(line)
    if i == -1:
        continue
    result += score_points[line[i]]

print(f"Puzzle 1 = {result}")


#Puzzle 2
scores_list = []
for line in puzzle_input:
    brackets = find_missing_brackets(line)
    if not brackets:
        continue
    score = calculate_score(brackets)
    scores_list.append(score)

scores_list.sort()
middle_index = len(scores_list) // 2

print(f"Puzzle 2 = {scores_list[middle_index]}")