path = "AdventOfCode2024/day12/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    garden_plots_coors = {}
    coors = set()
    for i, row in enumerate(raw_data):
        for j, plant in enumerate(row.strip()):
            garden_plots_coors[(i, j)] = plant
            coors.add((i, j))
        
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

regions = []
while coors:
    region = []
    i, j = coors.pop()
    plant = garden_plots_coors[(i, j)]
    region.append((i, j))
    while True:
        region_changed = False
        for (i0, j0) in region:
            for (di, dj) in directions:
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
    area = len(region)
    perimeter = 0
    for (i, j) in region:
        for (di, dj) in directions:
            if (i + di, j + dj) not in region:
                perimeter += 1
    total_price += area * perimeter

print("Puzzle 2 =", total_price)
