#Trabajo con Archivos de Texto en Python

#1 Escritura de Archivo de Texto:

# Definimos el nombre del archivo
file_name = "my_notes.txt"  #Se guarda el nombre del archivo

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")  #Se abre el archivo

# Escritura con write(): para escribir tres líneas de notas personales
archivo_escritura.write("Nota 1: Repasar derivadas.\n")      #Escribe la cadena de texto y un salto de línea
archivo_escritura.write("Nota 2: Organizar el tiempo con Pomodoro antes de las evaluaciones.\n")
archivo_escritura.write("Nota 3: Practicar ejercicios de Python con archivos.\n ")

# Cerramos el archivo de escritura para guardar los cambios
archivo_escritura.close()

# 2 Lectura de Archivo de Texto:
# Modo de apertura: "r" para lectura (read).
archivo_lectura = open(file_name, "r")

# Lectura con read(): lee el contenido total del archivo
contenido_completo = archivo_lectura.read()
print("Contenido completo usando read():")
print(contenido_completo)

# Lectura con readline(): lee una línea a la vez
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())  # strip() elimina el salto de línea al final
print(linea_2.strip())
print(linea_3.strip())

# Cerramos el archivo de lectura
archivo_lectura.close()

