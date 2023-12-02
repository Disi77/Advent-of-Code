def is_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True


path = "AdventOfCode2016/day03/input.txt"
with open(path, encoding="utf-8", mode="r") as raw_data:
    puzzle_input = []
    for line in raw_data:
        values = [int(line[:5]), int(line[5:10]), int(line[10:15])]
        puzzle_input.append(values)


# Puzzle 1
counter = 0
for i in puzzle_input:
    if is_triangle(*i):
        counter += 1

print("Puzzle 1 =", counter)


#Puzzle 2
new_puzzle_input = []
for i in range(0, len(puzzle_input), 3):
    for j in range(3):
        values = [puzzle_input[i][j], puzzle_input[i + 1][j], puzzle_input[i + 2][j]]
        new_puzzle_input.append(values)

counter = 0
for i in new_puzzle_input:
    if is_triangle(*i):
        counter += 1

print("Puzzle 2 =", counter)
