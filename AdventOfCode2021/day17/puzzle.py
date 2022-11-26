def get_target_area(raw):
    target_area = {}
    raw = raw.replace("target area: x=", "").split(", y=")
    target_area["x"] = [int(x) for x in raw[0].split("..")]
    target_area["y"] = [int(x) for x in raw[1].split("..")]
    return target_area


class Probe():
    def __init__(self, x, y, target_area):
        self.name = (x, y)
        self.x_velocity = x
        self.y_velocity = y
        self.is_in_target_area = False
        self.trajectory = [(0, 0)]
        self.calculate_trajectory(target_area)
        
    def step(self):
        start = self.trajectory[-1]
        x, y = start
        new_position = x + self.x_velocity, y + self.y_velocity
        self.trajectory.append(new_position)
        if self.x_velocity != 0:
            self.x_velocity = self.x_velocity - 1 if self.x_velocity > 0 else self.x_velocity + 1
        self.y_velocity -= 1
    
    def calculate_trajectory(self, target_area):
        while True:
            self.step()
            x, y = self.trajectory[-1]
            if x > target_area["x"][1] or y < target_area["y"][0]:
                break
            if x in range(target_area["x"][0], target_area["x"][1]+1) and y in range(target_area["y"][0], target_area["y"][1]+1):
                self.is_in_target_area = True
                break
        

def print_probe_trajectory(target_area, probe):
    """
    Prints probe trajectory. Helps with debugging.
    """
    for x in range(10, target_area["y"][0] - 5, -1):
        for y in range(target_area["x"][1] + 10):
            if (x, y) == (0, 0):
                print("S", end="")
            elif (y, x) in probe.trajectory:
                print("#", end="")
            elif x in range(target_area["y"][0], target_area["y"][1]+1) and y in range(target_area["x"][0], target_area["x"][1]+1):
                print("T", end="")
            else:
                print(".", end="")
        print()


# Puzzle input
target_area = get_target_area("target area: x=269..292, y=-68..-44")


# Puzzle 1 + Puzzle 2
max_y = 0
result = 0
for x in range(1, target_area["x"][1] + 1):
    for y in range(target_area["y"][0] - 1, 100):
        probe = Probe(x, y, target_area)
        if probe.is_in_target_area:
            result += 1
            for coor in probe.trajectory:
                if max_y < coor[1]:
                    max_y = coor[1]

print(f"Puzzle 1 = {max_y}")
print(f"Puzzle 2 = {result}")
