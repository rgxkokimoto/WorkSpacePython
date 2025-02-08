# XXX de UF2.10 Clase_File.docx
####################################################################################################
                    #* PRUEBAS DEL AULA 
####################################################################################################

def leer(fichero):
    contenido = fichero.read()
    print("LEER FICHERO:")
    print(contenido)

def leerPorLineas(fichero):

    print("## LEER POR LINEAS ##")
    linea = fichero.readline()
    cont = 1

    while linea != "":
        print("# Linea " + str(cont) + ":", end="")
        print(linea)
        linea = fichero.readline()
        cont += 1

    #* Hecho por la cuenta de la vieja 
    '''print("## CONTENIDO DEL FICHERO ###")
    print(" LINEA 1", end=" ")
    linea = fichero.readline()
    print(linea)

    print("# LINEA 2", end=" ")
    linea = fichero.readline()
    print(linea)

    print("# LINEA 3", end=" ")
    linea = fichero.readline()
    print(linea)'''

def solicitarCadena(m):
    valido = False
    cadena = ""

    while not valido:

        cadena = input(m)

        if len(cadena) == 0:
            print("El valor no puede estar vacio")
        else:
            valido = True

    return cadena

def escribir (fichero):
    cadena = solicitarCadena("Introduce una cadena ")
    fichero.write("\n" + cadena)

def escribir_lineas(fichero):
    lista = ['\nProbando 1', '\nLínea 2']
    fichero.writelines(lista) # No salta de línea pon tu \n

def main ():
    #* El modo de apertura A posiciona el cursor al final del fichero si existe sino al principio
    #* El modo apertura R y W posicionan el cursor.
    fichero = open("b1-Ficheros/files/fichero.txt",'a+') # añadir y leer al final del archivo si existe

    # escribir(fichero)

    escribir_lineas(fichero)

    fichero.seek(0) #* Cuidao con los punteros sobretodo al escribir o leer algo 

    leer(fichero)

    posicion_puntero = fichero.tell()
    print(posicion_puntero)

    fichero.seek(0)

    leerPorLineas(fichero)

    if not fichero.closed:
        fichero.close() #! Recuerda esto 

main()

