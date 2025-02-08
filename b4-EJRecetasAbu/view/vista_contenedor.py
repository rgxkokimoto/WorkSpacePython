from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class FrameContenedor(ttk.Frame):

    # Constructor
    def __init__(self, parent):
        super().__init__(parent)
        self.frame = None

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

