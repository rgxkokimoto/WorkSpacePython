class Controlador:
    def __init__(self, contenedor, frame_ppal, modelo):
        self.contenedor = contenedor
        self.frame_ppal = frame_ppal
        self.modelo = modelo

    def guardar(self, receta):
        self.modelo.guardar(receta)
        self.vista.mostrar_mensaje('La receta se ha guardado correctamente')
        self.frame_ppal.cargar_recetas(self.modelo.leer())

#!
'''Está muy bien Alejandro. Hay algunas cositas:
El spinner debía ir de 5 en 5.
Fíjate que en este caso como no hay menú no es necesario el Frame vacío.
Y lo más importante es que, debería ser el método guardar del controlador el que se 
encargara de invocar a cargar_recetas pasándole la lista de recetas. Tu estás usando
el model desde la vista y el controlador debería de actuar de intermediario entre la 
vista y el modelo ¿me explico? Si en la vista pones el modelo ya no necesitas al controlador'''