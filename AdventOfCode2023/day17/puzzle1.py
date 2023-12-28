from heapq import heappush, heappop


def get_input_data():
    file = "AdventOfCode2023/day17/input.txt"
    with open(file, encoding="utf-8", mode="r") as raw_data:
        data = []
        for line in raw_data:
            data.append([int(x) for x in line.strip()])
    return data


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
HEAT_LOSSES = get_input_data()
MAX = len(HEAT_LOSSES)

START = (0, 0)
END = (MAX - 1, MAX - 1)

visited = set()
queue = []
init = (0, START, (0, 0), 0)
heappush(queue, init)

while True:
    heat_loss, (x, y), (dx, dy), dir_count = heappop(queue)

    if (x, y) == END:
        break

    if ((x, y), (dx, dy), dir_count) in visited:
        continue
    visited.add(((x, y), (dx, dy), dir_count))

    # Move straight at most 3 blocks
    if dir_count < 3:
        x1, y1 = x + dx, y + dy
        if x1 >= 0 and x1 < MAX and y1 >= 0 and y1 < MAX:
            heappush(queue, (heat_loss + HEAT_LOSSES[y1][x1], (x1, y1), (dx, dy), dir_count + 1))
            
    # Move left and right
    for new_dx, new_dy in DIRECTIONS:
        if (new_dx, new_dy) != (dx, dy) and (new_dx, new_dy) != (-dx, -dy):
            x1, y1 = x + new_dx, y + new_dy
            if x1 >= 0 and x1 < MAX and y1 >= 0 and y1 < MAX:
                heappush(queue, (heat_loss + HEAT_LOSSES[y1][x1], (x1, y1), (new_dx, new_dy), 1))

print("Puzzle 1 =", heat_loss)