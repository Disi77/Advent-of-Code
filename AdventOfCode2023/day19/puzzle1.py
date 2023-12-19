path = "AdventOfCode2023/day19/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()
    a, b = data.split("\n\n")

    workflows = {}
    for line in a.split("\n"):
        name, details = line.split("{")
        rules = []
        for rule in details[:-1].split(","):
            rules.append(rule)
        workflows[name] = rules

    part_list = []
    for line in b.split("\n"):
        part = {}
        for item in line[1:-1].split(","):
            key, value = item.split("=")
            part[key] = int(value)
        part_list.append(part)


def process_part(part):
    w = "in"
    while True:
        for rule in workflows[w]:
            if "<" in rule:
                category, value, w = rule.replace("<", ":").split(":")
                if part[category] < int(value):
                    if w in ["R", "A"]:
                        return w
                    break
            elif ">" in rule:
                category, value, w = rule.replace(">", ":").split(":")
                if part[category] > int(value):
                    if w in ["R", "A"]:
                        return w
                    break
            else:
                if rule in ["R", "A"]:
                    return rule
                w = rule


result = 0
for part in part_list:
    out = process_part(part)
    if out == "A":
        result += sum(part.values())

print("Puzzle 1 =", result)
