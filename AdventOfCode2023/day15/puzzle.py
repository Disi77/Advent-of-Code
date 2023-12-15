def get_label_index(label, lens_list):
    for i, (len_label, _) in enumerate(lens_list):
        if label == len_label:
            return i
    return -1


def hash_algorithm(string):
    result = 0
    for char in string:
        result = ((result + ord(char)) * 17) % 256
    return result


path = "AdventOfCode2023/day15/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    initialization_sequence = raw_data.read().split(",")


# Puzzle 1
all_steps_result = 0
for step in initialization_sequence:
    all_steps_result += hash_algorithm(step)
    
print("Puzzle 1 =", all_steps_result)


#Puzzle 2
boxes = [[] for _ in range(256)]

for step in initialization_sequence:
    if "=" in step:
        label, focal_len = step.split("=")
        focal_len = int(focal_len)
        box_i = hash_algorithm(label)
        len_i = get_label_index(label, boxes[box_i])
        if len_i == -1:
            boxes[box_i].append((label, focal_len))
        else:
            boxes[box_i][len_i] = (label, focal_len)
            
    elif "-" in step:
        label = step[:-1]
        box_i = hash_algorithm(label)
        len_i = get_label_index(label, boxes[box_i])
        if len_i != -1:
            del boxes[box_i][len_i]

all_lens_focusing_power = 0
for box_i, box in enumerate(boxes):
    for len_i, (label, focus_len) in enumerate(box):
        all_lens_focusing_power += (box_i + 1) * (len_i + 1) * focus_len

print("Puzzle 2 =", all_lens_focusing_power)
