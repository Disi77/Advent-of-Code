path = "AdventOfCode2015/day08/input.txt"

strings = []
with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        strings.append(line.strip())

result = 0
for s in strings:
    result += len(s) - len(eval(s))

print("Puzzle 1 =", result)


result = 0
for s in strings:
    # 4 is difference between "" and "\"\""
    result += 4
    s = s[1:-1]  # remove "" around string 
    if "\\\\" in s:
        result += s.count("\\\\") * 2  # 2 is difference between <a\"a> and <a\\\"a>
        s = s.replace("\\\\", "")
    if "\\\"" in s:
        result += s.count("\\\"") * 2  # 2 is difference between <a\\a> and <a\\\\a>
        s = s.replace("\\\"", "")
    result += s.count("\\x")  # 1 is difference between <\x27> and <\\x27>

print("Puzzle 2 =", result)
