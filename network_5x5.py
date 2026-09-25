import networkx as nx
import matplotlib.pyplot as plt
import random


# -----------------------------------
# 1. Create the road network
# -----------------------------------

G = nx.grid_2d_graph(5, 5)


# -----------------------------------
# 2. Assign random road weights
# -----------------------------------

random.seed(42)

for u, v in G.edges():
    G[u][v]["weight"] = random.randint(1, 10)


# -----------------------------------
# 3. Create positions for visualization
# -----------------------------------

pos = {(x, y): (x, y) for x, y in G.nodes()}

print("Number of nodes:", G.number_of_nodes())
print("Number of roads:", G.number_of_edges())

# -----------------------------------
# 3. Define start and destination
# -----------------------------------

start = (0, 0)
destination = (4,4)


# -----------------------------------
# 4. Find shortest route using Dijkstra
# -----------------------------------

route = nx.shortest_path(
    G,
    source=start,
    target=destination,
    weight="weight"
)


# -----------------------------------
# 5. Calculate total route cost
# -----------------------------------

route_cost = nx.shortest_path_length(
    G,
    source=start,
    target=destination,
    weight="weight"
)


print("Shortest route:",route,"\nTotal route cost:",route_cost)


# -----------------------------------
# 6. Identify edges in the route
# -----------------------------------

route_edges = list(zip(route[:-1], route[1:]))


# -----------------------------------
# 7. Draw the complete network
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
# 8. Highlight the shortest route
# -----------------------------------

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=route_edges,
    width=4,
    edge_color="red"
)


# -----------------------------------
# 9. Highlight start and destination
# -----------------------------------

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[start],
    node_color="green",
    node_size=900
)

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[destination],
    node_color="orange",
    node_size=900
)


# -----------------------------------
# 10. Display road weights
# -----------------------------------

edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8
)


plt.title("Dijkstra Shortest Route")

plt.axis("equal")
plt.show()