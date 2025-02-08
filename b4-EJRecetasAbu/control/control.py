class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def guardar(self, receta):
        self.modelo.guardar(receta)
        self.vista.mostrar_mensaje('La receta se ha guardado correctamente')