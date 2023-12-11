from re import findall


def get_combinations_for_four_ingredients():
    output = []
    for i in range(101):
        for j in range(101):
            for k in range(101):
                l = 100 - i - j - k
                if 0 <= l <= 100:
                    output.append((i, j, k, l))
    return output


path = "AdventOfCode2015/day15/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

ingredients = []
pattern = r"-?\d+"
for line in data:
    numbers = [int(x) for x in findall(pattern, line)]
    ingredients.append(numbers)


highest_score = 0
cookie_500_highest_score = 0
for (i, j, k, l) in get_combinations_for_four_ingredients():
    score = 1
    for index in range(len(ingredients[0]) - 1):
        score_ingredient = max(0, ingredients[0][index] * i + ingredients[1][index] * j + ingredients[2][index] * k + ingredients[3][index] * l)
        score *= score_ingredient
    cookie_score = ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l
    if score > highest_score:
        highest_score = score
    if cookie_score == 500 and cookie_500_highest_score < score:
        cookie_500_highest_score = score

print("Puzzle 1 =", highest_score)
print("Puzzle 2 =", cookie_500_highest_score)
