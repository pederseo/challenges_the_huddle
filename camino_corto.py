# 6) Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que encuentre el 
# camino más corto entre dos nodos especificados usando cualquier método que prefieras.
from collections import deque

def bfs(grafo, inicio, final):
    queue = deque([(inicio, [inicio])])
    seen = set()

    while queue:
        (nodo, camino) = queue.popleft()

        if nodo in seen:
            continue

        seen.add(nodo)

        if nodo == final:
            return len(camino) - 1, camino 

        for next_node in grafo[nodo]:
            if next_node not in seen:
                queue.append((next_node, camino + [next_node]))

    return float("inf"), []


grafo_no_ponderado = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

nodo_inicial = 'A'
nodo_final = 'E'
coste, camino = bfs(grafo_no_ponderado, nodo_inicial, nodo_final)
print(f"El camino más corto de {nodo_inicial} a {nodo_final} tiene un costo de {coste} y es {camino}")
