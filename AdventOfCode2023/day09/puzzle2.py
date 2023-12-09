def get_previous_number(numbers):
    if sum(numbers) == 0:
        return 0
    temp = []
    for i in range(1, len(numbers)):
        temp.append(numbers[i] - numbers[i - 1])
    a = get_previous_number(temp)
    temp.insert(0, temp[0] - a)
    return temp[0]


path = "AdventOfCode2023/day09/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        numbers = [int(x) for x in line.split()]
        data.append(numbers)

result = 0
for numbers in data:
    a = get_previous_number(numbers)
    result += numbers[0] - a
    
print("Puzzle 2 =", result)
