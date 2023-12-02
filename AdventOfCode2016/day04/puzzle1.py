from collections import Counter
from functools import reduce


path = "AdventOfCode2016/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 1
sum_ids = 0
for room in data:
    letters = reduce(lambda a, b: a + b, room.split("-")[:-1])
    id = int(room.split("-")[-1][:-7])
    checksum = room.split("-")[-1][-6:-1]

    rooms = Counter(letters)
    ordered_rooms = sorted(rooms.items(), key=lambda x: (-x[1], x[0]))
    five_most_common = "".join([x[0] for x in ordered_rooms[:5]])
    if checksum == five_most_common:
        sum_ids += id

print("Puzzle 1 =", sum_ids)
