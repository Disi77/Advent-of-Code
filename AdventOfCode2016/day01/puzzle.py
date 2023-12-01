path = "AdventOfCode2016/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    instructions = raw_data.read().split(", ")

# Puzzle 1
x = y = 0
face = 0
for i in instructions:
    turn = i[0]
    blocks = int(i[1:])
    koef = 1 if turn == "R" else -1

    if face == 0:
        x += koef * blocks
    elif face == 1:
        y -= koef * blocks
    elif face == 2:
        x -= koef * blocks
    elif face == 3:
        y += koef * blocks
    face = (face + koef) % 4
    
print("Puzzle 1 =", abs(x + y))


#Puzzle 2
x = y = 0
face = 0
coor = set()
for i in instructions:
    turn = i[0]
    blocks = int(i[1:])
    end = False
    koef = 1 if turn == "R" else -1

    if face == 0:
        for _ in range(blocks):
            x = x + koef
            if (x, y) in coor:
                end = True
                break
            coor.add((x, y))
    elif face == 1:
        for _ in range(blocks):
            y = y - koef
            if (x, y) in coor:
                end = True
                break
            coor.add((x, y))
    elif face == 2:
        for _ in range(blocks):
            x = x - koef
            if (x, y) in coor:
                end = True
                break 
            coor.add((x, y))          
    elif face == 3:
        for _ in range(blocks):
            y = y + koef
            if (x, y) in coor:
                end = True
                break
            coor.add((x, y))
            
    face = (face + koef) % 4

    if end:
        break

print("Puzzle 2 =", x + y)
