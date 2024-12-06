path = "AdventOfCode2019/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    numbers = []
    for line in raw_data:
        numbers.append(int(line.strip()))

# Puzzle 1
result = 0
for num in numbers:
    result += num // 3 - 2
print("Puzzle 1 =", result)


#Puzzle 2
result = 0
for num in numbers:
    while True:
        fuel = max(num // 3 - 2, 0)
        result += fuel
        if not fuel:
            break
        num = fuel
        
print("Puzzle 2 =", result)
