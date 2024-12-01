from collections import Counter
from datetime import datetime
import re


path = "AdventOfCode2018/day04/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        dt = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
        action = line.strip()[19:]
        data.append((dt, action))

data.sort()

# Puzzle 1
results = {}
for dt, action in data:
    if "Guard" in action:
        guard = re.search(r"Guard #(\d+)", action).group(1)
        if guard not in results:
            results[guard] = []
        continue
    if "falls asleep" in action:
        sleep = dt.minute
        continue
    if "wakes up" in action:
        results[guard] = results[guard] + list(range(sleep, dt.minute))

most_minutes_asleep = 0
for k, v in results.items():
    if most_minutes_asleep < len(v):
        sleepy_guard = k
        most_minutes_asleep = len(v)

most_common_minute = Counter(results[sleepy_guard]).most_common(1)[0][0]

print("Puzzle 1 =", int(sleepy_guard) * most_common_minute)


# Puzzle 2
results = {}

for dt, action in data:
    if "Guard" in action:
        guard = re.search(r"Guard #(\d+)", action).group(1)
        continue
    if "falls asleep" in action:
        sleep = dt.minute
        continue
    if "wakes up" in action:
        for m in range(sleep, dt.minute):
            results.setdefault(m, []).append(guard)

max_count = 0
for k, v in results.items():
    guard, minutes_count = Counter(v).most_common(1)[0]
    if minutes_count > max_count:
        max_count = minutes_count
        sleepy_guard = guard
        sleepy_guard_minute = k

print("Puzzle 2 =", int(sleepy_guard) * sleepy_guard_minute)
