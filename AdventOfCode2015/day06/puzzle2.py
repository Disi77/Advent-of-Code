import re


class Instruction():
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

lights_on = {}

for i in instructions:
    if i.type == "turn on":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                if (x, y) in lights_on:
                    lights_on[(x, y)] += 1
                else:
                    lights_on[(x, y)] = 1
    elif i.type == "turn off":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                if (x, y) in lights_on:
                    lights_on[(x, y)] -= 1
                    if lights_on[(x, y)] == 0:
                        del lights_on[(x, y)]
    elif i.type == "toggle":
        for x in range(i.fromX, i.toX + 1):
            for y in range(i.fromY, i.toY + 1):
                if (x, y) in lights_on:
                    lights_on[(x, y)] += 2
                else:
                    lights_on[(x, y)] = 2

total_brightness = 0
for brightness in lights_on.values():
    total_brightness += brightness


print("Puzzle 2 =", total_brightness)
