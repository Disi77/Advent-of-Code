import re


with open("day14_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [x.strip() for x in f.readlines()]

memory = {}
for row in input_data:
    if "mask" in row:
        mask = row[7:]

    elif "mem" in row:
        mem_num, mem_value = re.match(r"^mem\[([0-9]+)\] = ([0-9]+)$", row).groups()

        value_bin = f"{int(mem_value):036b}"

        result = ""
        for i, char in enumerate(value_bin):
            if mask[i] == "X":
                result += char
            else:
                result += mask[i]
        memory[mem_num] = int(result, 2)

result = sum(memory.values())

print(f"Sum of all values left in memory after it completes is {result}")
