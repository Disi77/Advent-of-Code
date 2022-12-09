from pathlib import Path
from re import match
from itertools import permutations


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text().split("\n")
pattern = r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$"

inputs = {}
names = set()
for i in instructions:
    name, verb, value, name2 = match(pattern, i).groups()
    value = int(value) if verb == "gain" else -1 * int(value)
    names.add(name)
    inputs[f"{name}+{name2}"] = value

optimal = 0
for arr in permutations(names):
    if arr[0] == list(names)[0]:
        h = 0
        arr = [arr[-1]] + list(arr) + [arr[0]]
        for i, p in enumerate(arr[1:-1], start=1):
            h += inputs[f"{p}+{arr[i + 1]}"]
            h += inputs[f"{p}+{arr[i - 1]}"]
        if h > optimal:
            optimal = h
            

print("Puzzle 1 =", optimal)

# with myself
optimal = 0
names.add("myself")
for arr in permutations(names):
    if arr[0] == list(names)[0]:
        h = 0
        arr = [arr[-1]] + list(arr) + [arr[0]]
        for i, p in enumerate(arr[1:-1], start=1):
            if p != "myself" and arr[i + 1] != "myself":
                h += inputs[f"{p}+{arr[i + 1]}"]
            if p != "myself" and arr[i - 1] != "myself":
                h += inputs[f"{p}+{arr[i - 1]}"]
        if h > optimal:
            optimal = h
            

print("Puzzle 2 =", optimal)