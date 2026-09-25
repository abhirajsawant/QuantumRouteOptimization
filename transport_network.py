import networkx as nx
import matplotlib.pyplot as plt
import random


# -----------------------------------
# 1. Create 5×5 road network
# -----------------------------------

G = nx.grid_2d_graph(5, 5)


# -----------------------------------
# 2. Generate transportation data
# -----------------------------------

random.seed(42)

for u, v in G.edges():

    # Road distance in km
    distance = random.uniform(1.0, 5.0)

    # Average speed in km/h
    speed = random.choice([30, 40, 50, 60])

    # Travel time in minutes
    time = (distance / speed) * 60

    # Congestion level
    congestion = random.uniform(0.0, 1.0)

    # Simple fuel consumption model
    fuel = distance * random.uniform(0.08, 0.15)

    # Store attributes
    G[u][v]["distance"] = distance
    G[u][v]["speed"] = speed
    G[u][v]["time"] = time
    G[u][v]["congestion"] = congestion
    G[u][v]["fuel"] = fuel

# -----------------------------------
# Transportation Cost function
# -----------------------------------

def calculate_cost(distance, time, congestion, fuel):

    weight_distance = 1.0
    weight_time = 0.5
    weight_congestion = 2.0
    weight_fuel = 5.0

    cost = (
        weight_distance * distance
        + weight_time * time
        + weight_congestion * congestion
        + weight_fuel * fuel
    )

    return cost

# -----------------------------------
# 4. Calculate cost for every road
# -----------------------------------

for u, v in G.edges():

    distance = G[u][v]["distance"]
    time = G[u][v]["time"]
    congestion = G[u][v]["congestion"]
    fuel = G[u][v]["fuel"]

    G[u][v]["cost"] = calculate_cost(
        distance,
        time,
        congestion,
        fuel
    )


# -----------------------------------
# 5. Start and destination
# -----------------------------------

start = (0, 0)
destination = (4, 4)


# -----------------------------------
# 6. Dijkstra using transportation cost
# -----------------------------------

route = nx.shortest_path(
    G,
    source=start,
    target=destination,
    weight="cost"
)

route_cost = nx.shortest_path_length(
    G,
    source=start,
    target=destination,
    weight="cost"
)


# -----------------------------------
# 7. Print results
# -----------------------------------

print("Transportation optimized route:")
print(route)

print("\nTotal transportation cost:")
print(route_cost)


# -----------------------------------
# 8. Visualization
# -----------------------------------

pos = {(x, y): (x, y) for x, y in G.nodes()}

route_edges = list(zip(route[:-1], route[1:]))

plt.figure(figsize=(9, 9))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightblue",
    edge_color="gray"
)

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=route_edges,
    width=4,
    edge_color="red"
)

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[start],
    node_size=900,
    node_color="green"
)

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[destination],
    node_size=900,
    node_color="orange"
)

plt.title("Transportation Cost Optimized Route")

plt.axis("equal")
plt.show()