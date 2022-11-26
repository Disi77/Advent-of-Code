with open("day12_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()

direction = "E"
x = y = 0

for item in input_data:
    action, value = item[0], int(item[1:])
    if action == "F":
        action = direction

    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    else:
        if action == "R":
            directions = "NESW"
        if action == "L":
            directions = "WSEN"
        index = directions.index(direction)
        index = (index + value // 90) % 4
        direction = directions[index]

print(f"Manhattan distance is {abs(x) + abs(y)}")
