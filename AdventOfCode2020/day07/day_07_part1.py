with open("day07_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read()

input_data = input_data.strip().split("\n")


def get_all_rules(data):
    """
    Create list of rules from data in format:
    (color1, num, color2)
    '<color1> bags contain <num> <color2> bags'
    """
    rules = []
    for record in data:
        count = record.count(",")
        record = record.split()
        bag_from = record[0] + " " + record[1]
        if "other" in record:
            rule = (bag_from, 0, "no other")
            rules.append(rule)
            continue
        for i in range(count+1):
            bag_to_count = record[4+4*i]
            bag_to = record[5+4*i] + " " + record[6+4*i]
            rule = (bag_from, int(bag_to_count), bag_to)
            rules.append(rule)
    return rules


# Created list of rules
rules = get_all_rules(input_data)

# Counting colors
santa_bag = "shiny gold"

colors = []
temp_colors = []

# Start with rules where is "shiny gold" bag on the right side
for rule in rules:
    if rule[2] == santa_bag:
        temp_colors.append(rule[0])

# Then for each of the rule with "shiny gold" bag find the parent rule
while True:
    temp = []
    for color in temp_colors:
        for rule in rules:
            if color == rule[2]:
                temp.append(rule[0])

    # All used colors saved in the list "colors"
    colors.extend(temp_colors)
    colors = list(set(colors))

    # Set colors for processing in next round
    temp_colors = list(temp)

    if not temp_colors:
        break


print("How many bag colors can contain at least one shiny gold bag?")
print(len(colors))
