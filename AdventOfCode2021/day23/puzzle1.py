def manual_solution_puzzle1():
    """
    My first solution without Python:

    ####################################
    # __ __ __ __ __ __ __ __ __ __ __ #
    ####### D  ## D  ## A  ## A  #######
          # C  ## C  ## B  ## B  # 
          ########################
    8 x 1
    ####################################
    # __ A_ __ __ __ __ __ __ __ __ __ #
    ####### D  ## D  ## A  ## __ #######
          # C  ## C  ## B  ## B  # 
          ########################
    3 x 10
    ####################################
    # __ A_ __ __ __ __ __ __ __ B_ __ #
    ####### D  ## D  ## A  ## __ #######
          # C  ## C  ## B  ## __ # 
          ########################
    7 x 1000
    ####################################
    # __ A_ __ __ __ __ __ __ __ B_ __ #
    ####### D  ## __ ## A  ## __ #######
          # C  ## C  ## B  ## D_ # 
          ########################
    8 x 1000
    ####################################
    # __ A_ __ __ __ __ __ __ __ B_ __ #
    ####### __ ## __ ## A  ## D_ #######
          # C  ## C  ## B  ## D_ # 
          ########################
    2 x 1
    ####################################
    # __ A_ __ __ __ __ __ A_ __ B_ __ #
    ####### __ ## __ ## __ ## D_ #######
          # C  ## C  ## B  ## D_ # 
          ########################
    5 x 10
    ####################################
    # __ A_ __ B_ __ __ __ A_ __ B_ __ #
    ####### __ ## __ ## __ ## D_ #######
          # C  ## C  ## __ ## D_ # 
          ########################
    6 x 100
    ####################################
    # __ A_ __ B_ __ __ __ A_ __ B_ __ #
    ####### __ ## __ ## __ ## D_ #######
          # C  ## __ ## C_ ## D_ # 
          ########################
    3 x 10
    7 x 100
    ####################################
    # __ A_ __ __ __ __ __ A_ __ B_ __ #
    ####### __ ## __ ## C_ ## D_ #######
          # __ ## B_ ## C_ ## D_ # 
          ########################
    7 x 1
    6 x 10
    ####################################
    # __ A_ __ __ __ __ __ __ __ __ __ #
    ####### __ ## B_ ## C_ ## D_ #######
          # A_ ## B_ ## C_ ## D_ # 
          ########################
    2 x 1
    ####################################
    # __ __ __ __ __ __ __ __ __ __ __ #
    ####### A_ ## B_ ## C_ ## D_ #######
          # A_ ## B_ ## C_ ## D_ # 
          ########################

    -----sum-----
    15000
     1300
      170
       19
    -----
    16489
    """
    return 16489


def print_game_field(game_field):
    """ 
    Not needed for final solution.

    ####################################
    # H0 H1 .. H2 .. H3 .. H4 .. H5 H6 #
    ####### A0 ## B0 ## C0 ## D0 #######
          # A1 ## B1 ## C1 ## D1 # 
          ########################
    """
    h0 = "." if game_field["H0"] is None else game_field["H0"]
    h1 = "." if game_field["H1"] is None else game_field["H1"]
    h2 = "." if game_field["H2"] is None else game_field["H2"]
    h3 = "." if game_field["H3"] is None else game_field["H3"]
    h4 = "." if game_field["H4"] is None else game_field["H4"]
    h5 = "." if game_field["H5"] is None else game_field["H5"]
    h6 = "." if game_field["H6"] is None else game_field["H6"]

    a0 = "." if game_field["A0"] is None else game_field["A0"]
    a1 = "." if game_field["A1"] is None else game_field["A1"]
    b0 = "." if game_field["B0"] is None else game_field["B0"]
    b1 = "." if game_field["B1"] is None else game_field["B1"]
    c0 = "." if game_field["C0"] is None else game_field["C0"]
    c1 = "." if game_field["C1"] is None else game_field["C1"]
    d0 = "." if game_field["D0"] is None else game_field["D0"]
    d1 = "." if game_field["D1"] is None else game_field["D1"]
    template = f"""
    ####################################
    # {h0}  {h1}  .. {h2}  .. {h3}  .. {h4}  .. {h5}  {h6}  #
    ####### {a0}  ## {b0}  ## {c0}  ## {d0}  #######
          # {a1}  ## {b1}  ## {c1}  ## {d1}  # 
          ########################
    """
    print(template)


def all_at_home(game_field):
    for key, fish in game_field.items():
        if key[0] == "H":
            continue
        if key[0] != fish:
            return False
    return True


def get_game_field(input_data):
    """ 
    ####################################
    # H0 H1 .. H2 .. H3 .. H4 .. H5 H6 #
    ####### A0 ## B0 ## C0 ## D0 #######
          # A1 ## B1 ## C1 ## D1 # 
          ########################
    """
    game_field = {}
    temp = ""
    for char in input_data:
        if char.isalpha():
            temp += char
    game_field["A0"] = temp[0]
    game_field["B0"] = temp[1]
    game_field["C0"] = temp[2]
    game_field["D0"] = temp[3]

    game_field["A1"] = temp[4]
    game_field["B1"] = temp[5]
    game_field["C1"] = temp[6]
    game_field["D1"] = temp[7]

    for i in range(7):
        key = "H" + str(i)
        game_field[key] = None
    
    return game_field


def get_count_of_steps_for_path(path):
    steps = 0
    for point in path:
        if point[0] == "H" and int(point[1]) in range(1, 6):
            steps += 2
        else:
            steps += 1
    return steps


def get_possible_moves_dict():
    # TODO create PATHS automatically from input
    paths = [["A0", "H1"],
             ["A0", "H2"],
             ["A0", "H2", "H3"],
             ["A0", "H1", "H0"],
             ["A0", "H2", "H3", "H4"],
             ["A0", "H2", "H3", "H4", "H5"],
             ["A0", "H2", "H3", "H4", "H5", "H6"],
             
             ["B0", "H2"],
             ["B0", "H3"],
             ["B0", "H3", "H4"],
             ["B0", "H2", "H1"],
             ["B0", "H3", "H4", "H5"],
             ["B0", "H2", "H1", "H0"],
             ["B0", "H3", "H4", "H5", "H6"],

             ["C0", "H3"],
             ["C0", "H4"],
             ["C0", "H4", "H5"],
             ["C0", "H3", "H2"],
             ["C0", "H3", "H2", "H1"],
             ["C0", "H4", "H5", "H6"],
             ["C0", "H3", "H2", "H1", "H0"],

             ["D0", "H4"],
             ["D0", "H5"],
             ["D0", "H5", "H6"],
             ["D0", "H4", "H3"],
             ["D0", "H4", "H3", "H2"],
             ["D0", "H4", "H3", "H2", "H1"],
             ["D0", "H4", "H3", "H2", "H1", "H0"]
            ]

    possible_moves_dict = {}
    for i in range(7):
        key = "H" + str(i)
        possible_moves_dict[key] = []
    for c in "ABCD":
        for i in "01":
            key = c + i
            possible_moves_dict[key] = []

    for item in paths:
        key = item[0]
        steps = get_count_of_steps_for_path(item[1:])
        value = [key, item[-1], steps, item[1:-1]]
        possible_moves_dict[key].append(value)
        key = item[-1]
        value = [key, item[0], steps, item[1:-1][::-1]]
        possible_moves_dict[key].append(value)

        new_point = item[0][0] + "1"
        new_item = [new_point] + item

        key = new_item[0]
        steps = get_count_of_steps_for_path(new_item[1:])
        value = [key, new_item[-1], steps, new_item[1:-1]]
        possible_moves_dict[key].append(value)
        key = new_item[-1]
        value = [key, new_item[0], steps, new_item[1:-1][::-1]]
        possible_moves_dict[key].append(value)
    
    return possible_moves_dict


def get_actual_possible_moves(game_field, possible_moves_dict):
    actual_possible_moves = []
    for coor, fish in game_field.items():
        if fish is None:
            continue
        if coor[0] == "H":
            for item in possible_moves_dict[coor]:
                if item[1][0] == fish:
                    for point in (item[3] + [item[1]]):
                        if game_field[point] is not None:
                            break
                    else:
                        if item[1][1] == "0":
                            if game_field[item[1][0] + "1"] == fish:
                                actual_possible_moves.append(item)
                        else:
                            actual_possible_moves.append(item)
                if item[1][0] > fish:
                    break

        else:
            if coor[1] == "1" and coor[0] == fish:
                continue
            if coor[1] == "0" and coor[0] == fish and game_field[coor[0] + "1"] == fish:
                continue
            for item in possible_moves_dict[coor]:
                for point in (item[3] + [item[1]]):
                    if game_field[point] is not None:
                        break
                else:
                    actual_possible_moves.append(item)
    return actual_possible_moves


def make_move(game_field, i):
    new_game_field = game_field.copy()
    new_game_field[i[1]] = game_field[i[0]]
    new_game_field[i[0]] = None
    return new_game_field


def calculate_energy_for_instruction(game_field, i, ENERGY):
    energy_value = i[2] * ENERGY[game_field[i[0]]]
    return energy_value


def count_min_needed_energy(game_field, ENERGY):
    energy = 0
           
    for char in "ABCD":
        steps = 0
        where_is = []
        for key, fish in game_field.items(): 
            if fish == char:
                if key[0] == char:
                    continue
                where_is.append(key)
    
        for point in where_is:
            if point[0] not in ["H", char]:
                if point[1] == "1":
                    steps += 1
                    point = point[0] + "0"
                if point[1] == "0":
                    index = "ABCD".index(str(point[0]))
                    if index < "ABCD".index(str(char)):
                        point = "H" + str(index + 2)
                    else:
                        point = "H" + str(index + 1)
                    steps += 2
            if point[0] == "H":
                for item in possible_moves_dict[point]:
                    if item[1] == char +"0":
                        steps += item[2]
                        break
        if len(where_is) == 2:
            steps += 1
        energy += steps * ENERGY[char]
    return energy


def find_shortest_way(game_field, possible_moves_dict, result, energy, ENERGY):  
    actual_possible_moves = get_actual_possible_moves(game_field, possible_moves_dict)
    if not actual_possible_moves:
        if all_at_home(game_field):
            if energy < result:
                return energy
        return result

    for move_description in actual_possible_moves:
        new_energy = calculate_energy_for_instruction(game_field, move_description, ENERGY)
        if energy + new_energy > result:
            continue
        temp = count_min_needed_energy(game_field, ENERGY)
        if energy + temp > result:
            continue

        new_game_field = make_move(game_field, move_description)
        result = find_shortest_way(new_game_field, possible_moves_dict, result, energy + new_energy, ENERGY)
    return result


# Puzzle 1
puzzle_input = """
#############
#...........#
###D#D#A#A###
  #C#C#B#B#
  #########
"""

from time import time
a = time()
print("Calculating ...")

ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}   

game_field = get_game_field(puzzle_input)
possible_moves_dict = get_possible_moves_dict()

result = find_shortest_way(game_field, possible_moves_dict, 100000, 0, ENERGY)
print(f"Puzzle 1 = {result}")

b = time()
print(f"Time of calculation: {round(b - a, 2)} sec")

