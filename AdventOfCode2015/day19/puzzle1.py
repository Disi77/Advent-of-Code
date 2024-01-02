path = "AdventOfCode2015/day19/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

# Puzzle 1
replacements_data, molecule = data.split("\n\n")
replacements = []
for item in replacements_data.split("\n"):
    key, replacement = item.split(" => ")
    replacements.append((key, replacement))

molecules = set()
for (key, replacement) in replacements:
    for i, m in enumerate(molecule):
        if len(key) == 1:
            if key == m:
                molecules.add(molecule[:i] + replacement + molecule[i+1:])
        elif len(key) == 2:
            if key == molecule[i:i+2]:
                molecules.add(molecule[:i] + replacement + molecule[i+2:])
  
print("Puzzle 1 =", len(molecules))
