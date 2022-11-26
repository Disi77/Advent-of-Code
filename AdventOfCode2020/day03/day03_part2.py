import math

with open("day03_input.txt", encoding="utf-8", mode="r") as f:
    map = [x.strip() for x in f.readlines()]

trees = []
slopes = [{"→": 1, "↓": 1},
          {"→": 3, "↓": 1},
          {"→": 5, "↓": 1},
          {"→": 7, "↓": 1},
          {"→": 1, "↓": 2}]

l_r = len(map[0])  # len of 1 row in input

for s in slopes:
    trees_in_s = 0
    i = 0
    for line in map[::s["↓"]]:
        if line[i] == "#":
            trees_in_s += 1
        if (i + s["→"]) >= l_r:
            i = i + s["→"] - l_r
        else:
            i += s["→"]
    trees.append(trees_in_s)

print(trees)
print(math.prod(trees))
