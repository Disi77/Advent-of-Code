from itertools import product
from collections import Counter


path = "AdventOfCode2015/day17/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    containers = []
    for line in raw_data:
        containers.append(int(line.strip()))

# Puzzle 1
eggnog = 150
combinations = product([0, 1], repeat=len(containers))
result = 0
possible_combinations = []

for c in combinations:
    capacity = 0
    for i, container in enumerate(containers):
        capacity += container * c[i]
    if capacity == eggnog:
        possible_combinations.append(c)
        result += 1

print("Puzzle 1 =", result)


#Puzzle 2
counter = Counter([sum(x) for x in possible_combinations])
result = sorted(list(counter.items()))

print("Puzzle 2 =", result[0][1])
