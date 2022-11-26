puzzle_input = []

with open("input.txt", encoding="utf-8", mode="r") as data:
    for line in data:
        command, value = line.strip().split()
        puzzle_input.append((command, int(value)))


# Puzzle 1
horizontal_position = depth = 0
for command, value in puzzle_input:
    if command == "forward":
        horizontal_position += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

result = horizontal_position * depth
print(f"Puzzle 1 = {result}")


# Puzzle 2
horizontal_position = depth = aim = 0
for command, value in puzzle_input:
    if command == "forward":
        horizontal_position += value
        depth += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

result = horizontal_position * depth
print(f"Puzzle 2 = {result}")