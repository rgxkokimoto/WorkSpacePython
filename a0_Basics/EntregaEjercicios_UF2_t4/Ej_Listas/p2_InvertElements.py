'''
Ejercicio 2
Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los
elementos de la lista en otra lista, pero en orden inverso, y muestra sus elementos por
la pantalla.
'''

listaCad = []

for i in range (0,5):
    listaCad.append(input(f"Introduce la {i + 1} Cadena: "))
    # listaCad += input(f"Introduce la {i + 1} Cadena: ") # el operador += me fragmentaba en carcateres la cadena 

listaInv = listaCad [:: -1] # esta forma me permite asignarlo a otra lista sin alterar la primera
# listaInv = listaCad.reverse() no funciono

'''
print(listaInv)

listPrub = ['Juan','Maria','Jose']

listPrub.reverse() # creo que el metodo no esta hecho de forma que se pueda asignar a otra lista 
# listPrubInv = listPrub.reverse()

print(listPrub) # así funciona
'''