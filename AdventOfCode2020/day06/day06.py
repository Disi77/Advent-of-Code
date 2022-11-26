with open("day06_input.txt", encoding="utf-8", mode="r") as f:
    input = f.read().split("\n\n")

sum = 0
for group in input:
    for char in set(group):
        if char.isalpha():
            sum += 1

print(f"Number of questions to which ANYone answered 'yes' is {sum}")


with open("day06_input.txt", encoding="utf-8", mode="r") as f:
    input = [x.strip() for x in f.read().split("\n\n")]

sum = 0
for group in input:
    if len(group.split("\n")) == 1:
        sum += len(group)
        continue
    sum += len(set.intersection(*[set(x) for x in group.split("\n")]))


print(f"Number of questions to which EVERYone answered 'yes' is {sum}")
