import os  # Importa el módulo os para interactuar con el sistema de archivos
import random  # Importa el módulo random para desordenar la lista

# Obtiene la lista de archivos en la ruta especificada
files = os.listdir(r"C:\Users\salva\OneDrive\Escritorio\IA\Practica 2\Ordenamiento Interno")

# Función para ordenar utilizando Quick Sort
def quicksort(arr):
    """Ordena una lista utilizando el algoritmo Quick Sort."""
    if len(arr) <= 1:  # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
        return arr
    pivot = arr[0]  # Selecciona el primer elemento como pivote
    # Sublistas de elementos menores y mayores al pivote
    less = [x for x in arr[1:] if x <= pivot]  # Elementos menores o iguales al pivote
    greater = [x for x in arr[1:] if x > pivot]  # Elementos mayores al pivote
    # Recursivamente ordena las sublistas y las concatena con el pivote
    return quicksort(less) + [pivot] + quicksort(greater)

# Desordena la lista de archivos
random.shuffle(files)

# Imprime la lista de archivos desordenada
print("Lista de archivos desordenada:")
for file in files:
    print(file)

# Ordena la lista de archivos utilizando Quick Sort
sorted_files = quicksort(files)

# Imprime la lista de archivos ordenada
print("\nLista de archivos ordenada:")
for file in sorted_files:
    print(file)
