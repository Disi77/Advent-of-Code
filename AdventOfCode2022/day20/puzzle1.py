from pathlib import Path


def print_actual_order(numbers):
    temp = list(numbers.values())
    temp.sort(key=lambda x: x[1])
    for n in temp:
        print(n[0], end="  ")
    print() 


# Get puzzle input
here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text().split("\n")

numbers = {}
for index, num in enumerate(puzzle_input):
    numbers[index] = (int(num), index)


# Calculate new indexes
for index in range(len(numbers)):
    num, pos = numbers[index]
    if num == 0:
        continue

    new_pos = (pos + num) % (len(numbers) - 1) 
    if new_pos == 0:
        new_pos = len(numbers) - 1

    if new_pos > pos:
        for k, v in numbers.items():
            number, original_pos = v
            if new_pos + 1 > original_pos > pos:
                numbers[k] = (number, original_pos - 1)
    
    else:
        for k, v in numbers.items():
            number, original_pos = v
            if new_pos - 1 < original_pos < pos:
                numbers[k] = (number, original_pos + 1)

    numbers[index] = (num, new_pos)

# Find indexes 1000, 2000, 3000
for k, v in numbers.items():
    if v[0] == 0:
        index_0 = v[1]
        break

index_1000 = (index_0 + 1000) % len(numbers)
index_2000 = (index_0 + 2000) % len(numbers)
index_3000 = (index_0 + 3000) % len(numbers)

result = 0
for k, v in numbers.items():
    number, index = v
    if index in (index_1000, index_2000, index_3000):
        result += number

print("Puzzle 1 =", result)
