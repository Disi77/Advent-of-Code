from pathlib import Path


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text()

path = []
folders = {}
for i in instructions.split("\n"):
    if i == "$ ls" or "dir " in i:
        continue
    if i == "$ cd ..":
        del path[-1]
        continue
    if "$ cd " in i:
        path.append(i.split()[-1])
        continue
    size = i.split()[0]
    for i in range(len(path), 0, -1):
        f_path = "/".join(path[:i])
        folders[f_path] = folders.get(f_path, 0) + int(size)


result = sum([size for size in folders.values() if size < 100_000])
print("Puzzle 1 =", result)

we_need = 30_000_000 - (70_000_000 - folders["/"])
result = min([size for size in folders.values() if size > we_need])
print("Puzzle 2 =", result)
