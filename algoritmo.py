import time
import random
import tracemalloc
#______________________________________________________________
def algoritmo(lista):
    contador = len(lista)
    indice = contador - 1
    for _ in range(contador):
        for i in range(indice):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
#______________________________________________________________





def tiempo_ejecucion(lista):
    tracemalloc.start()
    start_time = time.time()  # tiempo inicial

    algoritmo(lista)

    memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()  # tiempo final
    tiempo = end_time - start_time  # tiempo transcurrido

    print(f'Tiempo de ejecución:{tiempo} segundos \nMemoria: {memoria}')

def lista_desordenada(cantidad):
    lista = [random.randint(0, 1000) for _ in range(cantidad)]
    return lista


lista_100 = lista_desordenada(100)
lista_300 = lista_desordenada(300)
lista_500 = lista_desordenada(500)

lista_ordenada_100 = algoritmo(lista_100)
lista_ordenada_300 = algoritmo(lista_300)
lista_ordenada_500 = algoritmo(lista_500)

tiempo_ejecucion(lista_ordenada_100)
tiempo_ejecucion(lista_ordenada_300)
tiempo_ejecucion(lista_ordenada_500)
