from pathlib import Path


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n\n")

# Inputs preparation
monkeys = []
for m in puzzle_input:
    rows = m.split("\n")
    items = [int(i) for i in rows[1].replace("Starting items: ", "").split(", ")]
    formula = rows[2].replace("Operation: new = ", "").strip()
    divisor = int(rows[3].split()[-1])
    true_monkey = int(rows[4].split()[-1])
    false_monkey = int(rows[5].split()[-1])
    monkeys.append({"items": items,
                    "formula": formula,
                    "divisor": divisor,
                    "true_m": true_monkey,
                    "false_m": false_monkey,
                    "inspected_items": 0
                    })


# Monkey business
for round in range(1, 21):
    for m in monkeys:
        for index, i in enumerate(m["items"]):
            _, operator, b = m["formula"].split()
            b = i if b == "old" else int(b)
            worry_level = i * b if operator == "*" else i + b
            worry_level = worry_level // 3
            m["items"][index] = worry_level
            m["inspected_items"] += 1
            throw_to_monkey = m["true_m"] if worry_level % m["divisor"] == 0 else m["false_m"]
            monkeys[throw_to_monkey]["items"].append(worry_level)
        m["items"] = []

result = sorted([m["inspected_items"] for m in monkeys])
print("Puzzle 1 =", result[-1] * result[-2])
