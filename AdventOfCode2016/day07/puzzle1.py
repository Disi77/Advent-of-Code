from re import findall


def abba_in_string(str):
    '''
    Return True if string contains ABBA string.
    An ABBA is any four-character sequence which consists of a pair of two 
    different characters followed by the reverse of that pair, 
    such as xyyx or abba.
    '''
    for i in range(2, len(str) - 1):
        first = str[i - 2:i]
        second = str[i:i + 2]
        if first[0] == first[1]:
            continue
        if first[0] == second[1] and first[1] == second[0]:
            return True
    return False


def split_string_by_brackets(str):
    '''
    Splits a string using brackets and returns two lists.
    First contains substrings outside brackets and second
    substrings inside brackets.
    '''
    inside_brackets = r"[\[]([a-z]+)[\]]"
    str_inside = findall(inside_brackets, str)
    for s in str_inside:
        str = str.replace(f"[{s}]", "|")
    str_outside = str.split("|")
    return str_outside, str_inside


def supports_tls(ip):
    str_outside, str_inside = split_string_by_brackets(ip)
    for s in str_inside:
        if abba_in_string(s):
            return False
    for s in str_outside:
        if abba_in_string(s):
            return True


path = "AdventOfCode2016/day07/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

result = 0
for ip in data:
    if supports_tls(ip):
        result += 1
    
print("Puzzle 1 =", result)
