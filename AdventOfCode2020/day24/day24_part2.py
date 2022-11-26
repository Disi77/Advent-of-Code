with open("day24_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()


def get_coordinates_of_tile(line):
    r"""     if A row is even
       / \ / \
      | * | * |       (-1, 1)     (0, 1)
     / \ / \ / \
    | * | A | * |   (-1, 0)  (0, 0)  (1, 0)
     \ / \ / \ /
      | * | * |       (-1, -1)    (0, -1)
       \ / \ /

              if B row is odd
       / \ / \
      | * | * |       (0, 1)     (1, 1)
     / \ / \ / \
    | * | B | * |   (-1, 0)  (0, 0)  (1, 0)
     \ / \ / \ /
      | * | * |       (0, -1)    (1, -1)
       \ / \ /
    """

    line = line.strip()
    x = y = index = 0
    while index < len(line):
        dir = line[index]
        if dir not in DIR_ROW_EVEN:
            dir = line[index:index+2]
            index += 1
        index += 1
        if y % 2 == 0:
            x += DIR_ROW_EVEN[dir][0]
            y += DIR_ROW_EVEN[dir][1]
        else:
            x += DIR_ROW_ODD[dir][0]
            y += DIR_ROW_ODD[dir][1]
    return (x, y)


def black_around(black_tiles, tile):
    """
    Returns count of black tiles around tile.
    """
    black_neighbours = 0
    if tile[1] % 2 == 0:
        DIRECTIONS = dict(DIR_ROW_EVEN)
    else:
        DIRECTIONS = dict(DIR_ROW_ODD)
    for value in DIRECTIONS.values():
        new_tile = (tile[0] + value[0], tile[1] + value[1])
        if new_tile in black_tiles:
            black_neighbours += 1
            if black_neighbours == 3:
                break
    return black_neighbours


def change_of_tiles(black_tiles):
    """
    Returns list of black_tiles after 1 day.
    """
    black_to_remove = []
    black_to_add = []

    for tile in black_tiles:
        result = black_around(black_tiles, tile)
        if result == 0 or result == 3:
            black_to_remove.append(tile)

        if tile[1] % 2 == 0:
            DIRECTIONS = dict(DIR_ROW_EVEN)
        else:
            DIRECTIONS = dict(DIR_ROW_ODD)

        for value in DIRECTIONS.values():
            new_tile = (tile[0] + value[0], tile[1] + value[1])
            if new_tile not in black_tiles and new_tile not in black_to_add:
                result = black_around(black_tiles, new_tile)
                if result == 2:
                    black_to_add.append(new_tile)

    for item in black_to_remove:
        black_tiles.remove(item)

    for item in black_to_add:
        black_tiles.append(item)

    return black_tiles


black_tiles = []

DIR_ROW_EVEN = {"nw": (-1, 1),
                "w": (-1, 0),
                "sw": (-1, -1),
                "ne": (0, 1),
                "e": (1, 0),
                "se": (0, -1)}

DIR_ROW_ODD = {"nw": (0, 1),
               "w": (-1, 0),
               "sw": (0, -1),
               "ne": (1, 1),
               "e": (1, 0),
               "se": (1, -1)}

for line in input_data:
    tile = get_coordinates_of_tile(line)
    if tile in black_tiles:
        black_tiles.remove(tile)
    else:
        black_tiles.append(tile)


for i in range(1, 101):
    print("Calculating day", i)
    black_tiles = change_of_tiles(black_tiles)


print("How many tiles will be black after 100 days?")
print(len(black_tiles))
