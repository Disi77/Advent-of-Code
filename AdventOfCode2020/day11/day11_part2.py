with open("day11_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()


class Game():
    def __init__(self, game_field):
        self.field_size_x = len(game_field[0])
        self.field_size_y = len(game_field)
        self.game_field = game_field

    def count_alive_neighbors(self, x, y):
        count = 0
        directions = [(0, -1), (1, -1), (1, 0), (1, 1),
                      (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        for row_change, col_change in directions:
            row = x
            col = y
            while True:
                row += row_change
                col += col_change
                if not (0 <= row < len(self.game_field)):
                    break
                if not (0 <= col < len(self.game_field[0])):
                    break
                if self.game_field[row][col] == "#":
                    count += 1
                    break
                if self.game_field[row][col] == "L":
                    break

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
        if state == "#" and count >= 5:
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
