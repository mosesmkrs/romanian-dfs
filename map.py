import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Define the graph connections
graph_data = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# Create a NetworkX graph
G = nx.Graph(graph_data)

# Use a layout suitable for graphs
pos = nx.spring_layout(G, seed=42)  # Positions nodes using a force-directed algorithm

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_size=1500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    edgecolors="black"
)
plt.title("Romania Graph")
plt.show()
