def find_new_z(bricks, brick):
    (sx0, sy0, new_z, sx1, sy1, _) = brick
    while True:
        if new_z == 1:
            return new_z
        for (x0, y0, z0, x1, y1, z1) in bricks:
            if z0 <= new_z - 1 <= z1:
                if not (y1 < sy0 or sy1 < y0) and not (x1 < sx0 or sx1 < x0):
                    return new_z
        else:
            new_z -= 1


def bricks_fall(bricks, from_index, mode="fall"):
    bricks_fall = set()
    while True:
        change = False
        for index in range(from_index, len(bricks)):
            (x0, y0, z0, x1, y1, z1) = bricks[index]
            if z0 == 1:
                continue
            new_z = find_new_z(bricks, (x0, y0, z0, x1, y1, z1))
            if new_z != z0:
                diff = z0 - new_z
                bricks[index] = (x0, y0, z0 - diff, x1, y1, z1 - diff)
                change = True
                if mode == "disintegrate":
                    bricks_fall.add(index)
        if not change:
            break
    return bricks, len(bricks_fall)


path = "AdventOfCode2023/day22/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    bricks = []
    for line in raw_data:
        start, end = line.strip().split("~")
        x0, y0, z0 = [int(x) for x in start.split(",")]
        x1, y1, z1 = [int(x) for x in end.split(",")]
        bricks.append((x0, y0, z0, x1, y1, z1))
        bricks = sorted(bricks, key=lambda x: x[2])

# Puzzle 2
bricks, _ = bricks_fall(bricks.copy(), 0)

final_sum = 0
for index, brick in enumerate(bricks):
    bricks_new = bricks.copy()
    bricks_new.pop(index)
    _, result = bricks_fall(bricks_new, index, mode="disintegrate")
    if result:
        final_sum += result

print("Puzzle 2 =", final_sum)
