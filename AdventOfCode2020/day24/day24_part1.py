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


black_tiles = []

for line in input_data:
    tile = get_coordinates_of_tile(line)
    if tile in black_tiles:
        black_tiles.remove(tile)
    else:
        black_tiles.append(tile)

print("How many tiles are left with the black side up?")
print(len(black_tiles))
