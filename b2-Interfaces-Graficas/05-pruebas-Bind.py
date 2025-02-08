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

estilo_marco = ttk.Style()
estilo_marco.configure("TFrame", background="pink", relief="groove", bd="30",
padding="10")
contenedor = ttk.Frame(ventana_raiz, style="TFrame")
contenedor.pack(padx=5, pady=10)

stl_titulo = ttk.Style()
stl_titulo.configure("Titulo.TLabel", font=("Arial", 18), foreground="blue", background="pink",
relief="flat", bd="5")

lbl_titulo = ttk.Label(contenedor, text="Ventana de pruebas 3")
lbl_titulo['style'] = "Titulo.TLabel"
lbl_titulo.grid(row=0, column=0, columnspan=3,sticky='w')

lbl_datos = ttk.Label(contenedor, text="Datos:")
lbl_datos.grid(row=1, column=0, pady=5)


def validar(d, i, P, s, S, v, V, W):
    txta_result_val.delete("1.0", "end")
    txta_result_val.insert("end","OnValidate:\n")
    txta_result_val.insert("end","d='%s'\n" % d)
    txta_result_val.insert("end","i='%s'\n" % i)
    txta_result_val.insert("end","P='%s'\n" % P)
    txta_result_val.insert("end","s='%s'\n" % s)
    txta_result_val.insert("end","S='%s'\n" % S)
    txta_result_val.insert("end","v='%s'\n" % v)
    txta_result_val.insert("end","V='%s'\n" % V)
    txta_result_val.insert("end","W='%s'\n" % W)
 
    # No permite lo que no esté en minúsculas
    if S == S.lower():
        return True
    else:
        messagebox.showinfo("Error de datos", "La caja de texto no se admite mayúsculas")
        return False
 

txt_texto_datos = StringVar()
vcmd = (ventana_raiz.register(validar),'%d', '%i', '%P', '%s', '%S', '%v', '%V',
'%W')
txt_datos = ttk.Entry(contenedor,textvariable=txt_texto_datos,cursor='hand2', validate="key", validatecommand=vcmd)
txt_datos.grid(row=1,column=2,padx=5 , pady=5)
txt_datos.focus

btn_prueba = ttk.Button(contenedor, text="Prueba")
btn_prueba.grid(row=2, column=0,padx=5 ,pady=5)

btn_prueba2 = ttk.Button(contenedor, text="Prueba")
btn_prueba2.grid(row=2, column=1,padx=5 ,pady=5)

def raton(event):
    text_resultados.set("Se ha pulsado el botton del ratón" + str(txt_texto_datos.get() + str(event.x) + str(event.y)))

def raton2(event):
    text_resultados.set("Se ha pulsado el botton 2 ;O")

def tecla(event):
    text_resultados.set("Se ha pulsado el enter teniendo el botton el foco")

def tecla_txt(event):
    text_resultados.set("Se ha pulsado el enter teniendo la caja de texto el foco " + str(txt_texto_datos.get()))

btn_prueba.bind('<ButtonPress>', raton)
btn_prueba.bind('<Return>', tecla) # pulsar enter

btn_prueba2.bind('<ButtonPress>', raton2)

txt_datos.bind('<Return>', tecla_txt)

# KeyPress

text_resultados = StringVar()
lbl_resultados  = ttk.Label(contenedor, textvariable=text_resultados)
lbl_resultados.grid(row=3, column=0, padx=5, pady=5)

text_result_val = StringVar()
txta_result_val = Text(contenedor,height=10, width=40)
txta_result_val.grid(row=4 , column=0, columnspan=2, padx=5, pady=5)

ventana_raiz.mainloop()