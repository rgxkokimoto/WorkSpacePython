from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from model import clase_receta

class VistaReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controlador = None
        
        estilo = ttk.Style()
        estilo.configure("FA.TFrame", background="white")
        self.configure(style="FA.TFrame")
        
        self.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

        stl_lbl_titulo = ttk.Style()
        stl_lbl_titulo.configure("LblTitulo.TLabel", font=("Arial", 14,) , background="white")
        self.lbl_fa_titulo = ttk.Label(self, text="Recetas de la abuela" , relief="solid")
        self.lbl_fa_titulo['style'] = "LblTitulo.TLabel"
        self.lbl_fa_titulo.grid(row=0, column=0, columnspan=2, sticky='nesw')

        self.lbl_nombre = ttk.Label(self, text="Nombre:" , relief="solid", anchor="w")
        self.lbl_nombre.grid(row=1, column=0, sticky='nesw')
        self.nombre = StringVar()
        self.ent_nombre = ttk.Entry(self, textvariable=self.nombre)
        self.ent_nombre.grid(row=1, column=1, sticky='we')
        self.ent_nombre.focus()

        self.lbl_especificaciones = ttk.Label(self, text="Especificaciones:" , relief="solid", anchor="w")
        self.lbl_especificaciones.grid(row=2, column=0, columnspan=2, sticky='nesw')
        self.especificaciones = StringVar()
        self.ent_especificaciones = ttk.Entry(self, textvariable=self.especificaciones)
        self.ent_especificaciones.grid(row=3, column=0,columnspan=2 , sticky='nesw')

        self.lbl_tiempo_estimado = ttk.Label(self, text="Tiempo estimado:" , relief="solid", anchor="w")
        self.lbl_tiempo_estimado.grid(row=4, column=0, sticky='nesw')

        self.time_set = StringVar()
        self.time_set.set(5)
        self.spn_num = ttk.Spinbox(self, from_=5, to=120, increment=1, textvariable=self.time_set, state='readonly')
        self.spn_num.grid(row=4,column=1, sticky='nesw')

        self.lbl_dificultad = ttk.Label(self, text="Dificultad:" , relief="solid", anchor="w")
        self.lbl_dificultad.grid(row=5, column=0, sticky='nesw')
        self.cmb_valor_lvl = StringVar()
        lvls = ["Fácil", "Media", "Difícil"]
        self.cmb_lvl = ttk.Combobox(self, values=lvls, state="readonly", textvariable=self.cmb_valor_lvl)
        self.cmb_lvl.grid(row=5, column=1,sticky="nesw")
        self.cmb_lvl.current(1)

        self.btn_guardar = ttk.Button(self, text="Guardar")
        self.btn_guardar.bind("<Button-1>", self.raton)

        # self.btn_add = ttk.Button(self, text="Añadir Producto", command=self.guardar)
        self.btn_add = ttk.Button(self, text="Añadir Receta")
        # BINDING
        self.btn_add.bind('<Button-1>', self.raton)
        self.btn_add.bind('<Return>', self.tecla) # Al pulsar enter
        self.btn_add.grid(row=6, column=1, padx=5, pady=5, sticky='news')


    def set_controlador(self, controlador):
        self.controlador = controlador

    def limpiar_datos(self):
        self.lista_recetas.delete(0, "end")

    def raton(self, event):
        self.guardar()

    def tecla(self, event):
        self.guardar()

    def guardar(self):
        nombre = self.nombre.get()
        especificaciones = self.especificaciones.get()
        tiempo_estimado = self.tiempo_estimado.get()
        dificultad = self.dificultad.get()
        receta = clase_receta.Receta(nombre, especificaciones, tiempo_estimado, dificultad)
        
        if len(nombre) == 0:
            messagebox.showerror("Error", "El nombre no puede estar vacío")
            return
        
        self.controlador.guardar(receta)
        
