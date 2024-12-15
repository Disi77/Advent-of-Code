def blink(stones):
    new_stones = {}
    for stone_type, count in stones.items():
        if stone_type == "0":
            new_stones["1"] = new_stones.setdefault("1", 0) + count
        elif len(stone_type) % 2 == 0:
            lenght = len(stone_type) // 2
            new_stone = str(stone_type[:lenght])
            new_stones[new_stone] = new_stones.setdefault(new_stone, 0) + count

            new_stone = str(int(stone_type[lenght:]))  # to solve values like '000'
            new_stones[new_stone] = new_stones.setdefault(new_stone, 0) + count
            
        else:
            new_stone = str(int(stone_type) * 2024)
            new_stones[new_stone] = new_stones.setdefault(new_stone, 0) + count

    return new_stones

initial_arrangement = "2 54 992917 5270417 2514 28561 0 990"

stones = {}
for stone in initial_arrangement.split():
    stones[stone] = 1

blinks = 75
for i in range(blinks):
    stones = blink(stones)

    if i == 24:
        result1 = sum(x for x in stones.values())


print("Puzzle 1 =", result1)

result2 = sum(x for x in stones.values())
print("Puzzle 2 =", result2)
