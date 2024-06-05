##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import heapq

# Función para fusionar múltiples secuencias ordenadas utilizando Balanced Multiway Merging
def balanced_multiway_merge(sorted_sequences):
    merged_sequence = []  # Lista para almacenar la secuencia fusionada final
    heap = []  # Montículo para realizar la fusión equilibrada
    
    # Inicializar el montículo con el primer elemento de cada secuencia
    for i, seq in enumerate(sorted_sequences):
        if seq:  # Verificar si la secuencia no está vacía
            heapq.heappush(heap, (seq[0], i, 0))  # (elemento, índice de la secuencia, índice del elemento)

    # Fusionar las secuencias hasta que el montículo esté vacío
    while heap:
        value, seq_index, elem_index = heapq.heappop(heap)  # Obtener el elemento más pequeño del montículo
        merged_sequence.append(value)  # Agregar el elemento a la secuencia fusionada

        # Incrementar el índice del elemento actual en la secuencia correspondiente
        elem_index += 1

        # Verificar si aún hay elementos en la secuencia actual
        if elem_index < len(sorted_sequences[seq_index]):
            next_value = sorted_sequences[seq_index][elem_index]
            heapq.heappush(heap, (next_value, seq_index, elem_index))  # Agregar el próximo elemento al montículo
    
    return merged_sequence

# Datos de ejemplo: listas de nombres de estudiantes ordenadas alfabéticamente
sorted_sequences = [
    ['Anna', 'David', 'Emma'],
    ['James', 'Lucas', 'Olivia', 'Sophia'],
    ['Ethan', 'Isabella', 'Liam'],
    ['Ava', 'Benjamin', 'Mia'],
]

# Mostrar la secuencia original
print("Secuencias originales:")
for seq in sorted_sequences:
    print(seq)

# Fusionar las secuencias utilizando Balanced Multiway Merging
merged_sequence = balanced_multiway_merge(sorted_sequences)

# Mostrar la secuencia fusionada
print("\nSecuencia fusionada:")
print(merged_sequence)
