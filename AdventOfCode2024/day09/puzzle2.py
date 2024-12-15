def calculate_checksum(disk_map, SIZE):
    checksum = 0
    pointer = 0
    while pointer < SIZE:
        if pointer in disk_map:
            id = disk_map[pointer]
            for _ in range(files[id]["lenght"]):
                checksum += pointer * id
                pointer += 1
        else:
            pointer += 1
    return checksum

# read data
path = "AdventOfCode2024/day09/input.txt"
with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()
    SIZE = sum([int(x) for x in data])


# prepare initial state
file = True
pointer = id_counter = 0
disk_map = {}
files = {}
spaces = []
for item in data:
    if file:
        disk_map[pointer] = id_counter
        files[id_counter] = {"lenght": int(item), "position": pointer}
        pointer += int(item)
        id_counter += 1
        file = False
    else:
        if int(item) == 0:
            file = True
            continue
        spaces.append({"position": pointer, "lenght": int(item)})
        pointer += int(item)
        file = True

# move file blocks
for id in range(id_counter - 1, -1, -1):
    for i, space in enumerate(spaces):
        if space["position"] >= files[id]["position"]:
            break
        df = space["lenght"] - files[id]["lenght"]
        if df >= 0:
            del disk_map[files[id]["position"]]
            files[id]["position"] = space["position"]
            disk_map[space["position"]] = id
            if df == 0:
                spaces.pop(i)
            else:
                spaces[i] = {"position": space["position"] + files[id]["lenght"], "lenght": df}
            break

# calculate checksum
checksum = calculate_checksum(disk_map, SIZE)
print("Puzzle 2 =", checksum)
