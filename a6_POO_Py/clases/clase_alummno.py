class Alummno:
    
    def __init__(self, nombre="",num_exp=""):
        self.nombre = nombre
        self.__num_exp = num_exp # XXX  __ esto indica que es privado

    #get XXX en python los métodos get son para apellidos privados
    @property
    def num_exp(self): 
        return self.__num_exp
    
    #setter
    @num_exp.setter
    def num_exp(self, num_exp):
        self.__num_exp = num_exp

    #To_String
    def __str__(self):
        return "\nnombre: " + self.nombre + " - " + self.__num_exp

# herencia
class Alumno2(Alummno):
    
    #Automatico XXX
    def __init__(self, nombre="", num_exp="", accede_fct=True):
        super().__init__(nombre, num_exp)
        self.accede_fct = accede_fct

    def __str__(self):                                  #Ternario al reves 0 1   
        return super().__str__() + "Accerde a FCT: " + ("NO","SI") [self.accede_fct]


def main():
    alum1 = Alummno()
    alum1.nombre = "Ana"
    # alum1.__num_exp = "12345678" # sin set
    alum1.num_exp = "12345678" # con set

    # no saldra nada porque es privado necesitas los metodos get y set
    print(alum1)
    print(dir(alum1))
    

    # Alumno con herencia 

    alum2 = Alumno2("Pedro","2378965723868") # si no cojo nada me da el valor por defecto
    print(alum2)
    # salida metodos que usa alumno 
    # ['_Alummno__num_exp', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'nombre', 'num_exp']

main()