import time
import random
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
    start_time = time.time()  # tiempo inicial
    lista_ordenada = algoritmo(lista)
    end_time = time.time()  # tiempo final
    elapsed_time = end_time - start_time  # tiempo transcurrido

    print("Lista ordenada:", lista_ordenada)
    print("Tiempo de ejecución:", elapsed_time, "segundos")

def lista_desordenada(cantidad):
    lista = [random.randint(0, 1000) for _ in range(cantidad)]
    return lista


lista_100 = lista_desordenada(100)
lista_300 = lista_desordenada(300)
lista_300 = lista_desordenada(300)

lista_ordenada_100 = algoritmo(lista_100)
lista_ordenada_300 = algoritmo(lista_100)
lista_ordenada_500 = algoritmo(lista_100)

tiempo_ejecucion(lista_ordenada_100)
tiempo_ejecucion(lista_ordenada_300)
tiempo_ejecucion(lista_ordenada_500)

