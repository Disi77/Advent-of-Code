#Puzzle input for puzzle 1
puzzle_input = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    for i, line in enumerate(data):
        puzzle_input.extend(line.strip().split(" | ")[1].split())
            
#Puzzle 1
result = 0
for item in puzzle_input:
    if len(item) in [2, 3, 4, 7]:
        result += 1

print(f"Puzzle 1 = {result}")


#----------------------------------
#Puzzle input for puzzle 2

class Signal:
    def __init__(self, pattern, digits):
        self.pattern = self.sort(pattern)
        self.digits = self.sort(digits)

    def sort(self, input):
        input = input.split()
        for i, item in enumerate(input):
            s = sorted(item)
            input[i] = "".join(s)
        return input

signals = []
with open("input.txt", encoding="utf-8", mode="r") as data:
    for i, line in enumerate(data):
        pattern, digits = line.strip().split(" | ")
        s = Signal(pattern, digits)
        signals.append(s)

#Puzzle 2
def decoding(s):
    digits_dict = [""] * 10
    
    #Round 1 = find 1, 8, 7, 4
    for item in s.pattern:
        if len(item) == 2:
            digits_dict[1] = item
        if len(item) == 7:
            digits_dict[8] = item
        if len(item) == 3:
            digits_dict[7] = item
        if len(item) == 4:
            digits_dict[4] = item

    #Round 2 = find 0, 6, 9
    for item in s.pattern:
        if len(item) != 6:
            continue
        if contain_same_segments(item, digits_dict[4]) == 0:
            digits_dict[9] = item
        else:
            if contain_same_segments(item, digits_dict[7]) == 0:
                digits_dict[0] = item
            else:
                digits_dict[6] = item
    #Round 3 = find 2, 3, 5
    for item in s.pattern:
        if len(item) != 5:
            continue
        if contain_same_segments(item, digits_dict[7]) == 0:
            digits_dict[3] = item
        else:
            if contain_same_segments(item, digits_dict[6]) == 1:
                digits_dict[5] = item
            else:
                digits_dict[2] = item

    result = ""
    for digit in s.digits:
        result += str(digits_dict.index(digit))
    return int(result)

def contain_same_segments(item, segments):
    diff = 0
    for s in segments:
        if s not in item:
            diff += 1
    return diff
        

result = 0
for s in signals:
    result += decoding(s)

print(f"Puzzle 2 = {result}")