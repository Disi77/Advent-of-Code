def find_item_in_halfs(rucksack):
    A = set(rucksack[: int(len(rucksack) / 2)])
    B = set(rucksack[int(len(rucksack) / 2):])
    return list(A.intersection(B))[0]


def item_in_all3(rucksacks, index):
    A = set(rucksacks[index])
    B = set(rucksacks[index + 1])
    C = set(rucksacks[index + 2])
    return list(A.intersection(B, C))[0]


def get_item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 65 + 27


path = "AdventOfCode2022/day03/input.txt"

rucksacks = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        rucksacks.append(line.strip())

# Puzzle 1
prio_sum = 0
for r in rucksacks:
    item_in_both = find_item_in_halfs(r)
    prio_sum += get_item_priority(item_in_both)

print("Puzzle 1 =", prio_sum)

# Puzzle 2
prio_sum = 0
i = 0
for i in range(0, len(rucksacks), 3):
    item_in_all = item_in_all3(rucksacks, i)
    prio_sum += get_item_priority(item_in_all)

print("Puzzle 2 =", prio_sum)
