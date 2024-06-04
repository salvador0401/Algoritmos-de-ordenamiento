##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def selection_sort_countries(countries):
    """Ordena una lista de países por longitud de nombre utilizando Selection Sort."""
    n = len(countries)  # Obtiene la longitud de la lista de países
    for i in range(n - 1):  # Itera sobre la lista de países (excepto el último elemento)
        min_idx = i  # Selecciona el índice actual como el índice del elemento más pequeño
        for j in range(i + 1, n):  # Itera sobre los elementos restantes de la lista
            if len(countries[j]) < len(countries[min_idx]):  # Compara las longitudes de los nombres
                min_idx = j  # Actualiza el índice del elemento más pequeño encontrado
        # Intercambia los elementos para colocar el elemento más pequeño en la posición correcta
        countries[i], countries[min_idx] = countries[min_idx], countries[i]

# Lista de países
countries = [
    "India",
    "China",
    "Estados Unidos",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico",
    "Japan"
]

print("Lista de países original:")
for country in countries:
    print(country)#imprime el acomodo original

selection_sort_countries(countries)#Los irdena

print("\nLista de países ordenada por longitud de nombre:")
for country in countries:
    print(country)#muestra el nuevo orden
