import re
from sympy import symbols, Eq, solve

path = "AdventOfCode2024/day13/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    machine_instructions = raw_data.read().split("\n\n")

# Puzzle 1
pattern = "\d+"
a, b = symbols("a,b")

result = 0
for instruction in machine_instructions:
    nums = [int(x) for x in re.findall(pattern, instruction)]
    eq1 = Eq((nums[0] * a + nums[2] * b), nums[4])
    eq2 = Eq((nums[1] * a + nums[3] * b), nums[5])
    solution = solve((eq1, eq2), (a, b))
    button_A = solution[a]
    button_B = solution[b]
    
    if int(button_A) - float(button_A) == 0 and int(button_B) - float(button_B) == 0:
        result += int(button_A) * 3 + int(button_B)

print("Puzzle 1 =", result)
