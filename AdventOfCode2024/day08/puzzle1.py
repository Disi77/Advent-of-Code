from termcolor import colored
from itertools import combinations


path = "AdventOfCode2024/day08/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    antennas = {} # key: value  ->  (0, 1): "A"
    antennas_coor = {}  # key: value  ->  "A": [(0, 1), (0, 2) ...]
    for i, line in enumerate(raw_data):
        for j, char in enumerate(line.strip()):
            if char == ".":
                continue
            antennas[(i, j)] = char
            antennas_coor.setdefault(char, []).append((i, j))
    SIZE = (i + 1, j + 1)


def print_map(antennas, antinodes):
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if (i, j) in antennas and (i, j) in antinodes:
                print(colored(antennas[(i, j)], "blue"), end=" ")
            elif (i, j) in antennas:
                print(colored(antennas[(i, j)], "yellow"), end=" ")
            elif (i, j) in antinodes:
                print(colored("#", "blue"), end=" ")
            else:
                print(colored(".", "grey"), end=" ")
        print()
    print()


# Puzzle 1
def calculate_antinodes(n1, n2, SIZE):
    sx, sy = SIZE
    antinodes = set()
    x1, y1 = n1
    x2, y2 = n2
    xd, yd = x1 - x2, y1 - y2
    ax1, ay1 = x1 + xd, y1 + yd
    ax2, ay2 = x2 - xd, y2 - yd
    if 0 <= ax1 < sx and 0 <= ay1 < sy:
        antinodes.add((ax1, ay1))
    if 0 <= ax2 < sx and 0 <= ay2 < sy:
        antinodes.add((ax2, ay2))
    return antinodes

antinodes = set()

for antenna, nodes in antennas_coor.items():
    for n1, n2 in combinations(nodes, 2):
        for item in calculate_antinodes(n1, n2, SIZE):
            antinodes.add(item)
        # print_map(antennas, antinodes)
    
print("Puzzle 1 =", len(antinodes))
