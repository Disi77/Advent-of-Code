from termcolor import colored

path = "AdventOfCode2024/day15/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    map, instructions = raw_data.read().split("\n\n")
    walls = set()
    boxes = set()
    for i, line in enumerate(map.split("\n")):
        for j, char in enumerate(line):
            if char == "@":
                robot = (i, j)
            elif char == "#":
                walls.add((i, j))
            elif char == "O":
                boxes.add((i, j))
    instructions = instructions.replace("\n", "")
    SIZE = i + 1, j + 1


def print_warehouse_map(walls, boxes, robot, index, instructions):
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if (i, j) in walls:
                print(colored("#", "grey"), end=" ")
            elif (i, j) in boxes:
                print("O", end=" ")
            elif (i, j) == robot:
                print(colored("@", "yellow"), end=" ")
            else:
                print(colored(".", "grey"), end=" ")
        print()
    
    for i, v in enumerate(instructions):
        if i == index:
            print(colored(v, "yellow"), end="")
        else:
            print(v, end="")
    print()


def move(walls, boxes, robot, instruction):
    i, j = robot
    di, dj = 0, 0
    boxes_to_move = []
    match instruction:
        case "<":
            dj = -1
        case ">":
            dj = 1
        case "^":
            di = -1
        case "v":
            di = 1
    while True:
        i, j = i + di, j + dj
        if (i, j) in walls:
            return robot
        if (i, j) in boxes:
            boxes_to_move.append((i, j))
        if (i, j) not in boxes:
            if not boxes_to_move:
                return (i, j)
            for box in boxes_to_move:
                boxes.remove(box)
            for (bx, by) in boxes_to_move:
                boxes.add((bx + di, by + dj))
            return robot[0] + di, robot[1] + dj


# Puzzle 1
# print_warehouse_map(walls, boxes, robot, -1, instructions)
for index, instruction in enumerate(instructions):
    robot = move(walls, boxes, robot, instruction)
    # print_warehouse_map(walls, boxes, robot, index, instructions)

result = 0
for (i, j) in boxes:
    result += i * 100 + j

print("Puzzle 1 =", result)
