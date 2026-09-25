import networkx as nx
import matplotlib.pyplot as plt


# -----------------------------
# 1. Create road network
# -----------------------------

G = nx.Graph()

G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=3)
G.add_edge("B", "D", weight=4)
G.add_edge("C", "D", weight=2)


# -----------------------------
# 2. Find shortest route
# -----------------------------

start = "A"
destination = "D"

route = nx.shortest_path(
    G,
    source=start,
    target=destination,
    weight="weight"
)

distance = nx.shortest_path_length(
    G,
    source=start,
    target=destination,
    weight="weight"
)

print("Shortest route:", route)
print("Total cost:", distance)


# -----------------------------
# 3. Create positions
# -----------------------------

positions = {
    "A": (0, 0),
    "B": (1, 1),
    "C": (1, -1),
    "D": (2, 0)
}


# -----------------------------
# 4. Draw entire road network
# -----------------------------

nx.draw(
    G,
    positions,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=15
)


# -----------------------------
# 5. Highlight shortest route
# -----------------------------

route_edges = list(zip(route[:-1], route[1:]))

nx.draw_networkx_edges(
    G,
    positions,
    edgelist=route_edges,
    width=4,
    edge_color="red"
)


# -----------------------------
# 6. Show road weights
# -----------------------------

edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G,
    positions,
    edge_labels=edge_labels
)


plt.title("Shortest Route")
plt.show()