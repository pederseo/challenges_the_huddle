# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.

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
    visitados = set()
    
    def recursion(nodo):
 
        visitados.add(nodo)
        # Imprime el nodo visitado
        print(nodo, end=' ')
        
        # Recorre todos los vecinos del nodo actual
        for vecinos in grafo[nodo]:
            # Si el vecino no ha sido visitado, llama recursivamente a recursion
            if vecinos not in visitados:
                recursion(vecinos)
    
    recursion(nodo_inicial)
    
    return visitados

algoritmo_dfs(grafo, 'A')
