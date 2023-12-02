from collections import Counter
from functools import reduce

path = "AdventOfCode2016/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 2
alphabet = "abcdefghijklmnopqrstuvwxyz"

for room in data:
    letters = reduce(lambda a, b: a + b, room.split("-")[:-1])
    room_name = " ".join(room.split("-")[:-1])
    id = int(room.split("-")[-1][:-7])
    checksum = room.split("-")[-1][-6:-1]

    rooms = Counter(letters)
    ordered_rooms = sorted(rooms.items(), key=lambda x: (-x[1], x[0]))
    five_most_common = "".join([x[0] for x in ordered_rooms[:5]])
    if checksum != five_most_common:
        continue
    
    real_room_name = ""
    for char in room_name:
        if char == " ":
            continue
        index = alphabet.index(char)
        new_index = (index + id) % 26
        real_room_name += alphabet[new_index]
    
    if "northpole" in real_room_name:
        north_pole_room = real_room_name, id
        break

print("Puzzle 2 =", north_pole_room)
