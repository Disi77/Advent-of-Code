path = "AdventOfCode2017/day05/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    offsets = [int(num.strip()) for num in raw_data]

# Puzzle 1
steps = 0
pointer = 0
while True:
    new_pointer = offsets[pointer] + pointer
    steps += 1
    if new_pointer < 0 or new_pointer >= len(offsets):
        break
    offsets[pointer] += 1
    pointer = new_pointer

print("Puzzle 1 =", steps)

# Puzzle 2
with open(path, encoding="utf-8", mode="r") as raw_data:
    offsets = [int(num.strip()) for num in raw_data]

steps = 0
pointer = 0
while True:
    new_pointer = offsets[pointer] + pointer
    steps += 1
    if new_pointer < 0 or new_pointer >= len(offsets):
        break
    if offsets[pointer] >= 3:
        offsets[pointer] -= 1
    else:
        offsets[pointer] += 1
    pointer = new_pointer

print("Puzzle 2 =", steps)
