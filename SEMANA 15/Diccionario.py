# DICCIONARIO

#1 Crear el dicionario con las claves y valores

informacion_personal = {
    "Nombre": "Verónica Jiménez",
    "Edad": 28,
    "Ciudad": "Lago Agrio"
}
print("Diccionario original:", informacion_personal)


#2 Acceder y modificar "Ciudad"
print("Ciudad actual:", informacion_personal["Ciudad"]) #Acceder por clave "Ciudad" en el diccionario
informacion_personal["Ciudad"] = "Puyo"                 #Modificar el valor de la clave "Ciudad"
print("Después de cambiar 'Ciudad':", informacion_personal) #Mostrar el diccionario actualizado

#Agregar una nueva clave "Profesion"
informacion_personal["Profesion"] = "Desarrollador de Software" #Crear una nueva clave y valor en el diccionario
print("Después de agregar 'Profesion':", informacion_personal) #Mostrar el diccionario actualizado

#3 Verificar existencia de "Telefono y si no existe se lo agrega
if "Telefono" not in informacion_personal:      #Verificamos si existe o no en el diccionario
    informacion_personal["Telefono"] = "0992300085" #Si la clave no existe, la crea y le pone ese valor
    print("Después de verificar/agregar 'Telefono':", informacion_personal)  #Muestra el diccionario con el cambio

#4 Eliminar "Edad"
informacion_personal.pop("Edad", None)             #Eliminar la clave "Edad"
print("Diccionario final:", informacion_personal)  #Muestra el diccionario actualizado sin la Edad


