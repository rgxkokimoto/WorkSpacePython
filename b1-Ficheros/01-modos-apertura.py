

'''Python nos permite trabajar en dos niveles diferentes con respecto al sistema de
archivos y directorios.
Uno de ellos, es a través del módulo os, que como su nombre indica, nos facilita el
trabajo con todo el sistema de archivos y directorios, a nivel del Sistema Operativo.

El segundo nivel, más simple, es el que nos permite trabajar con archivos, manipulando
su lectura y escritura a nivel de la aplicación y tratando a cada archivo como un objeto.
'''

####################################################################################################
#* LEER UN FICHERO CON LA CLASE FILE
####################################################################################################

'''Para asignar a una variable un valor de tipo file, solo es necesario recurrir a la función
integrada open(), la cual está destinada a la apertura de un archivo.'''

#! Cuidado en mi caso la ruta se escribe con '/'
fichero = open("b1-Ficheros/files/prubs.txt", "r")

'''La función integrada open(), recibe dos parámetros:
- El primero es la ruta hacia el archivo que se desea abrir
- Y el segundo, el modo en el cual abrirlo'''

####################################################################################################
#* MODOS DE APERTURA
####################################################################################################

# | Código | Modo de apertura | Ubicación del puntero |
# |--------|------------------|-----------------------|
# | 'r'     | Lectura          | Al principio del archivo |
# | 'w'     | Escritura (sobreescribe) | Al principio del archivo |
# | 'x'     | Escritura        | Al principio del archivo (crea nuevo, falla si existe) |
# | 'a'     | Añadir contenido | Al final del archivo si exite el archivo sino `crea el archivo y lee al cominezo |
# | 'b'     | Binario          | Depende del modo (por ejemplo, 'rb' o 'wb') |
# | 't'     | Texto (default)  | Al principio del archivo |
# | '+'     | Lectura y escritura | Depende del modo (por ejemplo, 'r+', 'w+', 'a+') |
#! Luego puedes hacer las convinaciones que veas 
#! lo importante es tener en cuenta como se va a comportar el puntero