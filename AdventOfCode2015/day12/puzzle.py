from pathlib import Path

here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text()


def sum_numbers_in_string(s):
    n = ""
    result = 0
    for i in s:
        if i.isdigit() or i == "-":
            n += i
        else:
            if n:
                result += int(n)
                n = ""
    return result


def remove_red(s): 
    while s.count(':"red"') > 0:
        start = end = s.index(':"red"')
        brackets = ""
        for i in range(start, -1, -1):
            c = s[i]
            if c == "}":
                brackets += c
            elif c == "{":
                if not brackets:
                    start = i
                    break
                else:
                    brackets = brackets[:-1]
        for i in range(end, len(s)):
            c = s[i]
            if c == "{":
                brackets += c
            elif c == "}":
                if not brackets:
                    end = i
                    break
                else:
                    brackets = brackets[:-1]
        s = s.replace(s[start: end + 1], "")
    return s


print("Puzzle 1 =", sum_numbers_in_string(puzzle_input))

puzzle_input = remove_red(puzzle_input)
print("Puzzle 2 =", sum_numbers_in_string(puzzle_input))