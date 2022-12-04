import re


def get_wire_a_signal(instructions, signals):
    while instructions:
        for index, i in enumerate(instructions):
            if "AND" in i:
                w_from1, w_from2, w_to = i.replace("AND", "->").split(" -> ")
                if w_from1.isdigit() and w_from2 in signals:
                    signals[w_to] = int(w_from1) & signals[w_from2]
                    del instructions[index]
                    break
                else:
                    if w_from1 in signals and w_from2 in signals:
                        signals[w_to] = signals[w_from1] & signals[w_from2]
                        del instructions[index]
                        break
            elif "OR" in i:
                w_from1, w_from2, w_to = i.replace("OR", "->").split(" -> ")
                if w_from1 in signals and w_from2 in signals:
                    signals[w_to] = signals[w_from1] | signals[w_from2]
                    del instructions[index]
                    break
            elif "LSHIFT" in i:
                w_from, value, w_to = i.replace("LSHIFT", "->").split(" -> ")
                if w_from in signals:
                    signals[w_to] = signals[w_from] << int(value)
                    del instructions[index]
                    break
            elif "RSHIFT" in i:
                w_from, value, w_to = i.replace("RSHIFT", "->").split(" -> ")
                if w_from in signals:
                    signals[w_to] = signals[w_from] >> int(value)
                    del instructions[index]
                    break
            elif "NOT" in i:
                _, wire, w_to = i.replace(" -> ", " ").split()
                if wire in signals:
                    signals[w_to] = int((~signals[wire]) % 65535) + 1
                    del instructions[index]
                    break
            else:
                signal, wire = i.split(" -> ")
                if signal.isdigit():
                    signals[wire] = int(signal)
                    del instructions[index]
                    break
                else:
                    if signal in signals:
                        signal = signals[signal]
                        signals[wire] = signal
                        del instructions[index]
                        break
    return signals["a"]


path = "AdventOfCode2015/day07/input.txt"
instructions = []
with open(path, encoding="utf-8", mode="r") as raw_data:
    for line in raw_data:
        instructions.append(line.strip())

signals = {}
signal_a = get_wire_a_signal(instructions.copy(), signals)
print("Puzzle 1 =", signal_a)

signals = {}
for index, i in enumerate(instructions):
    if re.search(r" -> b$", i):
        instructions[index] = str(signal_a) + " -> b"
        break

signal_a = get_wire_a_signal(instructions, signals)
print("Puzzle 2 =", signal_a)
