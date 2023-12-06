path = "AdventOfCode2023/day05/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

# the main idea here is that for an input in range (a0, b0) after aplying the next rule and
# with a result (a1, b1) the smallest value is always left value in the result = a1
# so we can use the logic similar to puzzle 1 but this time for ranges and not for
# all values (we care what the values look like in the bounds)

# save seeds ranges
seeds = [int(x) for x in data.split("\n")[0].split(":")[1].split()]
ranges = []
for i in range(0, len(seeds), 2):
    from_i = int(seeds[i])
    to_i = from_i + int(seeds[i + 1]) - 1
    ranges.append((from_i, to_i))

# save rules as 2D list
rules_raw = data.split("\n\n")[1:]
rules = []
for r in rules_raw:
    rule = []
    for numbers in r.split("\n")[1:]:
        rule.append([int(x) for x in numbers.split()])
    rules.append(rule)

for rule_set in rules:
    new_ranges = []
    for X, Y in ranges:
        for x1, x0, lenght in rule_set:
            y0 = x0 + lenght - 1
            y1 = x1 + lenght - 1
            if y0 < X or Y < x0:
                #            x---y   or   x---y
                # x0---y0                     x0---y0
                continue
            if X <= x0 and y0 <= Y:
                #   x---------y
                #     x0---y0
                new_ranges.append((x1, y1))
                continue
            if x0 <= X and Y <= y0:
                #        x---y
                #     x0-------y0
                new_ranges.append((x1 - x0 + X, x1 - x0 + Y))
                continue
            if X <= x0 and Y <= y0:
                #     x---y
                #       x0---y0
                new_ranges.append((x1, x1 - x0 + Y))
                continue
            if x0 <= X and y0 <= Y:
                #        x---y
                #     x0---y0
                new_ranges.append((x1 - x0 + X, y1))
                continue

    # we need to identify the ranges that will continue unchanged
    range_leftovers = ranges.copy()
    while True:
        change = False
        for i, (X, Y) in enumerate(range_leftovers):
            for _, x0, lenght in rule_set:
                y0 = x0 + lenght - 1
                if x0 <= X and Y <= y0:
                    #   x0--------y0
                    #       x---y
                    del range_leftovers[i]
                    change = True
                    break
                elif X < x0 and y0 < Y:
                    #      x0---y0
                    #    x---------y
                    del range_leftovers[i]
                    range_leftovers.append((X, x0))
                    range_leftovers.append((y0, Y))
                    change = True
                    break
                elif y0 < X or Y < x0:
                    #    x0---y0        x0---y0
                    #             x---y
                    continue
                elif x0 < X and y0 < Y:
                    #       x---y
                    #   x0---y0
                    range_leftovers[i] = (y0 + 1, Y)
                    change = True
                    break
                elif X < x0 and Y < y0:
                    #   x----y
                    #      x0---y0
                    range_leftovers[i] = (X, x0 - 1)
                    change = True
                    break
        if not change:
            break

    for item in range_leftovers:
        new_ranges.append(item)

    ranges = new_ranges.copy()

print("Puzzle 1 =", min(ranges)[0])
