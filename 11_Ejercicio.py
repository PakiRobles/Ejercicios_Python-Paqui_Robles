#Ejercicio 11: Calculadora de Edad
#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
from datetime import datetime
año_nacimiento=int((input("Dinos tu fecha de nacimiento : ")))
año_actual = datetime.now().year
edad = (año_actual - año_nacimiento)
print("Tu edad es : ", edad, "años")


