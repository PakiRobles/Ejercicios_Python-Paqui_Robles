#Ejercicio 5: Suma de Números Pares
#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

suma = 0
for num in range(1,100):
  if num % 2 == 0:
    suma = suma + num
print(suma)

  


