with open("day22_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read()

player1, player2 = input_data.strip().split("\n\n")
player1 = [int(x) for x in player1.strip().split("\n")[1:]]
player2 = [int(x) for x in player2.strip().split("\n")[1:]]


while True:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.extend([card1, card2])
    else:
        player2.extend([card2, card1])

    if not player1 or not player2:
        break

winner = player1 + player2
result = 0
for i in range(1, len(winner) + 1):
    result += winner[-i] * i

print(f"The winning score is {result}")
