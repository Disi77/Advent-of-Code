from pathlib import Path
from re import match
from itertools import combinations


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text().split("\n")
pattern = r"Sensor at x=(-?\d+), y=(-?\w+): closest beacon is at x=(-?\d+), y=(-?\d+)"

sensors = []
for i in instructions:
    sx, sy, bx, by = match(pattern, i).groups()
    manhattan = abs(int(sx) - int(bx)) + abs(int(sy) - int(by))
    sensors.append((int(sx), int(sy), manhattan))

# Searched point coors = intersection of lines
# line equation y = ax + b
# line is between 2 diamonds where adjacent edges are 2 apart

#    - -                     1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2
#    2 1 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#  0 . . . . . \ . . # . . . # . . . . . . . . . . . . . . / 
#  1 . . . . . . \ # . . . . . # . . . . . . . . . . . . / .
#  2 . . . . . . # \ . . . . . . # . . . # . . . . . . / . .
#  3 . . . . . # . . \ . . . . . . # . # . # . . . . / . . .
#  4 . . . . # . . . . \ . . . . . . # . . . # . . / . . . .
#  5 . . . # . . . . . . \ . . . . # . # . . . # / . . . . .
#  6 . . # . . . . . . . . \ . . # . . . # . . / # . . . . .
#  7 . # . . . . . . . . S . \ # . . . . S # / # . # . . . .
#  8 . . # . . . . . . . . . . \ # . . . # / # . # . # . . .
#  9 . . . # . . . . . . . . . . \ # . # / # . # . . . # . .
# 10 . . . . # . . . . . . . . . # \ # / # . # . . . . . # .
# 11 . . . . . # . . . . . . . # . # x # . # . . . . . . . #
# 12 . . . . . . # . . . . . # . # / # \ # . . . . . . . . .
# 13 . . . . . . . # . . . # . # / # . # \ . . . . . . . . .
# 14 . . . . . . . . # . # . # / S . . . # \ . . S . . . . .
# 15 . . . . . . . . . # . # / . . # . # . . \ . . . . . . .
# 16 . . . . . . . . . . # / # . . . # . . . . \ . . . . . .
# 17 . . . . . . . . . . / . . # . # . # . . . . \ . . . . #
# 18 . . . . . . . . . / . . . . # . . . # . . . . \ . . # .
# 19 . . . . . . . . / . . . . . . . . . . # . . . . \ # . .
# 20 . . . . . . . / . . . . . . . . . . . . # . . . # \ . .
# 21 . . . . . . / . . . . . . . . . . . . . . # . # . . \ .
# 22 . . . . . / . . . . . . . . . . . . . . . . # . . . . \


line_params = set()  # line params (a, b)  ->  y = ax + b

# try to find 2 sensors with 1 size gap between them 
for d0, d1 in combinations(sensors, 2):
    if d0[0] > d1[0]:  # compare 2 sensors and everytime on the left is the one with smaller X coor
        d0, d1 = d1, d0

    sx0, sy0, m0 = d0
    sx1, sy1, m1 = d1

    # Find couples where line direction is /
    ax, ay = sx0, sy0 + m0  # left sensor/diamond, bottom corner
    bx, by = sx1, sy1 - m1  # right sensor/diamond, top corner
    new_ax = ax + (ay - by)   
    if bx - new_ax == 2:
        B = - 1 * (sx0 + 1) + sy0 + m0
        line_params.add((-1, B))

    # Find couples where line direction is \
    ax, ay = sx0, sy0 - m0  # left sensor/diamond, top corner
    bx, by = sx1, sy1 + m1  # right sensor/diamond, bottom corner
    new_bx = bx - (by - ay)
    if new_bx - ax == 2:
        B = - 1 * (sx1 - 1) + sy1 + m1
        line_params.add((1, B))


beacon = []  # here is a list because test data contains more than 1 + 1 lines
for c in combinations(line_params, 2):
    line1, line2 = c
    a1, b1 = line1
    a2, b2 = line2
    if a1 == a2:
        continue
    # find 2 lines intersection
    x = (b2 - b1) // (a1 - a2)
    y = a1 * x + b1
    beacon.append((x, y))

print("Puzzle 2 =", beacon[0][0] * 4_000_000 + beacon[0][1])
