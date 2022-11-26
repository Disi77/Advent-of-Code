input_data = "467528193"


class Cups_game:
    def __init__(self, input_data):
        """
        Create start settings for game
        """
        # Create "linked list" as dictionary for input data + values from
        # 10 to 1,000,000 inclusive
        self.cups = {}
        data = [int(x) for x in input_data] + list(range(10, 1_000_001))
        for index, item in enumerate(data):
            if index <= len(data)-2:
                self.cups[item] = data[index+1]
            else:
                self.cups[item] = data[0]
        self.max = max(self.cups)
        # Set first "current cup", first "3 picked up cups" and first "destination cup"
        self.current = int(input_data[0])
        self.picked_up_cups = [int(input_data[1]), int(input_data[2]), int(input_data[3])]
        self.destination = self.calculate_destination()

    def calculate_destination(self):
        """
        Calculate destination cup.
        Destination cup is -1 from current cup.
        Destination is not between picked up cups.
        If destination cup is potentionaly == 0, then use the biggest
        possible cup.
        """
        destination = self.current - 1
        while destination in self.picked_up_cups:
            destination -= 1
        if destination == 0:
            destination = self.max
        while destination in self.picked_up_cups:
            destination -= 1
        return destination

    def move(self):
        """
        Move in game.
        Paste picked up cups after destination cup.
        Calculate new current cup, new picked up cups and new destination cup.
        """
        self.cups[self.current] = self.cups[self.picked_up_cups[2]]
        self.cups[self.picked_up_cups[2]] = self.cups[self.destination]
        self.cups[self.destination] = self.picked_up_cups[0]
        self.current = self.cups[self.current]
        self.picked_up_cups = []
        self.picked_up_cups.append(self.cups[self.current])
        self.picked_up_cups.append(self.cups[self.picked_up_cups[-1]])
        self.picked_up_cups.append(self.cups[self.picked_up_cups[-1]])
        self.destination = self.calculate_destination()


# Do 10,000,000 moves and find out the first and second cup after cup 1
# As result return multiplication of these two cups
a = Cups_game(input_data)
for i in range(10_000_000):
    a.move()

first = a.cups[1]
second = a.cups[first]
print(f"Result of puzzle 2 is {first * second}")
