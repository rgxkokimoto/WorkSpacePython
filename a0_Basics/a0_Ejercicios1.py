""" # 1
us = input("Dime tu nombre Usuario")
print("Hola", us) """


"""# 2
base = int(input('Introduce la base: '))
altura = int(input('Introduce la altura: '))
per = (base * 2) + (altura * 2)
print("Tu rectangulo tiene un perimetro de:",per)"""

"""Ejercicio 3
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""

"""num = float(input("Introduce un numero:"))
num2 = float(input("\nIntroduce el siguente número"))
print("Suma:",num + num2)
print("Resta:",num - num2)
print("División:",num / num2)
print("Multiplicación:",num * num2)"""



"""Ejercicio 4
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es:
C = (F-32)*5/9"""

"""gradF = float(input("Introduce un grado:"))
gradC = (gradF-32)*5/9
print("Grados Celsius:",round(gradC))"""


"""
Ejercicio 5
Calcular la media de 3 números pedidos por teclado."""


"""num = int(input("\nIntroduce el 1º numero:"))
num2 = int(input("\nIntroduce el 2º numero:"))
num3 = int(input("\nIntroduce el 3º numero:"))

media = (num + num2 + num3)/3
print(round(media,2))"""


"""
Ejercicio 6
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
"""

mins =  int(input("Introduce un datos en minutos"))
horas =  mins // 60 # para que devuelva un entero 
minsRes = (horas*60) - mins
print(horas,"h", minsRes,"m")


"""Ejercicio 7
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su
sueldo base y comisiones.
Ejercicio 8
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuánto deberá pagar finalmente por su compra.
Ejercicio 9
Un alumno desea saber cuál será su calificación final en SGE. Dicha calificación se
compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
Ejercicio 10
Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de
su diferencia, de modo que el resultado sea siempre positivo).
Ejercicio 11"""
