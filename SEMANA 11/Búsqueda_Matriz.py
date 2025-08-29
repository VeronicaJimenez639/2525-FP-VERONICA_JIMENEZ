# Programa 1: Búsqueda en Arreglo Multidimensional

#Definimos una matriz 3x3
matriz = [
    [10,5,1],
    [8,3,14],
    [5,4,9]
]

# Definir el valor que se va a buscar
valor_buscado = 5

#Inicializar variables para encontrar la posición del valor_buscado
fila_encontrada = -1    #valor no encontrado todavía (-1)
columna_encontrada = -1 #valor no encontrado todavía (-1)

#Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):       #Bucle doble for -> recorre fila por fila y columna por columna
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:  #Si encuentra el valor ->guarda la posición
            fila_encontrada = fila
            columna_encontrada = columna
            break    #Detener la búsqueda una vez encontrado el valor
    if fila_encontrada != -1:
        break     #Salir del bucle si se encuentra el valor

# Verificar si se encontró el valor_buscado y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")