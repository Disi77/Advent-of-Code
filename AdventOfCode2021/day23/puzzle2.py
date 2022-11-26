def print_game_field(game_field):
    """ 
    Not needed for final solution.

    ####################################
    # H0 H1 .. H2 .. H3 .. H4 .. H5 H6 #
    ####### A0 ## B0 ## C0 ## D0 #######
          # A1 ## B1 ## C1 ## D1 # 
          # A2 ## B2 ## C2 ## D2 # 
          # A3 ## B3 ## C3 ## D3 # 
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
    a2 = "." if game_field["A2"] is None else game_field["A2"]
    a3 = "." if game_field["A3"] is None else game_field["A3"]

    b0 = "." if game_field["B0"] is None else game_field["B0"]
    b1 = "." if game_field["B1"] is None else game_field["B1"]
    b2 = "." if game_field["B2"] is None else game_field["B2"]
    b3 = "." if game_field["B3"] is None else game_field["B3"]

    c0 = "." if game_field["C0"] is None else game_field["C0"]
    c1 = "." if game_field["C1"] is None else game_field["C1"]
    c2 = "." if game_field["C2"] is None else game_field["C2"]
    c3 = "." if game_field["C3"] is None else game_field["C3"]

    d0 = "." if game_field["D0"] is None else game_field["D0"]
    d1 = "." if game_field["D1"] is None else game_field["D1"]
    d2 = "." if game_field["D2"] is None else game_field["D2"]
    d3 = "." if game_field["D3"] is None else game_field["D3"]

    template = f"""
    ####################################
    # {h0}  {h1}  .. {h2}  .. {h3}  .. {h4}  .. {h5}  {h6}  #
    ####### {a0}  ## {b0}  ## {c0}  ## {d0}  #######
          # {a1}  ## {b1}  ## {c1}  ## {d1}  # 
          # {a2}  ## {b2}  ## {c2}  ## {d2}  # 
          # {a3}  ## {b3}  ## {c3}  ## {d3}  # 
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
          # A2 ## B2 ## C2 ## D2 # 
          # A3 ## B3 ## C3 ## D3 # 
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

    game_field["A2"] = temp[8]
    game_field["B2"] = temp[9]
    game_field["C2"] = temp[10]
    game_field["D2"] = temp[11]

    game_field["A3"] = temp[12]
    game_field["B3"] = temp[13]
    game_field["C3"] = temp[14]
    game_field["D3"] = temp[15]

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
             ["A0", "H2", "H3", "H4"],
             ["A0", "H2", "H3", "H4", "H5"],
             ["A0", "H2", "H3", "H4", "H5", "H6"],
             ["A0", "H1", "H0"],
             
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
        for i in "0123":
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

        for i in range(1, 4):
            new_point = item[0][0] + str(i)
            new_item = [new_point] + item

            key = new_item[0]
            steps = get_count_of_steps_for_path(new_item[1:])
            value = [key, new_item[-1], steps, new_item[1:-1]]
            possible_moves_dict[key].append(value)
            key = new_item[-1]
            value = [key, new_item[0], steps, new_item[1:-1][::-1]]
            possible_moves_dict[key].append(value)
            item = new_item
    
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
                            if game_field[item[1][0] + "1"] == fish and game_field[item[1][0] + "2"] == fish and game_field[item[1][0] + "3"] == fish:
                                actual_possible_moves.append(item)
                        elif item[1][1] == "1":
                            if game_field[item[1][0] + "2"] == fish and game_field[item[1][0] + "3"] == fish:
                                actual_possible_moves.append(item)      
                        elif item[1][1] == "2":
                            if game_field[item[1][0] + "3"] == fish:
                                actual_possible_moves.append(item)
                        else:
                            actual_possible_moves.append(item)
                if item[1][0] > fish:
                    break

        else:
            if coor[1] == "3" and coor[0] == fish:
                continue
            if coor[1] == "2" and coor[0] == fish and game_field[coor[0] + "3"] == fish:
                continue
            if coor[1] == "1" and coor[0] == fish and game_field[coor[0] + "2"] == fish and game_field[coor[0] + "3"] == fish:
                continue
            if coor[1] == "0" and coor[0] == fish and game_field[coor[0] + "1"] == fish and game_field[coor[0] + "2"] == fish and game_field[coor[0] + "3"] == fish:
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
        at_home = []
        for key, fish in game_field.items(): 
            if fish == char:
                if key[0] == char:
                    at_home.append(key)
                    continue
                where_is.append(key)
    
        for point in where_is:
            if point[0] not in ["H", char]:
                if point[1] == "3":
                    steps += 3
                    point = point[0] + "0"
                elif point[1] == "2":
                    steps += 2
                    point = point[0] + "0"
                elif point[1] == "1":
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
        if len(where_is) == 4:
            steps += 6
        if len(where_is) == 3:
            if char + "0" in at_home:
                steps += 7
            if char + "1" in at_home:
                steps += 8
            if char + "2" in at_home:
                steps += 9
            steps += 3

        if len(where_is) == 2:
            if char + "0" in at_home and char + "1" in at_home:
                steps += 14
            if char + "0" in at_home and char + "2" in at_home:
                steps += 15
            if char + "0" in at_home and char + "3" in at_home:
                steps += 7
            if char + "1" in at_home and char + "2" in at_home:
                steps += 16
            if char + "1" in at_home and char + "3" in at_home:
                steps += 9
            steps += 1
        if len(where_is) == 1:
            if char + "3" not in at_home:
                steps += 20
            if char + "2" not in at_home:
                steps += 12
            if char + "1" not in at_home:
                steps += 5
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

# Puzzle 2
from time import time, asctime, localtime
a = time()

print(f"\nCalculation started at {asctime(localtime(time()))} ... It will take several minutes (24 on my notebook)")
ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}

puzzle_input = """
#############
#...........#
###D#D#A#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#C#B#B#
  #########
"""

game_field = get_game_field(puzzle_input)
possible_moves_dict = get_possible_moves_dict()

result = find_shortest_way(game_field, possible_moves_dict, 1000000, 0, ENERGY)
print(f"Puzzle 2 = {result}")

b = time()
print(f"Time of calculation: {round(b - a, 2)} sec = {round((b - a) / 60, 2)} min")