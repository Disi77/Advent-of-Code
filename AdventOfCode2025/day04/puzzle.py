path = "AdventOfCode2025/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    empty = set()
    for i, line in enumerate(raw_data):
        for j, char in enumerate(line.strip()):
            if char == ".":
                empty.add((i, j))
    SIZE = i + 1, j + 1


def get_coors_around(coor):
    i, j = coor
    coors_around = set()
    for i_coor in range(i - 1, i + 2):
        for j_coor in range(j - 1, j + 2):
            if i_coor < 0 or j_coor < 0:
                continue
            if i_coor >= SIZE[0] or j_coor >= SIZE[1]:
                continue
            if i_coor == i and j_coor == j:
                continue
            coors_around.add((i_coor, j_coor))
    return coors_around


def less_than_four_rolls_around(coor):
    rolls = 0
    for (i, j) in get_coors_around(coor):
        if (i, j) not in empty:
            rolls += 1
            if rolls >= 4:
                return False
    return True


removable_rolls = 0
while True:
    forklifts = set()
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            coor = i, j
            if coor in empty:
                continue
            if less_than_four_rolls_around(coor):
                forklifts.add(coor)
    if not removable_rolls:
        print("Puzzle 1 =", len(forklifts))
    for coor in forklifts:
        empty.add(coor)
    removable_rolls += len(forklifts)
    if not forklifts:
        break

print("Puzzle 2 =", removable_rolls)
