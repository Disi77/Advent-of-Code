from itertools import combinations


with open("day01_input.txt", encoding="utf-8", mode="r") as f:
    content = f.read().strip().split("\n")

numbers = [int(x) for x in content]


def sum_is_2020(numbers, x):
    for item in combinations(numbers, x):
        if sum(item) == 2020:
            return item


num1, num2 = sum_is_2020(numbers, 2)
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} * {num2} = {num1*num2}")

num1, num2, num3 = sum_is_2020(numbers, 3)
print(f"{num1} + {num2} + {num3} = {num1+num2+num3}")
print(f"{num1} * {num2} * {num3} = {num1*num2*num3}")
