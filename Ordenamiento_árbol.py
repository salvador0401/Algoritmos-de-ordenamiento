##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importamos el módulo random para realizar operaciones aleatorias

# Creamos un arreglo de strings desordenado
arreglo_desordenado = ['a', 'az', 'b', 'c', 'd']  # Definimos un arreglo inicial de strings
random.shuffle(arreglo_desordenado)  # Desordenamos el arreglo de forma aleatoria
print("Arreglo desordenado:", arreglo_desordenado)  # Imprimimos el arreglo desordenado

# Definimos la clase Nodo para representar un nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asignamos el valor al nodo
        self.izquierda = None  # Inicializamos el hijo izquierdo como None
        self.derecha = None  # Inicializamos el hijo derecho como None

# Función para insertar un nodo en el árbol
def insertar_nodo(raiz, valor):
    if raiz is None:  # Si la raíz es None, creamos un nuevo nodo con el valor
        return Nodo(valor)
    if valor < raiz.valor:  # Si el valor es menor que el valor de la raíz, insertamos en el subárbol izquierdo
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    else:  # Si el valor es mayor o igual que el valor de la raíz, insertamos en el subárbol derecho
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz  # Devolvemos la raíz del árbol (o subárbol) actualizado

# Función para ordenar un arreglo utilizando un árbol binario de búsqueda
def ordenar_arreglo(arreglo):
    raiz = None  # Inicializamos la raíz del árbol como None
    for valor in arreglo:  # Para cada valor en el arreglo
        raiz = insertar_nodo(raiz, valor)  # Insertamos el valor en el árbol
    return raiz  # Devolvemos la raíz del árbol construido

# Función para recorrer el árbol en orden (in-order traversal)
def recorrer_arbol(raiz):
    if raiz is not None:  # Si la raíz no es None
        recorrer_arbol(raiz.izquierda)  # Recorremos el subárbol izquierdo
        print(raiz.valor, end=" ")  # Imprimimos el valor de la raíz
        recorrer_arbol(raiz.derecha)  # Recorremos el subárbol derecho

# Ordenamos el arreglo utilizando el árbol binario de búsqueda
raiz = ordenar_arreglo(arreglo_desordenado)  # Construimos el árbol a partir del arreglo desordenado
print("\nArreglo ordenado:", end=" ")  # Imprimimos el mensaje de inicio para el arreglo ordenado
recorrer_arbol(raiz)  # Recorremos el árbol en orden e imprimimos los valores en orden ascendente
