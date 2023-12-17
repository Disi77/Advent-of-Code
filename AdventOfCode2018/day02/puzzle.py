from collections import Counter

path = "AdventOfCode2018/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 1
boxes2 = 0
boxes3 = 0
for box in data:
    for v in Counter(box).values():
        if v == 2:
            boxes2 += 1
            break
    for v in Counter(box).values():
        if v == 3:
            boxes3 += 1
            break

print("Puzzle 1 =", boxes2 * boxes3)


#Puzzle 2
def find_correct_box(data):
    for box1 in data:
        for box2 in data:
            diff = 0
            for i, letter in enumerate(box1):
                if letter != box2[i]:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                return box1, box2

box1, box2 = find_correct_box(data)

final_id = ""
for i, letter in enumerate(box1):
    if letter == box2[i]:
        final_id += letter

print("Puzzle 2 =", final_id)
