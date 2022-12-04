import re


class Instruction:
    def __init__(self, type, fromX, fromY, toX, toY):
        self.type = type
        self.fromX = int(fromX)
        self.fromY = int(fromY)
        self.toX = int(toX)
        self.toY = int(toY)


path = "AdventOfCode2015/day06/input.txt"
instructions = []
pattern = r"^(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$"

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        line = line.strip()
        result = re.match(pattern, line).groups()
        instructions.append(Instruction(*result))

lights_on = set()

for i in instructions:
    if i.type == "turn on":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                lights_on.add((x, y))
    elif i.type == "turn off":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                if (x, y) in lights_on:
                    lights_on.remove((x, y))
    elif i.type == "toggle":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                if (x, y) in lights_on:
                    lights_on.remove((x, y))
                else:
                    lights_on.add((x, y))

print("Puzzle 1 =", len(lights_on))
