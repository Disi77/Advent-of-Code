from pathlib import Path
from itertools import pairwise
from termcolor import colored, cprint
import time
from os import system, name


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_paths_coor(puzzle_input):
    paths = set()
    for row in puzzle_input:
        for p1, p2 in pairwise(row.split(" -> ")):
            x0, y0 = [int(i) for i in p1.split(",")]
            x1, y1 = [int(i) for i in p2.split(",")]
            if x0 == x1:
                if y0 < y1:
                    start = y0
                    end = y1
                else:
                    start = y1
                    end = y0
                for i in range(start, end + 1):
                    paths.add((x0, i))
            if y0 == y1:
                if x0 < x1:
                    start = x0
                    end = x1
                else:
                    start = x1
                    end = x0
                for i in range(start, end + 1):
                    paths.add((i, y0))
    return paths


def set_borders(paths, BORDERS):
    from_x = 500
    from_y = 0
    to_x = 500
    to_y = 0
    for (x, y) in paths:
        if x < from_x:
            from_x = x
        if x > to_x:
            to_x = x
        if y < from_y:
            from_y = y
        if y > to_y:
            to_y = y
    BORDERS["x"] = (from_x, to_x)
    BORDERS["y"] = (from_y, to_y)


def draw_paths(paths, sand, BORDERS):
    sand_source = (500, 0)

    from_x, to_x = BORDERS["x"]
    from_y, to_y = BORDERS["y"]

    for y in range(from_y, to_y + 2):
        # print(f"{y: >3}", end=" ")
        for x in range(from_x - 1, to_x + 2):
            if (x, y) in paths:
                print(colored("#", "green"), end=" ")
            elif (x, y) == sand_source:
                print("+", end=" ")
            elif (x, y) in sand:
                print(colored("o", "yellow"), end=" ")
            else:
                print("·", end=" ")
        print()

        
def produce_sand_unit(paths, sand, BORDERS):
    s1, s2 = (500, 1)
    from_x, to_x = BORDERS["x"]
    from_y, to_y = BORDERS["y"]
    while True:
        if not (from_x <= s1 <= to_x) or not (from_y <= s2 <= to_y):
            return False
        elif (s1, s2 + 1) not in paths and (s1, s2 + 1) not in sand:
            s2 += 1
        elif (s1 - 1, s2 + 1) not in paths and (s1 - 1, s2 + 1) not in sand:
            s1 -= 1
            s2 += 1
        elif (s1 + 1, s2 + 1) not in paths and (s1 + 1, s2 + 1) not in sand:
            s1 += 1
            s2 += 1     
        else:
            sand.add((s1, s2))
            return True


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

paths = get_paths_coor(puzzle_input)
BORDERS = {}
set_borders(paths, BORDERS)

sand = set()
while True:
    if not produce_sand_unit(paths, sand, BORDERS):
        break
    # else:
        # time.sleep(0.2)
        # clear()
        # draw_paths(paths, sand, BORDERS)
        
print("Puzzle 1 =", len(sand))
