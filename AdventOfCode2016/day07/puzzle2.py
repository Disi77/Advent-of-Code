from re import findall


def aba_in_string(str):
    '''
    Return list of ABA strings.
    An ABA is any three-character sequence which consists of the same character
    twice with a different character between them, such as xyx or aba.
    '''
    output = []
    for i in range(len(str) - 2):
        char1 = str[i]
        char2 = str[i+1]
        char3 = str[i+2]
        if char1 == char2:
            continue
        if char1 == char3:
            output.append(char1 + char2 + char3)
    return output


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


def supports_ssl(ip):
    str_outside, str_inside = split_string_by_brackets(ip)
    aba_outside = set()
    aba_inside = set()
    for s in str_inside:
        for bab in aba_in_string(s):
            aba = bab[1] + bab[0] + bab[1]
            aba_inside.add(aba)
    for s in str_outside:
        for aba in aba_in_string(s):
            aba_outside.add(aba)
    if aba_outside.intersection(aba_inside):
        return True
    return False


path = "AdventOfCode2016/day07/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

result = 0
for ip in data:
    if supports_ssl(ip):
        result += 1
    
print("Puzzle 2 =", result)
