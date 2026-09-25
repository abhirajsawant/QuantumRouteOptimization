import networkx as nx
import matplotlib.pyplot as plt
import random


# -----------------------------------
# 1. Create the road network
# -----------------------------------

G = nx.grid_2d_graph(5, 5)


# -----------------------------------
# 2. Assign road weights
# -----------------------------------

random.seed(42)

for u, v in G.edges():
    G[u][v]["weight"] = random.randint(1, 10)


# -----------------------------------
# 3. Create node positions
# -----------------------------------

pos = {(x, y): (x, y) for x, y in G.nodes()}


# -----------------------------------
# 4. Define start and destination
# -----------------------------------

start = (0, 0)
destination = (4, 4)


# -----------------------------------
# 5. Define A* heuristic
# -----------------------------------

def heuristic(node, goal):

    x1, y1 = node
    x2, y2 = goal

    return abs(x1 - x2) + abs(y1 - y2)


# -----------------------------------
# 6. Run A*
# -----------------------------------

route = nx.astar_path(
    G,
    source=start,
    target=destination,
    heuristic=heuristic,
    weight="weight"
)


# -----------------------------------
# 7. Calculate route cost
# -----------------------------------

route_cost = nx.astar_path_length(
    G,
    source=start,
    target=destination,
    heuristic=heuristic,
    weight="weight"
)


# -----------------------------------
# 8. Print results
# -----------------------------------

print("A* route:",route,"\nA* route cost:",route_cost)

# -----------------------------------
# 9. Create route edges
# -----------------------------------

route_edges = list(zip(route[:-1], route[1:]))


# -----------------------------------
# 10. Draw complete network
# -----------------------------------

plt.figure(figsize=(9, 9))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightblue",
    font_size=8,
    edge_color="gray"
)


# -----------------------------------
# 11. Highlight A* route
# -----------------------------------

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=route_edges,
    width=4,
    edge_color="red"
)


# -----------------------------------
# 12. Highlight start
# -----------------------------------

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[start],
    node_color="green",
    node_size=900
)


# -----------------------------------
# 13. Highlight destination
# -----------------------------------

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[destination],
    node_color="orange",
    node_size=900
)


# -----------------------------------
# 14. Display road weights
# -----------------------------------

edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8
)


plt.title("A* Shortest Route")

plt.axis("equal")

plt.show()