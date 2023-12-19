import copy


def find_combinations(c, w):
    if w == "R":
        return
    if w == "A":
        combinations.append(c)
        return

    for rule in WORKFLOWS[w]:
        if "<" in rule:
            category, value, next_w = rule.replace("<", ":").split(":")
            value = int(value)
            new_c = copy.deepcopy(c)
            new_c[category][1] = min(new_c[category][1], value - 1)
            find_combinations(new_c, next_w)
            c[category][0] = max(c[category][0], value)
        elif ">" in rule:
            category, value, next_w = rule.replace(">", ":").split(":")
            value = int(value)
            new_c = copy.deepcopy(c)
            new_c[category][0] = max(new_c[category][0], value + 1)
            find_combinations(new_c, next_w)
            c[category][1] = min(c[category][1], value)
        else:
            new_c = copy.deepcopy(c)
            find_combinations(new_c, rule)


path = "AdventOfCode2023/day19/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()
    a, _ = data.split("\n\n")

    WORKFLOWS = {}
    for line in a.split("\n"):
        name, details = line.split("{")
        rules = []
        for rule in details[:-1].split(","):
            rules.append(rule)
        WORKFLOWS[name] = rules

combinations = []
c = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
find_combinations(c, "in")

result = 0
for record in combinations:
    record_result = 1
    for k, v in record.items():
        record_result *= v[1] - v[0] + 1
    result += record_result

print("Puzzle 2 =", result)
