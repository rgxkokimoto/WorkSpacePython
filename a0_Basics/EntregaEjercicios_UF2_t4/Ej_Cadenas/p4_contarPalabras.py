"""Ejercicio 4
Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras
tiene."""

cad = input("Introduce una frase: ")

lista = cad.split() # si pones el metodo vacio te separa por palabras y no cuenta ningun espacio de mas que util

print("El numero de palabras de tu frase es",len(lista))

