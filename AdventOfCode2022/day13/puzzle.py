from pathlib import Path


here = Path(__file__).parent
puzzle_input = Path(here / "input.txt").read_text()
packets = puzzle_input.split("\n\n")

def is_right_order(packet_L, packet_R):
    i_l = i_r = 0  # index for left and right packets
    while True:
        L = packet_L[i_l]
        R = packet_R[i_r]

        if L == R == "[" or L == R == "]":
            i_l += 1
            i_r += 1

        elif L+R in ["][", "],"]:
            return -1

        elif L+R in ["[]", ",]"]:
            return 1

        elif L == "]" and R.isdigit():
            return -1

        elif R == "]" and L.isdigit():
            return 1

        elif L == ",":
            i_l += 1

        elif R == ",":
            i_r += 1

        elif L.isdigit() and R.isdigit():
            num_l = L
            if packet_L[i_l + 1].isdigit():
                num_l += packet_L[i_l + 1]
            num_l = int(num_l)

            num_r = R
            if packet_R[i_r + 1].isdigit():
                num_r += packet_R[i_r + 1]
            num_r = int(num_r)

            if num_l < num_r:
                return -1
            elif num_l > num_r:
                return 1

            i_l += len(str(num_l))
            i_r += len(str(num_r))

        elif L == "[" and R.isdigit():
            is10 = packet_R[i_r + 1].isdigit()
            if is10:
                num = packet_R[i_r:i_r+2]
            else:
                num = packet_R[i_r]
            packet_R = packet_R[:i_r] + f"[{num}]" + packet_R[i_r+1:]

        elif L.isdigit() and R == "[":
            is10 = packet_L[i_l + 1].isdigit()
            if is10:
                num = packet_L[i_l:i_l+2]
            else:
                num = packet_L[i_l]
            packet_L = packet_L[:i_l] + f"[{num}]" + packet_L[i_l+1:]


result = []
for index, packet in enumerate(packets):
    packet_L, packet_R = packet.split("\n")
    if is_right_order(packet_L, packet_R) == -1:
        result.append(index + 1)

print("Puzzle 1 =", sum(result))

puzzle_input = puzzle_input.replace("\n\n", "\n").split("\n")
divider_packet1 = "[[2]]"
divider_packet2 = "[[6]]"

puzzle_input.extend([divider_packet1, divider_packet2])

from functools import cmp_to_key
puzzle_input = sorted(puzzle_input, key=cmp_to_key(is_right_order))

result = (puzzle_input.index(divider_packet1) + 1) * (puzzle_input.index(divider_packet2) + 1)
print("Puzzle 2=", result)
