from termcolor import colored


def print_grid(lights, size):
    ON = colored("۞", "yellow")
    OFF = colored(".", "grey")
    for y in range(size):
        for x in range(size):
            if (x, y) in lights:
                print(ON, end=" ")
            else:
                print(OFF, end=" ")
        print()
    print()


def get_neighbors_on(x, y, lights):
    neighbors_on = 0
    around = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for (dx, dy) in around:
        if (x + dx, y + dy) in lights:
            neighbors_on += 1
    return neighbors_on


def step(lights, size, puzzle=1):
    new_lights = set()
    for y in range(size):
        for x in range(size):
            if (x, y) in lights:
                neighbors_on = get_neighbors_on(x, y, lights)
                if neighbors_on in [2, 3]:
                    new_lights.add((x, y))
            else:
                neighbors_on = get_neighbors_on(x, y, lights)
                if neighbors_on == 3:
                    new_lights.add((x, y))
    if puzzle == 2:
        add_corner_lights(new_lights, size)
    return new_lights


def add_corner_lights(lights, size):
        lights.add((0, 0))
        lights.add((0, size - 1))
        lights.add((size - 1, 0))
        lights.add((size - 1, size - 1))


path = "AdventOfCode2015/day18/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = set()
    for y, line in enumerate(raw_data):
        for x, item in enumerate(line):
            if item == "#":
                data.add((x, y))

size = 100

# Puzzle 1
lights = data.copy()

for i in range(size):
    lights = step(lights, size)
print("Puzzle 1 =", len(lights))


#Puzzle 2
lights = data.copy()

add_corner_lights(lights, size)
for i in range(size):
    lights = step(lights, size, puzzle=2)

print("Puzzle 2 =", len(lights))
