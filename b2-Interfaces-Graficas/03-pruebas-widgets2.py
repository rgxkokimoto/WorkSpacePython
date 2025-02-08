from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana_raiz = Tk()
ventana_raiz.title("Pruebas Widgets 2")
ventana_raiz.geometry("600x500")
ventana_raiz.maxsize(700, 600)
ventana_raiz.minsize(400, 300)

contenedor = ttk.Frame(ventana_raiz)
contenedor.pack(padx=10)

stl_titulo = ttk.Style()
stl_titulo.configure("Titulo.TLabel", font=("Arial", 18), foreground="blue", background="yellow",
relief="flat", bd="5")

lbl_etiqueta1 = ttk.Label(contenedor, text="Ventana de pruebas 2")
# lbl_etiqueta1.configure(font=("Arial", 18)) # Sin estilo :(
# lbl_etiqueta1['foreground'] = "blue"
lbl_etiqueta1['style'] = "Titulo.TLabel"
lbl_etiqueta1.grid(row=0, column=0, columnspan=3, pady=5)

lbl_comentarios = ttk.Label(contenedor, text="Comentario: ")
lbl_comentarios.grid(row=1, column=0, padx=5, pady=5)

atxt_comentarios = Text(contenedor, height=5, width=40)
atxt_comentarios.insert("1.0", "Primera fila del area de texto")
atxt_comentarios.grid(row=1, column=1, pady=5)

scr_comentarios_v = ttk.Scrollbar(contenedor, orient="vertical", command=atxt_comentarios.yview)
atxt_comentarios['yscrollcommand'] = scr_comentarios_v.set
scr_comentarios_v.grid(row=1, column=2, pady=5, sticky="nsw")

lbl_aficiones = ttk.Label(contenedor, text="Aficiones")
lbl_aficiones.grid(row=2, column=0, padx=5, pady=5)

def seleccion_check():
    print("Seleccionado musica? " + str(chk_valor_musica.get()) + "\nSeleccionado deporte? " + str(chk_valor_deporte.get()))


chk_valor_musica = StringVar()

chk_musica = ttk.Checkbutton(contenedor, text="Musica", command=seleccion_check, variable=chk_valor_musica)
chk_musica.grid(row=2, column=1, pady=5, sticky="w")

chk_valor_deporte = StringVar()
chk_deporte = ttk.Checkbutton(contenedor, text="Deporte", command=seleccion_check, variable=chk_valor_deporte)
chk_deporte.grid(row=2, column=2, pady=5, sticky="w")

lbl_curso = ttk.Label(contenedor, text="Curso: ")
lbl_curso.grid(row=3, column=0, padx=5, pady=5)

def seleccion_rbtn():
    print("Se ha escogido el curso " + rbtn_sel.get())
    print("Dia seleccionado: " + cmb_valor_dia.get() + " " + cmb_dia.get())
    print("Indice del dia seleccionado: " + str(cmb_dia.current()))
    print("Edad seleccionada: " + edad_sel.get())
    print("Color seleccionado: " + color_sel.get())
    destinos.append("Highlands de Irlanda que me gustan mucho")
    list_items_dest.set(destinos)
    #* Probamos los metodos de Listbox
    print("Esta Japon seleccionao? " + str(lst_destinos.selection_includes(1)))
    print(lst_destinos.curselection())
    #? messagebox.showinfo("Mensaje informativo", "Este es el contenido del mensaje de informacion")
    #! messagebox.showerror("Mensaje de error", "Este es el contenido del mensaje de error")
    #* if messagebox.askokcancel("Confirmacion con OK", "Desea saber cual es la opcion seleccionada?"):
    #* print("Ha contestado")
    resp = messagebox.askyesnocancel("Confirmacion a tres botones", "Desea saber la eleccion?")

    if resp != None:
        print("Opcion " + resp)


rbtn_sel = StringVar()
rbtn_primero = ttk.Radiobutton(contenedor, text="Primero", value="1º DAM", variable=rbtn_sel, command=seleccion_rbtn)
rbtn_primero.grid(row=3, column=1, padx=5, pady=5, sticky="w")

rbtn_segundo = ttk.Radiobutton(contenedor, text="Segundo", value="2º DAM", variable=rbtn_sel, command=seleccion_rbtn)
rbtn_segundo.grid(row=3, column=2, padx=5, pady=5, sticky="w")

lbl_dia = ttk.Label(contenedor, text="Dia: ")
lbl_dia.grid(row=4, column=0, padx=5, pady=5)

cmb_valor_dia = StringVar()
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
cmb_dia = ttk.Combobox(contenedor, values=dias, state="readonly", textvariable=cmb_valor_dia)
cmb_dia.grid(row=4, column=1, padx=5, pady=5, sticky="w")
#cmb_dia.set("Viernes")
print(cmb_dia.current()) #? Deberia dar un -1 al estar vacio
cmb_dia.current(3) #? Seleccionamos el dia en posicion 3

lbl_edad = ttk.Label(contenedor, text="Edad: ")
lbl_edad.grid(row=5,column=0,padx=5,pady=0)

edad_sel = StringVar()
edad_sel.set(0)
spn_num = ttk.Spinbox(contenedor, from_=0, to=120, increment=1, textvariable=edad_sel, state='readonly')
spn_num.grid(row=5,column=1,padx=5,pady=5)

lbl_colores = ttk.Label(contenedor, text="Colores: ")
lbl_colores.grid(row=6, column=0, padx=5, pady=5)

colores = ["Rojo", "Azul", "Amarillo", "Verde", "Naranja", "Morado"]
color_sel = StringVar()
color_sel.set(colores[0])
spn_color = ttk.Spinbox(contenedor, textvariable=color_sel, state="readonly")
spn_color.grid(row=6, column=1, padx=5, pady=5)
spn_color['values'] = colores

lbl_destinos = ttk.Label(contenedor, text="Destinos a los que viajar: ")
lbl_destinos.grid(row=7, column=0, padx=5, pady=5, sticky="w")

destinos = ["Nueva York", "Japon", "Dubai","Cuenca"]
list_items_dest = Variable(value=destinos)
lst_destinos = Listbox(contenedor, height=5, listvariable=list_items_dest, selectmode="single")
lst_destinos.selection_set(0,1)
lst_destinos.grid(row=8, column=0 ,padx=5, pady=(5,0), sticky="w")

scr_lista_h = ttk.Scrollbar(contenedor, orient="horizontal", command=lst_destinos.xview)
lst_destinos["xscrollcommand"] = scr_lista_h.set
scr_lista_h.grid(row=9, column=0, padx=5, pady=(0,5), sticky="new")

lbl_alumnos = ttk.Label(contenedor, text="Alumnos: ")
lbl_alumnos.grid(row=7, column=1, padx=5, pady=5, sticky="w")

tbl_alumnos = ttk.Treeview(contenedor)
tbl_alumnos['columns'] = ["nombre","apellidos", "edad"]
tbl_alumnos["show"] = "headings"
tbl_alumnos["height"] = 5
tbl_alumnos.column("nombre", width=100, anchor="center")
tbl_alumnos.heading("nombre", text="NOMBRE")
tbl_alumnos.column("apellidos", width=100, anchor="center")
tbl_alumnos.heading("apellidos", text="APELLIDOS")
tbl_alumnos.column("edad", width=50, anchor="center")
tbl_alumnos.heading("edad", text="EDAD")

datos_alumno = []
for i in range(1,6):
    datos_alumno.append((f"Nom_alumno {i}", f"Apellido_alum {i}", (18+i)))

cont = 1
for fila in datos_alumno:
    id = tbl_alumnos.insert("", END, text=f"fila{cont}", values=fila, open=False)
    print(id)
    cont += 1

tbl_alumnos.grid(row=8, column=1, columnspan=2, padx=5, pady=(5,0), sticky="w")

ventana_raiz.mainloop()