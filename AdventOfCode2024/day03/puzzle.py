import re


path = "AdventOfCode2024/day03/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    memory = raw_data.read()

# Puzzle 1
result = 0
pattern = "mul\(\d{1,3},\d{1,3}\)"
for item in re.findall(pattern, memory):
    n1, n2 = item[4:-1].split(",")
    result += int(n1) * int(n2)
print("Puzzle 1 =", result)


#Puzzle 2
result = 0
do = True
pattern = "mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
for item in re.findall(pattern, memory):
    if item == "do()":
        do = True
    elif item == "don't()":
        do = False
    else:
        if not do:
            continue
        n1, n2 = item[4:-1].split(",")
        result += int(n1) * int(n2)
print("Puzzle 2 =", result)
