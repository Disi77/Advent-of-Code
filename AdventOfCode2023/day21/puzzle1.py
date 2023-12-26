from termcolor import colored
import time
from os import system, name


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def print_garden_map(rocks, garden_plots, start):
    time.sleep(0.1)
    clear()
    for y in range(STEPS * 2 + 2):
        for x in range(STEPS * 2 + 2):
            if (x, y) in rocks:
                print(colored(ROCK, "grey"), end=" ")
            elif (x, y) in garden_plots:
                print(colored("O", "blue"), end=" ")
            elif (x, y) == start:
                print(colored("S", "magenta"), end=" ")
            else:
                print(colored(".", "grey"), end=" ")
        print()
    print() 


ROCK = "#"
STEPS = 64
path = "AdventOfCode2023/day21/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    rocks = set()
    for (y, row) in enumerate(raw_data):
        for (x, tile) in enumerate(row):
            if tile == ROCK:
                rocks.add((x, y))
            if tile == "S":
                start = (x, y) 

garden_plots = {start}

for step in range(1, STEPS + 1):
    temp = set()
    for (x, y) in garden_plots:
        for (dx, dy) in (1, 0), (-1, 0), (0, 1), (0, -1):
            if (x + dx, y + dy) in rocks:
                continue
            temp.add((x + dx, y + dy))
    garden_plots = temp.copy()
    # print_garden_map(rocks, garden_plots, start)

print("Puzzle 1 =", len(garden_plots))
