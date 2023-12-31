from sympy import symbols, Eq, solve


path = "AdventOfCode2023/day24/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    hailstones = []
    for line in raw_data:
        part1, part2 = line.strip().split(" @ ")
        x, y, z = [int(x) for x in part1.split(", ")]
        dx, dy, dz = [int(x) for x in part2.split(", ")]
        hailstones.append((x, y, z, dx, dy, dz))
 
counter = 1
symbols_names = "X Y Z dx dy dz c1, c2, c3"
equations_strings = []
for (x, y, z, dx, dy, dz) in hailstones[:3]:
    c = f"c{counter}"
    equations_strings.append(f"{x} + {c} * {dx} = X + dx * {c}")
    equations_strings.append(f"{y} + {c} * {dy} = Y + dy * {c}")
    equations_strings.append(f"{z} + {c} * {dz} = Z + dz * {c}")
    counter += 1

X, Y, Z, dx, dy, dz, c1, c2, c3 = symbols(symbols_names)

equations = [Eq(eval(equation.split('=')[0].strip()), eval(equation.split('=')[1].strip())) for equation in equations_strings]

solutions = solve(equations, (X, Y, Z, dx, dy, dz, c1, c2, c3))

print("Puzzle 2 =",sum(solutions[0][:3]))
