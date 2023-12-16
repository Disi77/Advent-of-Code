def sum_around_square(x, y, grid_values):
    around = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    result = 0
    for (dx, dy) in around:
        x1, y1 = x + dx, y + dy
        if (x1, y1) in grid_values:
            result += grid_values[(x1, y1)]
    return result


def calculate_puzzle2_result(puzzle_input):
    grid = [None]
    grid_values = {}
    x = y = 0
    # 0 = left, 1 = up, 2 = right,3 = down
    directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0),  3: (0, -1)}
    for koef in range(1, 10_000):
        if koef == 1:
            direction = 2
            grid.append((x, y))
            grid_values[(x, y)] = 1
        if koef % 2 != 0:
            for direction in [2, 1]:
                for _ in range(koef):
                    x += directions[direction][0]
                    y += directions[direction][1]
                    grid.append((x, y))
                    result = sum_around_square(x, y, grid_values)
                    if result > puzzle_input:
                        return result
                    else:
                        grid_values[(x, y)] = sum_around_square(x, y, grid_values)
        else:
            for direction in [0, 3]:
                for _ in range(koef):
                    x += directions[direction][0]
                    y += directions[direction][1]
                    grid.append((x, y))
                    result = sum_around_square(x, y, grid_values)
                    if result > puzzle_input:
                        return result
                    else:
                        grid_values[(x, y)] = sum_around_square(x, y, grid_values)

puzzle_input = 265149
result = calculate_puzzle2_result(puzzle_input)
print("Puzzle 2 =", result)
