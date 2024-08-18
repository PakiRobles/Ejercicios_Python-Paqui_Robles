#Ejercicio 6: Verificación de Palíndromo
#Crea un programa que verifique si una palabra ingresada por el usuario es un
#palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("introduce la palabra:")
reverso_palabra = palabra [::-1]
print(f'{reverso_palabra}')
if reverso_palabra == palabra:
  print ("Palíndromo")
else:
  print ("No es palíndromo")

