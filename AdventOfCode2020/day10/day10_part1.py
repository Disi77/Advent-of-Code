with open("day10_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [int(x) for x in f.readlines()]

input_data.append(0)
input_data.append(max(input_data) + 3)
input_data.sort()

diff1 = diff2 = diff3 = 0
for index, value in enumerate(input_data[:-1]):
    if input_data[index+1] - value == 1:
        diff1 += 1
    elif input_data[index+1] - value == 2:
        diff2 += 1
    elif input_data[index+1] - value == 3:
        diff3 += 1

print(diff1, diff3)
print(f"Part 1 - puzzle answer is {diff1 * diff3}")
