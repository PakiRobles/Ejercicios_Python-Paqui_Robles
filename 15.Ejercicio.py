#Ejercicio 15: Conversor de Tiempo
#Escribe un programa que convierta un número de minutos en horas y minutos. Por
#ejemplo, 145 minutos serían 2 horas y 25 minutos.
minutos = float(input("introduce los minutos : "))
def conversor(hour):
  min = minutos // 60
  return(min)
print (f"Los minutos son: {conversor(min)}")



