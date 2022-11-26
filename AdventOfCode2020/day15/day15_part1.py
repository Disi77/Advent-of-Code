numbers = [0, 8, 15, 2, 12, 1, 4]

end_turn = 2020
start_turn = len(numbers)


def get_2_last_index(numbers):
    indexes = []
    last_num = numbers[-1]
    for i, num in enumerate(numbers):
        if last_num == num:
            indexes.append(i)
    return indexes[-1], indexes[-2]


for turn in range(start_turn, end_turn):
    last_num = numbers[-1]
    last_count_in_numbers = numbers.count(last_num)
    if last_count_in_numbers == 1:
        numbers.append(0)
        continue
    last_index, second_last_index = get_2_last_index(numbers)
    numbers.append(last_index - second_last_index)

print(f"THe 2020th number is {numbers[-1]}")
