with open("day10_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [int(x) for x in f.readlines()]


input_data.append(0)
input_data.append(max(input_data) + 3)
input_data.sort()

results = []

while input_data:
    for index, value in enumerate(input_data[:-1]):
        if not input_data[index + 1] - 1 == value:
            break
    group = input_data[:index+1]
    input_data = input_data[index+1:]
    if len(group) > 2:
        results.append(len(group))

total_num = 1
for group_len in results:
    if group_len == 3:
        total_num *= 2
    if group_len == 4:
        total_num *= 4
    if group_len == 5:
        total_num *= 7

print(f"Part 2 - puzzle answer is {total_num}")
