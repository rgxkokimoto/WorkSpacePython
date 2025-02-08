
# como se declaran los tipos de coleciones 

my_list = [4,"hola",False]
my_tuple = (78,23.4,"pepe")
my_conjunto = set([24,"pepe","many"])
my_dic = {1 : 'pepe' , 2 : 'Albondigas' , 3 : 'Perro'}


#===================================================================
# TUPLAS 
#===================================================================
# - COLECION DE DATOS INMUTABLE 

# inicializan 
mi_tupla = ('Holaa' , 12 , True)
print(mi_tupla[1])


# adceder a porciones de una tupla 
print(mi_tupla[1:2])  # media
print(mi_tupla[1:])  # media ultima 
print(mi_tupla[:1])  # primera 

# adceder de manera inversa 
print(mi_tupla[-1])  #adcede al ultimo
# XXX si pones un numero que no existe te dara error

#===================================================================
# LISTAS
#===================================================================
# #  son modificables.

lista = [0, 'hola' , 1 , True]

# Modificar 
lista[0] = 1

# Añadir 
lista.append('new')
lista += "pepe" # XXX si haces eso añades todos los carcateres por separado


#===================================================================
# DICIONARIOS && METODOS DE DICCIONARIOS
#===================================================================

# Dicionarios parecidos a un Mapa en hava hasMap TreeMap
diction = {1 : 'pepe' , 2 : 'Albondigas' , 3 : 'Perro'}

print(diction[1])

# Borrar pareja
del diction[3]

# XXX METODOS DE DICCIONARIOS

# Retorna una lista de todas las CLAVES usadas en el diccionario dic
mapa = {1: "uno", 2: "dos", 3: "tres", 4:
"cuatro", 5: "cinco"}
list(mapa)

#Retorna una nueva lista de los elementos completos del diccionario clave-valor
mapa.items()
print(list(mapa.items()))

# Obtener la cantidad de elementos del diccionario
len(mapa)

# Retorna una nueva vista de las claves del diccionario.
mapa.keys()
list(mapa.keys())

# Retorna una nueva vista de los valores del diccionario.
mapa.values()
list(mapa.values())

"""Retorna el elemento dentro del
diccionario almacenado bajo la clave que le indiques,
si clave está en el diccionario; si no, retorna un default que le indiques.
""" 
mapa.get(3)
mapa.get(6, "no está")
mapa.get(6) # sin valor por defector retorna un none


"""Si clave está incluida en el diccionario, retorna el
valor almacenado. Si no, inserta con la clave clave el
valor definido en default y retorna default. El valor
por defecto de default es None."""

mapa.setdefault(3)
mapa.setdefault(6, "seis")
mapa.setdefault(7)

# Elimina todos los elementos del diccionario.
# mapa.clear()

#Elimina elimina la entrada con clave clave del diccionario.
#Lanza una excepción si clave no está en el diccionario. XXX
del(mapa[7])

"""Si clave está en el diccionario, lo elimina del diccionario y
retorna su valor;

 si no está, retorna default.

Si no se especifica valor para default y la clave no se encuentra en
el diccionario, se lanza la excepción"""

mapa.pop(6)
mapa.pop(8, "no está")

#Elimina y retorna la última pareja (clave, valor) añadida
#al diccionario.
mapa.popitem()

#Retorna un iterador que recorre las claves del diccionario
#duc. Es una forma abreviada de iter(d.keys()).
list(iter(mapa))

#Retorna un iterador que recorre las claves en orden
#inverso. Es una forma abreviada de reversed(d.keys()).
list(reversed(mapa))
list(reversed(mapa.values()))
list(reversed(d.items()))

#Copia un diccionario con distinta referencia, es decir, si
#modificamos el diccionario origen no se modifica la copia. 
mapa2 = mapa.copy()