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
data = [[[list(x) for x in data]]]

cycles = 6


def add_empty_level(data):
    z = len(data[0])
    y = len(data[0][0])
    x = len(data[0][0][0])

    new_z = z + 2
    new_y = y + 2
    new_x = x + 2

    new_data = []
    empty_dim4 = [[["." for row in range(new_x)] for col in range(new_y)] for slice in range(new_z)]
    new_data.append(copy.deepcopy(empty_dim4))
    for dim4 in data:
        new_dim4 = []
        empty_dim3 = [["." for row in range(new_x)] for col in range(new_y)]
        new_dim4.append(copy.deepcopy(empty_dim3))

        for dim3 in dim4:
            new_dim3 = []
            empty_dim2 = list(new_y * ".")

            new_dim3.append(copy.deepcopy(empty_dim2))
            for dim2 in dim3:
                new_dim2 = ["."] + copy.copy(dim2) + ["."]
                new_dim3.append(copy.deepcopy(new_dim2))

            new_dim3.append(copy.copy(empty_dim2))
            new_dim4.append(copy.deepcopy(new_dim3))

        new_dim4.append(copy.deepcopy(empty_dim3))
        new_data.append(copy.deepcopy(new_dim4))

    new_data.append(copy.deepcopy(empty_dim4))

    return new_data


def calculate_state_for_cube(data, new_data, coor):
    x, y, z, w = coor
    coor_around = []
    for ww in (w-1, w, w+1):
        if 0 <= ww < len(data):
            for zz in (z-1, z, z+1):
                if 0 <= zz < len(data[0]):
                    for yy in (y-1, y, y+1):
                        if 0 <= yy < len(data[0][0]):
                            for xx in (x-1, x, x+1):
                                if 0 <= xx < len(data[0][0][0]):
                                    if (xx, yy, zz, ww) != (x, y, z, w):
                                        coor_around.append((xx, yy, zz, ww))

    active_cubes_around = 0

    for x, y, z, w in coor_around:
        if data[w][z][y][x] == "#":
            active_cubes_around += 1

    x, y, z, w = coor
    if data[w][z][y][x] == "#":
        if active_cubes_around in [2, 3]:
            result = "#"
        else:
            result = "."

    if data[w][z][y][x] == ".":
        if active_cubes_around == 3:
            result = "#"
        else:
            result = "."

    return result


def next_generation(data):
    new_data = copy.deepcopy(data)
    for w, dim4 in enumerate(data):
        for z, dim3 in enumerate(dim4):
            for y, dim2 in enumerate(dim3):
                for x, cube in enumerate(dim2):
                    new_data[w][z][y][x] = calculate_state_for_cube(data, new_data, (x, y, z, w))
    return new_data


for cycle in range(cycles):
    data = add_empty_level(data)
    data = next_generation(data)

count_my = 0
for dim4 in data:
    for slice in dim4:
        for row in slice:
            count_my += row.count("#")

print(f"Part 2 - puzzle answer is {count_my}")
