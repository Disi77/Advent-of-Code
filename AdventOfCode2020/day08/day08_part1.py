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
            break


a = Accumulator()
find_loop(a, input_data)
print(f"Value in the accumulator is {a.value}")
