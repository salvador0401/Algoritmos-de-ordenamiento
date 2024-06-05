##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import os  # Importamos el módulo os para operaciones del sistema
import heapq  # Importamos el módulo heapq para manipular heaps
import random  # Importamos el módulo random para generar datos aleatorios
from datetime import datetime, timedelta  # Importamos datetime y timedelta para manipular fechas

# Generar datos de ventas simulados
def generate_sales_data(num_records):
    base_date = datetime(2023, 1, 1)  # Fecha base para generar datos
    sales_data = []  # Lista para almacenar los datos de ventas
    for _ in range(num_records):  # Generamos el número especificado de registros
        date = base_date + timedelta(days=random.randint(0, 365))  # Fecha aleatoria en el año
        amount = random.uniform(10, 1000)  # Monto de venta aleatorio entre 10 y 1000
        sales_data.append((date, amount))  # Añadimos el registro a la lista
    return sales_data  # Devolvemos la lista de datos de ventas

# Dividir la lista en sublistas más pequeñas
def divide_data(sales_data, chunk_size):
    for i in range(0, len(sales_data), chunk_size):  # Dividimos los datos en trozos de tamaño chunk_size
        yield sales_data[i:i + chunk_size]  # Generamos cada fragmento

# Ordenar y escribir los datos divididos en archivos temporales
def write_temp_files(sales_data_chunks):
    filenames = []  # Lista para almacenar los nombres de los archivos temporales
    for i, chunk in enumerate(sales_data_chunks):  # Para cada fragmento de datos
        chunk.sort()  # Ordenamos el fragmento
        filename = f'temp_sales_{i}.txt'  # Nombre del archivo temporal
        with open(filename, 'w') as f:  # Abrimos el archivo para escribir
            for record in chunk:  # Para cada registro en el fragmento
                f.write(f"{record[0].isoformat()} {record[1]:.2f}\n")  # Escribimos la fecha y el monto en el archivo
        filenames.append(filename)  # Añadimos el nombre del archivo a la lista
    return filenames  # Devolvemos la lista de nombres de archivos

# Leer registros de un archivo
def read_records_from_file(filename):
    with open(filename, 'r') as f:  # Abrimos el archivo para leer
        for line in f:  # Para cada línea en el archivo
            date_str, amount = line.strip().split()  # Separamos la fecha y el monto
            yield (datetime.fromisoformat(date_str), float(amount))  # Generamos el registro como una tupla

# Fusión de archivos ordenados en un solo archivo
def merge_files(filenames, output_filename):
    min_heap = []  # Min heap para mantener los elementos ordenados
    file_iters = [read_records_from_file(filename) for filename in filenames]  # Iteradores para leer los archivos
    
    # Inicializar el heap con el primer elemento de cada archivo
    for i, file_iter in enumerate(file_iters):
        try:
            record = next(file_iter)  # Obtenemos el primer registro de cada archivo
            heapq.heappush(min_heap, (record, i))  # Añadimos el registro al heap
        except StopIteration:  # Si el archivo está vacío, continuamos
            continue

    with open(output_filename, 'w') as f_out:  # Abrimos el archivo de salida para escribir
        while min_heap:  # Mientras el heap no esté vacío
            min_record, file_index = heapq.heappop(min_heap)  # Extraemos el menor registro del heap
            f_out.write(f"{min_record[0].isoformat()} {min_record[1]:.2f}\n")  # Escribimos el registro en el archivo de salida
            try:
                next_record = next(file_iters[file_index])  # Obtenemos el siguiente registro del archivo correspondiente
                heapq.heappush(min_heap, (next_record, file_index))  # Añadimos el siguiente registro al heap
            except StopIteration:  # Si el archivo se ha agotado, continuamos
                continue

# Generar datos de ventas simulados
num_records = 100  # Número de registros de ventas a generar
sales_data = generate_sales_data(num_records)  # Generamos los datos de ventas

# Escribir los datos originales a un archivo desordenado
original_filename = 'Straight_merging_unsorted_sales_data.txt'  # Nombre del archivo original desordenado
with open(original_filename, 'w') as f:  # Abrimos el archivo para escribir
    for record in sales_data:  # Para cada registro de ventas
        f.write(f"{record[0].isoformat()} {record[1]:.2f}\n")  # Escribimos la fecha y el monto en el archivo

print("Contenido del archivo original desordenado:")  # Imprimimos un mensaje
with open(original_filename, 'r') as f:  # Abrimos el archivo para leer
    for line in f:  # Para cada línea en el archivo
        print(line.strip())  # Imprimimos la línea sin espacios en blanco adicionales

# Dividir datos en fragmentos más pequeños
chunk_size = 20  # Tamaño de cada fragmento
sales_data_chunks = list(divide_data(sales_data, chunk_size))  # Dividimos los datos en fragmentos

# Escribir fragmentos ordenados en archivos temporales
temp_filenames = write_temp_files(sales_data_chunks)  # Escribimos los fragmentos en archivos temporales

# Fusionar los archivos ordenados en un archivo final
output_filename = 'Straight_merging_sorted_sales_data.txt'  # Nombre del archivo de salida ordenado
merge_files(temp_filenames, output_filename)  # Fusionamos los archivos temporales en el archivo de salida

print("\nContenido del archivo ordenado:")  # Imprimimos un mensaje
with open(output_filename, 'r') as f:  # Abrimos el archivo para leer
    for line in f:  # Para cada línea en el archivo
        print(line.strip())  # Imprimimos la línea sin espacios en blanco adicionales

# Limpieza de archivos temporales
for filename in temp_filenames:  # Para cada archivo temporal
    os.remove(filename)  # Eliminamos el archivo
