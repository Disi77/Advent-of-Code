from puzzle1 import Broadcaster, FlipFlop, Conjunction, get_modules


def find_round_for_module(m, modules):
    pulses_for_processing = []
    round = 0
    while True:
        round += 1
        pulses_for_processing.append(("broadcaster", "low"))
        while True:
            new_pulses_for_processing = []
            for name, pulse_type in pulses_for_processing:
                pulse = modules[name].process_pulse(pulse_type)
                for destination_module in modules[name].destination_modules:
                    if pulse == None:
                        continue
                    if destination_module == END_MODULE:
                        continue
                    new_pulses_for_processing.append((destination_module, pulse))
                    if (name == m and pulse == "high"):
                        return round
                    if isinstance(modules[destination_module], Conjunction):
                        modules[destination_module].set_input_module(modules[name].name, pulse)
            pulses_for_processing = new_pulses_for_processing.copy()
            if not pulses_for_processing:
                break


def reset_modules(modules):
    for m in modules.values():
        m.reset()


END_MODULE = "rx"
modules = get_modules()

MODULES_TO_CHECK = []
for module in modules.values():
    if END_MODULE in module.destination_modules:
        for m in modules.values():
            if module.name in m.destination_modules:
                MODULES_TO_CHECK.append(m.name)

result = 1
for m in MODULES_TO_CHECK:
    reset_modules(modules)
    result *= find_round_for_module(m, modules)

print("Puzzle 2 =", result)
