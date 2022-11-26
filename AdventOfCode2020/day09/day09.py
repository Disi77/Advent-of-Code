from itertools import combinations


with open("day09_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [int(x) for x in f.readlines()]


def get_number(input_data):
    preambule = []
    for index, num in enumerate(input_data):
        if index < 25:
            preambule.append(num)
            continue
        for result in combinations(preambule, 2):
            if sum(result) == num:
                preambule.pop(0)
                preambule.append(num)
                break
        else:
            return num


def get_encryption_weakness(input_data, result):
    for start in range(len(input_data)):
        for end in range(start + 2, len(input_data)):
            if sum(input_data[start:end]) == result:
                num_min = min(input_data[start:end])
                num_max = max(input_data[start:end])
                return num_min + num_max


result = get_number(input_data)
print(f"Part 1 - puzzle answer is {result}")

result2 = get_encryption_weakness(input_data, result)
print(f"Part 2 - puzzle answer is {result2}")
