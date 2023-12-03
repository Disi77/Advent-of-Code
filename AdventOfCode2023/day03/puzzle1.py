import re


def number_adjacent_to_symbol(data, num_coor):
    x0, y0 = num_coor[0]
    x1, y1 = num_coor[1]

    # check the area around the number
    # top left corner coor
    area_x0 = max(0, x0 - 1)
    area_y0 = max(0, y0 - 1)
    # bottom right corner coor
    area_x1 = min(x1 + 1, len(data[0]) - 1)
    area_y1 = min(y1 + 1, len(data) - 1)

    for line in data[area_y0:area_y1 + 1]:
        for char in line[area_x0:area_x1 + 1]:
            if char.isdigit():
                continue
            if char != ".":
                return True
    return False


path = "AdventOfCode2023/day03/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

regex_pattern = r'\b\d+(?:\d+)?\b'

final_sum = 0
for row_index, row in enumerate(data):
    numbers_in_row = re.findall(regex_pattern, row)
    if not numbers_in_row:
        continue

    start = 0
    for num in numbers_in_row:
        col_index = row.index(num, start)
        start = col_index + len(num)
        
        num_coor = [(col_index, row_index), (col_index + len(num) - 1, row_index)]
        
        if number_adjacent_to_symbol(data, num_coor):
            final_sum += int(num)

print("Puzzle 1 =", final_sum)
