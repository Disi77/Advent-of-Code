path = "AdventOfCode2016/day09/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

# Puzzle 1
decompressed_file = ""
index = 0
while True:
    if data[index].isalpha():
        decompressed_file += data[index]
        index += 1
    else:
        end = data.index(")", index)
        n1, n2 = [int(x) for x in data[index + 1: end].split("x")]
        decompressed_file += data[end + 1: end + 1 + n1] * n2
        index = end + 1 + n1
    if index >= len(data):
        break

print("Puzzle 1 =", len(decompressed_file))
