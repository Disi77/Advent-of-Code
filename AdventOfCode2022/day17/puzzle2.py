from pathlib import Path
from os import system, name
from time import sleep
from termcolor import colored


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def calculate_tower_height(tower):
    height = 0
    for item in tower:
        if item[1] > height:
            height = item[1]
        
    return height


def draw_chamber(tower, rock, rocks_count, sleep_time):
    sleep(sleep_time)
    clear()

    if not rock:
        rock = set()
    
    tower_height = calculate_tower_height(tower)
    y_from = max(tower_height + 6, 20)
    y_to = max(0, y_from - 20)

    print("  lvl" + 9 *" " + "units")
    for y in range(y_from, y_to - 1, -1):
        if y % 10 == 0:
            print(f"{y: 5d}", end="")
        else:
            print(5 * " ", end="")
        if y == 0:
            print("+", end="")
        else:
            print("|", end="")
        for x in range(7):
            if y == 0:
                print("-", end="")
            elif (x, y) in tower:
                print(colored("#", "green"), end="")
            elif (x, y) in rock:
                print(colored("@", "yellow"), end="")
            else:
                print(".", end="")
        if y == 0:
            print("+", end="")
        else:
            print("|", end="")
        if y % 10 == 0:
            print(rocks_count)
        else:
            print()


def create_rock(rocks_counter, tower):
    rocks = {"-": set([(0, 0), (1, 0), (2, 0), (3, 0)]),
             "+": set([(0, 0), (1, 0), (2, 0), (1, -1), (1, 1)]),
             "┘": set([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
             "|": set([(0, 0), (0, 1), (0, 2), (0, 3)]),
             "□": set([(0, 0), (1, 0), (0, 1), (1, 1)])
             }
    rocks_types_list = list(rocks.keys())
    rock_type = rocks_types_list[rocks_counter % len(rocks_types_list)]

    entry_point = get_rock_entry_point(tower)
    if rock_type == "+":
        x, y = entry_point
        entry_point = (x, y + 1)
    rock = set()
    for (x, y) in rocks[rock_type]:
        rock.add((x + entry_point[0], y + entry_point[1]))
    return rock, rock_type


def get_rock_entry_point(tower):
    return 2, calculate_tower_height(tower) + 4


def move_rock_right(rock, tower):
    try:
        new_rock = set()
        for (x, y) in rock:
            x = x + 1
            if x > 6:
                raise IndexError
            if (x, y) in tower:
                raise IndexError
            new_rock.add((x, y))
        return new_rock
    except IndexError:
        return rock


def move_rock_left(rock, tower):
    try:
        new_rock = set()
        for (x, y) in rock:
            x = x - 1
            if x < 0:
                raise IndexError
            if (x, y) in tower:
                raise IndexError
            new_rock.add((x, y))
        return new_rock
    except IndexError:
        return rock


def move_rock_down(rock, tower):
    try:
        new_rock = set()
        for (x, y) in rock:
            y = y - 1
            if y == 0:
                raise IndexError
            if (x, y) in tower:
                raise IndexError
            new_rock.add((x, y))
        return new_rock
    except IndexError:
        for item in rock:
            tower.add(item)
        return None


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text()

rocks_final_count = 1_000_000_000_000
rocks_counter = round = 0
tower = set()
rock = None

statistics = {}
find_pattern = True

while True:
    # Get instruction < or >
    instruction_index = round % len(instructions)
    direction = instructions[instruction_index]

    # Create new rock
    if not rock:
        rock, rock_type = create_rock(rocks_counter, tower)
        rocks_counter += 1

    # Check rocks count in chamber
    if rocks_counter == rocks_final_count + 1:
        break

    # Try to find pattern
    if instruction_index == 0:
        if rock_type not in statistics:
            statistics[rock_type] = []
        statistics[rock_type].append((rocks_counter, calculate_tower_height(tower)))

        if find_pattern:
            for k, v in statistics.items():
                if len(v) == 3:
                    v1, v2, v3 = v
                    if v2[0] - v1[0] == v3[0] - v2[0] and v2[1] - v1[1] == v3[1] - v2[1]:
                        pattern_rock = v2[0] - v1[0]
                        pattern_tower = v2[1] - v1[1]

                        repetition = (rocks_final_count - rocks_counter) // pattern_rock
                        # Skip the repeating middle part
                        rocks_counter += repetition * pattern_rock
                        find_pattern = False
                        break

    if direction == ">":
        rock = move_rock_right(rock, tower)
    if direction == "<":
        rock = move_rock_left(rock, tower)
    
    rock = move_rock_down(rock, tower)
    round += 1

# Calculate tower height
middle_part = repetition * pattern_tower
print("Puzzle 2 =", calculate_tower_height(tower) + middle_part)