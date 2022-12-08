from pathlib import Path


def tree_is_visible(i, j, rows):
    tree = rows[i][j]
    row_count = len(rows)
    col_count = len(rows[0])

    is_higher = [False, False, False, False]
    # up
    for row in range(i - 1, -1, -1):
        if tree <= rows[row][j]:
            is_higher[0] = True
            break
    # down
    for row in range(i + 1, row_count):
        if tree <= rows[row][j]:
            is_higher[1] = True
            break
    # left
    for col in range(j - 1, -1, -1):
        if tree <= rows[i][col]:
            is_higher[2] = True
            break
    # right
    for col in range(j + 1, col_count):
        if tree <= rows[i][col]:
            is_higher[3] = True
            break

    return sum(is_higher) < 4


def scenic_score(i, j, rows):
    tree = rows[i][j]
    row_count = len(rows)
    col_count = len(rows[0].strip())

    score = [0, 0, 0, 0]
    # up
    for row in range(i - 1, -1, -1):
        if tree > rows[row][j]:
            score[0] += 1
        elif tree <= rows[row][j]:
            score[0] += 1
            break
    # down
    for row in range(i + 1, row_count):
        if tree > rows[row][j]:
            score[1] += 1
        elif tree <= rows[row][j]:
            score[1] += 1
            break
    # left
    for col in range(j - 1, -1, -1):
        if tree > rows[i][col]:
            score[2] += 1
        elif tree <= rows[i][col]:
            score[2] += 1
            break
    # right
    for col in range(j + 1, col_count):
        if tree > rows[i][col]:
            score[3] += 1
        elif tree <= rows[i][col]:
            score[3] += 1
            break
    return score[0] * score[1] * score[2] * score[3]


here = Path(__file__).parent
forest = Path(here / "input.txt").read_text().split()

visible = 0
for i in range(len(forest)):
    for j in range(len(forest[0])):
        visible += tree_is_visible(i, j, forest)

print("Puzzle 1 =", visible)


score = 0
for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree_scenic_score = scenic_score(i, j, forest)
        if tree_scenic_score > score:
            score = tree_scenic_score
            
print("Puzzle 2 =", score)