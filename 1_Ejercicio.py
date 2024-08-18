#Ejercicio 1: Conversor de Temperatura
#Escribe un programa que convierta una temperatura de grados Celsius a grados
#Fahrenheit.°F = (°C x 1,8) + 32

def conversor (c):
  return (c*1.8)+32

n = float(input("Introduce los grados celsius : "))
print(f"La temperatura en Fahrenheit es: {conversor(n)}")



