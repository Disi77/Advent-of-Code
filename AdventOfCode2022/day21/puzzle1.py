from pathlib import Path


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

instructions = {}
for line in puzzle_input:
    number, value = line.split(": ")
    if value.isdigit():
        value = int(value)
    instructions[number] = value

def calculate_new_value(n1, operator, n2):
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "*":
        return n1 * n2
    if operator == "/":
        return n1 // n2


while isinstance(instructions["root"], str):
    for number, value in instructions.items():
        if isinstance(value, str):
            n1, operator, n2 = value.split()
            if isinstance(instructions[n1], int) and isinstance(instructions[n2], int):
                new_value = calculate_new_value(instructions[n1], operator, instructions[n2])
                instructions[number] = new_value

print("Puzzle 1 =", instructions["root"])
