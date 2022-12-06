def increment_psw(psw):
    psw = list(psw)
    for i in range(-1, -len(psw) - 1, -1):
        char = psw[i]
        code = ord(char)

        new_code = (code + 1 - ord("a")) % 26 + ord("a")
        new_char = chr(new_code)

        psw[i] = new_char
        if new_code - code == 1:
            break

    return "".join(psw)


def psw_is_valid(psw):
    # psw may not contains the letters "i", "o" or "l"
    if "i" in psw or "o" in psw or "l" in psw:
        return False
    # psw must contain at least 2 differenct non-overlapping pairs
    # of letters
    if len(set(psw)) > 6:
        return False
    pairs = 0
    for l in set(psw):
        if l * 2 in psw:
            pairs += psw.count(l * 2)
    if pairs < 2:
        return False
    # psw must include one increasing straight of at least 
    # 3 letters like "abc"
    for i in range(len(psw) - 2):
        if ord(psw[i]) == ord(psw[i + 1]) - 1 == ord(psw[i + 2]) - 2:
            return True
    return False


psw = "hepxcrrq"

while True:
    psw = increment_psw(psw)
    if psw_is_valid(psw):
        break

print("Puzzle 1 =", psw)

while True:
    psw = increment_psw(psw)
    if psw_is_valid(psw):
        break

print("Puzzle 2 =", psw)
