import re
from itertools import cycle


path = "AdventOfCode2023/day08/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

pattern = r"\b([A-Z]+)\b"
nodes = {}

for line in data.split("\n\n")[1].split("\n"):
    node, node_left, node_right = re.findall(pattern, line)
    nodes[node] = [node_left, node_right]

instructions = data.split("\n\n")[0]
pointer = "AAA"
steps = 0

for i in cycle(instructions):
    steps += 1
    if i == "L":
        pointer = nodes[pointer][0] 
    elif i == "R":
        pointer = nodes[pointer][1]
    if pointer == "ZZZ":
        break

print("Puzzle 1 =", steps)
