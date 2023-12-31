path = "AdventOfCode2023/day23/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    
    PATHS = set()
    SLOPES = {}
    ROCKS = set()
    for y, line in enumerate(raw_data):
        for x, tile in enumerate(line.strip()):
            if tile == ".":
                PATHS.add((x, y))
            if tile in "<>v^":
                SLOPES[(x, y)] = tile

    SIZE = y + 1
    for (x, y) in PATHS:
        if y == 0:
            START = (x, y)
        if y == SIZE - 1:
            END = (x, y)

            
def walk(x, y, visited):
    visited.add((x, y))
    while True:
        possible_moves = set()
        if (x, y) in SLOPES:
            dir = SLOPES[(x, y)]
            x1, y1 = x, y
            if dir == "v":
                y1 += 1
            elif dir == ">":
                x1 += 1    
            possible_moves.add((x1, y1))
        else:
            for (x1, y1) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (x1, y1) in visited:
                    continue
                elif (x1, y1) in PATHS:
                    possible_moves.add((x1, y1))
                elif (x1, y1) in SLOPES:
                    if (x1 - x, y1 - y) in [(1, 0), (0, 1)]: # we have only ">" or "v" in the maze
                        possible_moves.add((x1, y1))

        if len(possible_moves) == 0:
            return
        elif len(possible_moves) == 1:
            x1, y1 = possible_moves.pop()
            if (x1, y1) == END:
                path_lenghts.add(len(visited))
                return
            visited.add((x1, y1))
            x, y = x1, y1
        else:
            for (x1, y1) in possible_moves:
                walk(x1, y1, visited.copy())
            return


path_lenghts = set()
walk(START[0], START[1], set())
print("Puzzle 1 =", max(path_lenghts))
