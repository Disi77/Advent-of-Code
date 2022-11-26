from collections import Counter


class Cave():
    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.is_small = not self.name.isupper()


def create_list_of_caves():
    puzzle_input = []
    with open("input.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            item = line.strip().split("-")
            puzzle_input.append(item)
            puzzle_input.append(item[::-1])

    caves = {}
    for start, end in puzzle_input:
        if end == "start":
            continue
        if start in caves:
            caves[start].children.append(end)
        else:
            caves[start] = Cave(start, [end])

    if "end" in caves:
        del caves["end"]
    
    return caves


def find_paths_puzzle1(cave_count, caves, cave, path):
    path += cave.name + " "
    for p in cave.children:
        if p == "end":
            cave_count +=1
            continue
        if caves[p].is_small and p in path:
            continue
        cave_count = find_paths_puzzle1(cave_count, caves, caves[p], path)
    return cave_count


def find_paths_puzzle2(cave_count, caves, cave, path):
    path += cave.name + " "
    for p in cave.children:
        if p == "end":
            cave_count += 1
            continue
        if caves[p].is_small:
            small = [x for x in path.split() if x.islower()]
            r = Counter(small)
            if 2 in r.values() and p in r:
                continue
        cave_count = find_paths_puzzle2(cave_count, caves, caves[p], path)
    return cave_count

#Puzzle 1
caves = create_list_of_caves()
cave_count = find_paths_puzzle1(0, caves, caves["start"], "")
print(f"Puzzle 1 = {cave_count}")


#Puzzle 2
caves = create_list_of_caves()
cave_count = find_paths_puzzle2(0, caves, caves["start"], "")
print(f"Puzzle 2 = {cave_count}")
