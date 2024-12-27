def calculate_perimeter(region):
    if len(region) in [1, 2]:
        return 4
    
    region.sort()
    perimeter = 0

    top_sides = []
    bottom_sides = []
    left_sides = []
    right_sides = []

    for (i, j) in region:
        if (i-1, j) not in region:
            top_sides.append((i, j))
        if (i+1, j) not in region:
            bottom_sides.append((i, j))
        if (i, j-1) not in region:
            left_sides.append((i, j))
        if (i, j+1) not in region:
            right_sides.append((i, j))
    
    # top + bottom sides calculation
    for side_coors in top_sides, bottom_sides:
        row, col = side_coors[0]
        perimeter += 1
        for (i, j) in side_coors:
            if row == i:
                if col not in [j, j - 1]:
                    perimeter += 1
            else:
                row = i
                perimeter += 1
            col = j
    
    # left + right sides calculation
    for side_coors in left_sides, right_sides:
        side_coors = sorted(side_coors, key=lambda coor: coor[1])
        row, col = side_coors[0]
        perimeter += 1
        for (i, j) in side_coors:
            if col == j:
                if row not in [i, i - 1]:
                    perimeter += 1
            else:
                col = j
                perimeter += 1
            row = i

    return perimeter


path = "AdventOfCode2024/day12/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    garden_plots_coors = {}
    coors = set()
    for i, row in enumerate(raw_data):
        for j, plant in enumerate(row.strip()):
            garden_plots_coors[(i, j)] = plant
            coors.add((i, j))
        
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

regions = []
while coors:
    region = []
    i, j = coors.pop()
    plant = garden_plots_coors[(i, j)]
    region.append((i, j))
    while True:
        region_changed = False
        for (i0, j0) in region:
            for (di, dj) in DIRECTIONS:
                i1, j1 = i0 + di, j0 + dj
                if (i1, j1) not in region and (i1, j1) in garden_plots_coors and garden_plots_coors[(i1, j1)] == plant:
                    region.append((i1, j1))
                    coors.remove((i1, j1))
                    region_changed = True
            if region_changed:
                break
        else:
            break
    regions.append(region)


total_price = 0
for region in regions:
    total_price += len(region) * calculate_perimeter(region)

print("Puzzle 2 =", total_price)
