import re


def calculate_quadrant(x, y):
    # +-------+-------+
    # |       |       |
    # |   1   |   2   |
    # |       |       |
    # +-------+-------+
    # |       |       |
    # |   3   |   4   |
    # |       |       |
    # +-------+-------+
    if x == (X // 2) or y == (Y // 2):
        return 0
    
    if x < (X // 2):
        if y < (Y // 2):
            return 1
        return 2
    
    else:
        if y < (Y // 2):
            return 3
        return 4


path = "AdventOfCode2024/day14/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    robots = []
    for line in raw_data:
        robot = [int(x) for x in re.findall("[-]{0,1}\d+", line.strip())]
        robots.append(robot)

# Puzzle 1
robots_in_quadrant = {1: 0, 2: 0, 3: 0, 4: 0}
X, Y = 103, 101
new_robots = []
for robot in robots:
    y0, x0, dy, dx = robot
    x1 = (100 * dx + x0) % X
    y1 = (100 * dy + y0) % Y

    quadrant = calculate_quadrant(x1, y1)
    if quadrant:
        robots_in_quadrant[quadrant] += 1

result = 1
for v in robots_in_quadrant.values():
    result *= v

print("Puzzle 1 =", result)
