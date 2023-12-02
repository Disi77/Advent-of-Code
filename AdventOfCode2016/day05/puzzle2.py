from hashlib import md5

door_id = "uqwqemis"

psw = 8 * [None]

for i in range(10 ** 6, 10 ** 10):
    str_to_hash = door_id + str(i)
    hash = md5(str_to_hash.encode()).hexdigest()

    if hash.startswith("00000"):
        position = hash[5]
        if not position.isdigit():
            continue
        position = int(position)
        if position not in range(8):
            continue
        if psw[position] is not None:
            continue

        char = hash[6]
        psw[position] = char

        if None not in psw:
            break

print("Puzzle 2 =", "". join(psw))
