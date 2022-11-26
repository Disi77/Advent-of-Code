def get_puzzle_input():
    with open("input.txt", mode="r", encoding="utf-8") as file:
        puzzle_input = file.read().split("\n\n")

    enh_alg = set()
    for i, item in enumerate(puzzle_input[0].strip()):
        if item == "#":
            binary = f"{i:011b}"[2:]
            enh_alg.add(binary)

    input_image = set()
    for i, row in enumerate(puzzle_input[1].strip().split("\n")):
        for j, char in enumerate(row):
            if char == "#":
                coor = (i, j)
                input_image.add(coor)

    return enh_alg, input_image


def print_image(input_image):
    """
    Only for debugging. Not needed for final solution.
    """
    size = get_size_of_image(input_image)
    for row in range(size["i_from"] - 10, size["i_to"] + 11):
        for col in range(size["j_from"] - 10, size["j_to"] + 11):
            if (row, col) in input_image:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


def get_size_of_image(input_image):
    import sys
    max_i, max_j = 0, 0
    min_i, min_j = sys.maxsize, sys.maxsize
    for (i, j) in input_image:
        max_i = i if i > max_i else max_i
        max_j = j if j > max_j else max_j
        min_i = i if i < min_i else min_i
        min_j = j if j < min_j else min_j
    return {"i_from": min_i,
            "i_to": max_i,
            "j_from": min_j,
            "j_to": max_j
            }


def get_binary_number(row, col, input_image, background, size):
    binary = ""
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i, j) in input_image:
                binary += "1"
            elif i < size["i_from"] or i > size["i_to"] or j < size["j_from"] or j > size["j_to"]:
                if background == ".":
                    binary += "0"
                elif background == "#":
                    binary += "1"
            else:
                binary += "0"
    return binary


def convert_pixels(enh_alg, input_image, background="."):
    size = get_size_of_image(input_image)
    new_image = set()
    for row in range(size["i_from"] - 2, size["i_to"] + 3):
        for col in range(size["j_from"] - 2, size["j_to"] + 3):
            binary_number = get_binary_number(row, col, input_image, background, size)
            if binary_number in enh_alg:
                new_image.add((row, col))
    return new_image


# Puzzle input
enh_alg, image = get_puzzle_input()

# Puzzle 1 + Puzzle 2
backgrounds = [".", "#"]
for i in range(50):
    image = convert_pixels(enh_alg, image, backgrounds[i % 2])
    if i == 1:
        print(f"Puzzle 1 = {len(image)}")

print(f"Puzzle 2 = {len(image)}")
