with open("day03_input.txt", encoding="utf-8", mode="r") as f:
    map = [x.strip() for x in f.readlines()]

trees = 0
i = 0
l_r = len(map[0])  # len of 1 row in input
for line in map:
    if line[i] == "#":
        trees += 1
    if (i + 3) >= l_r:
        i = i + 3 - l_r
    else:
        i += 3

print(trees)
