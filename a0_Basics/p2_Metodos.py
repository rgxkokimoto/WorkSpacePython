# METODOS por defacto wow!

# Casteos
a = int(3.4)  # 3

a = int("123") # funciona

b = float(2)  # 2.0

# a = int("2.3")   # Esto no se puede y da error hay que convertirlo

type("Hola")  #<class 'str'>

abs(-54)  # valor absoluto 54

numDiv = divmod(7 , 2)  # Te da una tupla con: (resultado , resto)
print("Resultado:",numDiv[0],"Resto:",numDiv[1])
pow(2, 3)  # Potencias 2 elevado a tres

numRound = round(7.3678, 3) #  P1 = double  P2 = corte del redondeo  
print("Numero redondeado:",numRound)

print("2 + 2 es =", 2 + 2)  # La coma te hace un espacio
print("2 + 2 es =" + "4") # el mas no lo hace 

# INPUT
nombre = input("Dime tu nombre: ")
print("Bienvenido", nombre)

# Conversion 
numero = int(input("Intoduce un entero:"))

#=========================================================================================
# XXX METODOS DE STRINGS 
#=========================================================================================

# capitalize() aumenta la primera letra a mayuscula
cadCap = "hola mundo!"
print(cadCap.capitalize())

# swapcase() cambia todas las palabras de un string  segun en la que este
cadSwap = "hola mundo!"
print(cadSwap.swapcase())

# zfill Añade numeros alante
numZF = 123 
print(str(numero).zfill(4))
print(str(numero).zfill(8))

# center le das un numero y un caracter y te imprime ese caracter junto al string rodeandolo por los dos lados 
print(cadCap.center(50, "#")) 


#LEN() no es especifico solo de string pero si lo aplicas a estos te devuelve el numero de carcateres

len("jdjkkd") # 6

#COUNT

cadCount = "Hola mundo!"
print(cadCount.count("o"))

print(cadCount.count("o",2,5)) # puedes decirle un rango a partir de donde quieres que busque 

#FIND
"""Retorna un entero representando la posición
donde inicia la subcadena dentro de cadena. Si
no la encuentra, retorna -1"""
print(cadCount.find("e")) 
print(cadCount.find("mi", 0, 10)) # posicion_inicio, posicion_fin]

#=========================================================================================
### XXX METODOS DE SUSTITUCION
#=========================================================================================

#FORMAT sustituye por lo que recibe el metodo
cadFormat1 = "bienvenido a mi aplicación {0}"
print(cadFormat1.format("en Python"))

# 
cadFormat2 = "Importe bruto: ${0} + IVA: ${1} = Importe neto:{2}"
print(cadFormat2.format(100, 21, 121))

cadFormat = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto:{neto}"
print(cadFormat.format(bruto = 100, iva = 21, neto = 121))

# STRIP == TRIM 
cadena = " Bienvenido "
print(cadena.strip())

# join une cosas entorno a un separador que le indiques
tupla = ("p1","p2","p3")
separador = "###"
print(separador.join(tupla))

# PARTITION 
"""Retorna una tupla de tres elementos
donde el primero es el contenido de la
cadena previo a la primera ocurrencia
del separador, el segundo, el
separador mismo y el tercero, el
contenido de la cadena posterior al
separador"""

tupla = "http://www.google.com".partition("www.")
print(tupla)
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio:{1}".format(protocolo, dominio))

# split 
"""Retorna una lista con todos
elementos encontrados al
dividir la cadena por un
separador"""

keywords = "python, guia, curso, tutorial".split(", ")
print(keywords)

# XXX Metodos para listas 

# ORIGEN
lista1 = ["A", "B", "C"]
lista2 = lista1
lista3 = lista1[:] # Guarda valor base

del lista1[1] # XXX

print(lista1)
print(lista2)
print(lista3)

# append Agregar un elemento al final de la lista
nombres = ["Alvaro", "Miguel", "David"]
nombres.append("Jose")
print(nombres)

# extend Agregar varios elementos al final de la lista. 
nombres.extend(["Jorge", "Juan", "Jose"])
print(nombres)

# INSERT Agregar un elemento en una posición determinada
nombres.insert(0,"alacas")

# pop Eliminar el último elemento de la lista sin parametros
nombres.pop()
nombres.pop(3)

# REMOVE Elimina la primera ocurrencia que encuentra
nombres.remove("Jose")

# XXX METODOS DE ORDEN Y LISTAS

# reverse Invertir el orden de una lista 
nombres.reverse()

nombres.sort() # Ordenar una lista en forma ascendente
nombres.sort(reverse=True) # Ordenar una lista en forma descendente

# Obtener el máximo valor de la lista
lista = [2, 9, 4, 7, 6, 5, 8, 3]
max(lista)
max(nombre) # se vasara en la primera letra en orden alfabetico a = 0 z = 25
min(lista)

# Obtener la cantidad de elementos de la lista len(lista)
len(lista) 

# INDEX 
# Obtener el índice en el que aparece el
# elemento por primera vez.
# Nos devuelve una excepcion si no esta XXX
nombres.index("Juan")
nombres.index("Juan", 2, 4)


# XXX METODOS DE DICCIONARIOS

# Retorna una lista de todas las claves usadas en el diccionario dic
mapa = {1: "uno", 2: "dos", 3: "tres", 4:
"cuatro", 5: "cinco"}
list(mapa)

# Obtener la cantidad de elementos del diccionario
len(mapa)

#Retorna una nueva vista de los elementos del diccionario (pares (key, value))
mapa.items()
list(mapa.items())

# Retorna una nueva vista de las claves del diccionario.
mapa.keys()
list(mapa.keys())

# Retorna una nueva vista de los valores del diccionario.
mapa.values()
list(mapa.values())

"""Retorna el elemento dentro del
diccionario almacenado bajo la clave clave,
si clave está en el diccionario; si no, retorna default.
""" 
mapa.get(3)
mapa.get(6, "no está")
mapa.get(6)


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
retorna su valor; si no está, retorna default. Si no se
especifica valor para default y la clave no se encuentra en
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