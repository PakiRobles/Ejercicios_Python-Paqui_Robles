#Ejercicio 7: Calculadora Simple
#Crea un programa que realice operaciones aritméticas simples (suma, resta,
#multiplicación, división) según la elección del usuario.

#def sumar (x , y):
  #return x + y
#def restar (x , y):
 # return x - y
#def multiplicar (x , y):
 # return x * y
#def dividir (x, y):
 # return x / y
operacion = input ("elige la operacion a realizar: Sumar(1), Restar (2), Multiplicar(3), Dividir (4) : ")
x = (float(input("introduce un número : " )))
y = (float(input("introduce el siguiente numero : ")))
if operacion == '1':
  resultado = x + y
if operacion == '2':
  resultado = x - y
if operacion == '3':
  resultado = x * y
if operacion == '4': 
  resultado = x / y
print (resultado)




