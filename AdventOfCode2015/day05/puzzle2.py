def contains_two_pairs(line):
    pairs = []
    for index in range(len(line) - 1):
        pairs.append(line[index:index+2])
    for pair in pairs:
        if pair in line:
            index = line.index(pair)
            if pair in line[index + 2:]:
                return True
    return False


def contains_xyx_pattern(line):
    for index in range(len(line) - 2):
        substring = line[index:index + 3]
        if substring[0] == substring[2]:
            return True
    return False


path = "AdventOfCode2015/day05/input.txt"

strings = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        strings.append(line.strip())

nice_strings_sum = 0
for line in strings:
    if not contains_two_pairs(line):
        continue
    if not contains_xyx_pattern(line):
        continue
    nice_strings_sum += 1

print("Puzzle 2 =", nice_strings_sum)
