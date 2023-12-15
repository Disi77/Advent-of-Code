from termcolor import colored
from os import system, name
import time


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
    max_x, max_y = get_dish_size(rounded_rocks, cube_rocks)
    time.sleep(0.1)
    clear()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
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
                # print_dish(rounded_rocks, cube_rocks)
                break
        else:
            break


def calculate_total_load(rounded_rocks, cube_rocks):
    _, max_y = get_dish_size(rounded_rocks, cube_rocks)
    result = 0
    for (x, y) in rounded_rocks:
        result += max_y - y + 1

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


move_rocks_north(rounded_rocks, cube_rocks)
result = calculate_total_load(rounded_rocks, cube_rocks)
print("Puzzle 1 =", result)
