# read data
path = "AdventOfCode2024/day09/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read()

# prepare initial state of disk map
file = True
id_counter = 0
disk_map = []
for item in data:
    if file:
        for i in range(int(item)):
            disk_map.append(id_counter)
        file = False
        id_counter += 1
    else:
        for i in range(int(item)):
            disk_map.append(None)
        file = True

# move file blocks
none_count = disk_map.count(None)
filesystem_len = len(disk_map) - none_count

for i in range(filesystem_len):
    if disk_map[i] == None:
        while True:
            block = disk_map.pop()
            if block:
                disk_map[i] = block
                break

# calculate checksum
disk_map = disk_map[:filesystem_len]
checksum = 0
for i, block in enumerate(disk_map):
    checksum += i * block

print("Puzzle 1 =", checksum)
