import re
path = "AdventOfCode2024/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 1
pattern = "XMAS"
size = len(data)
count = 0

# rows
for row in data:
    count += len(re.findall(pattern, row))
    count += len(re.findall(pattern, row[::-1]))

# cols
for i in range(size):
    col = "".join(item[i] for item in data)
    count += len(re.findall(pattern, col))
    count += len(re.findall(pattern, col[::-1]))

# diag up + right
for i in range(3, size):
    for j in range(size - 3):
        diag = data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3]
        count += len(re.findall(pattern, diag))
        count += len(re.findall(pattern, diag[::-1]))

# diag down + right
for i in range(size - 3):
    for j in range(size - 3):
        diag = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        count += len(re.findall(pattern, diag))
        count += len(re.findall(pattern, diag[::-1]))
    
print("Puzzle 1 =", count)


#Puzzle 2
count = 0
for i in range(1, size - 1):
    for j in range(1, size - 1):
        if data[i][j] != "A":
            continue
        if data[i - 1][j - 1] + data[i + 1][j + 1] not in ["MS", "SM"]:
            continue
        if data[i + 1][j - 1] + data[i - 1][j + 1] not in ["MS", "SM"]:
            continue
        count += 1

print("Puzzle 2 =", count)
