def find_vertical_line_reflection(pattern_raw_data):
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

    for i in range(len(pattern[0]) - 1):
        for row in pattern:
            left, right = row[:i+1], row[i+1:]
            lenght = min(len(left), len(right))
            left, right = left[-lenght:], right[:lenght]
            if left[::-1] != right:
                break
        else:
            return i + 1
    return -1


def find_horizontal_line_reflection(pattern_raw_data):
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
    return find_vertical_line_reflection(pattern)


def transpose_pattern(pattern_raw_data):
    rows = pattern_raw_data.strip().split('\n')

    num_rows = len(rows)
    num_col = len(rows[0])

    pattern = [''.join(rows[row][col] for row in range(num_rows)) for col in range(num_col)]
    return '\n'.join(pattern)


path = "AdventOfCode2023/day13/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = raw_data.read().split("\n\n")

result = 0
for pattern in data:
    number = find_vertical_line_reflection(pattern)
    if number != -1:
        result += number
    number = find_horizontal_line_reflection(pattern)
    if number != -1:
        result += 100 * number

print("Puzzle 1 =", result)
