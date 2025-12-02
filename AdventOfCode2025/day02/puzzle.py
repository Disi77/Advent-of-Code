path = "AdventOfCode2025/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    ids = []
    for item in raw_data.read().split(","):
        ids.append([int(i) for i in item.split("-")])
        

# Puzzle 1
result = 0
for start, end in ids:
    for num in range(start, end + 1):
        lenght = len(str(num))
        if lenght % 2 != 0:
            continue
        first = str(num)[:lenght // 2]
        second = str(num)[lenght // 2 :]
        if first == second:
            result += int(first + second)

print("Puzzle 1 =", result)


# Puzzle 2
result = set()
for start, end in ids:
    for num in range(start, end + 1):
        lenght = len(str(num))
        if lenght < 2:
            continue
        for size in range(1, lenght // 2 + 1):
            if lenght % size:
                continue
            chunks = [
                str(num)[i : i + size] for i in range(0, lenght, size)
            ]
            if len(set(chunks)) == 1:
                result.add(num)

print("Puzzle 2 =", sum(result))
