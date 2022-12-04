import re


path = "AdventOfCode2022/day04/input.txt"
section_assignments = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        section_assignments.append(line.strip())

puzzle1_result = 0
puzzle2_result = 0
pattern = r"^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$"

for pair in section_assignments:
    e1_from, e1_to, e2_from, e2_to = re.match(pattern, pair).groups()
    E1 = set(range(int(e1_from), int(e1_to) + 1))
    E2 = set(range(int(e2_from), int(e2_to) + 1))
    if not E1.difference(E2) or not E2.difference(E1):
        puzzle1_result += 1
    if E1.intersection(E2):
        puzzle2_result += 1


print("Puzzle 1 =", puzzle1_result)
print("Puzzle 2 =", puzzle2_result)
