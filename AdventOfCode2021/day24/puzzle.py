# The inspiration came from REEDIT
# Thanks to Gravitar64
# https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hqstr1a/?utm_source=share&utm_medium=web2x&context=3

# Manual solution in file "manual_solution.txt"

def get_input_data():
    """
    Get the lines I really need for the solution.
    """
    input_data = []
    with open("AdventOfCode2021/day24/input.txt", mode="r", encoding="utf-8") as file:
        command = None
        for i, line in enumerate(file):
            if i % 18 == 4:
                line = line.strip()
                input_data.append(line)
                if "26" in line:
                    command = 5
                else:
                    command = 15
            elif i % 18 == command:
                line = line.strip()
                input_data.append(line)
    return input_data


def solution(pointer, input_data, digits, highest=True):
    """
    Can find highest or smallest number
    """
    while 0 in digits:
        if "1" in input_data[pointer]:
           pointer += 2
           continue
        if "26" in input_data[pointer]:
            index2 = pointer // 2
            x2 = int(input_data[pointer + 1].split()[2])
            for i in range(index2 - 1, -1, -1):
                if digits[i] == 0:
                    index1 = i
                    break
            x1 = int(input_data[index1 * 2 + 1].split()[2])
            diff = x1 + x2
            if highest:
                if diff < 0:
                    digits[index1] = 9
                    digits[index2] = 9 + diff
                else:
                    digits[index1] = 9 - diff
                    digits[index2] = 9
            else:
                if diff < 0:
                    digits[index1] = 1 - diff
                    digits[index2] = 1
                else:
                    digits[index1] = 1
                    digits[index2] = 1 + diff

            pointer += 2
 

# Puzzle input
input_data = get_input_data()


# Puzzle 1
digits = [0] * 14
solution(0, input_data, digits, highest=True)
result1 = "".join([str(num) for num in digits])
print(f"Puzzle 1 = {result1}")


# Puzzle 2
digits = [0] * 14
solution(0, input_data, digits, highest=False)
result2 = "".join([str(num) for num in digits])
print(f"Puzzle 1 = {result2}")