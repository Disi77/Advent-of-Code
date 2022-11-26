from sympy.ntheory.modular import crt


with open("day13_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()

bus_numbers = [int(x) for x in input_data[1].replace("x,", ""). split(",")]
data = input_data[1].strip().split(",")

residues = []
for i, num in enumerate(bus_numbers):
    result = num - data.index(str(num))
    residues.append(result)

result = crt(bus_numbers, residues)

print("What is the earliest timestamp such that all of the listed bus IDs")
print("depart at offsets matching their positions in the list?")
print("=", result[0])
