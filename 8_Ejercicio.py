#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
#imc = peso (kg) / altura m2(la altura*la altura)

altura = (float(input("Indicanos tu altura : ")))/100
peso = (float(input("Indicanos tu peso : ")))
altura_al_cuadrado = altura * altura
imc = peso / altura_al_cuadrado
print (f" Tu indice de masa corporal es : ", imc)