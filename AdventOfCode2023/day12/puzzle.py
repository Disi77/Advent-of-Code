# inpired by https://advent-of-code.xavd.id/writeups/2023/day/12/ 
from functools import cache


@cache
def count_possible_arrangement(spring, numbers):
    # example: .??#.?#??#????#?? 2,4,1,1,1
    result = 0
    # if not numbers left and not # in spring => return True=1 (valid)
    if not numbers:
        return "#" not in spring

    # first_num = 2, numbers = 4,1,1,1
    first_num, numbers = numbers[0], numbers[1:]
    # for i in range(17 - 7 - 4 - 2 + 1)  => for i in range(5)
    # by lenght of spring and by numbers there are several options where the first damage part must
    # be placed so that everything fits there
    for start in range(len(spring) - sum(numbers) - len(numbers) - first_num + 1):
        # for i =    0   1    2     3      4
        # if "#" in  ""  "."  ".?"  ".??"  ".??#"
        if "#" in spring[:start]:
            break
        # for i = 0  1  2  3  4
        # end =   2  3  4  5  6
        end = start + first_num
        # if end > lenght of spring => skip
        # if "." in the piece under investigation => skip (e.g. in number=3 and piece="?.?")
        # if "#" after the piece under ivestigation => skip
        #        (we cannot fit number 3 in piece "?.?" if the next char is #)
        if (
            end <= len(spring)
            and "." not in spring[start:end]
            and spring[end : end + 1] != "#"
        ):
            # if all conditions are True then run the same for rest of spring and rest of numbers
            result += count_possible_arrangement(spring[end + 1 :], numbers)
    return result


path = "AdventOfCode2023/day12/input.txt"
with open(path, encoding="utf-8", mode="r") as raw_data:
    data = []
    for line in raw_data:
        data.append(line.strip())

result_p1 = result_p2 = 0
for record in data:
    spring, numbers = record.split()
    numbers = tuple([int(x) for x in numbers.split(",")])
    result_p1 += count_possible_arrangement(spring, numbers)
    result_p2 += count_possible_arrangement("?".join([spring] * 5), numbers * 5)

print("Puzzle 1 =", result_p1)
print("Puzzle 2 =", result_p2)
