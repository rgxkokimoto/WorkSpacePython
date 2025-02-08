# PROGRAMACION MODULAR Y EXTRUCTURADA MEJORA EL MANTENIMIENTO LA REUTILIZACIÓN Y LA DEPURACIÓN

# COMO SE DEFINE UNA FUNCIÓN
def nomFun():
    # aqui algoritmos
    print("Primera Función!!!")


# EJECUCIÓN void
nomFun()

# CON RETORNO
def func_Con_Return():
    return "Hola mundo!!!"


# CON PARAMETROS
def func_With_params(p1,p2):
    print(f"{p1}, y el segundo valor lo DIVIDIMOS por 2 ={p2/2}")


mens = func_Con_Return()
print(mens)

func_With_params("pepe",8)
# XXX el orden de los parametros importa aunque hay formas de controlar esto
# func_With_params(8,"pepe")
# XXX  tambien dará error si le falta un parametro
# func_With_params("pepe")


# PARAMETROS POR OMISÓN
def func_with_om(p1,p2='juan'): # XXX valor por defecto
    print("hola","pepe")


func_with_om("Jorge") # por defecto se hace 

func_with_om("Jorge", "Buenos dias")

## XXX Puedo invocar a una función alterando el orden de los parametros si especifico las key word de estos
func_With_params(p2=18,p1="Valor") # así no dará problemas

# PARAMETROS ARBITRARIOS

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print('parámetro fijo:', parametro_fijo)
    # Los parámetros arbitrarios se recorren como tuplas:
    for argumento in arbitrarios:
        print(argumento)

recorrer_parametros_arbitrarios('fijo', 'arbitrario1', 'arbitrario2', 'arbitrario3')

# TODO no se que hace esto
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print(parametro_fijo)
    for argumento in arbitrarios:
        print(argumento)
    for clave in kwords:
        print("El valor de", clave, "es", kwords[clave])


recorrer_parametros_arbitrarios("fijo", "arbitrario1", "arbitrario2", "arbitrario3", clave1="valor1",
    clave2="valor2")


# DESEMPAQUEDATO DE PARÁMETROS (LISTAS TUPLAS ETC...)
'''Puede ocurrir una situación inversa a la anterior. Es decir, que la función espere una lista
fija de parámetros, pero que éstos, se encuentren contenidos en una lista o tupla. En este
caso, el signo asterisco (*) deberá preceder al nombre de la lista o tupla que es pasada
como parámetro durante la llamada a la función'''
def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = [1500, 10]
print(calcular(*datos)) # asi le dices que los parametros se encuentran en la lista 


'''Lo mismo para el caso de que los valores pasados como parámetros a una función, se
encuentren disponibles en un diccionario. Aquí, deberán pasarse a la función, precedidos
de dos asteriscos (**):'''

def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = {"descuento": 10, "importe": 1500}
print(calcular(**datos))


# XXX LOCALS Y GLOBAÑS
'''
Python dispone de dos funciones nativas: locals() y globals()
Ambas funciones, retornan un diccionario. En el caso de locals(), éste diccionario se
compone de todas las funciones de ámbito local, mientras que el de globals(), retorna lo
propio pero a nivel global
'''

# XXX FUNCIONES RECURSIVAS
# CUIDADO TIENES QUE ASEGURATE DE QUE TIENE UN FINAL puede ocurrir como en un bucle
def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\n¡Fallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)  # Llamada recursiva
        else:
            print("\n¡Perdiste!")
    else:
        print("\nGanaste!")
