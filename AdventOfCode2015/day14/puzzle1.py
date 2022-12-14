from pathlib import Path
import re


here = Path(__file__).parent
reindeer = Path(here / "input.txt").read_text().split("\n")

pattern = r"^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.$"

race_time = 2503

results = {}
for r in reindeer:
    name, speed, speed_time, rest_time = re.match(pattern, r).groups()
    distance = 0
    mode = "fly"
    mode_time = 0
    for sec in range(1, race_time + 1):
        mode_time += 1
        if mode == "fly":
            distance += int(speed)
            if mode_time == int(speed_time):
                mode = "rest"
                mode_time = 0
        elif mode == "rest" and mode_time == int(rest_time):
            mode = "fly"
            mode_time = 0

    results[name] = distance

print("Puzzle =", sorted(list(results.values()))[-1])
