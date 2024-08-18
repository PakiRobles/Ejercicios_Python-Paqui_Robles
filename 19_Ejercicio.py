#Ejercicio 19: Verificación de Año Bisiesto
#Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no 
año= int (input("introduce el año : "))
if año % 4 == 0 and año % 100 !=0 or año % 400 == 0:
    print ("El año", año, "es bisiesto")
else:
    print ("El años", año, "no es bisiesto")


