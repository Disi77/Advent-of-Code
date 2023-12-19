import turtle as t

path = "AdventOfCode2023/day18/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    dig_plan = []
    for line in raw_data:
        dig_plan.append(line.strip())


t.penup()
t.goto(-200, 100)
t.pendown()
t.fillcolor("yellow")
t.speed(0)
t.begin_fill()

directions = {"0": "R", "1": "D", "2": "L", "3": "U"}
for record in dig_plan:
    _, _, instruction = record.split()
    instruction = instruction[2:-1]
    distance = int(instruction[:-1], base=16)
    direction = directions[instruction[5]]
    if direction == "R":
        t.setheading(0)
    elif direction == "L":
        t.setheading(180)
    elif direction == "U":
        t.setheading(90)
    elif direction == "D":
        t.setheading(270)
    t.forward(distance/20_000)
t.end_fill()

t.exitonclick()