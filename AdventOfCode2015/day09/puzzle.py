def get_puzzle_input():
    path = "AdventOfCode2015/day09/input.txt"

    data = []
    with open(path, encoding="utf-8", mode="r") as raw_data:
        for line in raw_data:
            data.append(line.strip())

    distances = []
    for d in data:
        temp = d.split()
        distances.append((temp[0], temp[2], int(temp[4])))

    return distances


def get_cities(distances):
    cities = set()
    for city1, city2, distance in distances:
        cities.add(city1)
        cities.add(city2)
    return cities


def get_paths(cities):
    from itertools import permutations

    return permutations(cities)


distances = get_puzzle_input()
cities = get_cities(distances)
paths = get_paths(cities)

results = {}
for p in paths:
    path_distance = 0
    for index in range(len(p) - 1):
        for city1, city2, d in distances:
            if (
                city1 == p[index] and city2 == p[index + 1] or
                city2 == p[index] and city1 == p[index + 1]
                ):
               path_distance += d
    results[p] = path_distance

print("Puzzle 1 =", min(results.values()))
print("Puzzle 2 =", max(results.values()))

