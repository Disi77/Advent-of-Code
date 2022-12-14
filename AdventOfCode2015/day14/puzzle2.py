from pathlib import Path
import re


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

pattern = r"^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.$"

class Reindeer():
    def __init__(self, name, speed, speed_time, rest_time):
        self.name = name
        self.speed = speed
        self.speed_time = speed_time
        self.rest_time = rest_time
        self.points = 0
        self.distance = 0
        self.mode = "fly"
        self.mode_time = 0
        

def add_point_to_leader(reindeer):
    best_distance = 0
    for r in reindeer:
        if r.distance > best_distance:
            best_distance = r.distance

    for r in reindeer:
        if r.distance == best_distance:
            r.points += 1


reindeer = []

for r in puzzle_input:
    name, speed, speed_time, rest_time = re.match(pattern, r).groups()
    reindeer.append(Reindeer(name, int(speed), int(speed_time), int(rest_time)))

race_time = 2503

for sec in range(race_time):
    for r in reindeer:
        r.mode_time += 1
        if r.mode == "fly":
            r.distance += r.speed
            if r.mode_time == r.speed_time:
                r.mode = "rest"
                r.mode_time = 0
        elif r.mode == "rest" and r.mode_time == r.rest_time:
            r.mode = "fly"
            r.mode_time = 0

    add_point_to_leader(reindeer)


result = max([r.points for r in reindeer])

print("Puzzle =", result)
