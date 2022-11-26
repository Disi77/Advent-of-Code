#Puzzle input
puzzle_input = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    for num in data.read().split(","):
        puzzle_input.append(int(num))
    
#Puzzle 1
best_position = None
best_fuel = None

for position in range(max(puzzle_input)+1):
    fuel = 0
    for crab in puzzle_input:
        fuel += abs(crab - position)
    if best_position is None or fuel < best_fuel:
        best_position = position
        best_fuel = fuel

print(f"Puzzle 1 = {best_fuel}")

#Puzzle 2
end = max(puzzle_input)
fuel_rates = []
for index in range(end + 1):
    result = 0
    for i in range(index + 1):
        result += i
    fuel_rates.append(result)

best_position = None
best_fuel = None

for position in range(max(puzzle_input)+1):
    fuel = 0
    for crab in puzzle_input:
        fuel += fuel_rates[abs(crab - position)]
    if best_position is None or fuel < best_fuel:
        best_position = position
        best_fuel = fuel

print(f"Puzzle 2 = {best_fuel}")