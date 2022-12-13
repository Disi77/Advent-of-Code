from pathlib import Path
import string


def get_smallest_unvisited(unvisited, distances):
    s = (-1, -1)
    v = None
    for n in unvisited:
        if v is None or distances[n] < v:
            s = n
            v = distances[n]
    return s


def find_letter_coor(map, l):
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value == l:
                return (j, i)


def prepare_data(map):
    '''
    Returns
       - dict with distances (default value = 10,000)
       - empty set for visited squares
       - set with all unvisited squares
    '''
    distances = {}
    for i in range(len(map[0])):
        for j in range(len(map)):
            distances[(i, j)] = 10000

    return distances, set(), set(distances)


def get_distances(S, E, map):
    distances, visited, unvisited = prepare_data(map)
    distances[S] = 0
    while True:
        x, y = get_smallest_unvisited(unvisited, distances)
        if (x, y) == E:
            break

        # find neighbors (areas around actual square)
        neighbors = []
        # LEFT
        if len(map[0]) > x >= 1:
            neighbors.append((x - 1, y))
        # RIGHT
        if len(map[0]) - 1 > x >= 0:
            neighbors.append((x + 1, y))
        # UP
        if len(map) > y >= 1:
            neighbors.append((x, y - 1))
        # DOWN
        if len(map) - 1 > y >= 0:
            neighbors.append((x, y + 1))

        for n in neighbors:
            if LETTERS.index(map[n[1]][n[0]]) - LETTERS.index(map[y][x]) <= 1:
                alt = distances[(x, y)] + 1
                if alt < distances[n]:
                    distances[n] = alt
        
        visited.add((x, y))
        unvisited.remove((x, y))
    return distances[E]


here = Path(__file__).parent
map = Path(here / "input.txt").read_text().split("\n")

LETTERS = string.ascii_lowercase + "E"

# Puzzle 1

S = find_letter_coor(map, "S")
E = find_letter_coor(map, "E")
map[S[1]] = "a" + map[S[1]][1:]

result = get_distances(S, E, map)
print("Puzzle 1 =", result)


# Puzzle 2

result = 10000
coor_a = []
for i in range(len(map)):
    if map[i][0] == "a":
        coor_a.append((0, i))

coor_a.sort()
a = len(coor_a)
for i, S in enumerate(coor_a):
    l = get_distances(S, E, map)
    if l < result:
        result = l

print("Puzzle 2 =", result)