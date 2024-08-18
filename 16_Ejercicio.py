# Ejercicio 16: Contador de Números Pares e Impares
#Crea un programa que cuente y muestre la cantidad de números pares e impares en 
#una lista ingresada por el usuario
 
numeros1 = (int(input ("cuantos número quieres contar :")))
numeros2 = (int(input ("cuantos número quieres contar :")))
cont1 = 0
cont2 = 0
if numeros1 % 2 == 0 :
  cont1 = cont1 + 1
  print("El número", numeros1, "es par")
else:
  cont2 = cont2 + 1
  print("El número", numeros1, "es impar")

if numeros2 % 2 == 0 :
  cont1 = cont1 + 1
  print("El número", numeros2, "es par")
else:
  cont2 = cont2 + 1
  print("El número", numeros2, "es impar")

print ("El total de numeros pares es :", cont1)
print ("El total de numeros impares es :", cont2)