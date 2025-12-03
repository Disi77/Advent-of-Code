path = "AdventOfCode2025/day03/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    banks = [line.strip() for line in raw_data]

# Puzzle 1
joltage = 0
for bank in banks:
    batteries = [int(x) for x in bank]
    first_largest = max(batteries[:-1])
    first_index = batteries.index(first_largest)
    second_largest = max(batteries[first_index + 1 :])
    joltage += int(f"{first_largest}{second_largest}")

print("Puzzle 1 =", joltage)


# Puzzle 2
joltage = 0
batteries_on = 12
batteries_count = len(banks[0])
for bank in banks:
    batteries = [int(x) for x in bank]
    start_i = 0
    battery = ""
    for i in range(batteries_on):
        largest = max(batteries[start_i : batteries_count - batteries_on + 1 + i])
        start_i = batteries.index(largest, start_i) + 1
        battery += str(largest)
    joltage += int(battery)

print("Puzzle 2 =", joltage)
