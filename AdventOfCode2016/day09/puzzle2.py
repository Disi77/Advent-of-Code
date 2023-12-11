def decompress_file(file):
    file_lenght = 0
    if "(" not in file:
        return len(file)
    index = 0
    while True:
        if file[index].isalpha():
            file_lenght += 1
            index += 1
        else:
            end = file.index(")", index)
            n1, n2 = [int(x) for x in file[index + 1: end].split("x")]
            file_lenght += n2 * decompress_file(file[end + 1: end + 1 + n1])
            index = end + 1 + n1
        if index >= len(file):
            break
    return file_lenght


path = "AdventOfCode2016/day09/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    file = raw_data.read()

result = decompress_file(file)

print("Puzzle 2 =", result)
