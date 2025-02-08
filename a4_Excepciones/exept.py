import sys


# CAPTURAR VARIAS EXCEPCIONES EN UN TRY:
try:
# aquí ponemos el código que puede lanzar excepciones
    3/0
except IOError:
# entrará aquí en caso que se haya producido una excepción IOError
    print("IO")
except ZeroDivisionError:
# entrará aquí en caso que se haya producido
# una excepción ZeroDivisionError
    print("o1")
except:
    print(" o")

# que no corresponda a ninguno de los tipos especificados en
# los except previos


'''
Manejo de Excepciones en Python. Finally
Después de los bloques try y except, puede ubicarse un bloque finally donde se escriben
las sentencias de finalización, que son típicamente acciones de limpieza. 

Finaly se va ejecutar al final siempre.

Si hay un bloque except, no es necesario que esté presente el finally.
'''


try:
    archivo = open("miarchivo.txt")
    # procesar el archivo
except IOError:
    print("Error de entrada/salida.")
# realizar procesamiento adicional
except:
# procesar otra posible excepción
    print("poPAPU")
finally:
    # si el archivo no está cerrado hay que cerrarlo
    if not(archivo.closed):
        archivo.close()


'''Ejecución de Excepciones en Python.
Python comienza a ejecutar las instrucciones que se encuentran dentro de un bloque try. Si
durante la ejecución de esas instrucciones se produce una excepción, Python interrumpe la
ejecución en el punto exacto en que surgió la excepción y pasa a la ejecución del bloque
except correspondiente.
Para ello, Python verifica uno a uno los bloques except y si encuentra alguno cuyo tipo haga
referencia al tipo de excepción producida, comienza a ejecutarlo. Si no encuentra ningún
bloque del tipo correspondiente, pero hay un bloque except sin tipo, lo ejecuta.
Al terminar de ejecutar el bloque correspondiente, se pasa a la ejecución del bloque finally, si
se encuentra definido.
Si, por otra parte, no hay problemas durante la ejecución del bloque try, se completa la
ejecución del bloque, y luego se pasa directamente a la ejecución del bloque finally (si es que
está definido).
'''


'''
Propagación de Excepciones
Es posible, además, que después de realizar algún procesamiento particular de una
excepción, se quiera que se propague hacia la función que había invocado a la función
en la que se ha producido. Para hacer esto Python nos ofrece la instrucción XXX raise.
Si se invoca esta instrucción dentro de un bloque except, sin pasarle parámetros, Python
propagará la excepción atrapada por ese bloque.
Nos podría interesar que, en lugar de propagar la excepción tal cual fue atrapada,
quisiéramos lanzar una excepción más significativa para quien invocó a la función actual
y que posiblemente contenga cierta información de contexto. Para levantar una
excepción de cualquier tipo, utilizamos también la sentencia XXX raise, pero indicándole el
tipo de excepción que deseamos lanzar y pasando a la excepción los parámetros con
información adicional que queramos facilitar
'''

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")


def main():
    try:
        dividendo = 5
        divisor = 0
        print(dividir(dividendo, divisor))
    except ZeroDivisionError as ex:
        print("Ha ocurrido una excepción: ", ex)
main()


# RAISE tambien es util para capturar excepciones expecifiacas junto a una condición if


def solicNumRange():
    
    
    try: 
        num = input("Introduce un numero del uno al 10: ")

        if num not in range(0,10): # jaja se puede hacer esto ;)
            raise IndexError
    except IndexError:
        print("El numero esta fuera de rango")


'''Acceso a información de contexto
Para acceder a la información de contexto estando dentro de un bloque except existen
dos alternativas.
Se puede utilizar la función exc_info del módulo sys. Esta función devuelve una tupla
con información sobre la última excepción atrapada en un bloque except. Dicha tupla
contiene tres elementos: el tipo de excepción, el valor de la excepción y las llamadas
realizadas.
Otra forma de obtener información sobre la excepción es utilizando la misma sentencia
except, pasándole un identificador para que almacene una referencia a la excepción
atrapada.
'''


def main():
    try:
        dividendo = 5
        divisor = 0
        print(dividir(dividendo, divisor))
    except ZeroDivisionError as ex:
        print("Ha ocurrido una excepción: ", ex)
        print(sys.exc_info()) # TODO
        print(type(ex))
        print(ex.args)


'''A continuación se listan algunas de las excepciones disponibles por defecto, así como la
clase de la que deriva cada una de ellas entre paréntesis.
• BaseException: Clase de la que heredan todas las excepciones.
• Exception(BaseException): Super clase de todas las excepciones que no sean de
salida.
• StandarError(Exception): Clase base para todas las excepciones que no tengan
que ver con salir del intérprete.
• ArithmeticError(StandardError): Clase base para los errores aritméticos.
• FloatingPointError(ArithmeticError): Error en una operación de coma flotante.
• OverflowError(ArithmeticError): Resultado demasiado grande para poder
representarse.
Excepciones de Python
• ZeroDivisionError(ArithmeticError): Lanzada cuando el segundo argumento de
una operación de división o módulo era 0
• AssertionError(StandardError): Falló la condición de un estamento assert.
• AttributeError(StandardError): No se encontró el atributo.
• EOFError(StandardError): Se intentó leer más allá del final de fichero.
• EnvironmentError(StandardError): Clase padre de los errores relacionados con la
entrada/salida.
• IOError(EnvironmentError): Error en una operación de entrada/salida.
• OSError(EnvironmentError): Error en una llamada a sistema.
• WindowsError(OSError): Error en una llamada a sistema en Windows.
• ImportError(StandardError): No se encuentra el módulo o el elemento del módulo
que se quería importar.
Excepciones de Python
• LookupError(StandardError): Clase padre de los errores de acceso.
• IndexError(LookupError): El índice de la secuencia está fuera del rango posible.
• KeyError(LookupError): La clave no existe.
• MemoryError(StandardError): No queda memoria suficiente.
• NameError(StandardError): No se encontró ningún elemento con ese nombre.
• UnboundLocalError(NameError): El nombre no está asociado a ninguna variable.
• ReferenceError(StandardError): El objeto no tiene ninguna referencia fuerte
apuntando hacia él.
• RuntimeError(StandardError): Error en tiempo de ejecución no especificado.
• NotImplementedError(RuntimeError): Ese método o función
no está implementado.Excepciones de Python
• LookupError(StandardError): Clase padre de los errores de acceso.
• IndexError(LookupError): El índice de la secuencia está fuera del rango posible.
• KeyError(LookupError): La clave no existe.
• MemoryError(StandardError): No queda memoria suficiente.
• NameError(StandardError): No se encontró ningún elemento con ese nombre.
• UnboundLocalError(NameError): El nombre no está asociado a ninguna variable.
• ReferenceError(StandardError): El objeto no tiene ninguna referencia fuerte
apuntando hacia él.
• RuntimeError(StandardError): Error en tiempo de ejecución no especificado.
• NotImplementedError(RuntimeError): Ese método o función
no está implementado.
Excepciones de Python
• SyntaxError(StandardError): Clase padre para los errores sintácticos.
• IndentationError(SyntaxError): Error en la indentación del archivo.
• TabError(IndentationError): Error debido a la mezcla de
espacios y tabuladores.
• SystemError(StandardError): Error interno del intérprete.
• TypeError(StandardError): Tipo de argumento no apropiado.
• ValueError(StandardError): Valor del argumento no apropiado.
https://docs.python.org/3.13/library/exceptions.html#base-classesExcepciones de Python
• SyntaxError(StandardError): Clase padre para los errores sintácticos.
• IndentationError(SyntaxError): Error en la indentación del archivo.
• TabError(IndentationError): Error debido a la mezcla de
espacios y tabuladores.
• SystemError(StandardError): Error interno del intérprete.
• TypeError(StandardError): Tipo de argumento no apropiado.
• ValueError(StandardError): Val'''



'''Validaciones: assert
El uso de assert en Python nos permite realizar comprobaciones. Si la expresión
contenida dentro del mismo es False, se lanzará una excepción, concretamente
AssertionError
La sentencia assert nos permite realizar la validación de un dato. Se debe usar para
controlar condiciones que no deberían ocurrir jamás.'''


def main():
    i = 2
    dividendo = 5
    divisor = 0

    if i == 1:
        try:
            print(dividir(dividendo, divisor))
        except ZeroDivisionError as ex:
            print("Ha ocurrido una excepción: ", ex)
            print(sys.exc_info()) # TODO
            print(type(ex))
            print(ex.args)
    else: 
        try:
            assert divisor != 0
            print(dividendo,divisor)
        except AssertionError:
            print(sys.exc_info())
            print("No se ")

main()