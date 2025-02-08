from tkinter import *
from tkinter import ttk

ventana_raiz = Tk()
ventana_raiz.title("Primera Ventana")
ventana_raiz.geometry("600x300")
ventana_raiz.maxsize(700,400) # Limites 
ventana_raiz.minsize(400,200) 

# Dentro de este contenendor veremos los primeros elementos
contenedores = ttk.Frame(ventana_raiz)
contenedores.pack()

#! Buena práctica recuerda poner el tipo al principio "lbl"
#* Pon el raton encima de la clase para ver las propiedades

lbl_etiqueta1 = ttk.Label(contenedores, text="Primera etiqueta")
lbl_etiqueta1.configure(font=("Arial", 18))
lbl_etiqueta1['foreground'] = "blue"

#! Para hacer textos variables tienes que usar esta clase y un atributo concreto es diferente a un label normal
text = StringVar()
text.set("Segunda etiqueta")
lbl_variable = ttk.Label(contenedores, textvariable=text)

# IMAGEN PhotoImage
img = PhotoImage(file= 'b2-Interfaces-Graficas/img/bicho.png', width= 300)
#Tetxto de la imagen
textoUe = StringVar()
textoUe.set("Universidad ladrona")
lbl_etiquetaImg  = ttk.Label(contenedores, image=img, textvariable=textoUe)

lbl_pwd = ttk.Label(contenedores, text="Nombre: ")
lbl_pwd.grid(row=2, column= 0, pady=5)

txt_pwd_valor = StringVar()
txt_pwd = ttk.Entry(contenedores, textvariable=txt_pwd_valor, show="*")

txt_texto_nom = StringVar()
txt_nombre = ttk.Entry(contenedores, textvariable=txt_texto_nom, cursor='hand2')
txt_nombre.focus()

def prueba():
    print('Contenido de txt_nombre: ' + str(txt_pwd.get()))

btn_prueba = ttk.Button(contenedores, text="Prueba", command=prueba)
btn_salir = ttk.Button(contenedores, text="Salir", command=lambda: ventana_raiz.quit())

# Posiciones
lbl_etiqueta1.grid(row=0,column=0, pady=5, columnspan=2)
lbl_etiquetaImg.grid(row=1,column=1, pady=5)
lbl_variable.grid(row=1,column=0, pady=5)
txt_pwd.grid(row=3, column=1, pady=5)
txt_nombre.grid(row=2, column=1, pady=5)

btn_prueba.grid(row=4, column=0, columnspan=1, pady=5)
btn_salir.grid(row=4, column=1, columnspan=1, pady=5)

ventana_raiz.mainloop()