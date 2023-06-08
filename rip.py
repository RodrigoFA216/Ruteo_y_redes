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

# Diccionario de tablas de enrutamiento de los routers
routing_tables = {
    "Router A": {
        "Router A": 0,
        "Router B": 1,
        "Router C": 1,
        "Router D": float("inf"),
        "Router E": float("inf"),
    },
    "Router B": {
        "Router A": 1,
        "Router B": 0,
        "Router C": 1,
        "Router D": 1,
        "Router E": float("inf"),
    },
    "Router C": {
        "Router A": 1,
        "Router B": 1,
        "Router C": 0,
        "Router D": 1,
        "Router E": 1,
    },
    "Router D": {
        "Router A": float("inf"),
        "Router B": 1,
        "Router C": 1,
        "Router D": 0,
        "Router E": 1,
    },
    "Router E": {
        "Router A": float("inf"),
        "Router B": float("inf"),
        "Router C": 1,
        "Router D": 1,
        "Router E": 0,
    },
}


# Función para graficar las tablas de enrutamiento
def graficar_tablas_enrutamiento():
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)

    for router, routing_table in routing_tables.items():
        labels = {
            node: f"{node}\n{distancia}" for node, distancia in routing_table.items()
        }
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color="lightblue")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels, font_size=10)

    plt.axis("off")
    plt.title("Tablas de Enrutamiento")
    plt.show()


# Graficar las tablas de enrutamiento inicialmente
graficar_tablas_enrutamiento()

# Ejecutar el algoritmo RIP para actualizar las tablas de enrutamiento
for _ in range(3):  # Ejecutar 3 iteraciones del algoritmo RIP
    for router, routing_table in routing_tables.items():
        for vecino in G.neighbors(router):
            for destino in routing_tables[vecino]:
                if destino != router:
                    nueva_distancia = (
                        routing_tables[vecino][destino] + routing_table[vecino]
                    )
                    if nueva_distancia < routing_table[destino]:
                        routing_table[destino] = nueva_distancia

    # Graficar las tablas de enrutamiento después de cada iteración
    graficar_tablas_enrutamiento()
