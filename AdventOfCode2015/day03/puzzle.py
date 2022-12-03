def move(instruction, x, y):
    if instruction == ">":
        x += 1
    elif instruction == "<":
        x += -1
    elif instruction == "^":
        y += 1
    elif instruction == "v":
        y += -1
    return x, y


path = "AdventOfCode2015/day03/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    instructions = raw_data.read()

visited_houses = [(0, 0)]
x, y = 0, 0
for i in instructions:
    x, y = move(i, x, y)
    if (x, y) not in visited_houses:
        visited_houses.append((x, y))

print("Puzzle 1 =", len(visited_houses))


visited_houses = [(0, 0)]
x1, y1 = 0, 0  # Santa's move
x2, y2 = 0, 0  # Robo-Santa's move
for round, i in enumerate(instructions):
    if round % 2 == 0:
        x1, y1 = move(i, x1, y1)
        if (x1, y1) not in visited_houses:
            visited_houses.append((x1, y1))
    else:
        x2, y2 = move(i, x2, y2)
        if (x2, y2) not in visited_houses:
            visited_houses.append((x2, y2))

print("Puzzle 2 =", len(visited_houses))