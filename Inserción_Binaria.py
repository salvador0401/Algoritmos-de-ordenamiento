def binary_search(arr, item, low, high):
    """Realiza una búsqueda binaria para encontrar la posición donde insertar el item."""
    while low <= high:  # Mientras el índice bajo sea menor o igual al índice alto
        mid = (low + high) // 2  # Calcula el índice medio
        if arr[mid] == item:  # Si el elemento medio es igual al elemento buscado
            return mid + 1  # Devuelve la posición siguiente al elemento medio encontrado
        elif arr[mid] < item:  # Si el elemento medio es menor que el elemento buscado
            low = mid + 1  # Ajusta el índice bajo para buscar en la mitad superior
        else:  # Si el elemento medio es mayor que el elemento buscado
            high = mid - 1  # Ajusta el índice alto para buscar en la mitad inferior
    return low  # Devuelve el índice bajo (posición de inserción)

def insertion_sort_binary(arr):
    """Ordena una lista utilizando la Inserción Binaria."""
    for i in range(1, len(arr)):  # Itera sobre los elementos de la lista a partir del segundo elemento
        current_book = arr[i]  # Almacena el elemento actual a insertar
        # Encuentra la posición correcta para current_book en la sublista arr[0:i] usando búsqueda binaria
        pos = binary_search(arr, current_book, 0, i - 1)
        # Mueve los elementos hacia la derecha para hacer espacio para current_book
        arr = arr[:pos] + [current_book] + arr[pos:i] + arr[i+1:]
    return arr  # Devuelve la lista ordenada

# Lista de libros por título
books = [
    "El Principito",
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "Matar a un ruiseñor",
    "La Odisea",
    "1984",
    "Orgullo y prejuicio",
    "Guerra y paz",
    "Crimen y castigo",
    "La Divina Comedia"
]

print("Lista de libros original:")
for book in books:
    print(book)#Se muestra la lista original

sorted_books = insertion_sort_binary(books)#Se ordenan los libros por inserccion binaria

print("\nLista de libros ordenada por título:")
for book in sorted_books:
    print(book)#Se muestra el nuevo orden
