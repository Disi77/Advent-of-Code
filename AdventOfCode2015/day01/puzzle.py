path = "AdventOfCode2015/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

result = data.count("(") - data.count(")")
print("Puzzle 1 =", result)

floor = 0
for i, instruction in enumerate(data):
    if floor == -1:
        break
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1

print("Puzzle 2 =", i)