from math import factorial


# this is simple loop and I assume that the result will be a number that 
# has many divisors (= the house will be visited by many elves) and 
# therefore I use the multiple 2 * 3 * 4 * 5 * 6 * 7 = factorial(7) 
# as the default value for the house number, but it is rather just 
# a trial-and-error method
# the smaller the factorial = the slower the algorithm
# the larger the factorial = the more likely the correct value will be skipped
# factorial(7) is best for my input

# Puzzle 1
puzzle_input = 36_000_000 // 10
house = factorial(7)

for num in range(house, puzzle_input, house):
    presents = 0
    for elf in range(1, num + 1):
        if num % elf == 0:
            presents += elf
    
    if presents >= puzzle_input:
        break

print("Puzzle 1 =", num)
