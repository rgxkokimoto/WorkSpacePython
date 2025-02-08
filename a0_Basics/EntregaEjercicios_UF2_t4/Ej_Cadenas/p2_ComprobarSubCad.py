"""
Realizar un programa que comprueba si una cadena leída por teclado comienza por
una subcadena introducida por teclado.
"""

# TODO y que pasa si tiene mas de un espacio en la cadena

subcad = input("Introduce la subCadena: ")
cad = input("Intoduce la cadena por teclado: ")

numSubcad = len(subcad)

f = cad.find(subcad,0,numSubcad)

if(f == 0):
    print("La cadena si contiene la subcadena")
else:
    print(f"La cadena {cad} no contiene {subcad} al principio")