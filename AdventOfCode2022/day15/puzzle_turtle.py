from pathlib import Path
from re import match
import turtle as t

# This tool draws picture of test data
# Is not the best code, but works

S = (-300, 300)
Sx, Sy = S

# Speed up the drawing
# t.tracer(n=20, delay=0)

t.penup()
t.speed(0)
t.pensize(5)

def draw_sensor(x, y):
    t.penup()
    t.goto(Sx + 40 + 20 * x, Sy - 20 * y)
    t.pensize(10)
    t.color("orange")
    t.pendown()
    t.forward(1)
    t.pensize(5)
    t.color("black")
    t.penup()


def draw_beacon(x, y):
    t.penup()
    t.goto(Sx + 40 + 20 * x, Sy - 20 * y)
    t.pensize(10)
    t.color("blue")
    t.pendown()
    t.forward(1)
    t.pensize(5)
    t.color("black")
    t.penup()


def draw_connection(sx, sy, bx, by):
    t.penup()
    t.pensize(1)
    t.goto(Sx + 40 + 20 * sx, Sy - 20 * sy)
    t.color("aqua")
    t.pendown()
    t.goto(Sx + 40 + 20 * bx, Sy - 20 * by)
    t.color("black")
    t.pensize(5)
    t.penup()


def draw_diamond(sx, sy, bx, by):
    m = abs(sx - bx) + abs(sy - by)
    t.penup()
    t.pensize(1)
    sensor_x = Sx + 40 + 20 * sx
    sensor_y = Sy - 20 * sy
    t.goto(sensor_x, sensor_y + 20 * m)
    t.pendown()
    t.color("black", "ivory")
    t.begin_fill()
    t.goto(sensor_x + 20 * m, sensor_y)
    t.goto(sensor_x, sensor_y - 20 * m)
    t.goto(sensor_x - 20 * m, sensor_y)
    t.goto(sensor_x, sensor_y + 20 * m)
    t.end_fill()
    t.penup()
    t.pensize(5)


def draw_borders():
    t.penup()
    t.goto(Sx + 40, Sy)
    t.pendown()
    t.pensize(5)
    t.goto(Sx + 40 + 20 * 20, Sy)
    t.goto(Sx + 40 + 20 * 20, Sy - 20 * 20)
    t.goto(Sx + 40, Sy - 20 * 20)
    t.goto(Sx + 40, Sy)
    t.penup()


def mark_point(x, y, color):
    t.penup()
    t.goto(Sx + 40 + 20 * x, Sy - 20 * y)
    t.pendown()
    t.color(color)
    t.pensize(20)
    t.forward(1)
    t.penup()


def draw_grid():
    for row in range(25):
        t.goto(Sx, Sy - 20 * row)
        for y in range(30):
            t.pendown()
            t.forward(1)
            t.penup()
            t.forward(19)

here = Path(__file__).parent
instructions = Path(here / "input_testdata.txt").read_text().split("\n")
pattern = r"Sensor at x=(-?\d+), y=(-?\w+): closest beacon is at x=(-?\d+), y=(-?\d+)"

devices = []
for i in instructions:
    sx, sy, bx, by = match(pattern, i).groups()
    devices.append((int(sx), int(sy), int(bx), int(by)))


# Grid
draw_grid()

# Sensors, Beacons, Diamonds
for sx, sy, bx, by in devices:
    draw_diamond(sx, sy, bx, by)
    draw_connection(sx, sy, bx, by)
    draw_sensor(sx, sy)
    draw_beacon(bx, by)

draw_borders()
mark_point(14, 11, "green")

t.exitonclick()
