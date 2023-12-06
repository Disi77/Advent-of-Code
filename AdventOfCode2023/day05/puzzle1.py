path = "AdventOfCode2023/day05/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

seeds = [int(x) for x in data.split("\n")[0].split(":")[1].split()]
maps = data.split("\n\n")[1:]
min_location = None

for source in seeds:
    for map in maps:
        destination = None
        rules = []
        for numbers in map.split("\n")[1:]:
            rules.append([int(x) for x in numbers.split()])

        for rule in rules:
            if rule[1] <= source <= (rule[1] + rule[2]):
                destination = source - rule[1] + rule[0]
                break
        
        source = destination if destination else source

    min_location = min(min_location, destination) if min_location else destination

print("Puzzle 1 =", min_location)
