from functools import reduce
from itertools import product

path = "AdventOfCode2024/day07/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    equations = []
    for line in raw_data:
        equations.append(line.strip())

# Puzzle 2
total_calibration_result = 0
for e in equations:
    result, rest = e.split(": ")
    result = int(result)
    numbers = [int(x) for x in rest.split()]
    for combination in product("+*|", repeat=len(numbers) - 1):
        equation_result = numbers[0]
        for i, operator in enumerate(combination):
            if operator == "+":
                equation_result += numbers[i + 1]
            elif operator == "*":
                equation_result *= numbers[i + 1]
            else:
                equation_result = int(str(equation_result) + str(numbers[i + 1]))
        if equation_result == result:
            total_calibration_result += result
            break

print("Puzzle 2 =", total_calibration_result)
