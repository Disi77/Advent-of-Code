import re

with open("day02_input.txt", encoding="utf-8", mode="r") as f:
    content = f.readlines()

count = 0
for line in content:
    psw_obj = re.match(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]*)", line)
    pos1, pos2, char, psw = psw_obj.groups()
    occurence = 0
    for p in pos1, pos2:
        try:
            if psw[int(p)-1] == char:
                occurence += 1
        except IndexError:
            pass
    if occurence == 1:
        count += 1
print(count)
