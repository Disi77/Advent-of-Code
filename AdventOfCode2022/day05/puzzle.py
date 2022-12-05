def get_stacks(stacks_raw):
    # <stacks_raw> contains stacks input as one string
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3

    # loop over rows from bottom to top (skip row with stack numbers)
    # and save each crate as item in the list of lists
    # lists contain empty spaces e.g. for
    #  .  [D]  .
    # we have to save the information that on both sides there is empy slot
    stacks = []
    for s in stacks_raw.split("\n")[::-1]:
        if "[" not in s:
            continue
        col = [s[i: i + 4].strip() for i in range(0, len(s), 4)]
        stacks.append(col)

    # transpose the matrix to have in 1 sublist 1 stack column
    stacks_rows = [[stacks[j][i] for j in range(len(stacks))] for i in range(len(stacks[0]))]

    # remove empty slots because now we have columns in rows
    stacks_rows = [" ".join(a).strip().split() for a in stacks_rows]
    return stacks_rows


def get_instructions(instructions_raw):
    import re

    instructions = []
    pattern = r"^move (\d+) from (\d+) to (\d+)$"
    for i in instructions_raw.strip().split("\n"):
        count, from_col, to_col = re.match(pattern, i).groups()
        instructions.append((int(count), int(from_col), int(to_col)))
    return instructions


def move_crates(instructions, stacks, mode="one"):
    for count, from_col, to_col in instructions:
        # Puzzle 1 - move crates by one
        if mode == "one":
            for _ in range(count):
                crate = stacks[from_col - 1].pop()
                stacks[to_col - 1].append(crate)
        # Puzzle 2 - move crates as group
        if mode == "all":
            stacks[to_col - 1] = stacks[to_col - 1] + stacks[from_col - 1][-count:]
            stacks[from_col - 1] = stacks[from_col - 1][:-count]


def format_output(stacks):
    return "".join([a[-1].replace("[", "").replace("]", "").strip() for a in stacks])

path = "AdventOfCode2022/day05/input.txt"
with open(path, encoding="utf-8", mode="r") as raw_data:
    stacks_raw, instructions_raw = raw_data.read().split("\n\n")

instructions = get_instructions(instructions_raw)

stacks = get_stacks(stacks_raw)
move_crates(instructions, stacks, "one")
print("Puzzle 1 =", format_output(stacks))


stacks = get_stacks(stacks_raw)
move_crates(instructions, stacks, "all")
print("Puzzle 2 =", format_output(stacks))