def needed_paper(l, w, h):
    sides = sorted([l, w, h])
    return 2 * l * w + 2 * w * h + 2 * h * l + sides[0] * sides[1]


def needed_ribbon(l, w, h):
    sides = sorted([l, w, h])
    return 2 * (sides[0] + sides[1]) + l * w * h


path = "AdventOfCode2015/day02/input.txt"

data = []
with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        data.append(line.strip())

wrapping_paper_sum = 0
ribbon_sum = 0
for i in data:
    l, w, h = i.split("x")
    l, w, h = int(l), int(w), int(h)
    wrapping_paper_sum += needed_paper(l, w, h)
    ribbon_sum += needed_ribbon(l, w, h)

print("Puzzle 1 = ", wrapping_paper_sum)
print("Puzzle 2 = ", ribbon_sum)
