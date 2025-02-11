from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from model import clase_receta
from model.class_model import Model

NUM_ITEMS_VIS = 10

class VistaReceta(ttk.Frame):
    def __init__(self, parent, lista=[]):
        super().__init__(parent)
        self.lista_recetas = lista
        self.controlador = None

        self.model = Model()
        
        estilo = ttk.Style()
        estilo.configure("FA.TFrame", background="white")
        self.configure(style="FA.TFrame")

        # Configurar las columnas y filas para que se expandan

        self.grid(row=0, column=0, sticky="nesw")

        #self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(7, weight=1)
        
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

        self.lbl_especificaciones = ttk.Label(self, text="Especificaciones:" , relief="solid", anchor="center")
        self.lbl_especificaciones.grid(row=2, column=0, columnspan=2, sticky='nesw')

        self.atxt_especificaciones = Text(self, height=2)
        self.atxt_especificaciones.insert("1.0", "Especificaciónes :")
        self.atxt_especificaciones.grid(row=3, column=0,columnspan=2 , sticky='nesw')
        self.scr_especific_v = ttk.Scrollbar(self, orient="vertical", command=self.atxt_especificaciones.yview)
        self.atxt_especificaciones['yscrollcommand'] = self.scr_especific_v.set
        self.scr_especific_v.grid(row=3, column=1, sticky="nes")

        self.lbl_tiempo_estimado = ttk.Label(self, text="Tiempo estimado:" , relief="solid", anchor="w")
        self.lbl_tiempo_estimado.grid(row=4, column=0, sticky='nesw')

        self.time_set = StringVar()
        self.time_set.set(5)
        self.spn_num = ttk.Spinbox(self, from_=5, to=120, increment=1, textvariable=self.time_set, state='readonly')
        self.spn_num.grid(row=4,column=1, sticky='nesw')


        self.lbl_dificultad = ttk.Label(self, text="Dificultad:" , relief="solid", anchor="w")
        self.lbl_dificultad.grid(row=5, column=0, sticky='nesw')

        self.cmb_valor_lvl = StringVar()
        lvls = ["Facil", "Media", "Dificil"]
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
        self.btn_add.grid(row=6, column=0,columnspan=2, sticky='news')

        self.list_item = Variable(value=self.lista_recetas)
        self.listbox = Listbox(self, height=NUM_ITEMS_VIS, listvariable=self.list_item)
        self.listbox.grid(row=7, column=0, columnspan=2, sticky='nswe')

        self.scrollbar_v = ttk.Scrollbar(self, orient='vertical', command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar_v.set
        self.scrollbar_v.grid(row=7, column=1, sticky='nes')

    def set_controlador(self, controlador):
        self.controlador = controlador

    def limpiar_datos(self):
        self.lista_recetas.delete(0, "end")

    def raton(self, event):
        self.guardar()

    def tecla(self, event):
        self.guardar()

    def cargar_recetas(self, lista):
        self.lista_recetas = lista
        self.list_item.set(self.lista_recetas)

    def guardar(self):
        nombre = self.nombre.get()
        especificaciones = self.atxt_especificaciones.get("1.0", "end-1c")
        tiempo_estimado = self.time_set.get()
        dificultad = self.cmb_valor_lvl.get()
        receta = clase_receta.Receta(nombre, especificaciones, tiempo_estimado, dificultad)

        # Limpiar los campos
        self.ent_nombre.delete(0, "end")
        self.atxt_especificaciones.delete("1.0", "end")
        self.spn_num.set(5)
        self.cmb_lvl.current(1)

        if len(nombre) == 0:
            messagebox.showerror("Error", "El nombre no puede estar vacío")
            return
        
        self.controlador.guardar(receta)
        self.cargar_recetas(self.model.leer())
        
