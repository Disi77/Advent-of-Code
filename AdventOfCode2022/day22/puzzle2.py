from pathlib import Path
from os import name, system
from time import sleep
from math import sqrt
from termcolor import colored


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def print_map(map, pointer, direction):
    sleep(0.5)
    clear()
    for y in range(3 * SIZE):
        for x in range(4 * SIZE):
            if (x, y) == pointer:
                match direction:
                    case "left":
                        print(colored("<", "magenta"), end=" ")
                    case "right":
                        print(colored(">", "magenta"), end=" ")
                    case "up":
                        print(colored("^", "magenta"), end=" ")
                    case "down":
                        print(colored("v", "magenta"), end=" ")
            elif (x, y, ".") in map:
                print(".", end=" ")
            elif (x, y, "#") in map:
                print(colored("#", "cyan"), end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


def change_direction(direction, letter):
    index = DIRECTIONS.index(direction)
    if letter == "R":
        index += 1
    elif letter == "L":
        index -= 1
    index = index % 4
    return DIRECTIONS[index]


def cube_size(map):
    return int(sqrt(len(map) // 6))


def get_col_index(row, map, side):
    if side == "right":
        return max([x for (x, y, _) in map if y == row])
    elif side == "left":
        return min([x for (x, y, _) in map if y == row])


def get_row_index(col, map, side):
    if side == "down":
        return max([y for (x, y, _) in map if x == col])
    elif side == "up":
        return min([y for (x, y, _) in map if x == col])


def make_step(pointer, direction, map):
    x, y = pointer
    new_direction = direction
    match direction:
        case "left":
            x = x - 1
            if x < ROWS_RANGES[y][0]:
                x, y, new_direction = get_new_coor(x, y, direction)
        case "right":
            x = x + 1
            if x > ROWS_RANGES[y][1]:
                x, y, new_direction = get_new_coor(x, y, direction)
        case "up":
            y = y - 1
            if y < COLS_RANGES[x][0]:
                x, y, new_direction = get_new_coor(x, y, direction)
        case "down":
            y = y + 1
            if y > COLS_RANGES[x][1]:
                x, y, new_direction = get_new_coor(x, y, direction)
    if (x, y, ".") in map:
        return (x, y), new_direction
    elif (x, y, "#") in map:
        return pointer, direction


def get_ranges(map):
    rows_ranges = []
    cols_ranges = []

    map_rows = map_cols = 0
    for (x, y, _) in map:
        if x > map_cols:
            map_cols = x
        if y > map_rows:
            map_rows = y

    for row in range(map_rows + 1):
        col_from = get_col_index(row, map, "left")
        col_to = get_col_index(row, map, "right")
        rows_ranges.append((col_from, col_to))

    for col in range(map_cols + 1):
        row_from = get_row_index(col, map, "up")
        row_to = get_row_index(col, map, "down")
        cols_ranges.append((row_from, row_to))
    return rows_ranges, cols_ranges


def get_instructions(puzzle_input):
    instructions = []
    for part in puzzle_input.split("R"):
        for number in part.split("L"):
            instructions.append(int(number))
            instructions.append("L")
        instructions[-1] = "R"
    instructions.pop()
    return instructions


def get_map(puzzle_input):
    map = set()
    for y, row in enumerate(puzzle_input.split("\n")):
        for x, value in enumerate(row):
            if value in [".", "#"]:
                map.add((x, y, value))
    return map


def get_new_coor(x, y, direction):
    if direction in ["left", "right"]:
        for rule in CUBE_EDGES[direction]:
            if y in range(rule["from"], rule["from"] + SIZE):
                value = abs(rule["to"] + (y - rule["from"]))

                if rule["dir"] in ["down", "up"]:
                    x = value
                else:
                    y = value
                break

    elif direction in ["up", "down"]:
        for rule in CUBE_EDGES[direction]:
            if x in range(rule["from"], rule["from"] + SIZE):
                value = abs(rule["to"] + (x - rule["from"]))

                if rule["dir"] in ["down", "up"]:
                    x = value
                else:
                    y = value
                break

    match rule["dir"]:
        case "down":
            y = get_row_index(x, map, "up")
        case "up":
            y = get_row_index(x, map, "down")
        case "left":
            x = get_col_index(y, map, "right")
        case "right":
            x = get_col_index(y, map, "left")

    return x, y, rule["dir"]


def get_test_data_dube_edges():
    """
    Created manually for test data
    """
    return {"right": [{"from": 0,        "to": -(SIZE * 3 - 1), "dir": "left"},
                      {"from": SIZE,     "to": -(SIZE * 4 - 1), "dir": "down"},
                      {"from": SIZE * 2, "to": -(SIZE - 1),     "dir": "left"}
                      ],
            "left":  [{"from": 0,        "to": SIZE,            "dir": "down"},
                      {"from": SIZE,     "to": -(SIZE * 4 - 1), "dir": "up"},
                      {"from": SIZE * 2, "to": -(SIZE * 2 - 1),  "dir": "up"}
                      ],
            "up":    [{"from": 0,        "to": -(SIZE * 3 - 1), "dir": "down"},
                      {"from": SIZE,     "to": 0,               "dir": "right"},
                      {"from": SIZE * 2, "to": -(SIZE - 1),     "dir": "down"},
                      {"from": SIZE * 3, "to": -(SIZE * 2 - 1), "dir": "left"}
                      ],
            "down":  [{"from": 0,        "to": -(SIZE * 3 - 1), "dir": "up"},
                      {"from": SIZE,     "to": -(SIZE * 3 - 1), "dir": "right"},
                      {"from": SIZE * 2, "to": -(SIZE - 1),     "dir": "up"},
                      {"from": SIZE * 3, "to": -(SIZE * 2 - 1), "dir": "right"}
                      ]
            }


def get_cube_edges():
    """
    Created manually
    """
    return {"right": [{"from": 0,        "to": -(SIZE * 3 - 1), "dir": "left"},
                      {"from": SIZE,     "to": SIZE * 2,        "dir": "up"},
                      {"from": SIZE * 2, "to": -(SIZE - 1),     "dir": "left"},
                      {"from": SIZE * 3, "to": SIZE,            "dir": "up"},
                      ],
            "left":  [{"from": 0,        "to": -(SIZE * 3 - 1), "dir": "right"},
                      {"from": SIZE,     "to": 0,               "dir": "down"},
                      {"from": SIZE * 2, "to": -(SIZE - 1),     "dir": "right"},
                      {"from": SIZE * 3, "to": SIZE,            "dir": "down"},
                      ],
            "up":    [{"from": 0,        "to": SIZE,            "dir": "right"},
                      {"from": SIZE,     "to": SIZE * 3,        "dir": "right"},
                      {"from": SIZE * 2, "to": 0,               "dir": "up"}
                      ],
            "down":  [{"from": 0,        "to": SIZE * 2,        "dir": "down"},
                      {"from": SIZE,     "to": SIZE * 3,        "dir": "left"},
                      {"from": SIZE * 2, "to": SIZE,            "dir": "left"}
                      ]
            }


here = Path(__file__).parent
puzzle_map, puzzle_instructions = Path(here / "input.txt").read_text().split("\n\n")
map = get_map(puzzle_map)
instructions = get_instructions(puzzle_instructions)

ROWS_RANGES, COLS_RANGES = get_ranges(map)
SIZE = cube_size(map)
DIRECTIONS = ["right", "down", "left", "up"]

CUBE_EDGES = get_cube_edges()
# CUBE_EDGES = get_test_data_dube_edges()

direction = "right"
pointer = (get_col_index(0, map, "left"), 0)

for i in instructions:
    # print_map(map, pointer, direction)
    if i in ["R", "L"]:
        direction = change_direction(direction, i)
        continue
    for step in range(i):
        new_pointer, direction = make_step(pointer, direction, map)
        if new_pointer == pointer:
            break
        pointer = new_pointer
        # print_map(map, pointer, direction)


facing = DIRECTIONS.index(direction)

print("Puzzle 2 =", (pointer[1] + 1) * 1000 + (pointer[0] + 1) * 4 + facing)
