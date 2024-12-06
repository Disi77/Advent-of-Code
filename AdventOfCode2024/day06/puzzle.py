from termcolor import colored
from os import system, name
from time import sleep


path = "AdventOfCode2024/day06/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    obstacle_map = set()
    for i, line in enumerate(raw_data):
        for j, char in enumerate(line.strip()):
            if char == "#":
                obstacle_map.add((i, j))
            elif char == "^":
                guard_start = (i, j, char)
    SIZE = (i + 1, j + 1)


# Puzzle 1
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def print_map(obstacle_map, visited, guard, obstruction=None):
    sleep(0.3)
    clear()
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if obstruction and (i, j) == obstruction:
                print(colored("O", "magenta"), end=" ")
            elif (i, j) in obstacle_map:
                print(colored("#", "blue"), end=" ")
            elif i == guard[0] and j == guard[1]:
                print(colored(guard[2], "red"), end=" ")
            elif (i, j) in visited:
                print(colored(".", "yellow"), end=" ")
            else:
                print(colored(".", "grey"), end=" ")
        print()
    print(f"Result: {result}")


def guard_out_of_map(guard):
    if guard[0] >= SIZE[0] or guard[0] < 0:
        return True
    if guard[1] >= SIZE[1] or guard[1] < 0:
        return True
    return False


def move(obstacle_map, guard):
    x, y, direction = guard
    while True:
        match direction:
            case "^":
                if (x - 1, y) in obstacle_map:
                    direction = ">"
                else:
                    x -= 1
                    break

            case ">":
                if (x, y + 1) in obstacle_map:
                    direction = "v"
                else:
                    y += 1
                    break

            case "v":
                if (x + 1, y) in obstacle_map:
                    direction = "<"
                else:
                    x += 1
                    break

            case "<":
                if (x, y - 1) in obstacle_map:
                    direction = "^"
                else:
                    y -= 1
                    break
    return (x, y, direction)


guard = guard_start
visited = set()
visited.add((guard[0], guard[1]))

while True:
    # print_map(obstacle_map, visited, guard)
    guard = move(obstacle_map, guard)
    visited.add((guard[0], guard[1]))
    if guard_out_of_map(guard):
        break

# print_map(obstacle_map, visited, guard)

print("Puzzle 1 =", len(visited) - 1)


#Puzzle 2
result = 0
possible_positions = visited - set(obstacle_map)
possible_positions.remove((guard_start[0], guard_start[1]))

for (i, j) in possible_positions:
    guard = guard_start
    visited = {guard}
    new_obstacle_map = obstacle_map.copy()
    new_obstacle_map.add((i, j))
    while True:
        guard = move(new_obstacle_map, guard)
        if guard in visited:
            result += 1
            break
        else:
            visited.add(guard)
        if guard_out_of_map(guard):
            break

print("Puzzle 2 =", result)
