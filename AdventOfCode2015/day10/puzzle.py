def split_numbers(number):
    number += "."
    result = []
    buffer = ""
    for i in range(len(number) - 1):
        buffer += number[i]
        if number[i] != number[i + 1]:
            result.append(buffer)
            buffer = ""
    return result


def create_new_number(numbers_list):
    result = ""
    for item in numbers_list:
        result += str(len(item))
        result += item[0]
    return result


number = "1113122113"

for i in range(50):
    temp = split_numbers(number)
    number = create_new_number(temp)
    if i == 39:
        print("Puzzle 1", len(number))

print("Puzzle 2", len(number))