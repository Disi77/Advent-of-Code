def get_data():
    path = "AdventOfCode2023/day23/input.txt"

    with open(path, encoding="utf-8", mode="r") as raw_data:
        paths = set()
        for y, line in enumerate(raw_data):
            for x, tile in enumerate(line.strip()):
                if tile in ".<>v^":
                    paths.add((x, y))
        size = y + 1
        for (x, y) in paths:
            if y == 0:
                start = (x, y)
            if y == size - 1:
                end = (x, y)
    return paths, start, end


def get_crossroads(PATHS, START, END):
    crossroads_coor = {}
    # find crossroads in the maze, crossroad is tile with more than 2 possible moves around
    for (x, y) in PATHS:
        possible_moves = []
        for x1, y1 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (x1, y1) in PATHS:
                possible_moves.append((x1, y1))
        if len(possible_moves) > 2 or (x, y) in [START, END]:
            crossroads_coor[(x, y)] = possible_moves

    crossroads = {}
    # for every crossroad find surrounding crossroads and calculate the steps to them
    for (cx, cy) in crossroads_coor:
        crossroads[(cx, cy)] = {}
        for (x, y) in crossroads_coor[(cx, cy)]:
            visited = [(cx, cy)]
            while True:
                visited.append((x, y))
                if (x, y) in crossroads_coor:
                    crossroads[(cx, cy)][(x, y)] = len(visited) - 1
                    break
                for (x1, y1) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (x1, y1) in visited:
                        continue
                    if (x1, y1) in PATHS:
                        x, y = x1, y1
                        break
    return crossroads


def walk(x, y, visited, visited_lenght, result):
    visited.add((x, y))

    if (x, y) == END:
        if result < visited_lenght:
            result = visited_lenght
        return result
    
    for (x1, y1), lenght in CROSSROADS[(x, y)].items():
        if (x1, y1) not in visited:
            new_visited = visited.copy()
            result = walk(x1, y1, new_visited, visited_lenght + lenght, result)
    
    return result


PATHS, START, END = get_data()
CROSSROADS = get_crossroads(PATHS, START, END)
result = walk(START[0], START[1], set(), 0, 0)

print("Puzzle 2 =", result)
