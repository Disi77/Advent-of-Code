path = "AdventOfCode2023/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 1
result = 0
for line in data:
    for char in line:
        if char.isdigit():
            number = char
            break
    for char in line[::-1]:
        if char.isdigit():
            number += char
            break
    result += int(number)
    
print("Puzzle 1 =", result)


#Puzzle 2
digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

result = 0
for line in data:
    # create a list with tuples (index, digit), where index is position of digit in the input
    numbers = []
    for i, digit in enumerate(digits):
        start = 0
        while True:
            index = line.find(digit, start)
            if index == -1:
                break
            numbers.append((index, str(i + 1)))
            start = index + 1

    for i, char in enumerate(line):
        if char.isdigit():
            numbers.append((i, char))
            break

    for i in range(len(line) - 1, -1, -1):
        char = line[i]
        if char.isdigit():
            numbers.append((i, char))
            break

    numbers.sort()
    number = numbers[0][1] + numbers[-1][1]
    result += int(number)

print("Puzzle 2 =", result)
