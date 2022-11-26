def count_larger_numbers(numbers):
    larger = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            larger += 1
    return larger


def create_sums_of_three(numbers):
    new_numbers = []
    for i, v in enumerate(numbers[:-2]):
        sum = v + numbers[i + 1] + numbers[i + 2]
        new_numbers.append(sum)
    return new_numbers


report = []

with open("input.txt", encoding="utf-8", mode="r") as puzzle_input:
    for line in puzzle_input:
        report.append(int(line.strip()))

# Puzzle 1
print(f"Puzzle 1 = {count_larger_numbers(report)}")

# Puzzle 2
sums_of_measurements = create_sums_of_three(report)
print(f"Puzzle  = {count_larger_numbers(sums_of_measurements)}")
