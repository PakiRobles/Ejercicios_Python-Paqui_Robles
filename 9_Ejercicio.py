#Ejercicio 9: Conversor de Divisas
#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

euros = float(input("¿Cuántos dolares quieres convertir?: "))
cambio_euros= float(euros*0.85)
print(f"El cambio a euros es de ", cambio_euros, "€")