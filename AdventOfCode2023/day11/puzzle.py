from termcolor import colored
from itertools import combinations


def print_space(galaxies):
    sx, sy = 0, 0
    for (gx, gy) in galaxies:
        if gx > sx:
            sx = gx
        if gy > sy:
            sy = gy
    for y in range(sy + 1):
        for x in range(sx + 1):
            if (x, y) in galaxies:
                print(colored("#", "yellow"), end="")
            else:
                print(".", end="")
        print()
    print()


def expand_space(galaxies, size):
    size_diff = size - 1
    # expand galaxy x axis
    galaxies_list = list(galaxies)
    galaxies_list.sort()
    index = 0
    while True:
        for (gx, gy) in galaxies_list:
            if gx == index:
                break
        else:
            for gi, (gx, gy) in enumerate(galaxies_list):
                if gx > index:
                    galaxies_list[gi] = (gx + size_diff, gy)
            index += size_diff

        index += 1
        if index == galaxies_list[-1][0]:
            break

    # expand galaxy y axis
    galaxies_list.sort(key=lambda x: x[1])
    index = 0
    while True:
        for (gx, gy) in galaxies_list:
            if gy == index:
                break
        else:
            for gi, (gx, gy) in enumerate(galaxies_list):
                if gy > index:
                    galaxies_list[gi] = (gx, gy + size_diff)
            index += size_diff

        index += 1
        if index == galaxies_list[-1][1]:
            break

    return set(galaxies_list)


path = "AdventOfCode2023/day11/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    galaxies = set()
    for y, line in enumerate(raw_data):
        for x, char in enumerate(line.strip()):
            if char == "#":
                galaxies.add((x, y))
    space_size = (x + 1, y + 1)


# Puzzle 1
galaxies_after_expand = expand_space(galaxies, 2)
result = 0
for (x0, y0), (x1, y1) in list(combinations(galaxies_after_expand, 2)):
    result += abs(x0 - x1) + abs(y0 - y1)
    
print("Puzzle 1 =", result)


#Puzzle 2
galaxies_after_expand = expand_space(galaxies, 10**6)
result = 0
for (x0, y0), (x1, y1) in list(combinations(galaxies_after_expand, 2)):
    result += abs(x0 - x1) + abs(y0 - y1)

print("Puzzle 2 =", result)
