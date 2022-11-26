# Using Dijkstra's algorithm for finding the shortest paths between nodes in a graph
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

def get_puzzle_input():
    grid = []
    with open("input.txt", mode="r", encoding="utf-8") as file:
        for row in file:
            numbers = [int(x) for x in row.strip()]
            grid.append(numbers)
    return grid

def expand_grid(grid):
    new_grid = []
    orig_size = len(grid)
    size = orig_size * 5
    for i in range(size):
        new_row = []
        for j in range(size):
            if i < orig_size and j < orig_size:
                new_item = grid[i][j]
            else:
                temp_i = i % orig_size
                temp_j = j % orig_size
                new_item = grid[temp_i][temp_j] + i // orig_size + j // orig_size
                while new_item > 9:
                    new_item -= 9
            new_row.append(new_item)
        new_grid.append(new_row)
    return new_grid


def get_list_of_nodes(grid):
    nodes = {}
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            coor = (i, j)
            nodes[coor] = []
            directions = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            for new_i, new_j in directions:
                if new_i in range(0, len(grid)) and new_j in range(0, len(grid)):
                    pair = (new_i, new_j), grid[new_i][new_j]
                    nodes[coor].append(pair)
    return nodes


def dijkstra_shortest_path_puzzle1(nodes, pointer):
    visited, temp = set(), set()
    distance = {pointer: 0}
    while True:
        visited.add(pointer)
        for coor, dist in nodes[pointer]:
            if coor in visited:
                continue
            temp.add(coor)
            new_distance = distance[pointer] + dist
            if coor not in distance or new_distance < distance[coor]:
                distance[coor] = new_distance
        if pointer in temp:
            temp.remove(pointer)
        if not temp:
            break

        min_distance = None
        index = 0

        for node in temp:
            if not min_distance or distance[node] < min_distance:
                min_distance = distance[node]
                index = node
        
        pointer = index
    return distance


# Puzzle 1
grid = get_puzzle_input()
nodes = get_list_of_nodes(grid)

start = (0, 0)
end = (len(grid) - 1, len(grid) - 1)

result = dijkstra_shortest_path_puzzle1(nodes, start)   
print(f"Puzzle 1 = {result[end]}")


# Puzzle 2
grid = get_puzzle_input()
grid = expand_grid(grid)
nodes = get_list_of_nodes(grid)

end = (len(grid) - 1, len(grid) - 1)

result = dijkstra_shortest_path_puzzle1(nodes, start)
print(f"Puzzle 2 = {result[end]}")
