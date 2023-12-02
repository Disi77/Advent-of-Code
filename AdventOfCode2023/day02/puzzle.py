from functools import reduce

path = "AdventOfCode2023/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    games = []
    for line in raw_data:
        games.append(line.strip())

# Puzzle 1
BAG = {"red": 12, "green": 13, "blue": 14}

def game_validation(sets):
    for s in sets:
        for item in s.split(", "):
            value, color = item.split()
            if BAG[color] < int(value):
                return False
    return True

result = 0
for game in games:
    id = int(game.split(":")[0].split()[1])
    sets = game.split(":")[1].split(";")
    if game_validation(sets):
        result += id

print("Puzzle 1 =", result)


#Puzzle 2
result = 0
for game in games:
    id = int(game.split(":")[0].split()[1])
    sets = game.split(":")[1].replace(";", ",").split(",")

    color_max = {"red": 0, "blue": 0, "green": 0}
    for s in sets:
        value, color = s.strip().split()
        color_max[color] = max(color_max[color], int(value))
    result += reduce(lambda a, b: a*b, color_max.values())

print("Puzzle 2 =", result)
