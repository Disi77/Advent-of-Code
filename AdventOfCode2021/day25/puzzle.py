def get_input_data():
    cucumbers = {">": set(), "v": set()}
    size = [0, 0]
    with open("AdventOfCode2021/day25/input.txt", mode="r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            for j, item in enumerate(line.strip()):
                if item != ".":
                    coor = (i, j)
                    cucumbers[item].add(coor)
                    if i > size[0]:
                        size[0] = i
                    if j > size[1]:
                        size[1] = j
        size[0] += 1
        size[1] += 1
    return cucumbers, size
        

def print_field(c, size):
    for i in range(size[0]):
        for j in range(size[1]):
            if (i, j) in cucumbers[">"]:
                print(">", end="")
            elif (i, j) in cucumbers["v"]:
                print("v", end="")
            else:
                print(".", end="")
        print()


cucumbers, size = get_input_data()
round = 0

while True:
    new_state_left = set()
    new_state_down = set()
    change = False

    for c in cucumbers[">"]:
        i, j = c
        j = (j + 1) % size[1]
        new_c = (i, j)
        if new_c not in cucumbers[">"] and new_c not in cucumbers["v"]:
            new_state_left.add(new_c)
            change = True
        else:
            new_state_left.add(c)
    
    for c in cucumbers["v"]:
        i, j = c
        i = (i + 1) % size[0]
        new_c = (i, j)
        if new_c not in new_state_left and new_c not in cucumbers["v"]:
            new_state_down.add(new_c)
            change = True
        else:
            new_state_down.add(c)

    round += 1
    if change:
        cucumbers[">"] = new_state_left
        cucumbers["v"] = new_state_down
    else:
        break

print(round)