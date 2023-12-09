from collections import Counter

path = "AdventOfCode2016/day06/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())


most_common = ""
least_common = ""

for i in range(len(data[0])):
    new_line = "".join([x[i] for x in data])
    result = Counter(new_line).most_common()
    most_common += result[0][0]
    least_common += result[-1][0]

print("Puzzle 1 =", most_common)
print("Puzzle 2 =", least_common)
