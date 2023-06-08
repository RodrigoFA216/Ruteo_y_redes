import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, source):
    # Inicialización de variables
    distances = {node: float("inf") for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[source] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Seleccionar el nodo con la distancia mínima
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        # Actualizar las distancias de los vecinos del nodo actual
        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor]["weight"]
            distance = distances[current_node] + edge_weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node

    return distances, previous


def draw_shortest_path(graph, distances, previous, source, target):
    # Obtener el camino más corto
    path = []
    current_node = target
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    # Dibujar el grafo
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw_networkx(
        graph, pos, with_labels=True, node_size=500, node_color="lightblue"
    )

    # Obtener los pesos de cada enlace
    edge_labels = nx.get_edge_attributes(graph, "weight")

    # Resaltar el camino más corto
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=2.0, edge_color="red")

    # Dibujar los pesos de cada enlace
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Grafo Dijkstra con el camino más corto")
    plt.axis("off")
    plt.show()


# Crear el grafo de ejemplo
G = nx.Graph()
G.add_weighted_edges_from(
    [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
    ]
)

# Ejecutar el algoritmo de Dijkstra
source_node = "A"
target_node = "E"
distances, previous = dijkstra(G, source_node)

# Imprimir las distancias y el camino más corto
print(f"Distancias desde el nodo fuente ({source_node}):")
for node, distance in distances.items():
    print(f"{node}: {distance}")
print(f"\nCamino más corto desde {source_node} hasta {target_node}:")
print(previous)

# Dibujar el grafo con el camino más corto resaltado
draw_shortest_path(G, distances, previous, source_node, target_node)
