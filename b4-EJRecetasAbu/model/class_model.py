NOMBRE_FICHERO = 'b4-EJRecetasAbu/dta/recetas.txt'

'''
Clase encaragada de interactuar con la base de datos
Realiza Operaciones crud
'''

class Model:
    def __init__(self):
        pass

    def guardar(self,receta):
        f = open(NOMBRE_FICHERO, 'a')

        cadena = "nombre: " + receta.nombre + "\n" 
        "especificaciones: " + receta.especificaciones + "\n" 
        "tiempo estimado: " + receta.tiempo_estimado + "\n" 
        "dificultad: "+ receta.dificultad + "\n"

        f.write(cadena)
        f.close()

    def limpiar(self):
        f = open(NOMBRE_FICHERO, 'a')
        f.truncate()
        f.close()
        
    def leer(self):
        print("leer")
        lista_productos = []
        f = open(NOMBRE_FICHERO, 'r')
        linea = f.readline()
        cont = 0
        while linea != '':
            cont += 1
            lista_productos.append(linea)
            # print(linea)
            linea = f.readline()

        f.close()
        return lista_productos
