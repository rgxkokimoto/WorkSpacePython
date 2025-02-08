from tkinter import *
from tkinter import ttk 

ventana_raiz = Tk()
contenedor = ttk.Frame(ventana_raiz)

# Configuración de a ventana 

ventana_raiz.title("Primera Ventana")
ventana_raiz.geometry("400x200")

ventana_raiz.maxsize(600,200) # Limites 
ventana_raiz.minsize(300,100) 

ventana_raiz.configure(background="white")

# Contenedores 
cont = ttk.Frame(ventana_raiz, width=350, height=150)
# cont.pack( anchor='se') #! No vamos a usarlo ;)
# cont.place(relx=0.5 , rely=0.5, anchor="center") # Funciona con cordenadas #* Es Responsive :)))
# cont.grid(row=0,column=0, sticky=S) #! funciona con varios componentes

cont.grid()

marco_rojo = Frame(cont)
marco_rojo.grid(row=0,column=0)
marco_rojo.configure(width="200", height="100", bg="pink")

marco_rojo = Frame(cont)
marco_rojo.grid(row=0,column=1)
marco_rojo.configure(width="200", height="100", bg="yellow")

marco_rojo = Frame(cont)
marco_rojo.grid(row=0,column=2)
marco_rojo.configure(width="200", height="100", bg="red")

marco_rojo = Frame(cont)
marco_rojo.grid(row=1,column=0)
marco_rojo.configure(width="200", height="100", bg="blue")

marco_rojo = Frame(cont)
marco_rojo.grid(row=1,column=2)
marco_rojo.configure(width="200", height="100", bg="green")

####################################################################################################
                    #* COMPONENTES 
####################################################################################################



# Hilo principal de la ventana Ejecuta la ventana 
ventana_raiz.mainloop()