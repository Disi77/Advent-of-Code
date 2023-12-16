path = "AdventOfCode2017/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

# Puzzle 1
valid = 0
for psw in data:
    words_list = psw.split()
    if len(words_list) == len(set(words_list)):
        valid += 1
    
print("Puzzle 1 =", valid)


#Puzzle 2
valid = 0
for psw in data:
    words_list = psw.split()
    for i, w in enumerate(words_list):
        words_list[i] = "".join(sorted(list(w)))
    if len(words_list) == len(set(words_list)):
        valid += 1

print("Puzzle 2 =", valid)
