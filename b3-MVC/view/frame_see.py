from tkinter import *
from tkinter import messagebox
from tkinter import ttk

NUM_ITEMS_VIS = 5 

class FrameSee(ttk.Frame):
    def __init__(self, parent, lista=[]): # lista = [] es un valor por defecto
        super().__init__(parent) 

        self.lista = lista 
        self.controlador = None 

        estilo = ttk.Style()
        estilo.configure("FS.TFrame", background="pink")

        self.configure(style="FS.TFrame")
        self.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.fs_label = ttk.Label(self, text="Ver lista de la compra", background="pink")
        self.fs_label.configure(font=("Arial", 18, "bold"))
        self.fs_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        
        self.list_items = Variable(value=self.lista)
        self.listbox = Listbox(self, height=NUM_ITEMS_VIS, listvariable=self.list_items)
        self.listbox.grid(row=1, column=0, sticky='nes')
        
        self.scrollbar_v = ttk.Scrollbar(self, orient='vertical', command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar_v.set
        self.scrollbar_v.grid(row=1, column=1, sticky='nsw')

    def cargar_lista(self, lista):
        self.lista = lista
        self.list_items.set(self.lista)

    """def set_controlador(self, controlador):
        self.controlador = controlador"""
