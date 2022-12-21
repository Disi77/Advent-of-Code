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

DECRYPTION_KEY = 811589153
numbers = {}
for index, num in enumerate(puzzle_input):
    numbers[index] = (int(num) * 811589153, index)


# Calculate new indexes
for _ in range(10):
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
        
        if new_pos < pos:
            for k, v in numbers.items():
                number, original_pos = v
                if new_pos - 1 < original_pos < pos:
                    numbers[k] = (number, original_pos + 1)

        numbers[index] = (num, new_pos)


# Find indexes 1000, 2000, 3000
for k, v in numbers.items():
    if v[0] == 0:
        index0 = v[1]
        break

a = (index0 + 1000) % len(numbers)
b = (index0 + 2000) % len(numbers)
c = (index0 + 3000) % len(numbers)

result = 0
for k, v in numbers.items():
    number, index = v
    if index in (a, b, c):
        result += number

print("Puzzle 2 =", result)
