def generate_ntuple(number_of_values):
    result = []

    for combination in generate_combinations(number_of_values, 100):
        result.append(combination)

    return result

def generate_combinations(number_of_values, target_sum, current_combination=[]):
    if number_of_values == 1:
        current_combination.append(target_sum)
        yield tuple(current_combination)
        current_combination.pop()
    else:
        for i in range(target_sum + 1):
            current_combination.append(i)
            yield from generate_combinations(number_of_values - 1, target_sum - i, current_combination)
            current_combination.pop()

# Test for generating 4-tuples
four_tuples = generate_ntuple(2)
print(four_tuples)
