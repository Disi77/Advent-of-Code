def print_boards(boards):
    for board in boards:
        for row in board:
            for num in row:
                if num == "X":
                    print(" X ", end="")
                else:
                    print(f"{num:2} ", end="")
            print()
        print()
    print()        


def round(number, boards):
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for n, num in enumerate(row):
                if num == number:
                    boards[b][r][n] = "X"  


def find_bingo(board):
    for b in board, transpose_table(board):
        for row in b:
            try:
                bingo = "".join(row)
                if bingo == 5 * "X":
                    return True
            except TypeError:
                pass
    return False


def transpose_table(board):
    new_table = []
    for i in range(len(board[0])):
        new_row = []
        for j in range(len(board)-1, -1, -1):
            new_row.append(board[j][i])
        new_table.append(new_row)
    return new_table


def sum_unmarked_numbers(board):
    result = 0
    for row in board:
        for value in row:
            if value == "X":
                continue
            result += value
    return result


#Puzzle input
with open("input.txt", encoding="utf-8", mode="r") as file:
    data = file.read().split("\n\n")

numbers = []
for num in data.pop(0).split(","):
    numbers.append(int(num))

boards = []
for board in data:
    new_board = []
    for row in board.split("\n"):
        new_row = []
        for num in row.split():
            new_row.append(int(num))
        new_board.append(new_row)
    boards.append(new_board)


# Puzzle 1
is_bingo = False
for num in numbers:
    round(num, boards)
    for board in boards:
        if find_bingo(board):
            is_bingo = True
            break
    if is_bingo:
        break

result = sum_unmarked_numbers(board)
print("Puzzle 1 = ", result * num)


# Puzzle 2
winners = []
for num in numbers:
    round(num, boards)
    for i, board in enumerate(boards):
        if i in winners:
            continue
        if find_bingo(board):
            winners.append(i)
    if len(winners) == len(boards):
        break

result = sum_unmarked_numbers(boards[winners[-1]])
print("Puzzle 2 = ", result * num)