##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importa el módulo random para generar números aleatorios (no usado en este ejemplo específico)

# Lista de tareas con sus duraciones en minutos
tasks = [
    ("Lavar platos", 15),
    ("Responder correos electrónicos", 30),
    ("Hacer ejercicio", 45),
    ("Leer un capítulo de un libro", 25),
    ("Preparar almuerzo", 60),
    ("Reunión de trabajo", 120),
    ("Limpiar la casa", 90),
    ("Estudiar programación", 50)
]

def shell_sort_tasks(tasks):
    n = len(tasks)  # Obtiene la longitud de la lista de tareas
    gap = n // 2  # Inicializa la brecha (gap) como la mitad de la longitud de la lista
    
    while gap > 0:  # Mientras la brecha sea mayor que 0
        for i in range(gap, n):  # Recorre los elementos desde la brecha hasta el final de la lista
            temp_task = tasks[i]  # Guarda temporalmente la tarea actual
            j = i  # Inicializa j con el índice actual
            # Ordena las tareas en la sublista definida por la brecha
            while j >= gap and tasks[j - gap][1] > temp_task[1]:  # Mientras j sea mayor o igual a la brecha y la tarea en j-gap sea mayor que la tarea temporal
                tasks[j] = tasks[j - gap]  # Desplaza la tarea en j-gap a la posición j
                j -= gap  # Decrementa j en la cantidad de la brecha
            tasks[j] = temp_task  # Coloca la tarea temporal en su posición correcta
        gap //= 2  # Reduce la brecha a la mitad para la siguiente iteración

# Imprime la lista original de tareas con sus duraciones
print("Lista de tareas original:")
for task, duration in tasks:  # Recorre cada tarea y su duración
    print(f"{task}: {duration} minutos")  # Imprime la tarea y su duración

# Llama a la función para ordenar las tareas
shell_sort_tasks(tasks)

# Imprime la lista ordenada de tareas por duración
print("\nLista de tareas ordenada por duración:")
for task, duration in tasks:  # Recorre cada tarea y su duración en la lista ordenada
    print(f"{task}: {duration} minutos")  # Imprime la tarea y su duración

