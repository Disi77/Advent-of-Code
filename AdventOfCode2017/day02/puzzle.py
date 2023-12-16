from itertools import combinations

path = "AdventOfCode2017/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append([int(x) for x in line.strip().split("\t")])


# Puzzle 1
result = 0
for numbers in data:
    result += max(numbers) - min(numbers)
    
print("Puzzle 1 =", result)


#Puzzle 2
result = 0
for numbers in data:
    for num1, num2 in combinations(numbers, 2):
        if num1 % num2 == 0:
            result += num1 // num2
        if num2 % num1 == 0:
            result += num2 // num1

print("Puzzle 2 =", result)
