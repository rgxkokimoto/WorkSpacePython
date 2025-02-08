from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from model import clase_producto

class FrameAdd(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None

        estilo = ttk.Style()
        estilo.configure("FA.TFrame", background="white")
        self.configure(style="FA.TFrame")
        
        self.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

        stl_lbl_titulo = ttk.Style()
        stl_lbl_titulo.configure("LblTitulo.TLabel", font=("Arial", 18, "bold") , background="white")
        self.lbl_fa_titulo = ttk.Label(self, text="Añadir prod a la lista")
        self.lbl_fa_titulo['style'] = "LblTitulo.TLabel"
        self.lbl_fa_titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        stl_lbl_fa = ttk.Style()
        stl_lbl_fa.configure("LblFA.TLabel", background="white", font=("Arial", 12, "bold"))
        
        self.lbl_descripcon = ttk.Label(self, text="Descripción", background="white")
        self.lbl_descripcon.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.descripion = StringVar()
        self.ent_descripcion = ttk.Entry(self, textvariable=self.descripion)
        self.ent_descripcion.grid(row=1, column=1, padx=5, pady=5, sticky='we')
        self.ent_descripcion.focus()

        self.lbl_cantidad = ttk.Label(self, text="Cantidad", background="white")
        self.lbl_cantidad.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.cantidad = StringVar()
        self.ent_cantidad = ttk.Entry(self, textvariable=self.cantidad)
        self.ent_cantidad.grid(row=2, column=1, padx=5, pady=5, sticky='we')

        # self.btn_add = ttk.Button(self, text="Añadir Producto", command=self.guardar)
        self.btn_add = ttk.Button(self, text="Añadir Producto")
        # BINDING
        self.btn_add.bind('<Button-1>', self.raton)
        self.btn_add.bind('<Return>', self.tecla)
        self.btn_add.grid(row=3, column=1, padx=5, pady=5, sticky='we')
        
    def set_controlador(self, controlador):
        self.controlador = controlador
    
    def limpiar_datos(self):
        self.ent_descripcion.delete(0, "end")
        self.ent_cantidad.delete(0, "end")
    
    def raton(self, event):
        self.guardar()
    
    def tecla(self, event):
        self.guardar()

    def guardar(self):
        # VALIDAR
        desc = self.descripion.get()
        cant = self.cantidad.get()

        if len(desc) == 0:
            messagebox.showerror("Error de datos", "La descripción no puede estar vacía")
            self.ent_descripcion.focus()

        else:
            if len(cant) == 0:
                messagebox.showerror("Error de datos", "La cantidad no puede estar vacía")
                self.ent_cantidad.focus()

            else:
                producto = clase_producto.Producto(desc, cant)
                print(producto)
                
                if self.controlador:
                    self.controlador.guardar(producto)
                self.limpiar_datos()
                self.ent_descripcion.focus()
