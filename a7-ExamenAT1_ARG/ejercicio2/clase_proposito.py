import sys

class Proposito:
       #Constructor
    def __init__(self, description="", clasificacion=1, prioridad=1):
        self.descripcion = description # asignar al parametro
        self.clasificacion = clasificacion
        self.prioridad = prioridad
    
    def tradPrority(n):
        isOk = False
        dic_p = {1:"baja", 2:"medio-baja", 3:"media", 4:"medio-alta", 5:"alta"}

        while not isOk: 
            try:
                assert n is range(1,5)
                cad = dic_p.get(n)
                isOk = True
                return cad
            except AssertionError:
                print("Introduzca un valor numerico dentro del rango ")
                return 1


    def three_last_words(self):
         
        ls_words = self.descripcion.strip().split(" ")
        ls_words.reverse()
        return f"{ls_words[2]} {ls_words[1]} {ls_words[0]}"
    

    '''Que tenga un método que permita mostrar los datos de un propósito por
    consola con el siguiente formato:
    Ejemplo de lo que se debe mostrar por consola:
    Descripción: Ir a Budapest antes de septiembre del 2025
    Clasificación: Viajes
    Prioridad: media
    Cumplir antes de septiembre del 2025'''

    #ToString
    def __str__(self):
        dic_c = {1: "Salud", 2:"Amigos", 3:"Familia", 4:"Viajes", 5:"Deporte o Trabajo", }
        
        dic_p = {1:"baja", 2:"medio-baja", 3:"media", 4:"medio-alta", 5:"alta"}


        cadena = "Descrición: " + self.descripcion + "\nClasificación: " + dic_c.get(self.clasificacion) + "\nPrioridad: " + dic_p.get(self.prioridad) + "\nCumplir antes de " + self.three_last_words()
        return cadena
    

'''p = Proposito("Ir a Budapest antes de septiembre del 2025",3,4)
p2 = Proposito("Aprender a hacer meditación antes",4 ,5)
p3 = Proposito("Dominar el lenguaje de python antes de febrero de 2025",4 ,5)
 
p.descripcion
p.clasificacion
p.prioridad'''

#print(len("Ir a Budapest antes de septiembre del 2025".split(" ")))