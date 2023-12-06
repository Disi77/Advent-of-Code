import re
from time import time
from math import sqrt


pattern = r'\b\d+\b'

path = "AdventOfCode2023/day06/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

# Puzzle 1
times = [int(x) for x in re.findall(pattern, data.split("\n")[0])]
distances = [int(x) for x in re.findall(pattern, data.split("\n")[1])]

result = 1
for i in range(len(times)):
    race_time = times[i]
    record = distances[i]

    win = 0
    for t in range(1, race_time + 1):
        race_distance = (race_time - t) * t
        if record < race_distance:
            win += 1
    result *= win

print("Puzzle 1 =", result)


#Puzzle 2
race_time = int("".join(re.findall(pattern, data.split("\n")[0])))
record = int("".join(re.findall(pattern, data.split("\n")[1])))

start = time()
win = 0
for t in range(1, race_time + 1):
    race_distance = (race_time - t) * t
    if record < race_distance:
        win += 1

print("\nPuzzle 2 solved via brutal force =", win)
print(f"Solved in {round(time() - start, 5)} seconds")

# Puzzle 2 can by solved by math too !
# you can use the quadratic equation
#     record < (race_time - t) * t
#     0 < -t^2 + race_time * t - record
#     0 = a * x^2 + b * x + c
start = time()
discriminant = sqrt(race_time ** 2 - 4 * record)
root1 = (- race_time + discriminant) / 2
root2 = (- race_time - discriminant) / 2

print("\nPuzzle 2 solved via math =", int(root1) - int(root2))
print(f"Solved in {round(time() - start, 5)} seconds")
