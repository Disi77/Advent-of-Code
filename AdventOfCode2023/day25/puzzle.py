import networkx as nx


path = "AdventOfCode2023/day25/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    data = {}
    for line in raw_data:
        key, values = line.strip().split(": ")
        data[key] = [x for x in values.split()]

G = nx.Graph(data)

for component1, component2 in list(nx.minimum_edge_cut(G)):
    G.remove_edge(component1, component2)

group1, group2 = nx.connected_components(G)

print("Puzzle 1 =", len(group1) * len(group2))
