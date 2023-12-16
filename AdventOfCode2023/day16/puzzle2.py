def generate_initial_beams(layout):
    size_x = len(layout[0])
    size_y = len(layout)

    initial_beams = []
    for x in range(size_x):
        initial_beams.append((x, -1, "v"))
        initial_beams.append((x, size_y, "^"))
    for y in range(size_y):
        initial_beams.append((-1, y, ">"))
        initial_beams.append((size_x, y, "<"))
    
    print(len(initial_beams))
    return initial_beams


def get_layout():
    path = "AdventOfCode2023/day16/input.txt"

    with open(path, encoding="utf-8", mode="r") as raw_data:
        layout = []
        for line in raw_data:
            layout.append([x for x in line.strip()])
    return layout


def do_cycle(beams, old_beams, layout, energized):
    size_x, size_y = len(layout[0]), len(layout)
    directions = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
    for beam_index, (x0, y0, direction) in enumerate(beams):
        dx, dy = directions[direction]
        x1, y1 = (x0 + dx, y0 + dy)

        if x1 < 0 or x1 >= size_x or y1 < 0 or y1 >= size_y:
            energized.add((x0, y0))
            del beams[beam_index]

        elif layout[y1][x1] == ".":
            energized.add((x0, y0))
            new_beam = (x1, y1, direction)
            if new_beam not in old_beams:
                beams[beam_index] = new_beam
                old_beams.add(new_beam)

        elif layout[y1][x1] == "\\":
            if direction == ">":
                direction = "v"
            elif direction == "<":
                direction = "^"
            elif direction == "v":
                direction = ">"
            elif direction == "^":
                direction = "<"
            energized.add((x0, y0))
            new_beam = (x1, y1, direction)
            if new_beam not in old_beams:
                beams[beam_index] = new_beam
                old_beams.add(new_beam)

        elif layout[y1][x1] == "/":
            if direction == ">":
                direction = "^"
            elif direction == "<":
                direction = "v"
            elif direction == "v":
                direction = "<"
            elif direction == "^":
                direction = ">"
            energized.add((x0, y0))
            new_beam = (x1, y1, direction)
            if new_beam not in old_beams:
                beams[beam_index] = new_beam
                old_beams.add(new_beam)

        elif layout[y1][x1] == "-":
            if direction in [">", "<"]:
                energized.add((x0, y0))
                new_beam = (x1, y1, direction)
                if new_beam not in old_beams:
                    beams[beam_index] = new_beam
                    old_beams.add(new_beam)
            else:
                energized.add((x0, y0))
                new_beam = (x1, y1, ">")
                if new_beam not in old_beams:
                    beams[beam_index] = new_beam
                    old_beams.add(new_beam)
                else:
                    del beams[beam_index]

                new_beam = (x1, y1, "<")
                if new_beam not in beams and new_beam not in old_beams:
                    beams.append(new_beam)
                    old_beams.add(new_beam)

        elif layout[y1][x1] == "|":
            if direction in ["^", "v"]:
                energized.add((x0, y0))
                new_beam = (x1, y1, direction)
                if new_beam not in old_beams:
                    beams[beam_index] = new_beam
                    old_beams.add(new_beam)
            else:
                energized.add((x0, y0))
                new_beam = (x1, y1, "^")
                if new_beam not in old_beams:
                    beams[beam_index] = new_beam
                    old_beams.add(new_beam)
                else:
                    del beams[beam_index]

                new_beam = (x1, y1, "v")
                if new_beam not in beams and new_beam not in old_beams:
                    beams.append(new_beam)
                    old_beams.add(new_beam)


layout = get_layout()
initial_beams = generate_initial_beams(layout)
final_result = 0

for initial_beam in initial_beams:
    beams = [initial_beam]
    old_beams = set()
    energized = set()
    cycle = 0
    result = (cycle, 0)

    while beams:
        cycle += 1
        do_cycle(beams, old_beams, layout, energized)
        if cycle == 1:
            x, y, direction = initial_beam
            energized.remove((x, y))

        if result[1] != len(energized):
            result = (cycle, len(energized))
        else:
            if result[0] + 10 == cycle:
                break
    
    if result[1] > final_result:
        final_result = result[1]
        
print("Puzzle 2 =", final_result)
