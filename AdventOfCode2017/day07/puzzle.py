from collections import Counter


path = "AdventOfCode2017/day07/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    towers_data = [line.strip() for line in raw_data]

# Puzzle 1
relevant_towers = [t for t in towers_data if "->" in t]
bottom_program = None
for t in relevant_towers:
    tower_name = t.split(" ")[0]
    for t in relevant_towers:
        children = t.split("->")[1]
        if tower_name in children:
            break
    else:
        bottom_program = tower_name
    if bottom_program:
        break


print("Puzzle 1 =", bottom_program)


# Puzzle 2
class Tower:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def total_weight(self):
        return self.weight + sum(child.total_weight() for child in self.children)


towers = {}
for t in towers_data:
    tower_raw = t.split(" ")
    name = tower_raw[0]
    weight = int(tower_raw[1][1:-1])
    if "->" in t:
        children = t.split("->")[1].strip().split(", ")
    else:
        children = []

    towers[name] = Tower(name, weight, children)

for tower in towers.values():
    for i, child in enumerate(tower.children):
        tower.children[i] = towers[child]

result = None
for tower in towers.values():
    if not tower.children:
        continue
    weights = [child.total_weight() for child in tower.children]
    if len(set(weights)) > 1:
        wrong_w = Counter(weights).most_common(2)[1][0]
        correct_w = Counter(weights).most_common(1)[0][0]
        for child in tower.children:
            if child.total_weight() == wrong_w:
                final_w = child.weight - (wrong_w - correct_w)
                if not result or result > final_w:
                    result = final_w

print("Puzzle 2 =", result)
