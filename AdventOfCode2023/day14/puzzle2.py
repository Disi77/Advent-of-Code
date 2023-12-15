from termcolor import colored
from os import system, name
import time

start = time.time()


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_dish_size(rounded_rocks, cube_rocks):
    max_x = max_y = 0
    for item in [rounded_rocks, cube_rocks]:
        for (x, y) in item:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    return max_x, max_y


def print_dish(rounded_rocks, cube_rocks):
    time.sleep(0.1)
    clear()
    for y in range(DISH_MAX_Y + 1):
        for x in range(DISH_MAX_X + 1):
            if (x, y) in rounded_rocks:
                print(colored("O", "green"), end="")
            elif (x, y) in cube_rocks:
                print(colored("#", "grey"), end="")
            else:
                print(".", end="")
        print()
    print()


def move_rocks_north(rounded_rocks, cube_rocks):
    while True:
        for rock in rounded_rocks:
            x, y = rock
            if y == 0:
                continue
            new_rock = (x, y - 1)
            if new_rock not in rounded_rocks and new_rock not in cube_rocks:
                rounded_rocks.remove((rock))
                rounded_rocks.add(new_rock)
                break
        else:
            break


def move_rocks_south(rounded_rocks, cube_rocks):
    while True:
        for rock in rounded_rocks:
            x, y = rock
            if y == DISH_MAX_Y:
                continue
            new_rock = (x, y + 1)
            if new_rock not in rounded_rocks and new_rock not in cube_rocks:
                rounded_rocks.remove((rock))
                rounded_rocks.add(new_rock)
                break
        else:
            break


def move_rocks_west(rounded_rocks, cube_rocks):
    while True:
        for rock in rounded_rocks:
            x, y = rock
            if x == 0:
                continue
            new_rock = (x - 1, y)
            if new_rock not in rounded_rocks and new_rock not in cube_rocks:
                rounded_rocks.remove((rock))
                rounded_rocks.add(new_rock)
                break
        else:
            break


def move_rocks_east(rounded_rocks, cube_rocks):
    while True:
        for rock in rounded_rocks:
            x, y = rock
            if x == DISH_MAX_X:
                continue
            new_rock = (x + 1, y)
            if new_rock not in rounded_rocks and new_rock not in cube_rocks:
                rounded_rocks.remove((rock))
                rounded_rocks.add(new_rock)
                break
        else:
            break


def spin_cycle(rounded_rocks, cube_rocks):
    move_rocks_north(rounded_rocks, cube_rocks)
    move_rocks_west(rounded_rocks, cube_rocks)
    move_rocks_south(rounded_rocks, cube_rocks)
    move_rocks_east(rounded_rocks, cube_rocks)


def calculate_total_load(rounded_rocks, cube_rocks):
    result = 0
    for (x, y) in rounded_rocks:
        result += DISH_MAX_Y - y + 1

    return result


path = "AdventOfCode2023/day14/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    rounded_rocks = set()
    cube_rocks = set()
    for y, line in enumerate(raw_data):
        for x, tile in enumerate(line.strip()):
            if tile == "O":
                rounded_rocks.add((x, y))
            elif tile == "#":
                cube_rocks.add((x, y))

DISH_MAX_X, DISH_MAX_Y = get_dish_size(rounded_rocks, cube_rocks)

snapshoots = {}
cycle = 1
cycle_end = 1000000000
jump = False
while True:
    spin_cycle(rounded_rocks, cube_rocks)
    if not jump:
        for index, snapshoot in snapshoots.items():
            if not snapshoot.difference(rounded_rocks):
                cycle += ((cycle_end - cycle) // (cycle - index)) * (cycle - index)
                jump = True
    if cycle == cycle_end:
        break
    snapshoots[cycle] = rounded_rocks.copy()
    cycle += 1

result = calculate_total_load(rounded_rocks, cube_rocks)
print("Puzzle 2 =", result)
print(time.time() - start)
