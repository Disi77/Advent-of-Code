from math import factorial


# Puzzle 2
puzzle_input = 36_000_000
house = factorial(5)

for num in range(house, puzzle_input, house):
    presents = 0
    for elf in range(1, num + 1):
        if num % elf == 0 and elf * 50 >= num:
            presents += elf * 11
    if presents >= puzzle_input:
        break

print("Puzzle 2 =", num)
