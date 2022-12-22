from pathlib import Path


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

instructions = {}
for line in puzzle_input:
    number, value = line.split(": ")
    if value.isdigit():
        value = int(value)
    instructions[number] = value

instructions["root"] = instructions["root"].replace("+", "=")
instructions["humn"] = "x"
equation = instructions["root"]

while True:
    parts = equation.split()
    for part in parts:
        if len(part) == 4 and not part.isdigit():
            equation = equation.replace(part, f"( {str(instructions[part])} )")
            break
    else:
        break


# Source: https://towardsdatascience.com/the-most-efficient-way-to-solve-any-linear-equation-in-three-lines-of-code-bb8f66f1b463
def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag

result = solve_linear(equation)


print("Puzzle 2 =", int(round(result)))
