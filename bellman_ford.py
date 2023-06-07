import matplotlib.pyplot as plt
import numpy as np

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, peso):
        self.grafo.append([u, v, peso])

    def bellman_ford(self, origen):
        distancias = [float('inf')] * self.V
        distancias[origen] = 0

        for _ in range(self.V - 1):
            for u, v, peso in self.grafo:
                if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso

        # Verificar si hay ciclos de peso negativo
        for u, v, peso in self.grafo:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                print("El grafo contiene un ciclo de peso negativo")
                return

        # Graficar el grafo
        self.dibujar_grafo()

        # Imprimir las distancias más cortas
        for i in range(self.V):
            print(f"Distancia desde el origen hasta el nodo {i}: {distancias[i]}")

    def dibujar_grafo(self):
        plt.figure()
        plt.title("Grafo")
        plt.xlabel("Nodo")
        plt.ylabel("Peso")

        for u, v, peso in self.grafo:
            plt.plot([u, v], [0, peso], 'bo-')

        plt.show()

# Crear un grafo de ejemplo
g = Grafo(5)
g.agregar_arista(0, 1, -1)
g.agregar_arista(0, 2, 4)
g.agregar_arista(1, 2, 3)
g.agregar_arista(1, 3, 2)
g.agregar_arista(1, 4, 2)
g.agregar_arista(3, 2, 5)
g.agregar_arista(3, 1, 1)
g.agregar_arista(4, 3, -3)

# Calcular las distancias más cortas desde el nodo 0
g.bellman_ford(0)
