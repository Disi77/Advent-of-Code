from pathlib import Path


def do_cycle(cycle, signal):
    if cycle + 1 in range(20, 221, 40):
        signal += (cycle + 1) * X
    return cycle + 1, signal


def draw_pixel(sprite, cycle, CRT):
    row = cycle // 40
    index = cycle % 40 - 1
    if index in range(sprite - 1, sprite + 2):
        CRT.append((index, row))


def draw_result(CRT):
    for j in range(6):
        for i in range(40):
            if (i, j) in CRT:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text().split("\n")


cycle = signal = 0
X = 1
for i in instructions:
    if "noop" in i:
        cycle, signal = do_cycle(cycle, signal)
    else:
        cycle, signal = do_cycle(cycle, signal)
        cycle, signal = do_cycle(cycle, signal)
        X += int(i.split()[1])

print("Puzzle 1 =", signal)

CRT = []
cycle = 0
X = sprite = 1
for i in instructions:
    if "noop" in i:
        cycle += 1
        draw_pixel(sprite, cycle, CRT)
    else:
        cycle += 1
        draw_pixel(sprite, cycle, CRT)
        cycle += 1
        draw_pixel(sprite, cycle, CRT)
        X += int(i.split()[1])
        sprite += int(i.split()[1])

draw_result(CRT)
