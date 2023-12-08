from functools import reduce
from itertools import cycle
from math import gcd
from re import findall


path = "AdventOfCode2023/day08/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

pattern = r"\b([A-Z0-9]+)\b"
nodes = {}

for line in data.split("\n\n")[1].split("\n"):
    node, node_left, node_right = findall(pattern, line)
    nodes[node] = [node_left, node_right]

instructions = data.split("\n\n")[0]
pointers = []
for node in nodes:
    if node.endswith("A"):
        pointers.append(node)

steps = 0
steps_for_pointers = [0] * len(pointers)

for i in cycle(instructions):
    steps += 1
    for p, pointer in enumerate(pointers):
        if i == "L":
            pointers[p] = nodes[pointer][0]
        elif i == "R":
            pointers[p] = nodes[pointer][1]
        if pointers[p].endswith("Z") and not steps_for_pointers[p]:
            steps_for_pointers[p] = steps
    if not 0 in steps_for_pointers:
        break

result = reduce(lambda a, b: abs(a * b) // gcd(a, b), steps_for_pointers)

print("Puzzle 2 =", result)
