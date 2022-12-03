def find_item_in_both(rucksack):
    first = rucksack[: int(len(rucksack) / 2)]
    second = rucksack[int(len(rucksack) / 2):]
    for i in first:
        for j in second:
            if i == j:
                return i


def get_item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 65 + 27


def item_in_all3(rucksacks, index):
    first = rucksacks[index]
    second = rucksacks[index + 1]
    third = rucksacks[index + 2]
    for i in first:
        for j in second:
            for k in third:
                if i == j == k:
                    return i


path = "AdventOfCode2022/day03/input.txt"

rucksacks = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        rucksacks.append(line.strip())

# Puzzle 1
prio_sum = 0
for r in rucksacks:
    item_in_both = find_item_in_both(r)
    prio_sum += get_item_priority(item_in_both)

print("Puzzle 1 =", prio_sum)

# Puzzle 2
prio_sum = 0
i = 0
while i < len(rucksacks):
    item_in_all = item_in_all3(rucksacks, i)
    prio_sum += get_item_priority(item_in_all)
    i += 3

print("Puzzle 2 =", prio_sum)
