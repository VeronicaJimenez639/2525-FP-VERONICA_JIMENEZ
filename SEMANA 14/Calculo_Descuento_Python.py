def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
      Calcula el monto del descuento basado en un monto total y un porcentaje.

      Args:
        monto_total: El monto total de la compra.
        porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10).

      Returns:
        El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)  # Descuento = monto × (porcentaje/100)
    return descuento   # Devuelve el monto del descuento calculado

# Programa principal
# Primera llamada: Usando el porcentaje de descuento por defecto (10%)
print("PRIMER CASO")
monto1 = 120
descuento1 = calcular_descuento(monto1)  # Llamamos a la función (usa 10% por defecto)
monto_final1 = monto1 - descuento1       # Total a pagar = monto - descuento

# Muestra de resultados
print(f"Monto total de la compra: ${monto1}")
print(f"Porcentaje de descuento: 10%")
print(f"Monto del descuento: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")

print("\n"*2)  # Imprime 2 líneas en blanco para separar secciones

# Segunda llamada: indicando un porcentaje del 25%
print("SEGUNDO CASO")
monto2 = 1000    # Otro monto de compra
porcentaje2 = 25  # Descuento del 25 %
descuento2 = calcular_descuento(monto2, porcentaje2)    # Llamada con monto y porcentaje
monto_final2 = monto2 - descuento2  # Total a pagar = monto - descuento

# Muestra de resultados del segundo caso
print(f"Monto total de la compra: ${monto2}")
print(f"Porcentaje de descuento: {porcentaje2}%")
print(f"Monto del descuento: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")

