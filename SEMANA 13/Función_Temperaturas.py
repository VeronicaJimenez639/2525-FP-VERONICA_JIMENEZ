#Definición de una función para calcular la temperatura promedio.
def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}  # Diccionario donde guardaremos los resultados

    for ciudad, temperaturas in ciudades_temperaturas.items():  # Recorremos cada ciudad y su lista de temperaturas
        promedio = sum(temperaturas) / len(temperaturas)  # Calculamos el promedio de la lista de temperaturas
        temperaturas_promedio[ciudad] = promedio  # Guardamos en el diccionario de resultados

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Quito": [12, 17, 16, 18],
    "Guayaquil": [28, 33, 26, 27],
    "Cuenca": [16, 14, 17, 12]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items(): # Recorre el diccionario "temperaturas_promedio".
                                                       # "ciudad": toma la clave del diccionario, que en este caso es el nombre de la ciudad.
                                                       # "promedio": toma el valor asociado a esa clave, es decir, la temperatura promedio de esa ciudad.
    print(f"{ciudad}: {promedio:.0f}°C")   # Imprime el nombre de la ciudad seguido del promedio de temperatura.
                                           # '.0f' redondea el promedio a un número entero.
                                           # Se añade "°C" para indicar que la temperatura está en grados Celsius.
