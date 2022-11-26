with open("day11_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()


class Game():
    def __init__(self, game_field):
        self.field_size_x = len(game_field[0])
        self.field_size_y = len(game_field)
        self.game_field = game_field

    def count_alive_neighbors(self, x, y):
        count = 0
        for row in (-1, 0, 1):
            for column in (-1, 0, 1):
                x_coor = x + row
                y_coor = y + column
                if not (0 <= x_coor < len(self.game_field)):
                    continue
                if not (0 <= y_coor < len(self.game_field[0])):
                    continue
                if row == column == 0:
                    continue
                if self.game_field[x_coor][y_coor] == "#":
                    count += 1

        return count

    def new_generation(self):
        new_game_field = []
        for x, row in enumerate(self.game_field):
            new_row = []
            for y, cell in enumerate(row):
                count = self.count_alive_neighbors(x, y)
                state = self.game_field[x][y]
                new_state = self.get_new_state(state, count)
                new_row.append(new_state)
            new_game_field.append(new_row)
        return new_game_field

    def get_new_state(self, state, count):
        if state == "L" and count == 0:
            return "#"
        if state == "#" and count >= 4:
            return "L"
        return state


game = Game(input_data)
while True:
    state_start = ''.join(''.join(x) for x in game.game_field)
    game.game_field = game.new_generation()
    state_end = ''.join(''.join(x) for x in game.game_field)
    if state_start == state_end:
        print("Occupied seats: ", end="")
        print(state_end.count("#"))
        break
