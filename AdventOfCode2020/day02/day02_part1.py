import re

with open("day02_input.txt", encoding="utf-8", mode="r") as f:
    content = f.readlines()

count = 0
for line in content:
    psw_obj = re.match(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]*)", line)
    start, end, char, psw = psw_obj.groups()
    if int(start) <= psw.count(char) <= int(end):
        count += 1

print(count)
