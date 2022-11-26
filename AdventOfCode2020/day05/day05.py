with open("day05_input.txt", encoding="utf-8", mode="r") as f:
    data = [x.strip() for x in f.readlines()]


def find_row(start, end, instruction):
    if start == end:
        return start

    first, *instruction = instruction
    if first == "B":
        start = (end - start) // 2 + 1 + start
    if first == "F":
        end = (end - start) // 2 + start
    return find_row(start, end, instruction)


def find_column(start, end, instruction):
    if start == end:
        return start

    first, *instruction = instruction
    if first == "R":
        start = (end - start) // 2 + 1 + start
    if first == "L":
        end = (end - start) // 2 + start
    return find_column(start, end, instruction)


def decoding(seat):
    row = find_row(0, 127, seat[0:7])
    column = find_column(0, 7, seat[7:])
    seat_ID = row * 8 + column
    return seat_ID, row, column


results = []
for seat in data:
    results.append(decoding(seat))
results.sort()
print("Highest seat ID on a boarding pass is", results[-1][0])

occupied = []
for seat in results:
    occupied.append(seat[0])

for num in range(occupied[0], occupied[-1] + 1):
    if num not in occupied:
        print("My seat ID is", num)
