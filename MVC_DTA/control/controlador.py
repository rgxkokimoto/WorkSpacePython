# Unión entre la parte visual y el controll 

class Controlador:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        

    def guardar(self, producto):
        self.model.guardar(producto)
        self.view.mostrar_mensaje('El producto se ha guardado correctamente')

    

