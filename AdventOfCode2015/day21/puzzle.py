from itertools import combinations


class Player:
    def __init__(self, name, hit_points, damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def attack(self, defender):
        result = self.damage - defender.armor
        if result <= 0:
            result = 1
        defender.hit_points -= result
        # print(
        #     f"The {self.name} deals {self.damage}-{defender.armor}={result}; the {defender.name} goes down to {defender.hit_points} hit points."
        # )

    def use_items(self, items):
        for i in items:
            self.damage += i.damage
            self.armor += i.armor


class Item:
    def __init__(self, category, name, cost, damage, armor):
        self.category = category
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


weapons = [
    Item("weapons", "Dagger", 8, 4, 0),
    Item("weapons", "Shortsword", 10, 5, 0),
    Item("weapons", "Warhammer", 25, 6, 0),
    Item("weapons", "Longsword", 40, 7, 0),
    Item("weapons", "Greataxe", 74, 8, 0),
]

armors = [
    Item("armor", "Leather", 13, 0, 1),
    Item("armor", "Chainmail", 31, 0, 2),
    Item("armor", "Splintmail", 53, 0, 3),
    Item("armor", "Bandedmail", 75, 0, 4),
    Item("armor", "Platemail", 102, 0, 5),
    Item("armor", "None", 0, 0, 0),
]

rings = [
    Item("rings", "Damage +1", 25, 1, 0),
    Item("rings", "Damage +2", 50, 2, 0),
    Item("rings", "Damage +3", 100, 3, 0),
    Item("rings", "Defense +1", 20, 0, 1),
    Item("rings", "Defense +2", 40, 0, 2),
    Item("rings", "Defense +3", 80, 0, 3),
    Item("rings", "None", 0, 0, 0),
    Item("rings", "None", 0, 0, 0),
]

# Puzzle 1
min_costs = 10000
for w in weapons:
    for a in armors:
        for i1, i2 in combinations(range(len(rings)), 2):
            r1 = rings[i1]
            r2 = rings[i2]
            boss = Player("boss", 109, 8, 2)
            player = Player("player", 100, 0, 0)
            player.use_items([w, a, r1, r2])
            cost = w.cost + a.cost + r1.cost + r2.cost

            while True:
                player.attack(boss)
                if boss.hit_points <= 0:
                    if min_costs > cost:
                        min_costs = cost
                    break
                boss.attack(player)
                if player.hit_points <= 0:
                    break

print("Puzzle 1 =", min_costs)


# Puzzle 2
max_costs = 0
for w in weapons:
    for a in armors:
        for i1, i2 in combinations(range(len(rings)), 2):
            r1 = rings[i1]
            r2 = rings[i2]
            boss = Player("boss", 109, 8, 2)
            player = Player("player", 100, 0, 0)
            player.use_items([w, a, r1, r2])
            cost = w.cost + a.cost + r1.cost + r2.cost

            while True:
                player.attack(boss)
                if boss.hit_points <= 0:
                    break
                boss.attack(player)
                if player.hit_points <= 0:
                    if max_costs < cost:
                        max_costs = cost
                    break

print("Puzzle 2 =", max_costs)
