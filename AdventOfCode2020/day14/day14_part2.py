import re
from itertools import product


with open("day14_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [x.strip() for x in f.readlines()]

memory = {}
for row in input_data:
    if "mask" in row:
        mask = row[7:]
    elif "mem" in row:
        mem_address, mem_value = re.match(r"^mem\[([0-9]+)\] = ([0-9]+)$", row).groups()

        value_bin = f"{int(mem_address):036b}"
        result = ""
        for i, char in enumerate(value_bin):
            if mask[i] == "0":
                result += char
            else:
                result += mask[i]

        count_X = result.count("X")
        comb = product("01", repeat=count_X)

        for item in comb:
            result_address = result
            for i in item:
                result_address = result_address.replace("X", i, 1)
            memory[int(result_address, 2)] = int(mem_value)

result = sum(memory.values())
print(f"Sum of all values left in memory after it completes is {result}")
