archivo = open("b1-Ficheros/files/prubs.txt","r")

####################################################################################################
                    #* METODOS DEL PUNTERO  
####################################################################################################

'''
El puntero es esencial ya que indica en que linea o parte va a leer
#! no estoy seguro de si lee por lineas oh de otra forma ya que va con bytes
'''

#* .seek() Mueve el puntero hacia el byte indicado

#* .tell() Retorna la posición del puntero

####################################################################################################
                    #* METODOS PARA LEER  
####################################################################################################


'''archivo.seek(0)
print(archivo.read()) '''

'''
#* .read()
Lee todo el contenido de un archivo.
Si se le pasa la longitud de bytes,
leerá solo el contenido hasta la
longitud indicada.
#!es necesario poner el puntero en la ubicación 0 para leer todo.
'''

####################################################################################################
archivo.seek(0)
linea = archivo.readline()
while linea != "":
    print(linea)
    print(archivo.tell())
    linea = archivo.readline()

'''
#* .readline()
Lee una línea del archivo.
el puntero no funciona como piensas
el puntero no le la primera linea
es buena idea asignarle una variable a readline en bucles
#* muy necesario recorrer con un while
'''

####################################################################################################

#TODO a partir de aqui sin probar ##################################################################
#* .readlines()
'''
Lee todas las lineas de un archivo
'''

####################################################################################################

####################################################################################################
                    #* METODOS PARA Escribir  
####################################################################################################

####################################################################################################

# modos: r+ w a + y derivados

#* .WRITE() Escribe dentro del archivo

#* .WRITELINES(secuencia) 
'''
Secuencia será cualquier iterable
cuyos elementos serán escritos
uno por línea.
'''

archivo.close() #! Muy importante para quitar espacio en memoria


####################################################################################################
                #? PROPIEDADES DE LA CLASE FILE  
####################################################################################################

#? .closed retona verdadero si el archivo se cerro.

#? .retorna el modo de apertura

#? .name retorna el nombre del archivo

#? .encoding retorna la codificación de carcateres de una archivo  de texto