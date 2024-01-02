path = "AdventOfCode2015/day19/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    molecule = raw_data.read().split("\n\n")[1]

# Puzzle 2
# copied from this AWESOME solution from u/askalski
# https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

components_in_molecule = sum(1 for pismeno in molecule if pismeno.isupper())
result = components_in_molecule - molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1
print("Puzzle 2 =", result)

# another AWESOME solution from u/What-A-Baller
# https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

from random import shuffle


with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

replacements_data, molecule = data.split("\n\n")
replacements = []
for item in replacements_data.split("\n"):
    a, b = item.split(" => ")
    replacements.append((a, b))

result = 0
while molecule != 'e':
    for a, b in replacements:
        if b not in molecule:
            continue
        molecule = molecule.replace(b, a, 1)
        result += 1

print("Puzzle 2 =", result)
