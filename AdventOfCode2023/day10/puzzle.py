from termcolor import colored


COOR_DIRECTIONS = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
POSSIBLE_DIRECTIONS = {
    "|": ["up", "down"],
    "-": ["left", "right"],
    "└": ["up", "right"],
    "┘": ["up", "left"],
    "┐": ["left", "down"],
    "┌": ["down", "right"],
}
PATH = set()


class Pointer:
    def __init__(self, x, y, tile, last_x, last_y):
        self.x = x
        self.y = y
        self.tile = tile
        self.last_x = last_x
        self.last_y = last_y
        self.steps = 1

    def __str__(self):
        return f"({self.x}, {self.y}), previous ({self.last_x}, {self.last_y}), tile {self.tile}, steps {self.steps}"

    def move(self, grid):
        self.steps += 1
        for direction in POSSIBLE_DIRECTIONS[self.tile]:
            dx, dy = COOR_DIRECTIONS[direction]
            x1, y1 = self.x + dx, self.y + dy
            if x1 == self.last_x and y1 == self.last_y:
                continue
            self.tile = grid[y1][x1]
            self.last_x, self.last_y = self.x, self.y
            self.x, self.y = x1, y1
            PATH.add((self.x, self.y))
            return


def get_start_coor(grid):
    for y, line in enumerate(grid):
        if "S" in line:
            x = line.index("S")
            return x, y


def print_grid(grid, start, pointers, in_loop, PATH):
    pointers_coors = []
    for p in pointers:
        pointers_coors.append((p.x, p.y))
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (x, y) in pointers_coors:
                print(colored("✿", "magenta"), end="")
            elif (x, y) == start:
                print(colored("S", "yellow"), end="")
            elif (x, y) in in_loop:
                print(colored(".", "yellow"), end="")
            elif (x, y) not in PATH:
                print(".", end="")
            else:
                print(char, end="")
        print()
    print()


def replace_start_tile(start, grid):
    tiles_around = {}
    sx, sy = start
    for direction in ["up", "right", "down", "left"]:
        dx, dy = COOR_DIRECTIONS[direction][0], COOR_DIRECTIONS[direction][1]
        x, y = sx + dx, sy + dy
        if (
            direction == "up" and sy == 0
            or direction == "right" and sx == len(grid[0]) - 1
            or direction == "down" and sy == len(grid) - 1
            or direction == "left" and sx == 0
        ):
            tiles_around[direction] = None
        else:
            tiles_around[direction] = grid[y][x]

    results = {
        "left-right": "-",
        "left-up": "┘",
        "left-down": "┐",
        "up-down": "|",
        "up-right": "└",
        "down-right": "┌",
    }

    possible_results = ["up", "down", "left", "right"]
    if tiles_around["up"] in ["-", "└", "┘", ".", None]:
        index = possible_results.index("up")
        del possible_results[index]
    if tiles_around["right"] in ["|", "└", "┌", ".", None]:
        index = possible_results.index("right")
        del possible_results[index]
    if tiles_around["down"] in ["-", "┌", "┐", ".", None]:
        index = possible_results.index("down")
        del possible_results[index]
    if tiles_around["left"] in ["|", "┐", "┘", ".", None]:
        index = possible_results.index("left")
        del possible_results[index]

    for key, tile in results.items():
        if key == "-".join(possible_results) or key == "-".join(possible_results[::-1]):
            start_tile = tile
            break

    sx, sy = start
    grid[sy] = grid[sy][:sx] + start_tile + grid[sy][sx + 1 :]


path = "AdventOfCode2023/day10/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()
    data = data.replace("L", "└").replace("J", "┘").replace("7", "┐").replace("F", "┌")
    grid = []
    for line in data.split("\n"):
        grid.append(line)


pointers = []
x0, y0 = start = get_start_coor(grid)
PATH.add(start)

# up
dx, dy = COOR_DIRECTIONS["up"]
x1, y1 = x0 + dx, y0 + dy
if grid[y1][x1] in ("|", "┐", "┌"):
    pointer = Pointer(x1, y1, grid[y1][x1], x0, y0)
    pointers.append(pointer)
    PATH.add((x1, y1))

# right
dx, dy = COOR_DIRECTIONS["right"]
x1, y1 = x0 + dx, y0 + dy
if grid[y1][x1] in ("-", "┐", "┘"):
    pointer = Pointer(x1, y1, grid[y1][x1], x0, y0)
    pointers.append(pointer)
    PATH.add((x1, y1))

# down
dx, dy = COOR_DIRECTIONS["down"]
x1, y1 = x0 + dx, y0 + dy
if grid[y1][x1] in ("|", "└", "┘"):
    pointer = Pointer(x1, y1, grid[y1][x1], x0, y0)
    pointers.append(pointer)
    PATH.add((x1, y1))

# left
dx, dy = COOR_DIRECTIONS["left"]
x1, y1 = x0 + dx, y0 + dy
if grid[y1][x1] in ("-", "└", "┌"):
    pointer = Pointer(x1, y1, grid[y1][x1], x0, y0)
    pointers.append(pointer)
    PATH.add((x1, y1))

# this is needed for puzzle 2 for counting left and right borders
replace_start_tile(start, grid)

# puzzle 1
while True:
    P1, P2 = pointers
    if P1.x == P2.x and P1.y == P2.y:
        break
    P1.move(grid)
    P2.move(grid)

print("Puzzle 1 =", P1.steps)

# point inside a loop has odd number of edges on the left side
# and odd number of edges on the right side
in_loop = set()
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if (x, y) in PATH:
            continue
        borders_on_left = 0
        borders_on_right = 0
        for i, tile in enumerate(grid[y]):
            if (i, y) in PATH and tile in ["|", "┐", "┌"]:
                if i < x:
                    borders_on_left += 1
                elif i > x:
                    borders_on_right += 1
        if borders_on_left % 2 != 0 and borders_on_right % 2 != 0:
            in_loop.add((x, y))

print("Puzzle 2 =", len(in_loop))
# print_grid(grid, start, pointers, in_loop, PATH)
