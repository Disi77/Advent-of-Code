path = "AdventOfCode2017/day06/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    banks_start = [int(num) for num in raw_data.read().split("\t")]

steps = 0
banks = banks_start.copy()
seen_states = {}
state_string = " ".join([str(i) for i in banks])
seen_states[state_string] = steps

while True:
    steps += 1
    blocks = max(banks)
    i = banks.index(blocks)
    banks[i] = 0
    while blocks:
        i = (i + 1) % len(banks)
        banks[i] += 1
        blocks -=1

    state_string = " ".join([str(i) for i in banks])
    if state_string in seen_states:
        result = steps - seen_states[state_string]
        break
    seen_states[state_string] = steps

print("Puzzle 1 =", steps)
print("Puzzle 2 =", result)
