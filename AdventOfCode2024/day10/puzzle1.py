path = "AdventOfCode2024/day10/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    map = []
    zeros_coor = []
    for i, line in enumerate(raw_data):
        line = line.strip()
        map.append([int(x) for x in line])
        if "0" in line:
            for j, char in enumerate(line):
                if char == "0":
                    zeros_coor.append((i, j))
    SIZE = i+1, j+1

result = 0
possible_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
for start in zeros_coor:
    trails = set()
    trails.add(start)
    nines_coor = set()
    while trails:
        i0, j0 = trails.pop()
        for di, dj in possible_directions:
            i1, j1 = i0 + di, j0 + dj
            if not (0 <= i1 < SIZE[0]) or not (0<= j1 < SIZE[1]):
                continue
            if map[i1][j1] - map[i0][j0] != 1:
                continue
            if map[i1][j1] == 9: 
                nines_coor.add((i1, j1))
                continue
            trails.add((i1, j1))
    result += len(nines_coor)

print("Puzzle 1 =", result)
