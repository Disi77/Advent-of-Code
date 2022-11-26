#Puzzle input
points = []
with open("input.txt", mode="r", encoding="utf-8") as file:
    for row in file:
        r = []
        for num in row.strip():
            r.append(int(num))
        points.append(r)


#Puzzle 1
def is_low_point(points, i, j):
    directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for y, x in directions:
        if y not in range(len(points)) or x not in range(len(points[0])):
            continue
        if points[i][j] >= points[y][x]:
            return False
    return True

low_points = []
risk_level_sum = 0
for i, row in enumerate(points):
    for j, num in enumerate(row):
        if is_low_point(points, i, j):
            low_points.append((i, j))
            risk_level_sum += points[i][j] + 1
        

print(f"Puzzle 1 = {risk_level_sum}")


#Puzzle 2
def find_size_of_basin(basin, points, i, j):
    directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for y, x in directions:
        if y not in range(len(points)) or x not in range(len(points[0])):
            continue
        if points[y][x] == 9:
            continue
        if (y, x) in basin:
            continue
        basin.append((y, x))
        find_size_of_basin(basin, points, y, x)
    return
        

basin_sizes = []
for i, j in low_points:
    basin = [(i, j)]
    find_size_of_basin(basin, points, i, j)
    size = len(basin)
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)
result = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(f"Puzzle 2 = {result}")