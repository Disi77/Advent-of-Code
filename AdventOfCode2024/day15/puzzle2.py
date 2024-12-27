from termcolor import colored

path = "AdventOfCode2024/day15/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    map, instructions = raw_data.read().split("\n\n")
    new_map = ""
    for char in map:
        if char == "#":
            new_map += "##"
        elif char == "O":
            new_map += "[]"
        elif char == ".":
            new_map += ".."
        elif char == "@":
            new_map += "@."
        else:
            new_map += char

    walls = set()
    boxes = set()
    for i, line in enumerate(new_map.split("\n")):
        for j, char in enumerate(line):
            if char == "@":
                robot = (i, j)
            elif char == "#":
                walls.add((i, j))
            elif char == "[":
                boxes.add((i, j))
    instructions = instructions.replace("\n", "")
    SIZE = i + 1, j + 1


def print_warehouse_map(walls, boxes, robot, index, instructions):
    skip_next = False
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if skip_next:
                skip_next = False
                continue
            if (i, j) in walls:
                print(colored("#", "grey"), end="")
            elif (i, j) in boxes:
                print("[]", end="")
                skip_next = True
            elif (i, j) == robot:
                print(colored("@", "yellow"), end="")
            else:
                print(colored(".", "grey"), end="")
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
    boxes_to_move = set()
    match instruction:
        case "<":
            dj = -1
        case ">":
            dj = 1
        case "^":
            di = -1
        case "v":
            di = 1

    # left + right
    if instruction in ["<", ">"]:
        while True:
            i, j = i + di, j + dj
            if (i, j) in walls:
                return robot
            
            k = 0
            if instruction == "<":
                k = -1
            if (i, j + k) in boxes:
                boxes_to_move.add((i, j + k))
                i, j = i + di, j + dj
                continue

            for box in boxes_to_move:
                boxes.remove(box)
            for box in boxes_to_move:
                bx, by = box
                boxes.add((bx + di, by + dj))
            return robot[0] + di, robot[1] + dj
        
    # up + down
    group = [robot]
    if instruction in ["^", "v"]:
        while True:
            for (i, j) in group:
                i, j = i + di, j + dj
                if (i, j) in walls:
                    return robot
            
            new_group = []
            for (i, j) in group:
                i, j = i + di, j + dj
                if (i, j) in boxes:
                    boxes_to_move.add((i, j))
                    new_group.append((i, j))
                    new_group.append((i, j+1))
                if (i, j-1) in boxes:
                    boxes_to_move.add((i, j-1))
                    new_group.append((i, j))
                    new_group.append((i, j-1))
            
            if new_group:
                group = new_group.copy()
                continue
            
            for box in boxes_to_move:
                boxes.remove(box)
            for (bx, by) in boxes_to_move:
                boxes.add((bx + di, by + dj))
            return robot[0] + di, robot[1] + dj


# Puzzle 2
# print_warehouse_map(walls, boxes, robot, -1, instructions)
for index, instruction in enumerate(instructions):
    robot = move(walls, boxes, robot, instruction)
    # print_warehouse_map(walls, boxes, robot, index, instructions)

result = 0
for (i, j) in boxes:
    result += i * 100 + j

print("Puzzle 2 =", result)
