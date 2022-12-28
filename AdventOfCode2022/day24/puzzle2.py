from pathlib import Path


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

counter = 0

for (start, end) in [(START, END), (END, START), (START, END)]:
    walkers = set()
    walkers.add(start)  
    
    while True:
        counter += 1
        move_all_blizzards(blizzards)

        blizzards_coor = set()
        for b in blizzards:
            blizzards_coor.add((b.x, b.y))

        temp = set()
        for w in walkers:
            new_walkers = walker_move(w, blizzards_coor, end)
            temp.update(new_walkers)

        walkers = temp.copy()

        if end in walkers:
            break
    

print("Puzzle 2 =", counter)
