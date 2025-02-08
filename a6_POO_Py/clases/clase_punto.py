import math

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

def main():
    punto = Punto()
    punto.x = 2
    punto.y = 3
    print(punto.x)
    print(punto.y)

main()