import re


def get_input():
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


def value_valid(value, rules_dict):
    for key, data in rules.items():
        for x, y in data:
            if x <= value <= y:
                return True
    return False


rules, your_ticket, nearby_tickets = get_input()
ticket_scanning_error_rate = 0
for row in nearby_tickets:
    for value in row:
        if not value_valid(value, rules):
            ticket_scanning_error_rate += value

print(f"Part 1 - puzzle answer is {ticket_scanning_error_rate}")
