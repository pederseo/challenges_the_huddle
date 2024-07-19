# Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una 
# función que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.

from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def algoritmo_dfs(grafo, nodo_inicial):
    ''' Inicializa un conjunto para los nodos visitados'''
    vicitados = set()
    # Inicializa una cola para los nodos por visitar
    queue = deque([nodo_inicial])
    
    # Mientras la cola no esté vacía
    while queue:
        # Saca un nodo de la cola
        nodo = queue.popleft()
        # Si el nodo no ha sido visitado
        if nodo not in vicitados:
            # Marca el nodo como visitado
            vicitados.add(nodo)
            # Imprime el nodo visitado
            print(nodo, end=' ')
            # Añade todos los vecinos no visitados a la cola
            for vecinos in grafo[nodo]:
                if vecinos not in vicitados:
                    queue.append(vecinos)

    return vicitados

algoritmo_dfs(grafo, 'A')
