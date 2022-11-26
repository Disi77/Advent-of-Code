class Packet():
    def __init__(self, input_binary):
        self.input_binary = input_binary
        self.version = int(input_binary[:3], 2)
        self.type_id = int(input_binary[3:6], 2)
        self.subpackets_binary = ""
        self.subpackets = []
        self.value = None

        if self.type_id == 4:
            self.value, self.rest = self.get_literal_value(input_binary[6:])
        
        else:
            self.length_type_id = int(input_binary[6])

            if self.length_type_id == 1:
                self.number_of_subpackets = int(input_binary[7:18], 2)
                self.subpackets_binary = input_binary[18:]

                for _ in range(self.number_of_subpackets):
                    new_packet = Packet(self.subpackets_binary)
                    self.subpackets.append(new_packet)
                    self.subpackets_binary = new_packet.rest
                self.rest = self.subpackets_binary

            elif self.length_type_id == 0:
                self.total_lenght_in_bits = int(input_binary[7:22], 2)
                self.subpackets_binary = input_binary[22:22 + self.total_lenght_in_bits]
                self.rest = input_binary[22 + self.total_lenght_in_bits:]
                if set(self.rest) == {"0"}:
                    self.rest = None

                while True:
                    new_packet = Packet(self.subpackets_binary)
                    self.subpackets.append(new_packet)
                    self.subpackets_binary = new_packet.rest
                    if not self.subpackets_binary or set(self.subpackets_binary) == {"0"}:
                        break
            
        self.calculate_value()

    def calculate_value(self):
        from sys import maxsize
        if self.type_id == 0:
            self.value = 0
            for p in self.subpackets:
                self.value += p.value
        
        elif self.type_id == 1:
            self.value = 1
            for p in self.subpackets:
                self.value *= p.value
        
        elif self.type_id == 2:
            self.value = maxsize
            for p in self.subpackets:
                if p.value < self.value:
                    self.value = p.value

        elif self.type_id == 3:
            self.value = -1 * maxsize
            for p in self.subpackets:
                if p.value > self.value:
                    self.value = p.value

        elif self.type_id == 5:
            self.value = 0
            if self.subpackets[0].value > self.subpackets[1].value:
                self.value = 1
 
        elif self.type_id == 6:
            self.value = 0
            if self.subpackets[0].value < self.subpackets[1].value:
                self.value = 1
    
        elif self.type_id == 7:
            self.value = 0
            if self.subpackets[0].value == self.subpackets[1].value:
                self.value = 1

    def __str__(self):
        """
        Not needed for final solution. Helper for debugging.
        """
        if self.type_id == 4:
            return f"version: {self.version}, type ID: {self.type_id}, value: {self.value}"
        return f"version: {self.version}, type ID: {self.type_id}, length type ID: {self.length_type_id}, value: {self.value}, subpackets: {len(self.subpackets)}" 

    def get_literal_value(self, input_data):
        result = ""
        for _ in range(len(input_data) // 5):
            temp = input_data[:5]
            input_data = input_data[5:]
            result += temp[1:]
            if temp[0] == "0":
                return int(result, 2), input_data


def print_packet(packet, level=0):
    """
    Helps me to understand structure of input transmission - for sure not perfect.
    Not needed for final solution.
    """
    print(packet)
    if packet.subpackets:
        print(level * 3 * " ", "   ║")
        for i, s in enumerate(packet.subpackets):
            if i == len(packet.subpackets) - 1:
                print(level * 3 * " ", "   ╙--", end="")
                print_packet(s, level=level+1)

            else:
                print(level * 3 * " ", "   ╟--", end="")
                print_packet(s, level=level+1)


def get_input_data():
    with open("input.txt", mode="r", encoding="utf-8") as file:
        input_data = file.read().strip()
    return input_data


def from_hex_to_binary(data):
    input_binary = ""
    for i in data:
        b = f"{int(i, 16):04b}"
        input_binary += b
    return input_binary


def sum_versions(packet, result):
    result += packet.version
    if packet.subpackets:
        for s in packet.subpackets:
            result = sum_versions(s, result)
    return result

# Puzzle input
input_hex = get_input_data()
input_binary = from_hex_to_binary(input_hex)


# Puzzle 1
a = Packet(input_binary)
result = sum_versions(a, 0)
print(f"Puzzle 1 = {result}")


# Puzzle 2
print(f"Puzzle 2 = {a.value}")
