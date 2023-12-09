def get_last_number(numbers):
    if sum(numbers) == 0:
        return 0
    temp = []
    for i in range(1, len(numbers)):
        temp.append(numbers[i] - numbers[i - 1])
    a = get_last_number(temp)
    temp.append(temp[-1] + a)
    return temp[-1]


path = "AdventOfCode2023/day09/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        numbers = [int(x) for x in line.split()]
        data.append(numbers)

result = 0
for numbers in data:
    a = get_last_number(numbers)
    result += numbers[-1] + a
    
print("Puzzle 1 =", result)
