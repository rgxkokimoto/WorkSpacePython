from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class FrameContenedor(ttk.Frame):

    # Constructor
    def __init__(self, parent):
        super().__init__(parent)
        self.frame = None
        # Ensanchamos el contenedor para que ocupe toda la ventana
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # Método para seleccionar un frame
    def seleccionar_frame(self, frame):
        self.frame = frame
        self.frame.tkraise()

    # Método para mostrar un mensaje
    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Info", mensaje)

    # Método para mostrar un mensaje de error
    def mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

