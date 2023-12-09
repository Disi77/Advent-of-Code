from re import findall


def show_screen(pixels):
    for row in range(6):
        for col in range(50):
            if (col, row) in pixels:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


path = "AdventOfCode2016/day08/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    instructions = []
    for line in raw_data:
        instructions.append(line.strip())

pixels = set()
pattern = r'([0-9]+)'

for i in instructions:
    n1, n2 = [int(x) for x in findall(pattern, i)]
    if "rect" in i:
        for row in range(n2):
            for col in range(n1):
                pixels.add((col, row))
    elif "rotate row" in i:
        row_coor = []
        for item in pixels:
            if item[1] == n1:
                row_coor.append(item)
        for item in row_coor:
            pixels.remove(item)
        for item in row_coor:
            x, y = item
            new_x = (x + n2) % 50
            pixels.add((new_x, y))

    elif "rotate column" in i:
        col_coor = []
        for item in pixels:
            if item[0] == n1:
                col_coor.append(item)
        for item in col_coor:
            pixels.remove(item)
        for item in col_coor:
            x, y = item
            new_y = (y + n2) % 6
            pixels.add((x, new_y))
 
print("Puzzle 1 =", len(pixels))
print("Puzzle 2:")
show_screen(pixels)
