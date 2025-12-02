path = "AdventOfCode2025/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    instructions = [line.strip() for line in raw_data]

# Puzzle 1
position = 50
zeros = 0
for i in instructions:
    rotation = int(i[1:])
    if i[0] == "L":
        rotation *= -1
    position = (position + rotation) % 100
    zeros += position == 0


print("Puzzle 1 =", zeros)

# Puzzle 2
position = 50
zeros = 0
for i in instructions:
    rotation = int(i[1:])
    if i[0] == "R":
        zeros += (position + rotation) // 100
        position = (position + rotation) % 100
    else:
        position = 100 if position == 0 else position
        zeros += abs((position - rotation) // 100)
        position = (position - rotation) % 100
        zeros += position == 0

print("Puzzle 2 =", zeros)
