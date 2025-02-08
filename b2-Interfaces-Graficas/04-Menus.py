from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana_raiz = Tk()
ventana_raiz.title("Widjects 2")
ventana_raiz.geometry("600x600")
ventana_raiz.maxsize(600,600) # Limites 
ventana_raiz.minsize(400,300)

barra_menu = Menu(ventana_raiz)
ventana_raiz.config(menu=barra_menu)
ventana_raiz.option_add('*tearOff',FALSE)

opc_menu1 = Menu(barra_menu)
barra_menu.add_cascade(menu=opc_menu1, label='Tecto opción menú 1')

def opcion11():
    messagebox.showinfo("Opcion 1")


def opcion12():
    messagebox.showinfo("Opcion 2")

opc_menu1.add_command(label='Opcion menu1.1 ', command=opcion11)
opc_menu1.add_command(label='Opcion menu1.2 ', command=opcion12)

ventana_raiz.mainloop()

