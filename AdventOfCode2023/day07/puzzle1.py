from collections import Counter
from functools import cmp_to_key


def compare_cards(c1, c2):
    card_order = "AKQJT98765432"
    if card_order.index(c1) > card_order.index(c2):
        return 1
    elif card_order.index(c1) < card_order.index(c2):
        return -1
    return 0


def compare_hands(h1, h2):
    for c1, c2 in zip(h1, h2):
        result = compare_cards(c1, c2)
        if result != 0:
            return result
    return 0


path = "AdventOfCode2023/day07/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip().split())

# Puzzle 1
# 2d list for all defined groups = [[fives], [fours], [full houses], [threes], [two pairs], [one pairs], [high cards]]
groups = [[] for _ in range(7)]
bids = {}

for hand, bid in data:
    bids[hand] = int(bid)

    hand_counter = Counter(hand)
    results = Counter(hand_counter.values())

    if 5 in results:
        groups[0].append(hand)
    elif 4 in results:
        groups[1].append(hand)
    elif 3 in results and 2 in results:
        groups[2].append(hand)
    elif 3 in results:
        groups[3].append(hand)
    elif results[2] == 2:
        groups[4].append(hand)
    elif results[2] == 1:
        groups[5].append(hand)
    elif results[1] == 5:
        groups[6].append(hand)

result = 0
index = 1
for group in groups[::-1]:
    group.sort(key=cmp_to_key(compare_hands), reverse=True)
    for hand in group:
        result += index * bids[hand]
        index += 1 

print("Puzzle 1 =", result)
