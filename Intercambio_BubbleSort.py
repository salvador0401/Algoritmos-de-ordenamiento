def bubble_sort_names(names):
    """Ordena una lista de nombres utilizando el algoritmo Bubble Sort."""
    n = len(names)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                # Intercambia los nombres si están en el orden incorrecto
                names[j], names[j + 1] = names[j + 1], names[j]

# Lista de nombres desordenados
names = ["Juan", "Ana", "Pedro", "María", "Carlos", "Laura", "Luis", "Sofía"]

print("Lista de nombres original:")
print(names)#imprime el orden original

bubble_sort_names(names)#Acomoda alfabeticamente

print("\nLista de nombres ordenada:")
print(names)#Muestra el nuevo orden
