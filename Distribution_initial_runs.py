##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Función para ordenar los videos por duración utilizando Distribution of initial runs
def polyphase_sort_videos(videos):
    # Dividir los videos en ejecuciones iniciales
    initial_runs = [[]]  # Lista para almacenar las ejecuciones iniciales
    current_run = 0  # Índice de la ejecución actual
    for video in videos:  # Iteramos sobre los videos
        if not initial_runs[current_run] or initial_runs[current_run][-1][1] <= video[1]:  # Comprobamos si el video puede ser añadido a la ejecución actual
            initial_runs[current_run].append(video)  # Añadimos el video a la ejecución actual
        else:  # Si el video no puede ser añadido a la ejecución actual
            current_run += 1  # Pasamos a la siguiente ejecución
            initial_runs.append([video])  # Creamos una nueva ejecución y añadimos el video a ella
    
    # Fusionar las ejecuciones iniciales
    while len(initial_runs) > 1:  # Mientras haya más de una ejecución inicial
        merged_runs = []  # Lista para almacenar las ejecuciones fusionadas
        for i in range(0, len(initial_runs), 2):  # Iteramos sobre las ejecuciones en pares
            if i + 1 < len(initial_runs):  # Si hay al menos dos ejecuciones para fusionar
                merged_run = merge_runs(initial_runs[i], initial_runs[i + 1])  # Fusionamos dos ejecuciones consecutivas
                merged_runs.append(merged_run)  # Añadimos la ejecución fusionada a la lista
            else:  # Si solo hay una ejecución restante
                merged_runs.append(initial_runs[i])  # Añadimos la ejecución tal cual
        initial_runs = merged_runs  # Reemplazamos las ejecuciones originales por las nuevas ejecuciones fusionadas
    
    return initial_runs[0]  # Devolvemos la única ejecución final

# Función para fusionar dos ejecuciones iniciales ordenadas
def merge_runs(run1, run2):
    merged_run = []  # Lista para almacenar la ejecución fusionada
    i, j = 0, 0  # Índices para recorrer las dos ejecuciones
    while i < len(run1) and j < len(run2):  # Mientras haya elementos en ambas ejecuciones
        if run1[i][1] <= run2[j][1]:  # Comparamos las duraciones de los videos
            merged_run.append(run1[i])  # Añadimos el video de la primera ejecución
            i += 1  # Pasamos al siguiente video en la primera ejecución
        else:  # Si la duración del video en la segunda ejecución es menor
            merged_run.append(run2[j])  # Añadimos el video de la segunda ejecución
            j += 1  # Pasamos al siguiente video en la segunda ejecución
    while i < len(run1):  # Añadimos los videos restantes de la primera ejecución
        merged_run.append(run1[i])
        i += 1
    while j < len(run2):  # Añadimos los videos restantes de la segunda ejecución
        merged_run.append(run2[j])
        j += 1
    return merged_run  # Devolvemos la ejecución fusionada

# Lista de videos (nombre, duración en minutos)
videos = [
    ("Video1.mp4", 15),
    ("Video2.mp4", 30),
    ("Video3.mp4", 45),
    ("Video4.mp4", 25),
    ("Video5.mp4", 60),
    ("Video6.mp4", 120),
    ("Video7.mp4", 90),
    ("Video8.mp4", 50)
]

# Mostrar la lista de videos sin organizar
print("Lista de videos sin organizar:")
for video in videos:
    print(f"{video[0]}: {video[1]} minutos")

# Organizar los videos por duración utilizando Distribution of initial runs
sorted_videos = polyphase_sort_videos(videos)

# Mostrar los videos ordenados
print("\nLista de videos ordenada por duración:")
for video in sorted_videos:
    print(f"{video[0]}: {video[1]} minutos")
