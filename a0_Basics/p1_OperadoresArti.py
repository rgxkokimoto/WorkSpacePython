# Operadores aritmeticos 

a = 10 + 5 # 15
a = 12 - 7 # 5
a = -5 # -5
a = 7 * 5 # 35
a = 2 ** 3 # 8 # XXX potencias 
a = 12.5 / 2 # 6.25
a = 12.5 // 2 # 6.0 # XXX división redondeada a entera
a = 27 % 4 # 3 # Resto


'''PEP 8: operadores
Siempre colocar un espacio en blanco, antes y después de un operador'''

# Operador de asignación: = , +=

b = "pepe"
b += " mola" # pepe mola
# XXX +=, -=, *=, /=, %=, **=, //=

# Operadores de comparación: ==, !=, >=, >, <=, <

# Operadores lógicos: and, or, && , || 

# Operadores de pertenecia in , not in 

c = "jose"
"j" in c # True
"3" not in c # True
"jo" in c # True # TODO tambien funciona con cadenas

# XXX en coleciones 
estudiante = {'nombre': 'Juan', 'edad': 21}
if 'apellido' not in estudiante:
    print('La clave "apellido" no está en el diccionario.')

numeros = {1, 2, 3, 4, 5}
if 6 not in numeros:
    print('El número 6 no está en el conjunto.')

frutas = ['manzana', 'banana', 'cereza']
if 'pera' not in frutas:
    print('La pera no está en la lista de frutas.')

# Operadores de cadenas de caracteres: + , *

# Uso del operador +
cadena1 = "Hola, " + "mundo" # "Hola, mundo"

# Uso del operador * XXX
cadena3 = "¡Ja!" * 3 # Salida: ¡Ja!¡Ja!¡Ja!