class Broadcaster:
    def __init__(self, name, destination_modules):
        self.name = name
        self.destination_modules = destination_modules

    def process_pulse(self, pulse_type):
        return pulse_type

    def reset(self):
        pass


class FlipFlop:
    def __init__(self, name, destination_modules):
        self.name = name
        self.destination_modules = destination_modules
        self.status = 0

    def process_pulse(self, pulse_type):
        if pulse_type == "high":
            return None
        if pulse_type == "low" and not self.status:
            self.status = 1
            return "high"
        if pulse_type == "low" and self.status:
            self.status = 0
            return "low"

    def reset(self):
        self.status = 0


class Conjunction:
    def __init__(self, name, destination_modules):
        self.name = name
        self.destination_modules = destination_modules
        self.input_modules = {}

    def set_input_module(self, name, pulse_type="low"):
        self.input_modules[name] = pulse_type

    def process_pulse(self, _):
        for pulse in self.input_modules.values():
            if pulse == "low":
                return "high"
        return "low"

    def reset(self):
        for k, v in self.input_modules.items():
            self.input_modules[k] = "low"


def get_modules():
    path = "AdventOfCode2023/day20/input.txt"

    with open(path, encoding="utf-8", mode="r") as raw_data:
        data = []
        for line in raw_data:
            data.append(line.strip())

    modules = {}
    for config in data:
        name = config.split(" -> ")[0].replace("&", "").replace("%", "")
        dest_modules = [x.strip() for x in config.split(" -> ")[1].split(",")]
        if "broadcaster" in config:
            modules[name] = Broadcaster(name, dest_modules)
        if "%" in config:
            modules[name] = FlipFlop(name, dest_modules)
        if "&" in config:
            modules[name] = Conjunction(name, dest_modules)

    for mod1 in modules.values():
        if isinstance(mod1, Conjunction):
            for mod2 in modules.values():
                if mod1.name in mod2.destination_modules:
                    mod1.set_input_module(mod2.name)
    return modules


modules = get_modules()
high_pulses = 0
low_pulses = 0


for round in range(1000):
    low_pulses += 1
    pulses_for_processing = [("broadcaster", "low")]
    while True:
        new_pulses_for_processing = []
        for name, pulse_in in pulses_for_processing:
            pulse_out = modules[name].process_pulse(pulse_in)
            for dest_module in modules[name].destination_modules:
                if pulse_out == "high":
                    high_pulses += 1
                elif pulse_out == "low":
                    low_pulses += 1
                if dest_module == "rx":
                    continue
                if isinstance(modules[dest_module], FlipFlop) and pulse_out == "high":
                    continue
                if isinstance(modules[dest_module], Conjunction):
                    modules[dest_module].set_input_module(modules[name].name, pulse_out)

                new_pulses_for_processing.append((dest_module, pulse_out))

        pulses_for_processing = new_pulses_for_processing.copy()
        if not pulses_for_processing:
            break

print("Puzzle 1 =", high_pulses * low_pulses)
