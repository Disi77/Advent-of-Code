with open("day08_input.txt", encoding="utf-8", mode="r") as f:
    input_data = [x.strip() for x in f.readlines()]


class Accumulator:
    def __init__(self):
        self.value = 0
        self.pointer = 0

    def nop(self):
        self.pointer += 1

    def acc(self, value):
        self.value += value
        self.pointer += 1

    def jmp(self, value):
        self.pointer += value


def find_loop(acc, instructions):
    visited_indexes = []
    while True:
        instruction = instructions[acc.pointer][:3]
        value = int(instructions[acc.pointer][4:])
        visited_indexes.append(acc.pointer)
        if instruction == "nop":
            acc.nop()
        elif instruction == "acc":
            acc.acc(value)
        elif instruction == "jmp":
            acc.jmp(value)

        if acc.pointer in visited_indexes:
            return "loop"
        if acc.pointer == len(instructions):
            return "end"


def generate_data(instructions):
    count_nop_jmp = sum([1 for x in instructions if x[:3] in ["nop", "jmp"]])
    index = 0
    temp = list(instructions)
    for round in range(count_nop_jmp):
        for i, item in enumerate(instructions):
            if i >= index and item[:3] in ["nop", "jmp"]:
                break
        temp_instructions = list(temp)
        if "nop" in temp_instructions[i]:
            temp_instructions[i] = "jmp" + temp_instructions[i][3:]
        else:
            temp_instructions[i] = "nop" + temp_instructions[i][3:]
        index = i + 1
        yield temp_instructions


a = Accumulator()
input_data = generate_data(input_data)
while True:
    try:
        a = Accumulator()
        result = find_loop(a, next(input_data))
        if result == "end":
            break
    except StopIteration:
        pass

print(f"Value in the accumulator is {a.value}")
