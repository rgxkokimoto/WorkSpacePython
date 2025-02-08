class Lenguaje:

    def __init__(self, nombre="",creador="",anio=0.0,porc=0.0,diff=0.0):
        self.nombre = nombre
        self.creador = creador
        self.anio = anio
        self.porc = porc
        self.diff = diff

    def __str__(self):
        
        return (f"{self.nombre} {self.anio}\n"
            f"Creador: {self.creador}\n"
            f"Porcentaje de uso: {self.porc}%\n"
            f"Diferencia con el año anterior: {self.diff}")
    
    #- Que tenga un método que devuelva el apellido del creador sabiendo que será a partir de la primera palabra.
    def getSurname(self):
        fragLs = self.creador.partition(" ")
        return  fragLs[2]
    
    
    

    """- Que tenga un método que devuelva el porcentaje de hace un año.
    Ejemplo: C++ hace un año tenía un porcentaje de uso de 10.35"""
    def getLastYear(self):
        return self.porc + self.diff
