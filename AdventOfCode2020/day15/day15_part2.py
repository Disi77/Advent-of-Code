numbers = [0, 8, 15, 2, 12, 1, 4]

end_turn = 30_000_000
start_turn = len(numbers) + 1

numbers_dict = {}
for index, num in enumerate(numbers):
    numbers_dict[num] = [index+1]

last = numbers[-1]
for turn in range(start_turn, end_turn + 1):
    if len(numbers_dict[last]) == 1:
        last = 0
    else:
        last = numbers_dict[last][1] - numbers_dict[last][0]

    if last not in numbers_dict:
        numbers_dict[last] = [turn]
    else:
        numbers_dict[last].append(turn)

    if len(numbers_dict[last]) > 2:
        numbers_dict[last].pop(0)

print(f"THe 30,000,000th number is {last}")
