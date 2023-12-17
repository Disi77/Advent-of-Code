path = "AdventOfCode2018/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    changes = []
    for line in raw_data:
        changes.append(int(line.strip()))

# Puzzle 1
print("Puzzle 1 =", sum(changes))


#Puzzle 2
def find_duplicite_frequency(changes):
    result = 0
    frequency_list = set()
    while True:
        for num in changes:
            result += num
            if result not in frequency_list:
                frequency_list.add(result)
            else:
                return result

result = find_duplicite_frequency(changes)
print("Puzzle 2 =", result)
