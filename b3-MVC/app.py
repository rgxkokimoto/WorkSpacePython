from tkinter import *
'''
Clase principal de la aplicación donde se aplican las otras clases y sus lógicas
'''

from model.clase_model import Model
from view.clase_contenedor import Ventana
from view.frame_vacio import FrameVacio
from view.frame_add import FrameAdd
from view.frame_see import FrameSee
from control.controlador import Controlador

class App(Tk):
    def __init__(self):
        super().__init__()

        # Configuraciónes de la ventana Pinicial
        self.title('Lista de la compra')
        self.geometry('350x200')
        self.resizable(False, False)
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Calcular posición centrada
        x = (ancho_pantalla - 350) // 2
        y = (alto_pantalla - 200) // 2
        self.geometry(f"350x200+{x}+{y}")
        
        # Asignar vistas a variables que las representen
        self.crear_menu()
        self.model = Model()
        self.model.limpiar() # !!!! Limpia el archivo de texto

        # Craer los objetos que representan el contenedor el escenario donde ocurren las vistas
        self.contenedor = Ventana(self)
        self.contenedor.place(relx=0.5, rely=0.5, anchor='center')

        # Crear los frames que se van a mostrar en la ventana
        self.lista_frames = {}
        self.lista_frames[0] = FrameVacio(self.contenedor)
        self.lista_frames[1] = FrameAdd(self.contenedor)
        self.lista_frames[2] = FrameSee(self.contenedor)

        # Añadir los frames al contenedor
        self.contenedor.selecionar_frame(self.lista_frames[0])

        # Crear el controlador y pasarle la vista y el modelo
        self.controlador = Controlador(self.contenedor, self.model)

        # Establecer el controlador en los frames
        self.lista_frames[1].set_controlador(self.controlador)


    # Menu superior para seleccionar las vistas de la aplicación
    def crear_menu(self):
        barra_menu = Menu(self)
        self.config(menu=barra_menu)
        self.option_add('*tearOff', FALSE)

        menu_lista = Menu(barra_menu)
        barra_menu.add_cascade(menu=menu_lista, label='Opciones')

        menu_lista.add_command(label='Añadir producto', command=self.add)
        menu_lista.add_command(label='Ver Lista', command=self.ver)

    # Representacción de la vista de añadir producto
    def add(self):
        self.contenedor.selecionar_frame(self.lista_frames[1])

    # Representacción de la vista de ver lista
    def ver(self):
        self.contenedor.selecionar_frame(self.lista_frames[2])
        self.lista_frames[2].cargar_lista(self.model.leer())

# Lanzar la aplicación
if __name__ == '__main__':
    app = App()
    app.mainloop()