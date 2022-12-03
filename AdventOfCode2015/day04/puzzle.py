import hashlib


secret_prefix = "yzbqklnj"

for num in range(10 ** 8):
    secret_key = secret_prefix + str(num)
    result = hashlib.md5(secret_key.encode())
    if result.hexdigest()[:5] == "00000":
        break

print("Puzzle 1 =", num)

for num in range(num, 10 ** 8):
    secret_key = secret_prefix + str(num)
    result = hashlib.md5(secret_key.encode())
    if result.hexdigest()[:6] == "000000":
        break

print("Puzzle 2 =", num)