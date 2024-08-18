 #Ejercicio 20: Suma de Números en una Lista
 #Crea un programa que sume todos los números en una lista ingresada por el usuario.
conteo = int(input( "Cuantos número tiene tu lista : "))
lista =[]
for num in range(conteo):
  numero = int(input( "Introduce el número : "))
  lista.append(numero) 
sum_lista = sum(lista)
print(f"La suma de los numero de la lista es, {sum_lista}")






