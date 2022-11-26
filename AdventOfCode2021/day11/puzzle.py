def get_puzzle_input():
    puzzle_input = []
    with open("input.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            a = [int(x) for x in line.strip()]
            puzzle_input.append(a)
    return puzzle_input


def step(octopuses):
    flashes = 0
    for i, row in enumerate(octopuses):
        for j, octopus in enumerate(row):
            octopuses[i][j] = octopus + 1
    
    while True:
        result = octopus_firework(octopuses)
        if not result:
            break
        flashes += result
    return flashes


def octopus_firework(octopuses):      
    for i, row in enumerate(octopuses):
        for j, octopus in enumerate(row):
            if octopus > 9:
                octopuses[i][j] = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x < 0 or x >= len(octopuses) or y < 0 or y >= len(octopuses[0]):
                            continue
                        if octopuses[x][y] == 0:
                            continue
                        octopuses[x][y] += 1
                return 1        
    return 0


def all_octopuses_flash(octopuses):
    r = sum([sum(x) for x in octopuses])
    return r == 0


#Puzzle 1
octopuses = get_puzzle_input()
final_flashes = 0
for _ in range(100):
    final_flashes += step(octopuses)

print(f"Puzzle 1 = {final_flashes}")


#Puzzle 2
octopuses = get_puzzle_input()
counter = 1
while True:
    step(octopuses)
    if all_octopuses_flash(octopuses):
        break
    counter +=1

print(f"Puzzle 2 = {counter}")