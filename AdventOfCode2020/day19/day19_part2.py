import re


with open("day19_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read().split("\n\n")


def process_input_data(input_data):
    data = input_data[1].strip().split("\n")

    rules = {}
    for rule in input_data[0].strip().split("\n"):
        key, value = rule.split(":")
        if "\"" in value:
            value = value.split("\"")[1]
        rules[key] = value.strip()

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    return data, rules


def all_items_in_processed_rules(rule_name, rule_value):
    for part in rule_value.split(" | "):
        for item in part.strip().split():
            if item not in processed_rules:
                return False
    return True


# Data preparation from input data
messages, rules = process_input_data(input_data)

# Processing rules as long as only last rule 0 remains
processed_rules = {}
while True:
    # If rule contains only "a" or "b", then move rule from rules
    # to processed_rules
    rules_for_del = []
    for rule_name, rule_value in rules.items():
        try:
            if re.match(f"^[ab |]*$", rule_value):
                rule_value = rule_value.split(" | ")
                for index, item in enumerate(rule_value):
                    rule_value[index] = item.replace(" ", "")
                rules[rule_name] = " | ".join(rule_value)
                rules_for_del.append(rule_name)
            else:
                parts = rule_value.split(" | ")
                for part in parts:
                    if re.match(f"^[ab |]*$", part):
                        rules[rule_name] = rules[rule_name].replace(part, part.replace(" ", ""))
        except TypeError:
            pass
    for rule in rules_for_del:
        processed_rules[rule] = rules[rule]
        del rules[rule]

    # If in rules are only rule 0, 8 and 11, then end this loop
    if len(rules) == 3:
        break

    for rule_name, rule_value in rules.items():
        # For every rule, if at least one item from rule is not in processed
        # rules then skip processing of this rule and continue with another one
        if not all_items_in_processed_rules(rule_name, rule_value):
            continue

        items = rule_value.split(" | ")
        # Items = rule splitet by |
        for item in items:
            parts = item.split()
            # If one number in splited item
            if len(parts) == 1:
                part = parts[0]
                new_value = processed_rules[part]
                if new_value.count("|") == 0:
                    rules[rule_name] = rules[rule_name].replace(part, new_value.strip(), 1).strip()
                elif new_value.count("|") >= 0:
                    rules[rule_name] = rules[rule_name].replace(part, new_value.strip()).strip()
            # If two numbers in splited item
            elif len(parts) == 2:
                part1, part2 = parts
                count_of_line = 0
                for part in parts:
                    if "|" in processed_rules[part]:
                        count_of_line += 1
                if count_of_line == 0:
                    new_value = processed_rules[part1] + processed_rules[part2]
                    rules[rule_name] = rules[rule_name].replace(part1 + " " + part2, new_value, 1).strip()

                elif count_of_line == 1:
                    results = []
                    results1 = processed_rules[part1].split(" | ")
                    results2 = processed_rules[part2].split(" | ")
                    for result1 in results1:
                        for result2 in results2:
                            results.append(result1.strip() + result2.strip())
                    results = " | ".join(results)
                    rules[rule_name] = rules[rule_name].replace(item, results)
                elif count_of_line == 2:
                    results = []
                    results1 = processed_rules[part1].split(" | ")
                    results2 = processed_rules[part2].split(" | ")
                    for result1 in results1:
                        for result2 in results2:
                            results.append(result1.strip() + result2.strip())
                    results = " | ".join(results)
                    rules[rule_name] = rules[rule_name].replace(item, results)

# ('0', '8 11')
# ('11', '42 31 | 42 11 31')
# ('8', '42 | 42 8')

rules8 = []
for rule42 in processed_rules["42"].split(" | "):
    rules8.append(rule42)

rules11 = []
for rule42 in processed_rules["42"].split(" | "):
    for rule31 in processed_rules["31"].split(" | "):
        rules11.append(rule42.strip() + rule31.strip())

result = 0
for rule8 in rules8:
    for rule11 in rules11:
        if (rule8 + rule11) in messages:
            result += 1
            i = messages.index((rule8 + rule11))
            del messages[i]

# result = without aplying new rules
# then delete messages if included in this result

result2 = 0

while messages:
    temp = []
    for i, message in enumerate(messages):
        if message != "":
            temp.append(message)
    messages = list(temp)

    for i, message in enumerate(messages):
        if message[:8] in processed_rules["42"].split(" | "):
            messages[i] = message[8:]
        else:
            messages[i] = ""

    temp = []
    for i, message in enumerate(messages):
        if message != "":
            temp.append(message)
    messages = list(temp)

    for i, message in enumerate(messages):
        while True:
            if message[:8] in processed_rules["42"] and message[-8:] in processed_rules["31"]:
                message = message[8:-8]
            else:
                break
            if not message:
                result2 += 1
                break

print(f"After updatig rules 8 and 11 the new result is {result + result2}")
