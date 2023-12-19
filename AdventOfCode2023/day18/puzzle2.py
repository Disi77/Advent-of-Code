# Puzzle 2 solved using Shoelace Formula https://en.wikipedia.org/wiki/Shoelace_formula

path = "AdventOfCode2023/day18/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    dig_plan = []
    for line in raw_data:
        dig_plan.append(line.strip())

corners = [(0, 0)]
perimeter = 0
directions = {"0": "R", "1": "D", "2": "L", "3": "U"}
for record in dig_plan:
    _, _, instruction = record.split()
    instruction = instruction[2:-1]
    distance = int(instruction[:-1], base=16)
    direction = directions[instruction[5]]
    perimeter += distance
    x, y = corners[-1]
    if direction == "R":
        x += distance
    elif direction == "L":
        x -= distance
    elif direction == "U":
        y -= distance
    elif direction == "D":
        y += distance
    corners.append((x, y))


# Source of Shoelace Formula implementation: https://stackoverflow.com/a/66046814
class Polygon:
    def __init__(self, arr):
        self.arr = arr

    def area(self):
        total = 0
        i = 0
        while i != len(self.arr) - 1:
            total += self.arr[i][0] * self.arr[i + 1][1]
            total -= self.arr[i + 1][0] * self.arr[i][1]
            i += 1
        return (
            abs(
                total
                + self.arr[-1][0] * self.arr[0][1]
                - self.arr[-1][-1] * self.arr[0][0]
            )
            / 2
        )


a = Polygon(corners)
result = round(a.area() + 1 + perimeter / 2)
print("Puzzle 2 =", result)
