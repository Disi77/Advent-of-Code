from math import sqrt
from time import time


start = time()

puzzle_input = 265149

# Puzzle 1
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11  
# 20   7   8   9  10  ^
# 21  22  23  24  25  26    
# corner num is number from 1 in right down diagonal
# 1 -> 9 -> 25 ...
if int(sqrt(puzzle_input)) % 2 == 0:
    corner_num = (int(sqrt(puzzle_input)) + 1) ** 2
else:
    corner_num = (int(sqrt(puzzle_input)) + 2) ** 2

x = (int(sqrt(puzzle_input)) + 1) // 2
y = -x
steps_diff = corner_num - puzzle_input

# 0 = left, 1 = up, 2 = right,3 = down
num = corner_num
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0),  3: (0, -1)}
for step in range(steps_diff):
    direction = int(step // (sqrt(corner_num)- 1))
    num -= 1
    x += directions[direction][0]
    y += directions[direction][1]
    if num == puzzle_input:
        break

manhattan = abs(x) + abs(y)

print("Puzzle 1 =", manhattan)
print(time() - start)

start = time()
#Puzzle 1 - different aproach
# 0 = left, 1 = up, 2 = right,3 = down
grid = [None]
x = y = 0
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0),  3: (0, -1)}
for koef in range(1, 10_000):
    if koef == 1:
        direction = 2
        grid.append((x, y))
    if koef % 2 != 0:
        for direction in [2, 1]:
            for _ in range(koef):
                x += directions[direction][0]
                y += directions[direction][1]
                grid.append((x, y))
    else:
        for direction in [0, 3]:
            for _ in range(koef):
                x += directions[direction][0]
                y += directions[direction][1]
                grid.append((x, y))
    if len(grid) > puzzle_input:
        break

x, y = grid[puzzle_input]
result = abs(x) + abs(y)


print("Puzzle 1 =", result)
print(time() - start)
