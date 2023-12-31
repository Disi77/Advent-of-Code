path = "AdventOfCode2023/day24/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    hailstones = []
    for line in raw_data:
        part1, part2 = line.strip().split(" @ ")
        x, y, _ = [int(x) for x in part1.split(", ")]
        dx, dy, _ = [int(x) for x in part2.split(", ")]
        # y = k * x + q  =>  q = y - k * x
        # y + dy = k * (x + dx) + q
        # y + dy = k * (x + dx) + y - k * x
        # -----------
        # dy = k * dx
        # k = dy / dx
        K = dy / dx
        Q = y - K * x
        hailstones.append((K, Q, x, y, dx, dy))

MIN = 200000000000000
MAX = 400000000000000

intersections = 0
for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        k1, q1, x1, y1, dx1, dy1 = hailstones[i]
        k2, q2, x2, y2, dx2, dy2 = hailstones[j]
        # y = k1 * x + q1
        # y = k2 * x + q2
        # ---------------
        # k1 * x + q1 = k2 * x + q2
        # x * (k1 - k2) = q2 - q1
        # x = (q2 - q1) / (k1 - k2)
        if k1 == k2:
            # print("Hailstones' paths are parallel; they never intersect.")
            continue

        X = (q2 - q1) / (k1 - k2)
        Y = k1 * X + q1

        if (X < x1 and dx1==abs(dx1) or X > x1 and dx1!=abs(dx1)) and (X < x2 and dx2==abs(dx2) or X > x2 and dx2!=abs(dx2)):
            # print("Hailstones' paths crossed in the past for both hailstones.")
            continue
        elif X < x1 and dx1==abs(dx1) or X > x1 and dx1!=abs(dx1):
            # print("Hailstones' paths crossed in the past for hailstone 1.")
            continue
        elif X < x2 and dx2==abs(dx2) or X > x2 and dx2!=abs(dx2):
            # print("Hailstones' paths crossed in the past for hailstone 2.")
            continue
        elif MIN <= X <= MAX and MIN <= Y <= MAX:
            # print(f"Hailstones' paths will cross INSIDE the test area (at x={round(X, 3)}), y={round(Y, 3)}")
            intersections += 1
        else:
            # print(f"Hailstones' paths will cross outside the test area (at x={round(X, 3)}), y={round(Y, 3)}")
            continue

print("Puzzle 1 =", intersections)
