with open("day22_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read()


# Create dictionary with cards for both players from input data
player1, player2 = input_data.strip().split("\n\n")
game = {}
game["Player 1"] = [int(x) for x in player1.strip().split("\n")[1:]]
game["Player 2"] = [int(x) for x in player2.strip().split("\n")[1:]]


def play_game(game):
    """
    Play cards. Higher card wins. If value on the cards for both players
    is same or lower than count of cards players have in package, then
    the sub-game is playing. Result of subgame determine winner of parent game.
    If the game is in infinitive loop, then the winner is automatically
    the player 1.
    """
    temp = []
    while True:
        card1 = game["Player 1"].pop(0)
        card2 = game["Player 2"].pop(0)
        if card1 <= len(game["Player 1"]) and card2 <= len(game["Player 2"]):
            new_game = game.copy()
            new_game["Player 1"] = new_game["Player 1"][:card1]
            new_game["Player 2"] = new_game["Player 2"][:card2]
            who_wins = play_game(new_game)
            if "1" in who_wins:
                game["Player 1"].extend([card1, card2])
            else:
                game["Player 2"].extend([card2, card1])

        else:
            if card1 > card2:
                game["Player 1"].extend([card1, card2])
            else:
                game["Player 2"].extend([card2, card1])

        if not game["Player 1"]:
            return "Player 2 wins"

        if not game["Player 2"]:
            return "Player 1 wins"

        blueprint = ", ".join(str(x) for x in game["Player 1"]) + " " + ", ".join(str(x) for x in game["Player 2"])
        if blueprint not in temp:
            temp.append(blueprint)
        else:
            temp = []
            return "Player 1 wins"


who_wins = play_game(game)

winner = game["Player 1"] + game["Player 2"]
result = 0
for i in range(1, len(winner) + 1):
    result += winner[-i] * i


print(who_wins)
print(f"The winning score is {result}")
