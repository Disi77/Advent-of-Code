path = "AdventOfCode2022/day01/input.txt"

supplies = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    elf = 0
    for line in raw_data:
        try:
            calories = int(line.strip())
            elf += calories
        except ValueError:
            supplies.append(elf)
            elf = 0
    supplies.append(elf)

supplies.sort(reverse=True)

# Puzzle 1
print(f"Puzzle 1 = {supplies[0]}")

# Puzzle 2
print(f"Puzzle 2 = {supplies[0] + supplies[1] + supplies[2]}")
