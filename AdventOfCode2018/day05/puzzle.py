# path = "AdventOfCode2018/day05/input.txt"
path = "templates/2018/day05/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    polymer = raw_data.read()

# Puzzle 1
def react_polymer(polymer):
    while True:
        for i in range(1, len(polymer)):
            a, b = polymer[i - 1: i + 1]
            if a != b and a.lower() == b.lower():
                polymer = polymer.replace(a+b, "").replace(b+a, "")
                break
        else:
            break
    return polymer

result = react_polymer(polymer)
print("Puzzle 1 =", len(result))


#Puzzle 2
results = []
units = set(polymer.lower())
for u in units:
    new_polymer = polymer.replace(u, "").replace(u.upper(), "")
    results.append(len(react_polymer(new_polymer)))

results.sort()

print("Puzzle 2 =", results[0])
