class HydroVent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.is_horizontal = self.y1 == self.y2
        self.is_vertical = self.x1 == self.x2
        self.is_diagonal = abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

    def __str__(self):
        return f"<from {self.x1},{self.y1} to {self.x2},{self.y2}>"


def print_map(coordinates):
    """Prints map with coordinates. Not needed for solution itself."""
    for j in range(10):
        for i in range(10):
            if (i, j) in coordinates:
                print(coordinates[(i, j)], end=" ")
            else:
                print(".", end=" ")
        print()


def generate_coordinates(vent):
    coordinates = []
    step = 1
    if vent.is_horizontal:
        if vent.x1 > vent.x2:
            step = -1
        for x in range(vent.x1, vent.x2 + step, step):
            coordinates.append((x, vent.y1))
    elif vent.is_vertical:
        if vent.y1 > vent.y2:
            step = -1
        for y in range(vent.y1, vent.y2 + step, step):
            coordinates.append((vent.x1, y))
    elif vent.is_diagonal:
        coordinates.append((vent.x1, vent.y1))
        step_x = 1 if vent.x1 < vent.x2 else -1
        step_y = 1 if vent.y1 < vent.y2 else -1
        for multiplicator in range(1, abs(vent.x1 - vent.x2)+1):
            coor = (vent.x1 + multiplicator * step_x), (vent.y1 + multiplicator * step_y)
            coordinates.append(coor)
    return coordinates


def get_list_with_hydro_vents(input):
    hydro_vents_list = []        
    for line in input:
        from_to = line.replace(" -> ", ",").split(",")
        vent = HydroVent(int(from_to[0]),
                        int(from_to[1]),
                        int(from_to[2]),
                        int(from_to[3]))
        hydro_vents_list.append(vent)
    return hydro_vents_list


#Puzzle input
puzzle_input = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    for line in data:
        puzzle_input.append(line.strip())

#Puzzle 1
hydro_vents_list = get_list_with_hydro_vents(puzzle_input)
coordinates_counts = {}
for vent in hydro_vents_list:
    if vent.is_diagonal:
        continue
    coor = generate_coordinates(vent)
    for c in coor:
        if c in coordinates_counts:
            coordinates_counts[c] += 1
        else:
            coordinates_counts[c] = 1

result = 0
for v in coordinates_counts.values():
    if v > 1:
        result +=1

print(f"Puzzle 1 = {result}")


#Puzzle 2
hydro_vents_list = get_list_with_hydro_vents(puzzle_input)

coordinates_counts = {}
for vent in hydro_vents_list:
    coor = generate_coordinates(vent)
    for c in coor:
        if c in coordinates_counts:
            coordinates_counts[c] += 1
        else:
            coordinates_counts[c] = 1

result = 0
for v in coordinates_counts.values():
    if v > 1:
        result +=1
print(f"Puzzle 2 = {result}")