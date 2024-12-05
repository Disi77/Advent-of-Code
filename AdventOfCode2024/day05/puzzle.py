path = "AdventOfCode2024/day05/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    part1, part2 = raw_data.read().split("\n\n")

rules = []
for item in part1.split("\n"):
    rules.append(item.split("|"))

update_list = []
for item in part2.split("\n"):
    update_list.append(item.split(","))

# Puzzle 1
incorrect = []
result = 0
for updates in update_list:
    for n1, n2 in rules:
        if n1 in updates and n2 in updates:
            if updates.index(n1) > updates.index(n2):
                incorrect.append(updates)
                break
    else:
        result += int(updates[(len(updates) - 1) // 2])

print("Puzzle 1 =", result)


# Puzzle 2
result = 0
for updates in incorrect:
    # Get only relevant rules for incorrectly ordered updates
    relevant_rules = []
    for n1, n2 in rules:
        if n1 in updates and n2 in updates:
            relevant_rules.append((n1, n2))

    for i in range(len(updates)):
        # Find number that is not in second part of relevant rules
        # because that number must be moved forward
        rules_part2 = set([r for _, r in relevant_rules])
        for num in updates[i:]:
            if num not in rules_part2:
                updates.pop(updates.index(num))
                updates.insert(i, num)
                break
        
        # Remove not needed rules
        temp = []
        for n1, n2 in relevant_rules:
            if n1 != num:
                temp.append((n1, n2))
        relevant_rules = temp.copy()

    result += int(updates[(len(updates) - 1) // 2])


print("Puzzle 2 =", result)
