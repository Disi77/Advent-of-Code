def find_vertical_line_reflection(pattern_raw_data, ignore=None):
    '''
    Try to find vertical line reflection
             |
        #.##.|.##.
        ..#.#|#.#.
        ##...|...#
        ##...|...#
        ..#.#|#.#.
        ..##.|.##.
        #.#.#|#.#.
             |
    Returns index of column left of the vertical line.
    Returns -1 if there is no vertical reflection.
    '''
    pattern = [x for x in pattern_raw_data.split("\n")]
    reflections = []
    for i in range(len(pattern[0]) - 1):
        for row in pattern:
            left, right = row[:i+1], row[i+1:]
            lenght = min(len(left), len(right))
            left, right = left[-lenght:], right[:lenght]
            if left[::-1] != right:
                break
        else:
            reflections.append(i + 1)
 
    try:
        if ignore:
            del reflections[reflections.index(ignore)]
    except ValueError:
        pass
    if not reflections:
        return -1
    return reflections[0]


def find_horizontal_line_reflection(pattern_raw_data, ignore=None):
    '''
    Try to find horizontal line reflection
            #...##..#
            #....#..#
            ..##..###
            #####.##.
        -----------------
            #####.##.
            ..##..###
            #....#..#
    Returns index of row above of the horizontal line.
    Returns -1 if there is no horizontal reflection.
    '''
    pattern = transpose_pattern(pattern_raw_data)
    return find_vertical_line_reflection(pattern, ignore=ignore)


def transpose_pattern(pattern_raw_data):
    rows = pattern_raw_data.strip().split('\n')

    num_rows = len(rows)
    num_col = len(rows[0])

    pattern = [''.join(rows[row][col] for row in range(num_rows)) for col in range(num_col)]
    return '\n'.join(pattern)


def find_new_reflection(pattern_raw_data, original_reflection):
    for index, smudge in enumerate(pattern_raw_data):
        if smudge == ".":
            new_pattern = pattern_raw_data[:index] + "#" + pattern_raw_data[index + 1:]
        elif smudge == "#":
            new_pattern = pattern_raw_data[:index] + "." + pattern_raw_data[index + 1:]
        else:
            continue

        ignore = None
        if "V" in original_reflection:
            ignore = int(original_reflection[1:])

        number = find_vertical_line_reflection(new_pattern, ignore)
        result = f"V{number}"
        if number != -1 and original_reflection != result:
            return result
        
        ignore = None
        if "H" in original_reflection:
            ignore = int(original_reflection[1:])

        number = find_horizontal_line_reflection(new_pattern, ignore)
        result = f"H{number}"
        if number != -1 and original_reflection != result:
            return result
    return -1


path = "AdventOfCode2023/day13/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read().split("\n\n")

result = 0
for pattern in data:
    original_reflection = ""
    number = find_vertical_line_reflection(pattern)
    if number != -1:
        original_reflection += f"V{number}"
    number = find_horizontal_line_reflection(pattern)
    if number != -1:
        original_reflection += f"H{number}"
    reflection = find_new_reflection(pattern, original_reflection)
    if reflection == -1:
        print(pattern)
        reflection = original_reflection
    if "V" in reflection:
        result += int(reflection[1:])
    else:
        result += 100 * int(reflection[1:])


print("Puzzle 2 =", result)
