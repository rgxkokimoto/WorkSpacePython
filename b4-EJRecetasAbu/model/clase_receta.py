class Receta:
    #Constructor
    def __init__(self, nombre, especificaciones, tiempo_estimado, dificultad):
        self.nombre = nombre
        self.especificaciones = especificaciones
        self.tiempo_estimado = tiempo_estimado
        self.dificultad = dificultad

    #To String
    def __str__(self):
        cadena = "nombre: " + self.nombre + "\n" 
        + self.especificaciones + "\n" 
        "tiempo estimado: " + self.tiempo_estimado + "\n"
        + "dificultad: "+ self.dificultad
        return cadena


    
