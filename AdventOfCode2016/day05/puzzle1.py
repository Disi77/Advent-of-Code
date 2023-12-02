from hashlib import md5

door_id = "uqwqemis"

psw = ""
for i in range(10 ** 6, 10 ** 10):
    str_to_hash = door_id + str(i)
    hash = md5(str_to_hash.encode()).hexdigest()
    if hash.startswith("00000"):
        psw += hash[5]
        if len(psw) == 8:
            break

print("Puzzle 1 =", psw)
