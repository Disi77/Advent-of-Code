from re import findall


def overlap(c1, c2):
    x1, y1, dx1, dy1 = c1
    x2, y2, dx2, dy2 = c2
    if x1 + dx1 - 1 < x2 or x2 + dx2 - 1 < x1:
        return []
    if y1 + dy1 - 1 < y2 or y2 + dy2 - 1 < y1:
        return []
    x3_0 = x2 if x1 <= x2 else x1
    y3_0 = y2 if y1 <= y2 else y1
    x3_1 = x2 + dx2 - 1 if x1 + dx1 - 1 >= x2 + dx2 - 1 else x1 + dx1 - 1
    y3_1 = y2 + dy2 - 1 if y1 + dy1 - 1 >= y2 + dy2 - 1 else y1 + dy1 - 1

    return [x3_0, y3_0, x3_1 - x3_0 + 1, y3_1 - y3_0 + 1]


path = "AdventOfCode2018/day03/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(list(map(int, findall(r"\d+", line))))

repeated_inches = set()
for i, claim1 in enumerate(data):
    claims_overlap = False
    for j, claim2 in enumerate(data):
        if i == j:
            continue
        result = overlap(claim1[1:], claim2[1:])
        if result:
            claims_overlap = True
            break
    if not claims_overlap:
        break

print("Puzzle 2 =", claim1[0])
