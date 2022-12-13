from pathlib import Path


def tree_is_visible(i, j, rows):
    tree = rows[i][j]

    is_higher = 0
    # up
    for row in range(i - 1, -1, -1):
        if tree <= rows[row][j]:
            is_higher += 1
            break
    # down
    for row in range(i + 1, len(rows)):
        if tree <= rows[row][j]:
            is_higher += 1
            break
    # left
    for col in range(j - 1, -1, -1):
        if tree <= rows[i][col]:
            is_higher += 1
            break
    # right
    for col in range(j + 1, len(rows[0])):
        if tree <= rows[i][col]:
            is_higher += 1
            break

    return is_higher < 4


def scenic_score(i, j, rows):
    tree = rows[i][j]

    score = [0, 0, 0, 0]
    # up
    for row in range(i - 1, -1, -1):
        score[0] += 1
        if tree <= rows[row][j]:
            break
    # down
    for row in range(i + 1, len(rows)):
        score[1] += 1
        if tree <= rows[row][j]:
            break
    # left
    for col in range(j - 1, -1, -1):
        score[2] += 1
        if tree <= rows[i][col]:
            break
    # right
    for col in range(j + 1, len(rows[0].strip())):
        score[3] += 1
        if tree <= rows[i][col]:
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