with open("day12_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()

waypoint = [10, 1]
ship = [0, 0]

for item in input_data:
    action, value = item[0], int(item[1:])
    if action == "F":
        ship[0] += value * waypoint[0]
        ship[1] += value * waypoint[1]
    elif action == "N":
        waypoint[1] += value
    elif action == "S":
        waypoint[1] -= value
    elif action == "E":
        waypoint[0] += value
    elif action == "W":
        waypoint[0] -= value
    else:
        for _ in range(value // 90):
            new_x, new_y = waypoint[1], waypoint[0]
            if action == "R":
                new_y *= (-1)
            if action == "L":
                new_x *= (-1)
            waypoint[0], waypoint[1] = new_x, new_y


print(f"Manhattan distance is {abs(ship[0]) + abs(ship[1])}")
