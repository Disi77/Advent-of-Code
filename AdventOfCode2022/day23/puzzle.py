from pathlib import Path
from time import sleep
from termcolor import colored
from os import name, system


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_elves():
    elves = set()
    here = Path(__file__).parent
    puzzle_input = Path(here / "input.txt").read_text().split("\n")
    for j, row in enumerate(puzzle_input):
        for i, value in enumerate(row):
            if value == "#":
                elves.add((i, j))
    return elves


def get_borders(elves):
    i_from = min([i for (i, _) in elves])
    i_to = max([i for (i, _) in elves])
    j_from = min([j for (_, j) in elves])
    j_to = max([j for (_, j) in elves])
    return i_from, i_to, j_from, j_to


def print_elves(elves):
    sleep(0.5)
    clear()
    i_from, i_to, j_from, j_to = get_borders(elves)

    x_values = [str(i).rjust(3) for i in range(i_from - 1, i_to + 2)]
    max_length = max([len(i) for i in x_values])
    for round in range(max_length):
        print("    ", end=" ")
        for value in x_values:
            print(value[round], end=" ")
        print()

    for j in range(j_from - 1, j_to + 2):
        print(f"{j: 3d} ", end=" ")
        for i in range(i_from - 1, i_to + 2):
            if (i, j) in elves:
                print(colored("☺", "yellow"), end=" ")
            else:
                print(colored(".", "green"), end=" ")
        print()


def find_new_position(elf, elves, directions):
    directions_coor = {"NW": (-1, -1), "N": (0, -1), "NE": (1, -1),
                   "W":  (-1, 0),                "E":  (1, 0),
                   "SW": (-1, 1),  "S": (0, 1),  "SE": (1, 1)
                  }
    e1, e2 = elf
    
    # free space around Elf = Elf doesnt move
    for key, coor in directions_coor.items():
        c1, c2 = coor
        if (e1 + c1, e2 + c2) in elves:
            break
    else:
        return None

    # Find first free direction and move the Elf
    for direction in directions:
        for key, coor in directions_coor.items():
            c1, c2 = coor
            if direction in key:
                if (e1 + c1, e2 + c2) in elves:
                    break
        else:
            n1, n2 = directions_coor[direction]
            return n1 + e1, n2 + e2  


elves = get_elves()
directions = ["N", "S", "W", "E"]
round = 0

while True:
    elves_moved = False
    new_positions = {}
    for elf in elves:
        new = find_new_position(elf, elves, directions)
        if new:
            elves_moved = True
            if new not in new_positions:
                new_positions[new] = elf
            else:
                del new_positions[new]
    
    for new, old in new_positions.items():
        elves.add(new)
        elves.remove(old)

    # print_elves(elves)

    round += 1
    directions.append(directions.pop(0))

    if round == 10:
        x0, x1, y0, y1 = get_borders(elves)
        print("Puzzle 1 =", (x1 - x0 + 1) * (y1 - y0 + 1) - len(elves))

    if not elves_moved:
        break


print("Puzzle 2 =", round)