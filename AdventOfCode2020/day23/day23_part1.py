from colorama import Fore, Style


input_data = "467528193"


class Cups_game:
    def __init__(self, input_data):
        self.cups = [int(x) for x in input_data]
        self.current = self.cups[0]
        self.current_index = 0
        self.pick_up = self.cups[1:4]
        self.destination = self.calculate_destination()

    def move(self):
        # Remove 3 picked up cups from circle
        for item in self.pick_up:
            self.cups.remove(item)

        # Place the picked up cups into circle behind the destination cup
        index = self.cups.index(self.destination)
        self.cups = self.cups[:index+1] + self.pick_up + self.cups[index+1:]

        # Setup new current cup
        index_for_new_current = (self.cups.index(self.current) + 1) % len(self.cups)
        self.current = self.cups[index_for_new_current]

        self.current_index = (self.current_index + 1) % len(self.cups)

        # Setup new 3 cups for pick up
        index = self.cups.index(self.current)
        i1 = (index + 1) % len(self.cups)
        i2 = (index + 2) % len(self.cups)
        i3 = (index + 3) % len(self.cups)
        self.pick_up = [self.cups[i1], self.cups[i2], self.cups[i3]]

        # Setup new destination
        self.destination = self.calculate_destination()

        # Move with cups if current cup is not on correct index
        while self.cups.index(self.current) != self.current_index:
            cup = self.cups.pop(0)
            self.cups.append(cup)

    def calculate_destination(self):
        temp = self.current
        while True:
            temp -= 1
            if temp == 0:
                temp = max(self.cups) + 1
            elif temp not in self.pick_up:
                return temp

    def print_state_of_game(self):
        """
        Not important for game. Only prints state of game.
        """
        print("cups:", end=" ")
        for item in self.cups:
            if item == self.current:
                print(f"({item})", end=" ")
            else:
                if item in self.pick_up:
                    print(Fore.RED + str(item), end=" ")
                    print(Style.RESET_ALL, end="")
                else:
                    print(item, end=" ")
        print()
        print("pick up:", self.pick_up)
        print("destination:", self.destination)
        print("=" * 50)


game = Cups_game(input_data)
end = 100

print("-- before move 1 --")
game.print_state_of_game()

round = 1
while round <= end:
    print(f"-- after move {round} --")
    game.move()
    game.print_state_of_game()
    round += 1

result = game.cups
while result[0] != 1:
    cup = result.pop(0)
    result.append(cup)

result = "".join(str(x) for x in result[1:])
print("What are the labels on the cups after cup 1")
print(f"= {result}")
