path = "AdventOfCode2022/day06/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read().strip()

for i in range(len(data)):
    if len(set(data[i : i + 4])) == 4:
        result = i + 4
        break

print("Puzzle 1 =", result)

for i in range(len(data)):
    if len(set(data[i : i + 14])) == 14:
        result = i + 14
        break

print("Puzzle 2 =", result)
