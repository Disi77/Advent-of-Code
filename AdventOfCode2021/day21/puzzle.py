class Player():
    def __init__(self, start_position):
        self.position = start_position
        self.score = 0
    
    def roll_and_move(self, dice):
        sum = 0
        for _ in range(3):
            dice.next()
            sum += dice.score
        self.position += sum % 10
        if self.position > 10:
            self.position -= 10
        self.score += self.position
    

class Dice():
    def __init__(self):
        self.score = 100
        self.counter = 0
    
    def next(self):
        self.counter += 1
        self.score = 1 if self.score == 100 else self.score + 1

    

# Puzzle input
puzzle_input = """
Player 1 starting position: 2
Player 2 starting position: 7
"""
start = [int(x.split()[4]) for x in puzzle_input.strip().split("\n")]


# Puzzle 1
dice = Dice()
player1 = Player(start[0])
player2 = Player(start[1])

while True:
    player1.roll_and_move(dice)
    if player1.score >= 1000:
        break
    player2.roll_and_move(dice)
    if player2.score >= 1000:
        break

result = min(player1.score, player2.score) * dice.counter
print(f"Puzzle 1 = {result}")


#Puzzle 2

# after player 3x rolling = new 27 universes are created and in each universe the sum of outcome of the die
# is product from [1, 2, 3] => 111, 112, 113, 121, 122, 123, 131, 132, 133, 
#                              211, 212, 213, 221, 222, 223, 231, 232, 233, 
#                              311, 312, 313, 321, 322, 323, 331, 332, 333
# sums are:                     3    4    5    4    5    6    5    6    7
#                               4    5    6    5    6    7    6    7    8
#                               5    6    7    6    7    8    7    8    9
# we get 7 different states:    sum 3 = 1x      sum 4 = 3x     sum 5 = 6x     sum 6 = 7x
#                               sum 9 = 1x      sum 8 = 3x     sum 7 = 6x  

from itertools import product
from collections import Counter

combinations = Counter([sum(x) for x in list(product([1, 2, 3], repeat=3))])

game_states = {}
P1_score = P2_score = 0
P1_position, P2_position = start
key = (P1_position, P2_position, P1_score, P2_score)
game_states[key] = 1

round = 0
wins = [0, 0]

while game_states:
    new_game_states = {}
    for key, g in game_states.items():
        
        for outcome in combinations:
            index = round % 2
            new_pos = key[index] + outcome
            while new_pos > 10:
                new_pos -= 10
            new_score = key[index + 2] + new_pos

            if round % 2 == 0:
                new_key = (new_pos, key[1], new_score, key[3])
            else:
                new_key = (key[0], new_pos, key[2], new_score)

            if new_key in new_game_states:
                new_game_states[new_key] += g * combinations[outcome]
            else:
                new_game_states[new_key] = g * combinations[outcome]
    
    game_states = {}
    for k, g in new_game_states.items():
        if k[2] >= 21: wins[0] += g
        elif k[3] >= 21: wins[1] += g
        else: game_states[k] = g
    
    round += 1


print(f"Puzzle 2 =", max(wins))
