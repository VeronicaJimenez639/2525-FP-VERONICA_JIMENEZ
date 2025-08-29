 # Programa 2: Ordenación de Arreglo Multidimensional

# Crear una matriz bidimensional (3x3)
matriz = [
     [10, 22, 3],
     [4, 15, 6],
     [17, 8, 2]
]

# Definir una función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila): #Está función ordena la fila de menor a mayor
    n = len(fila)    # Cuántos elementos tiene la lista
    for i in range(n - 1):  # Controla el número de pasadas que hará el algoritmo
        for j in range(n - i - 1): # Compara elementos adyacentes en la fila
            if fila[j] > fila[j + 1]: # Si el número actual es mayor que el siguiente, se intercambian
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Definir una función para mostrar la matriz
def mostrar_matriz(matriz): # Recorre cada fila de la matriz y la imprime en pantalla
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila con Bubble Sort
for fila in matriz:   # Toma cada fila de la matriz y le aplica buble_sort_fila
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:") # Imprime la matriz con las filas ya ordenadas
mostrar_matriz(matriz)