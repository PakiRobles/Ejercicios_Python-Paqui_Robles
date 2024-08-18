#Ejercicio 4: Contador de Vocales
#Crea un programa que cuente el número de vocales en una palabra ingresada por el
#usuario.
def contador_vocales(vocales):
  return sum(1 for letra in vocales if letra.lower() in 'aeiou')
l = (input("Pon aquí la letra: "))
print(f"El numero de vocales es : {contador_vocales(l)}")




