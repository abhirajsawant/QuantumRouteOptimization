import networkx as nx
import random


# -----------------------------------
# Create network
# -----------------------------------

G = nx.grid_2d_graph(5, 5)

random.seed(42)

for u, v in G.edges():
    G[u][v]["weight"] = random.randint(1, 10)


# -----------------------------------
# Start and destination
# -----------------------------------

start = (0, 0)
destination = (4, 4)


# -----------------------------------
# A* heuristic
# -----------------------------------

def heuristic(node, goal):

    x1, y1 = node
    x2, y2 = goal

    return abs(x1 - x2) + abs(y1 - y2)


# -----------------------------------
# Dijkstra
# -----------------------------------

dijkstra_route = nx.shortest_path(
    G,
    source=start,
    target=destination,
    weight="weight"
)

dijkstra_cost = nx.shortest_path_length(
    G,
    source=start,
    target=destination,
    weight="weight"
)


# -----------------------------------
# A*
# -----------------------------------

astar_route = nx.astar_path(
    G,
    source=start,
    target=destination,
    heuristic=heuristic,
    weight="weight"
)

astar_cost = nx.astar_path_length(
    G,
    source=start,
    target=destination,
    heuristic=heuristic,
    weight="weight"
)


# -----------------------------------
# Results
# -----------------------------------

print("========== DIJKSTRA ==========")

print("Route:")
print(dijkstra_route)

print("Cost:")
print(dijkstra_cost)


print("\n========== A* ==========")

print("Route:")
print(astar_route)

print("Cost:")
print(astar_cost)


print("\n========== COMPARISON ==========")

if dijkstra_cost == astar_cost:
    print("Both algorithms found the same minimum cost.")
else:
    print("The results are different.")