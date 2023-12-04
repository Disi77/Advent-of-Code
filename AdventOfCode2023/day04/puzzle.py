path = "AdventOfCode2023/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.split(":")[1].strip())

# Puzzle 1
result = 0
for line in data:
    winning_raw, numbers_raw = line.split("|")
    winning = set([int(x) for x in winning_raw.split()])
    numbers = set([int(x) for x in numbers_raw.split()])

    winning_count = len(winning & numbers)
    if winning_count:
        result += 2 ** (winning_count - 1)

print("Puzzle 1 =", result)


#Puzzle 2
scratchcards = {key: 1 for key in range(1, len(data) + 1)}

for i, line in enumerate(data):
    card_num = i + 1
    winning_raw, numbers_raw = line.split("|")
    winning = set([int(x) for x in winning_raw.split()])
    numbers = set([int(x) for x in numbers_raw.split()])

    winning_count = len(winning & numbers)
    if not winning_count:
        continue

    for i in range(card_num + 1, card_num + 1 + winning_count):
        koef = scratchcards[card_num]
        scratchcards[i] += koef

result = sum(scratchcards.values())

print("Puzzle 2 =", result)
