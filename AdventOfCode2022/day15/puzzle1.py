from pathlib import Path
from re import match
from itertools import combinations


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text().split("\n")
pattern = r"Sensor at x=(-?\d+), y=(-?\w+): closest beacon is at x=(-?\d+), y=(-?\d+)"

sensors = []
for i in instructions:
    sx, sy, bx, by = match(pattern, i).groups()
    sensors.append((int(sx), int(sy), int(bx), int(by)))

row = 2_000_000
pos_without_beacon = set()
for sx, sy, bx, by in sensors:
    manhattan = abs(sx - bx) + abs(sy - by)
    y_distance = abs(row - sy)
    if y_distance <= manhattan:
        diff = manhattan - y_distance
        for x in range(sx - diff, sx + diff + 1):
            if (x, row) == (bx, by):
                continue
            pos_without_beacon.add(x)
        
print("Puzzle 1 =", len(pos_without_beacon))