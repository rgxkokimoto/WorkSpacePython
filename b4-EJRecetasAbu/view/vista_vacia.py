from tkinter import *
from tkinter import ttk

class VistaVacia(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")