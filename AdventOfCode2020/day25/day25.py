input_data = """
19774466
7290641
"""

public_key_card, public_key_door = [int(x) for x in input_data.strip().split("\n")]
subject_number = 7

loop_size_card = 0
temp_public_key_card = 1
while True:
    loop_size_card += 1
    temp_public_key_card *= subject_number
    temp_public_key_card = temp_public_key_card % 20201227
    if temp_public_key_card == public_key_card:
        break

print("Loop size card", loop_size_card)

loop_size_door = 0
temp_public_key_door = 1
while True:
    loop_size_door += 1
    temp_public_key_door *= subject_number
    temp_public_key_door = temp_public_key_door % 20201227
    if temp_public_key_door == public_key_door:
        break

print("Loop size door", loop_size_door)

subject_number = public_key_door
encryption_key_door = 1
for i in range(loop_size_card):
    encryption_key_door *= subject_number
    encryption_key_door = encryption_key_door % 20201227

print("Encryption key door", encryption_key_door)

subject_number = public_key_card
encryption_key_card = 1
for i in range(loop_size_door):
    encryption_key_card *= subject_number
    encryption_key_card = encryption_key_card % 20201227

print("Encryption key card", encryption_key_card)
