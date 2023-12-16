path = "AdventOfCode2017/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = [int(x) for x in raw_data.read()]


# Puzzle 1
result = 0
for i, num in enumerate(data):
    if i == 0:
        if num == data[-1]:
            result += num
    else:
        if num == data[i - 1]:
            result += num
    
print("Puzzle 1 =", result)


#Puzzle 2
halfway = len(data) // 2
result = 0
for i, num in enumerate(data):
    second_index = (i + halfway) % len(data)
    if num == data[second_index]:
        result += num

print("Puzzle 2 =", result)
