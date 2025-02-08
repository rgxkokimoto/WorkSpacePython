'''
Ejercicio 2
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
apariciones de cada carácter en la cadena.
'''

cad = []
cad += input("Intrduce una cadena: ")
print(cad)
di = {}

count = 0

for i in cad:
    count = 0
    for j in cad:
        if i == j: # conteo de cada caracter 
            count += 1
    di[i] = count # asigna valor con conteo si no estaba la clave la añade al dicionario.

print(di)


