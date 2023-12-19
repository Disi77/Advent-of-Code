from termcolor import colored


def print_trench(borders):
    for y in range(Y_MIN, Y_MAX + 1):
        for x in range(X_MIN, X_MAX + 1):
            if (x, y) in borders:
                print(colored("#", "yellow"), end=" ")
            elif is_inside(x, y, borders) and (x, y) not in borders:
                print(colored(".", "cyan"), end=" ")
            else:
                print(colored(".", "white"), end=" ")
        print()
    print()


def count_trench_capacity(borders):
    result = len(borders)
    for y in range(Y_MIN, Y_MAX + 1):
        for x in range(X_MIN, X_MAX + 1):
            if is_inside(x, y, borders) and (x, y) not in borders:
                result += 1
    return result


def is_inside(x0, y0, borders):
    left = 0
    right = 0
    for x1 in range(X_MIN, X_MAX + 1):
        if (x1, y0) in borders and (x1, y0+1) in borders:
            if x1 > x0:
                right += 1
            if x1 < x0:
                left += 1
    return left % 2 != 0 and right % 2 != 0


def get_borders_coor(dig_plan):
    directions = {"L": (-1, 0), "U": (0, -1), "R": (1, 0),  "D": (0, 1)}
    borders = set()
    x0, y0 = (0, 0)
    borders.add((x0, y0))
    for record in dig_plan:
        dir, number, _ = record.split()
        number = int(number)
        dx, dy = directions[dir]
        for koef in range(1, number + 1):
            x1, y1 = (dx * koef) + x0,  (dy * koef) + y0
            borders.add((x1, y1))
        x0, y0 = x1, y1
    return borders


path = "AdventOfCode2023/day18/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    dig_plan = []
    for line in raw_data:
        dig_plan.append(line.strip())

# Puzzle 1
borders = get_borders_coor(dig_plan)

X_MIN, Y_MIN = 0, 0
X_MAX, Y_MAX = 0, 0
for (x, y) in borders:
    if x > X_MAX:
        X_MAX = x
    if x < X_MIN:
        X_MIN = x
    if y > Y_MAX:
        Y_MAX = y
    if y < Y_MIN:
        Y_MIN = y

      
result = count_trench_capacity(borders)
print("Puzzle 1 =", result)
# print_trench(borders)
