import time
import random

# Crear una lista de 500 elementos aleatorios
lista = [random.randint(0, 1000) for _ in range(500)]

def algoritmo(lista):
    contador = len(lista)
    indice = contador - 1
    for _ in range(contador):
        for i in range(indice):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

# Medir el tiempo de ejecución solo para la llamada a bubble_sort
start_time = time.time()  # tiempo inicial

lista_ordenada = algoritmo(lista)

end_time = time.time()  # tiempo final

elapsed_time = end_time - start_time  # tiempo transcurrido

print("Lista ordenada:", lista_ordenada)
print("Tiempo de ejecución:", elapsed_time, "segundos")

