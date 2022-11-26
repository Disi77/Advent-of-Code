def get_puzzle_input():
    coordinates = []
    fold_coor = []
    with open("input.txt", mode="r", encoding="utf-8") as file:
        data = file.read().split("\n\n")
        for item in data[0].split("\n"):
            numbers = [int(x) for x in item.split(",")]
            coordinates.append(tuple(numbers))

        fold_coor = data[1].strip().replace("fold along ", "").split("\n")
    return coordinates, fold_coor


def print_puzzle2_result(coordinates):
    max_x = max([coor[0] for coor in coordinates])
    max_y = max([coor[1] for coor in coordinates])
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in coordinates:
                print("#", end="")
            else:
                print(" ", end="")
        print()


#Puzzle input
coordinates, fold_coor = get_puzzle_input()

# Puzzle 1 + Puzzle 2
for i, instruction in enumerate(fold_coor):
    key, value = instruction.split("=")
    value = int(value)
    if key == "x":
        direction = 0
    else:
        direction = 1
    temp = []
    for coor in coordinates:
        if coor[direction] < value:
            temp.append(coor)
        if coor[direction] > value:
            new = value - (coor[direction] - value)
            if direction == 0:
                new_coor = (new, coor[1])
            else:
                new_coor = (coor[0], new)         
            temp.append(new_coor)
    coordinates = list(set(temp))
    if i == 0:
        puzzle1_result = len(coordinates)

print(f"Puzzle 1 = {puzzle1_result}\n")

print("Puzzle 2 = ")
print_puzzle2_result(coordinates)

