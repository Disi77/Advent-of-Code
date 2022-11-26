# ------------- Solution 1 ----------------
def lanternfish_family(rounds, main_state):
    for _ in range(rounds):
        temp = {}
        for num in main_state:
            if num == 0:
                next_state = 6
                if next_state in temp:
                    temp[next_state] += main_state[num]
                else:
                    temp[next_state] = main_state[num]
                temp[8] = main_state[num]
            else:
                next_state = num - 1
                if next_state in temp:
                    temp[next_state] += main_state[num]
                else:
                    temp[next_state] = main_state[num]
        main_state = temp.copy()

    result = 0
    for _, v in main_state.items():
        result += v
    
    return result


#Puzzle input
puzzle_input = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    raw = data.read()

for num in raw.split(","):
    puzzle_input.append(int(num))

main_state = {}
for num in puzzle_input:
    if num in main_state:
        main_state[num] += 1
    else:
        main_state[num] = 1

#Puzzle 1
rounds = 80
result = lanternfish_family(rounds, main_state)
print(f"Puzzle 1 = {result}")

#Puzzle 2
rounds = 256
result = lanternfish_family(rounds, main_state)
print(f"Puzzle 2 = {result}")

# ------------- Solution 2 ----------------
with open("input.txt", encoding="utf-8", mode="r") as data:
    raw = data.read()

puzzle_input = [0] * 9
for num in raw.split(","):
    puzzle_input[int(num)] += 1

puzzles_rounds = {1: 80, 2: 256}

for puzzle, rounds in puzzles_rounds.items():
    state = puzzle_input.copy()
    for _ in range(rounds):
        new = [state[1],
            state[2],
            state[3],
            state[4],
            state[5],
            state[6],
            state[7] + state[0],
            state[8],
            state[0]
        ]
        for i in range(len(state)):
            state[i] = new[i]

    print(f"Puzzle {puzzle} = {sum(state)}")
    
