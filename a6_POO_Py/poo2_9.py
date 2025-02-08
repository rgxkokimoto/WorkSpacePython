import math

'''
Clases en Python
Las clases son los modelos sobre los cuáles se construirán objetos. En Python, una
clase se define con la instrucción class seguida de un nombre genérico para el objeto.
'''
class Concepto:
    pass

'''
La sentencia pass no hace nada. Se puede usar cuando una sentencia es requerida por
la sintaxis, pero el programa no requiere ninguna acción. Se usa normalmente para crear
clases en su mínima expresión.
Las clases se componentes de atributos y métodos.
'''
'''PEP 8: clases
El nombre de las clases se define en singular, utilizando CamelCase.



Atributos de una clase
Los atributos son las características intrínsecas del objeto y modifican su estado. Éstos,
se representan a modo de variables, solo que técnicamente, pasan a denominarse
atributos o propiedades:'''

class Punto:
    x = 0.0
    y = 0.0


'''PEP 8: propiedades
Las propiedades se definen de la misma forma que las variables (aplican las mismas
reglas de estilo).'''

'''Métodos de una clase
Los métodos son bloques de código (o funciones) de una clase que se utilizan para
definir el comportamiento de los objetos. Representan acciones propias que puede
realizar el objeto.'''

class Punto:
    x = 0.0
    y = 0.0
def distancia(self, otro):
    dx = self.x - otro.x
    dy = self.y - otro.y
    return math.sqrt((dx*dx + dy*dy))
'''
Todos los métodos de cualquier clase reciben como primer parámetro a la instancia
sobre la que está trabajando. (self'''

'''Instanciar una clase en Python.
Las clases por sí mismas, no son más que modelos que nos servirán para crear objetos
en concreto. Podemos decir que una clase, es el razonamiento abstracto de un objeto,
mientras que el objeto, es su materialización. A la acción de crear objetos, se la
denomina instanciar una clase y dicha instancia, consiste en asignar la clase, como
valor a una variable:'''

punto = Punto()
print(punto.x)
print(punto.y)


'''Propiedades de un objeto
Una vez creado un objeto, es decir, una vez hecha la instancia de clase, es posible
acceder a su métodos y propiedades. Para ello, Python utiliza una sintaxis muy simple:
el nombre del objeto, seguido de punto y la propiedad o método al cuál se desea
acceder:'''

objeto = MiClase()
objeto.atributo = "Nuevo valor"
print(objeto.atributo)
variable = objeto.metodo()
print(variable)


'''
Constructores en Python
En Python para crear un constructor se utiliza un método especial __init__.
'''
class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx*dx + dy*dy))
    
'''
El constructor nos permite inicializar los atributos de objetos.
Este método se invoca cada vez que se crea una nueva instancia de la clase. Un
constructor no puede retornar ningún valor.
'''

'''
Atributos privados en Python
La característica de no acceder o modificar los valores de los atributos directamente y
utilizar métodos para ello lo llamamos encapsulamiento.
Las variables que comienzan por un doble guión bajo __ la podemos considerar como
atributos privados.
'''

class Alumno:
    def __init__(self,nombre="", num_expediente=""):
        self.nombre = nombre
        self.__num_expediente = num_expediente


'''Encapsulamiento
En Python, las propiedades (getters) nos permiten implementar funciones que expongan de un
atributo privado.
Los métodos setters son métodos que nos permiten modificar el valor de los atributos a través
de un método.'''

class Circulo():
    def __init__(self,radio):
        self.__radio = radio
@property
def radio(self):
    print("Estoy dando el radio")

@radio.setter
def radio(self,radio):
    if radio >= 0:
        self.__radio = radio
    else:
        raise ValueError("El radio debe ser positivo")
    self.__radio=0
    return self.__radio

'''
Información de un objeto
Para saber de qué tipo es un objeto (o una variable), utilizamos la función type, y para
saber qué métodos y atributos tiene ese objeto (o variable) utilizamos la función dir.'''

cadena = "cadena de caracteres"
dir(cadena)
#salida
"""['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']"""
    

'''Mostrar objetos
Para mostrar objetos, Python indica que hay que agregarle a la clase un método
especial, llamado __str__ que debe devolver una cadena de caracteres con lo que
queremos mostrar. Ese método se invoca cada vez que se llama a la función str.
El método __str__ tiene un solo parámetro, self.'''

def __str__(self):
    """ Muestra el punto como un par ordenado. """
    return "(" + str(self.x) + ", " + str(self.y) + ")"

'''Herencia
Algunos objetos comparten las mismas propiedades y métodos que otro
objeto, y además agregan nuevas propiedades y métodos. A esto se lo
denomina herencia: una clase que hereda de otra. Vale aclarar, que en
Python, cuando una clase no hereda de ninguna otra, entonces hereda de
object, que es la clase principal de Python, que define un objeto.'''

# class ClaseDerivada(ClaseBase):

'''
Herencia
La función super() me proporciona una referencia a la clase base. Nos permite acceder
a los métodos de la clase madre.'''

class Punto3d(Punto):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self.z = z

def distancia(self,otro):
    dx = self.x - otro.x
    dy = self.y - otro.y
    dz = self.z - otro.z
    return (dx*dx + dy*dy + dz*dz)**0.5
'''Herencia
__class__ es un método especial de Python que sirve para saber la clase a la que
instancia un objeto.'''

'''Toda variable es un objeto, y por lo tanto tiene una clase (también llamado su tipo). Ésta
se almacena como objeto.__class__'''

# Python tiene dos funciones integradas que funcionan con herencia:
# • isinstance() para verificar el tipo de una instancia.
'''Ej: isinstance(obj, int) devuelve True solo si obj.__class__ es int o alguna clase derivada
de int.'''

'''
 issubclass() para comprobar herencia de clase.
Ej: issubclass(bool, int) da True ya que bool es una subclase de int'''




'''
Delegación
Llamamos delegación a la situación en la que una clase contiene (como atributos) una o
más instancias de otra clase, a las que delegará parte de sus funcionalidades.
'''
class Circulo():
    def __init__(self,centro,radio):
        self.centro=centro
        self.radio=radio
c = Circulo(Punto(2,3),5)
