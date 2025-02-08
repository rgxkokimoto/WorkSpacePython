'''
Ejercicio 4
Programa que declare una lista y la vaya llenando de números hasta que
introduzcamos un número negativo. Entonces se debe imprimir la lista generada (sólo
los elementos introducidos).
'''

listPos = []
n = 0
i = 0
while n >= 0:
    listPos.append(int(input("Introduce un numero: ")))
    n = listPos[i]
    i = i + 1

print(listPos)