ROCK = "#"
START = "S"
STEPS = 26501365

path = "AdventOfCode2023/day21/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    rocks = set()
    for (y, row) in enumerate(raw_data):
        for (x, tile) in enumerate(row):
            if tile == ROCK:
                rocks.add((x, y))
            if tile == START:
                sx, sy = (x, y) 

SIZE = len(row)

# with more steps it looks like quadratic growth
#                                #
#                     #         # #
#           #        # #       # # # 
#    #     # #      # # #     # # # #    
#           #        # #       # # #
#                     #         # # 
#                                #
# y = ax^2 + bx + c
# 
# we can find "x" and "y" for small counts of steps
# for x = [0, 1, 2] the steps = [65, 196, 327]
#        65 = 0 * 131 + 65
#       196 = 1 * 131 + 65
#       327 = 2 * 131 + 65
# 
# and then create system of quadratic equations and calculate "a", "b" and "c"
# y1 = a * x1 ** 2 + b * x1 + c
# y2 = a * x2 ** 2 + b * x2 + c
# y3 = a * x3 ** 2 + b * x3 + c
# -----------------------------
# y1 = a * 0 ** 2 + b * 0 + c
# y2 = a * 1 ** 2 + b * 1 + c
# y3 = a * 2 ** 2 + b * 2 + c
# -----------------------------
# y1 = c
# y2 = a + b + c
# y3 = a * 4 + b * 2 + c
# -----------------------------
# y1 = c
# y2 = a + b + y1       => b = y2 - a - y1
# y3 = 4*a + 2*b + y1   => 4*a = y3 - 2*(y2 - a - y1) - y1
#                          4*a = y3 - 2*y2 + 2*a + 2*y1 - y1
#                          2*a = y3 - 2*y2 + y1
#                            a = (y3 - 2*y2 + y1) / 2
# -----------------------------
# c = y1
# b = y2 - a - y1                => b = y2 - ((y3 - 2*y2 + y1) / 2) - y1
# a = (y3 - 2*y2 + y1) / 2          b = (2*y2 - 2*y1 - y3 + 2*y2 - y1) / 2
#                                   b = (-3*y1 + 4*y2 - y3) / 2
# -----------------------------
# a = (y3 - 2*y2 + y1) / 2
# b = (-3*y1 + 4*y2 - y3) / 2
# c = y1
# 
# then for STEPS = 26501365 = 202300 * 131 + 65
# we will be able to calculate final result
# y = a * 202300 ** 2 + b * 202300 + c


X = [0, 1, 2]
Y = []
pointer = 0

garden_plots = {(sx, sy)}

for step in range(1, STEPS + 1):
    temp = set()
    for (x, y) in garden_plots:
        for (dx, dy) in (1, 0), (-1, 0), (0, 1), (0, -1):
            if ((x + dx) % SIZE, (y + dy) % SIZE) in rocks:
                continue
            temp.add((x + dx, y + dy))
    garden_plots = temp.copy()
    if step % SIZE == 65:
        Y.append(len(garden_plots))
    if len(Y) == 3:
        break

y1, y2, y3 = Y

a = (y3 - 2 * y2 + y1) / 2
b = (-3 * y1 + 4 * y2 - y3) / 2
c = y1

x = STEPS // SIZE
y = a * x ** 2 + b * x + c

print("Puzzle 2 =", int(y))
