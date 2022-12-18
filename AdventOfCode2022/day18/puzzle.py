from pathlib import Path
from itertools import product


def get_neighbours(x, y, z):
    return [
        (x + 1, y, z),
        (x, y + 1, z),
        (x - 1, y, z),
        (x, y - 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    ]


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

cubes = []
for p in puzzle_input:
    x, y, z = p.split(",")
    cubes.append((int(x), int(y), int(z)))

sides = 0
for cube in cubes:
    for side_cube in get_neighbours(*cube):
        if side_cube not in cubes:
            sides += 1

print("Puzzle 1 =", sides)


def air_cubes_around(x, y, z):
    air_cubes = []
    for cube in get_neighbours(x, y, z):
        if cube not in cubes:
            air_cubes.append(cube)
    return air_cubes


def solid_cubes_around(x, y, z):
    results = set()
    for c1, c2, c3 in cubes:
        if c1 > x and c2 == y and c3 == z:
            results.add(1)
        elif c1 < x and c2 == y and c3 == z:
            results.add(2)
        elif c1 == x and c2 > y and c3 == z:
            results.add(3)
        elif c1 == x and c2 < y and c3 == z:
            results.add(4)
        elif c1 == x and c2 == y and c3 > z:
            results.add(5)
        elif c1 == x and c2 == y and c3 < z:
            results.add(6)
    return len(results) == 6

def cube_trapped(x, y, z):
    # around air cube (x, y, z) are not solid cubes in all 6 directions
    # = no path out
    if not solid_cubes_around(x, y, z):
        return False

    # air bubbles can have more complex shape
    # air cube (x, y, z) is already tested = we know that we dont know if the air cube
    # is or is not trapped => we have to test air cubes around
    tested_cubes.add((x, y, z))

    for cube in air_cubes_around(x, y, z):
        if cube in tested_cubes:
            continue
        return cube_trapped(*cube)

    # we tested all air cubes and didnt find any that leads to outside = we found
    # bubble trapped inside
    return True


tested_cubes = set()
sides = 0
for cube in cubes:
    for side_cube in get_neighbours(*cube):
        if side_cube not in cubes and not cube_trapped(*side_cube):
            sides += 1

print("Puzzle 2 =", sides)
