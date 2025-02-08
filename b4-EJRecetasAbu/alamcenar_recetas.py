from tkinter import *

from model.class_model import Model
# Vistas Obligatorias orientadas a la estructura de la GUI
from view.vista_contenedor import FrameContenedor
from view.vista_vacia import VistaVacia
# Vistas Principales orientadas a visualizar la lógica de la aplicación
from view.vista_recetas import VistaReceta 

from control.control import Controlador

class App(Tk):
    def __init__(self):
        super().__init__()

        # Configuración básicas de la ventana principal
         # Configuraciónes de la ventana Pinicial
        self.title('Recetas de la Abuela')
        # 533x257 px
        self.geometry('533x257')
        self.resizable(False, False)
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Calcular posición centrada
        x = (ancho_pantalla - 533) // 2
        y = (alto_pantalla - 257) // 2
        self.geometry(f"533x257+{x}+{y}")

        # Asignar las vistas principales a variables que las representen
        self.crear_menu()
        self.model = Model()
        self.model.limpiar()

        # Implementar los frames que componen la GUI
        self.contenedor = FrameContenedor(self)
        self.contenedor.place(relx=0.5, rely=0.5, anchor='center')

        self.lista_frames = {}
        self.lista_frames[0] = VistaVacia(self.contenedor)
        self.lista_frames[1] = VistaReceta(self.contenedor)

        # Añadir los frames al contenedor
        self.contenedor.seleccionar_frame(self.lista_frames[0])

        # Crear el controlador y pasarle la vista y el modelo
        self.controlador = Controlador(self.contenedor, self.model)

        # Presentar el controlador en las vistas que lo requieran
        self.lista_frames[1].set_controlador(self.controlador)


    def crear_menu(self):
        barra_menu = Menu(self)
        self.config(menu=barra_menu)
        self.option_add('*tearOff', FALSE)

        menu_lista = Menu(barra_menu)
        barra_menu.add_cascade(menu=menu_lista, label='Opciones')

        menu_lista.add_command(label='Recetas Abuela', command=self.vR)

    def vR(self):
        self.contenedor.seleccionar_frame(self.lista_frames[1])


if __name__ == '__main__':
    app = App()
    app.mainloop()