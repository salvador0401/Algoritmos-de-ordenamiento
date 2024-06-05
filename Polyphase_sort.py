##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import heapq  # Importamos el módulo heapq para manipular heaps
from datetime import datetime as dt  # Importamos datetime y lo renombramos como dt

# Función para fusionar dos secuencias ordenadas utilizando Polyphase Sort
def polyphase_merge(seq1, seq2):
    merged_seq = []  # Lista para almacenar la secuencia fusionada
    i, j = 0, 0  # Índices para recorrer las secuencias
    
    # Fusionar las secuencias hasta que una de ellas se agote
    while i < len(seq1) and j < len(seq2):
        if seq1[i][1] <= seq2[j][1]:  # Comparamos las fechas de llegada
            merged_seq.append(seq1[i])  # Añadimos el registro de la primera secuencia
            i += 1
        else:
            merged_seq.append(seq2[j])  # Añadimos el registro de la segunda secuencia
            j += 1
    
    # Agregar los elementos restantes de la primera secuencia
    while i < len(seq1):
        merged_seq.append(seq1[i])
        i += 1
    
    # Agregar los elementos restantes de la segunda secuencia
    while j < len(seq2):
        merged_seq.append(seq2[j])
        j += 1
    
    return merged_seq  # Devolvemos la secuencia fusionada

# Función para realizar una fase de Polyphase Sort
def polyphase_phase(sequences):
    num_sequences = len(sequences)
    merged_sequences = []  # Lista para almacenar las secuencias fusionadas
    
    # Fusionar pares de secuencias
    for i in range(0, num_sequences, 2):
        if i + 1 < num_sequences:
            merged_seq = polyphase_merge(sequences[i], sequences[i + 1])  # Fusionamos dos secuencias consecutivas
            merged_sequences.append(merged_seq)
        else:
            merged_sequences.append(sequences[i])  # Si solo hay una secuencia restante, la añadimos sin fusionar
    
    return merged_sequences  # Devolvemos las secuencias fusionadas

# Función para convertir la cadena de fecha en un objeto datetime
def parse_date(date_str):
    return dt.strptime(date_str, '%Y-%m-%d')  # Usamos dt en lugar de datetime

# Función para formatear la fecha en un formato legible
def format_date(date):
    return date.strftime('%Y-%m-%d')  # Formateamos la fecha como una cadena

# Datos de ejemplo: reservaciones de hotel (número de reserva, fecha de llegada)
reservations = [
    [(101, '2024-07-10'), (102, '2024-07-12'), (103, '2024-07-15')],
    [(104, '2024-07-11'), (105, '2024-07-14')],
    [(106, '2024-07-09'), (107, '2024-07-13')],
    [(108, '2024-07-08')],
    [(109, '2024-07-20'), (110, '2024-07-22')],
    [(111, '2024-07-17'), (112, '2024-07-19')],
    [(113, '2024-07-18'), (114, '2024-07-21')],
    [(115, '2024-07-16')],
]

# Convertir las fechas de llegada a objetos datetime
for seq in reservations:
    for i, (reservation_id, date_str) in enumerate(seq):
        seq[i] = (reservation_id, parse_date(date_str))  # Convertimos la cadena de fecha a datetime

# Mostrar las secuencias originales
print("Secuencias originales:")
for seq in reservations:
    print([(reservation_id, format_date(arrival_date)) for reservation_id, arrival_date in seq])

# Realizar fases de Polyphase Sort hasta que quede una única secuencia
while len(reservations) > 1:
    reservations = polyphase_phase(reservations)

# Mostrar la secuencia ordenada final
print("\nSecuencia ordenada por fecha de llegada:")
for reservation_id, arrival_date in reservations[0]:
    print(f"({reservation_id}, {format_date(arrival_date)})")  # Imprimimos el número de reserva y la fecha de llegada

