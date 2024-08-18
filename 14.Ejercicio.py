#Ejercicio 14: Calculadora de Descuento
#Crea un programa que calcule el precio final de un artículo después de aplicar un
#descuento del 20%.

def cuenta(d):
  return precio - (d*0.20)
precio = float(input("Introduce el precio : "))
print(f"El precio con descuento es : {cuenta(precio)}")