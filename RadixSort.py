##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def counting_sort(arr, exp):
    """Realiza una ordenación por conteo en función del dígito representado por exp."""
    n = len(arr)  # Longitud del arreglo
    output = [0] * n  # Arreglo de salida que almacenará los números ordenados
    count = [0] * 10  # Arreglo de conteo para almacenar la cuenta de ocurrencias de los dígitos (0-9)

    # Contar las ocurrencias de cada dígito en exp
    for i in range(n):  # Para cada elemento en el arreglo
        index = arr[i] // exp  # Calcula el dígito en la posición exp
        count[index % 10] += 1  # Incrementa la cuenta del dígito correspondiente

    # Cambiar count[i] para que contenga la posición actual de este dígito en output
    for i in range(1, 10):  # Ajusta las posiciones acumuladas en el arreglo de conteo
        count[i] += count[i - 1]

    # Construir la matriz de salida
    i = n - 1  # Inicia desde el final del arreglo original
    while i >= 0:  # Recorre el arreglo de derecha a izquierda
        index = arr[i] // exp  # Calcula el dígito en la posición exp
        output[count[index % 10] - 1] = arr[i]  # Coloca el elemento en la posición correcta en output
        count[index % 10] -= 1  # Decrementa la cuenta del dígito
        i -= 1  # Mueve al siguiente elemento

    # Copiar la matriz de salida a arr, de modo que arr ahora contenga números ordenados
    for i in range(n):  # Copia los elementos de output a arr
        arr[i] = output[i]

def radix_sort(arr):
    """Ordena una lista de números enteros utilizando Radix Sort."""
    # Encuentra el número máximo para saber el número de dígitos
    max_num = max(arr)  # Encuentra el número máximo en el arreglo

    # Realiza el conteo y ordenamiento por cada dígito
    exp = 1  # Inicializa exp como 1 (unidad)
    while max_num // exp > 0:  # Itera por cada dígito significativo
        counting_sort(arr, exp)  # Realiza una ordenación por conteo basada en el dígito actual
        exp *= 10  # Mueve al siguiente dígito significativo

# Lista de números de identificación de empleados
employee_ids = [
    5234, 7152, 3010, 1843, 6601,
    9324, 5112, 2054, 4730, 8990
]

print("Lista original de números de identificación de empleados:")  # Imprime el título para la lista original
print(employee_ids)  # Imprime la lista original

radix_sort(employee_ids)  # Ordena la lista de números de identificación utilizando Radix Sort

print("\nLista ordenada de números de identificación de empleados:")  # Imprime el título para la lista ordenada
print(employee_ids)  # Imprime la lista ordenada
