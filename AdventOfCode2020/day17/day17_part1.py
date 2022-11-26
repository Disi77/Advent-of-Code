import copy


data = """
...#..#.
#..#...#
.....###
##....##
......##
........
.#......
##...#..
""".strip().split("\n")
data = [[list(x) for x in data]]

cycles = 6


def add_empty_level(data):
    y = len(data[0])
    x = len(data[0][0])

    new_y = y + 2
    new_x = x + 2

    new_data = []
    empty_slice = [["." for row in range(new_x)] for col in range(new_y)]
    new_data.append(copy.deepcopy(empty_slice))

    for slice in data:
        new_slice = []
        empty_row = list(new_y * ".")
        new_slice.append(copy.copy(empty_row))
        for row in slice:

            new_row = ["."] + row + ["."]
            new_slice.append(new_row)
        new_slice.append(copy.copy(empty_row))
        new_data.append(new_slice)

    new_data.append(copy.deepcopy(empty_slice))

    return new_data


def calculate_state_for_cube(data, new_data, coor):
    x, y, z = coor
    coor_around = []
    for zz in (z-1, z, z+1):
        if 0 <= zz < len(data):
            for yy in (y-1, y, y+1):
                if 0 <= yy < len(data[0]):
                    for xx in (x-1, x, x+1):
                        if 0 <= xx < len(data[0][0]):
                            if (xx, yy, zz) != (x, y, z):
                                coor_around.append((xx, yy, zz))

    active_cubes_around = 0
    for x, y, z in coor_around:
        if data[z][y][x] == "#":
            active_cubes_around += 1

    x, y, z = coor
    if data[z][y][x] == "#":
        if active_cubes_around in [2, 3]:
            result = "#"
        else:
            result = "."

    if data[z][y][x] == ".":
        if active_cubes_around == 3:
            result = "#"
        else:
            result = "."

    return result


def next_generation(data):
    new_data = copy.deepcopy(data)
    for z, slice in enumerate(data):
        for y, row in enumerate(slice):
            for x, cube in enumerate(row):
                new_data[z][y][x] = calculate_state_for_cube(data, new_data, (x, y, z))
    return new_data


for cycle in range(cycles):
    data = add_empty_level(data)
    data = next_generation(data)

count_my = 0
for slice in data:
    for row in slice:
        count_my += row.count("#")

print(f"Part 1 - puzzle answer is {count_my}")
