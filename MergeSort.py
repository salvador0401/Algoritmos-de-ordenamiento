##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def merge_sort(products):
    """Ordena una lista de productos por precio utilizando Merge Sort."""
    if len(products) <= 1:  # Si la lista tiene un solo elemento o está vacía, ya está ordenada
        return products

    # Divide la lista en dos sublistas
    mid = len(products) // 2  # Encuentra el punto medio de la lista
    left_half = products[:mid]  # Sublista izquierda
    right_half = products[mid:]  # Sublista derecha

    # Ordena cada mitad recursivamente
    left_sorted = merge_sort(left_half)  # Ordena la sublista izquierda
    right_sorted = merge_sort(right_half)  # Ordena la sublista derecha

    # Combina las mitades ordenadas
    return merge(left_sorted, right_sorted)  # Devuelve las mitades combinadas y ordenadas

def merge(left, right):
    """Combina dos listas ordenadas en una sola lista ordenada."""
    sorted_list = []  # Lista que contendrá los elementos ordenados
    i = j = 0  # Índices para recorrer las listas izquierda y derecha

    # Compara elementos de ambas listas y combina en una lista ordenada
    while i < len(left) and j < len(right):  # Mientras haya elementos en ambas listas
        if left[i][1] < right[j][1]:  # Compara los precios de los productos
            sorted_list.append(left[i])  # Añade el producto de la izquierda si su precio es menor
            i += 1  # Incrementa el índice de la izquierda
        else:
            sorted_list.append(right[j])  # Añade el producto de la derecha si su precio es menor o igual
            j += 1  # Incrementa el índice de la derecha

    # Añade los elementos restantes de ambas listas
    sorted_list.extend(left[i:])  # Añade los elementos restantes de la izquierda, si hay
    sorted_list.extend(right[j:])  # Añade los elementos restantes de la derecha, si hay

    return sorted_list  # Devuelve la lista combinada y ordenada

# Lista de productos (nombre, precio)
products = [
    ("Laptop", 1200),
    ("Mouse", 20),
    ("Teclado", 50),
    ("Monitor", 300),
    ("Impresora", 150),
    ("Tablet", 400),
    ("Smartphone", 800),
    ("Cámara", 500),
    ("Auriculares", 100),
    ("Altavoces", 75)
]

print("Lista de productos original:")  # Imprime el título para la lista original
for product, price in products:  # Itera sobre cada producto y su precio en la lista
    print(f"{product}: ${price}")  # Imprime cada producto con su precio

sorted_products = merge_sort(products)  # Ordena la lista de productos por precio utilizando merge sort

print("\nLista de productos ordenada por precio:")  # Imprime el título para la lista ordenada
for product, price in sorted_products:  # Itera sobre cada producto y su precio en la lista ordenada
    print(f"{product}: ${price}")  # Imprime cada producto con su precio ordenado
