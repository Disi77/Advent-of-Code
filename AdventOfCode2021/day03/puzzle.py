def counts_of_digits(index, data):
    counts1 = 0
    for number in data:
        if number[index] == "1":
            counts1 += 1
    return len(data) - counts1, counts1


def most_common_value_oxygen_gen_rating(pointer, data):
    counts0, counts1 = counts_of_digits(pointer, data)
    if counts1 >= counts0:
        return "1"
    return "0"


def most_common_value_co2_scrubber_rating(pointer, data):
    counts0, counts1 = counts_of_digits(pointer, data)
    if counts1 >= counts0:
        return "0"
    return "1"


def generate_rating(data, rating_func):
    pointer = 0
    while True:
        temp = []
        m = rating_func(pointer, data)
        for number in data:
            if number[pointer] == m:
                temp.append(number)
        data = list(temp)
        if len(data) == 1:
            break
        pointer += 1
    return data[0]


#Puzzle input
puzzle_input = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    for line in data:
        puzzle_input.append(line.strip())


#Puzzle 1
counts_of_1 = []
for i in range(len(puzzle_input[0])):
    counts_of_1.append(counts_of_digits(i, puzzle_input)[0])

gamma_rate = epsilon_rate = ""
for number in counts_of_1:
    condition = number > len(puzzle_input) // 2
    gamma_rate += str(int(condition))
    epsilon_rate += str(int(not condition))

print(f"Puzzle 1 = {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


#Puzzle 2
data = list(puzzle_input)
oxygen_generator_rating = generate_rating(data, most_common_value_oxygen_gen_rating)

data = list(puzzle_input)
co2_scrubber_rating = generate_rating(data, most_common_value_co2_scrubber_rating)

print(f"Puzzle 2 = {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}")