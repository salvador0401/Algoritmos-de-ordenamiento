##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importamos el módulo random para generar datos aleatorios
import string  # Importamos el módulo string para manipular cadenas de texto

# Generar datos de estudiantes simulados
def generate_student_data(num_records):
    # Listas de nombres y apellidos simulados
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    students = []  # Lista para almacenar los datos de estudiantes
    for _ in range(num_records):  # Generamos el número especificado de registros
        name = f"{random.choice(first_names)} {random.choice(last_names)}"  # Nombre aleatorio
        age = random.randint(18, 25)  # Edad aleatoria entre 18 y 25 años
        students.append((name, age))  # Añadimos el registro a la lista
    return students  # Devolvemos la lista de datos de estudiantes

# Escribir datos a un archivo
def write_data_to_file(filename, data):
    with open(filename, 'w') as f:  # Abrimos el archivo para escribir
        for record in data:  # Para cada registro de datos
            f.write(f"{record[0]}, {record[1]}\n")  # Escribimos el registro en el archivo

# Leer datos de un archivo
def read_data_from_file(filename):
    with open(filename, 'r') as f:  # Abrimos el archivo para leer
        return [line.strip() for line in f]  # Devolvemos cada línea del archivo sin espacios en blanco adicionales

# Detectar sublistas ordenadas naturalmente
def detect_natural_runs(data):
    runs = []  # Lista para almacenar las sublistas ordenadas
    current_run = [data[0]]  # Inicializamos la primera sublista con el primer elemento
    for i in range(1, len(data)):  # Recorremos los datos a partir del segundo elemento
        if data[i][0] >= data[i - 1][0]:  # Si el nombre es mayor o igual al anterior
            current_run.append(data[i])  # Agregamos el registro a la sublista actual
        else:  # Si el nombre es menor que el anterior
            runs.append(current_run)  # Guardamos la sublista actual en la lista de sublistas
            current_run = [data[i]]  # Iniciamos una nueva sublista con el registro actual
    runs.append(current_run)  # Añadimos la última sublista
    return runs  # Devolvemos la lista de sublistas ordenadas

# Fusionar dos listas ordenadas
def merge_two_runs(run1, run2):
    merged_run = []  # Lista para almacenar la fusión de las dos sublistas
    i = j = 0  # Índices para recorrer las sublistas run1 y run2
    while i < len(run1) and j < len(run2):  # Mientras haya elementos en ambas sublistas
        if run1[i][0] < run2[j][0] or (run1[i][0] == run2[j][0] and run1[i][1] <= run2[j][1]):  # Comparación de nombres y edades
            merged_run.append(run1[i])  # Añadimos el elemento de run1
            i += 1  # Pasamos al siguiente elemento en run1
        else:  # Si el elemento de run2 es menor
            merged_run.append(run2[j])  # Añadimos el elemento de run2
            j += 1  # Pasamos al siguiente elemento en run2
    merged_run.extend(run1[i:])  # Añadimos los elementos restantes de run1
    merged_run.extend(run2[j:])  # Añadimos los elementos restantes de run2
    return merged_run  # Devolvemos la lista fusionada

# Fusionar todas las sublistas ordenadas
def merge_all_runs(runs):
    while len(runs) > 1:  # Mientras haya más de una sublista
        new_runs = []  # Lista para almacenar las nuevas sublistas fusionadas
        for i in range(0, len(runs), 2):  # Iteramos sobre las sublistas en pares
            if i + 1 < len(runs):  # Si hay al menos dos sublistas para fusionar
                new_runs.append(merge_two_runs(runs[i], runs[i + 1]))  # Fusionamos dos sublistas consecutivas
            else:  # Si solo hay una sublista restante
                new_runs.append(runs[i])  # Añadimos la sublista tal cual
        runs = new_runs  # Reemplazamos las sublistas originales por las nuevas sublistas fusionadas
    return runs[0]  # Devolvemos la lista resultante de la fusión

# Generar datos de estudiantes simulados
num_records = 50  # Número de registros de estudiantes a generar
student_data = generate_student_data(num_records)  # Generamos los datos de estudiantes

# Escribir los datos originales a un archivo desordenado
original_filename = 'Natural_merging_unsorted_students.txt'  # Nombre del archivo original desordenado
write_data_to_file(original_filename, student_data)  # Escribimos los datos en el archivo

print("Contenido del archivo original desordenado:")  # Imprimimos un mensaje
with open(original_filename, 'r') as f:  # Abrimos el archivo para leer
    for line in f:  # Para cada línea en el archivo
        print(line.strip())  # Imprimimos la línea sin espacios en blanco adicionales

# Leer los datos del archivo desordenado
data = [(line.split(', ')[0], int(line.split(', ')[1])) for line in read_data_from_file(original_filename)]

# Detectar sublistas ordenadas naturalmente
runs = detect_natural_runs(data)

# Fusionar todas las sublistas ordenadas
sorted_data = merge_all_runs(runs)

# Escribir los datos ordenados a un archivo
sorted_filename = 'Natural_merging_sorted_students.txt'  # Nombre del archivo de salida ordenado
write_data_to_file(sorted_filename, sorted_data)  # Escribimos los datos ordenados en el archivo de salida

print("\nContenido del archivo ordenado:")  # Imprimimos un mensaje
with open(sorted_filename, 'r') as f:  # Abrimos el archivo para leer
    for line in f:  # Para cada línea en el archivo
        print(line.strip())  # Imprimimos la línea sin espacios en blanco adicionales
