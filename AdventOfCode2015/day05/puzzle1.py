def contains_disallowed_substring(text):
    for s in ["ab", "cd", "pq", "xy"]:
        if s in text:
            return True
    return False


def contains_three_vowels(line):
    vowels = "aeiou"
    count = 0
    for char in line:
        if char in vowels:
            count += 1
    return count >= 3


def contains_double_letter(line):
    letters = set(line)
    for letter in letters:
        if 2 * letter in line:
            return True
    return False


path = "AdventOfCode2015/day05/input.txt"

strings = []

with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        strings.append(line.strip())

nice_strings_sum = 0
for line in strings:
    if contains_disallowed_substring(line):
        continue
    if not contains_three_vowels(line):
        continue
    if not contains_double_letter(line):
        continue
    nice_strings_sum += 1

print("Puzzle 1 =", nice_strings_sum)
