path = "AdventOfCode2016/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    instructions = []
    for line in raw_data:
        instructions.append(line.strip())

# Puzzle 1
#           keyboard:
#              1  2  3
#              4  5  6
#              7  8  9
keypad = {(-1, 1): "1",  (0, 1): "2",  (1, 1): "3",
          (-1, 0): "4",  (0, 0): "5",  (1, 0): "6",
          (-1, -1): "7", (0, -1): "8", (1, -1): "9"
          }

moves = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

x = y = 0
result = ""
for i in instructions:
    for move in i:
        x1 = x + moves[move][0]
        y1 = y + moves[move][1]
        if (x1, y1) not in keypad:
            x1, y1 = x, y
        x, y = x1, y1
    result += keypad[(x, y)]

print("Puzzle 1 =", result)


#Puzzle 2
#           keyboard:
#                 1
#              2  3  4
#           5  6  7  8  9
#              A  B  C
#                 D
keypad = {                             (0, 2): "1", 
                        (-1, 1): "2",  (0, 1): "3",  (1, 1): "4", 
          (-2, 0): "5", (-1, 0): "6",  (0, 0): "7",  (1, 0): "8", (2, 0): "9",
                        (-1, -1): "A", (0, -1): "B", (1, -1): "C",
                                       (0, -2): "D"
          }

x, y = -2, 0
result = ""
for i in instructions:
    for move in i:
        x1 = x + moves[move][0]
        y1 = y + moves[move][1]
        if (x1, y1) not in keypad:
            x1, y1 = x, y
        x, y = x1, y1
    result += keypad[(x, y)]

print("Puzzle 2 =", result)
