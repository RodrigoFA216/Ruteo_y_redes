import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo de la red
G = nx.Graph()
G.add_edges_from(
    [
        ("Router A", "Router B"),
        ("Router A", "Router C"),
        ("Router B", "Router C"),
        ("Router B", "Router D"),
        ("Router C", "Router D"),
        ("Router C", "Router E"),
        ("Router D", "Router E"),
    ]
)

# Dibujar el grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color="lightblue")
plt.title("Red de Routers")
plt.axis("off")
plt.show()
