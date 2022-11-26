from collections import Counter, defaultdict

def get_puzzle_input():
    with open("input.txt", mode="r", encoding="utf-8") as file:
        template, rest = file.read().split("\n\n")
    rules = {}
    for line in rest.strip().split("\n"):
        k, v = line.split(" -> ")
        rules[k] = v

    return template, rules


def step_puzzle1(template, rules):
    new = ""
    for i in range(1, len(template)):
        rule = template[i-1:i+1]
        new += rule[0] + rules[rule]
    new += template[-1]
    return new


def step_puzzle2(formula_el_counts, counts, rules):
    temp = defaultdict(int)
    for k, v in formula_el_counts.items():
        new_rule1 = k[0] + rules[k]
        new_rule2 = rules[k] + k[1]
        temp[new_rule1] += v
        temp[new_rule2] += v
        counts[rules[k]] += v
    return temp


# Puzzle 1
formula, rules = get_puzzle_input()

steps = 10
for i in range(steps):
    formula = step_puzzle1(formula, rules)

quantity = Counter(formula)
result = max(quantity.values()) - min(quantity.values())
print(f"Puzzle 1 = {result}")


# Puzzle 2
template, rules = get_puzzle_input()

formula = defaultdict(int)
for i in range(1, len(template)):
    pair = template[i-1:i+1]
    formula[pair] += 1

steps = 40
counts = defaultdict(int)
for k, v in Counter(template).items():
    counts[k] = v

for i in range(steps):
    formula = step_puzzle2(formula, counts, rules)

result = max(counts.values()) - min(counts.values())
print(f"Puzzle 2 = {result}")