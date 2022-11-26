import re


def get_input():
    """
    1) Open file with imput data and split this data to 3 parts
    2) Rules = dictionary, where:
                    * key = name of field
                    * value = list of 2 tuples, each tuple is pair of numbers,
                      numbers are lower and upper limits of the specified range
    3) Your ticket = list of integers = numbers in ticket
    4) Nearby tickets = list of lists, where each list is list of integers =
            numbers in each ticket
    """
    with open("day16_input.txt", encoding="utf-8", mode="r") as f:
        rules, your_ticket, nearby_tickets = f.read().split("\n\n")

    rules = rules.strip().split("\n")
    rules_dict = {}
    for rule in rules:
        regex = re.match(f"^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$", rule)
        rule = regex.groups()
        rules_dict[rule[0]] = [(int(rule[1]), int(rule[2])), (int(rule[3]), int(rule[4]))]

    your_ticket = your_ticket.strip().split("\n")[1].strip().split(",")
    your_ticket = [int(x) for x in your_ticket]

    nearby_tickets = nearby_tickets.strip().split("\n")[1:]
    nearby_tickets = [[int(y) for y in x.strip().split(",")] for x in nearby_tickets]
    return rules_dict, your_ticket, nearby_tickets


def delete_invalid_tickets(nearby_tickets, rules):
    """
    Delete all invalid tickets from list of nearby tickets
    """
    valid = []
    for row in nearby_tickets:
        for number in row:
            if not is_number_valid(number, rules):
                break
        else:
            valid.append(row)
    return valid


def is_number_valid(number, rules):
    """
    Validator of numbers from ticket.
    If number is in range from rules, then is valid = return True.
    If number is not in each range from rules, then is invalid = return False.
    """
    for value in rules.values():
        if number_meets_rule(number, value):
            return True
    return False


def number_meets_rule(number, value):
    for x, y in value:
        if x <= number <= y:
            return True
    return False


# Get and format input data
rules, your_ticket, nearby_tickets = get_input()

# In list of nearby tickets delete all invalid tickets
nearby_tickets = delete_invalid_tickets(nearby_tickets, rules)

# Transponse matrix of nearby_tickets
# Before 1 row = 1 ticket (which contains different fields)
# Now 1 row = 1 field (which contains different tickets)
nearby_tickets_transponse = [*zip(*nearby_tickets)]

# Create empty dictionary with results, where key = field on ticket
results = {}
for key in rules:
    results[key] = []

# Take all values for 1 field from nearby tickets and try if all values are
# in range which is defined in rules. If all meet the rule for field, then
# add number of column in results (first column = index 1)
for index, values_for_field in enumerate(nearby_tickets_transponse):
    for key, value in rules.items():
        for number in values_for_field:
            if number_meets_rule(number, value):
                pass
            else:
                break
        else:
            results[key].append(index+1)

# Now I have for each field the numbers of columns where values meet this rule.
# And I want to identify for each field the number of column.
new_results = {}
while results:
    columns = []
    for key, item in results.items():
        if len(item) == 1:
            new_results[key] = item[0]
            columns.append(item[0])
    for key, item in new_results.items():
        try:
            del results[key]
        except KeyError:
            pass
    for key, item in results.items():
        for number in columns:
            if number in item:
                del results[key][results[key].index(number)]

# From dictionary with results create list and sort it
temp_list = []
for key, value in new_results.items():
    temp_list.append((value, key))
temp_list.sort()

# Create dictionary for your ticket where key is name of field and
# value is concrete value from your ticket
final = {}
for column, name in temp_list:
    final[name] = your_ticket[column - 1]

# Find the fields with "departure" and multiply the values
multiply_result = 1
for key, value in final.items():
    if "departure" in key:
        multiply_result *= value

print(f"Part 2 - puzzle answer is {multiply_result}")
