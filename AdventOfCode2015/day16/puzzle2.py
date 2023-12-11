path = "AdventOfCode2015/day16/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        name = line[:line.index(":")]
        things = line[line.index(":") + 1:].strip().split(", ")
        sue_data = {"name": name}
        for t in things:
            t_name, t_value = t.split(": ")
            sue_data[t_name] = int(t_value)
        data.append(sue_data)

sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for record in data:
    match = 0
    for key, value in record.items():
        if key == "name":
            continue
        try:
            if key in ["cats", "trees"] and sue[key] < value:
                match += 1
            elif key in ["pomeranians", "goldfish"] and sue[key] > value:
                match += 1
            elif key not in ["pomeranians", "goldfish", "cats", "trees"] and sue[key] == value:
                match += 1
            else:
                break
        except KeyError:
            break
    if match == 3:
        break

print("Puzzle 2 =", record["name"])
