class Receta:

    #Constructor
    def __init__(self, nombre="", num_pasos=0, dificultad=1):
        self.nombre = nombre # asignar al parametro
        self.num_pasos = num_pasos
        self.dificultad = dificultad
    
    #Opciones del atributo dificultad
    dic_dif = {1: "poca", 2:"normal", 3:"alta"}
    dic_tpo = {1:5, 2:5, 3:7}

    #ToString
    def __str__(self):
        cadena = "La receta " + self.nombre + ", " + self.num_pasos
        cadena = cadena + ", " + self.dic_dif.get(self.dificultad)
        return cadena
    
    #Metodo complementario
    def calcular_tpo_ejec(self):
            return self.num_pasos *  self.dic_tpo.get(self.dificultad)


