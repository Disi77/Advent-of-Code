from pathlib import Path
from time import sleep
from os import name, system
from termcolor import colored


class Blizzard:
    def __init__(self, x, y, type, size):
        self.x = x
        self.y = y
        self.type = type
        self.size = size
    
    def move(self):
        match self.type:
            case "<":
                self.x = (self.x - 1) % self.size
            case ">":
                self.x = (self.x + 1) % self.size
            case "^":
                self.y = (self.y - 1) % self.size
            case "v":
                self.y = (self.y + 1) % self.size

    def __repr__(self):
        return f"{self.type} x={self.x} y={self.y}"


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def print_valley(blizzards, walkers):
    sleep(1)
    clear()
    print("minuta", counter, "počet chodců", len(walkers))
    for y in range(-1, SIZE_Y + 1):
        for x in range(-1, SIZE_X + 1):
            if x in [-1, SIZE_X] or y in [-1, SIZE_Y]:
                if x == 0 and y == -1 or x == (SIZE_X - 1) and y == (SIZE_Y):
                    if (x, y) in walkers:
                        print(colored("✿", "magenta"), end=" ")
                    else:
                        print(".", end=" ")
                else:
                    print(colored("✖", "grey"), end=" ")
            else:
                b_count = 0
                b_type = None
                for b in blizzards:
                    if (x, y) == (b.x, b.y):
                        b_count += 1
                        b_type = b.type
                if not b_count:
                    if (x, y) in walkers:
                        print(colored("✿", "magenta"), end=" ")
                    else:
                        print(".", end=" ")
                elif b_count == 1:
                    print(colored(b_type, "cyan"), end=" ")
                else:
                    print(colored(b_count, "cyan"), end=" ")
                
        print()
    print()


def move_all_blizzards(blizzards):
    for b in blizzards:
        b.move()


def get_blizzards(puzzle_input):
    blizzards = []
    for y, row in enumerate(puzzle_input):
        for x, value in enumerate(row):
            if value in list("<>"):
                b = Blizzard(x - 1, y - 1, value, SIZE_X)
                blizzards.append(b)
            elif value in list("^v"):
                b = Blizzard(x - 1, y - 1, value, SIZE_Y)
                blizzards.append(b)
    return blizzards


def walker_move(w, blizzards_coor, end):
    new_walkers = set()
    x, y = w

    if w not in blizzards_coor:
        new_walkers.add(w)

    
    for (new_x, new_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if (new_x, new_y) == end:
            new_walkers.add((new_x, new_y))
        elif (new_x, new_y) == (0, -1):
            new_walkers.add((new_x, new_y))
        elif new_x in [-1, SIZE_X] or new_y in [-1, -2, SIZE_Y]:
            continue
        elif (new_x, new_y) not in blizzards_coor:
            new_walkers.add((new_x, new_y))

    return new_walkers


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")
SIZE_X, SIZE_Y = len(puzzle_input[0]) - 2, len(puzzle_input) - 2

blizzards = get_blizzards(puzzle_input)

START = (0, -1)
END = (SIZE_X - 1, SIZE_Y)
walkers = set()
walkers.add(START)

counter = 0

while True:
    counter += 1
    move_all_blizzards(blizzards)

    blizzards_coor = set()
    for b in blizzards:
        blizzards_coor.add((b.x, b.y))

    temp = set()
    for w in walkers:
        new_walkers = walker_move(w, blizzards_coor, END)
        temp.update(new_walkers)

    walkers = set(temp)
    # print_valley(blizzards, walkers)

    if END in walkers:
        break
   
print("Puzzle 1 =", counter)
