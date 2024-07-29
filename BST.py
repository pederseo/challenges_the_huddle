# 5) Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, elemento):
        if self.raiz is None:
            self.raiz = Nodo(elemento)
            print(f"Insertado {elemento} como raíz")
        else:
            self._insertar(self.raiz, elemento)

    def _insertar(self, nodo, elemento):
        if elemento < nodo.elemento:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(elemento)
                print(f"Insertado {elemento} a la izquierda de {nodo.elemento}")
            else:
                self._insertar(nodo.izquierda, elemento)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(elemento)
                print(f"Insertado {elemento} a la derecha de {nodo.elemento}")
            else:
                self._insertar(nodo.derecha, elemento)

bst = BST()
elements = [15, 10, 20, 8, 12]
for el in elements:
    bst.insertar(el)
