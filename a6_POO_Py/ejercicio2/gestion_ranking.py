import clase_lenguaje as len
import sys



"""Crea un módulo gestión_ranking en el paquete ejercicio2, en el que:

- Almacene en una lista los 7 primeros lenguajes del ranking.
- Para cada lenguaje se solicitarán los datos necesarios por teclado.
- Y cuando se haya acabado de introducir lenguajes, muestre los datos de los 
lenguajes para poder comprobar el resultado. Para cada lenguaje muestre
además, el porcentaje de uso de hace un año.
- El programa deberá informar de cuántos lenguajes han perdido porcentaje,
 cuántos han ganado y cuál es el más usado.
 """

#TODO hacer un módulo para corregir excepciónes
def correctString(inp):
    st = ""
    while st.strip() == "":
      try:
        st = input(inp)
        assert st.strip() != ""
      except AssertionError:
        print("Porfavor no deje este campo vacio: ")
    return st

def correctYear(inp):
   isOk = False
   year = -1
   while not isOk:
      try:
         year = int(input(inp))
         assert year > 0 # XXX las condiciónes de assert funcionan si es True 
         isOk = True
      except ValueError:
         print("Introduzca un valor entero numerico")
      except AssertionError:
         print("El valor no puede ser negativo")

def correctPorc(inp):
   isOk = False
   year = -1
   while not isOk:
      try:
         year = float(input(inp)) 
         assert year < 0
         isOk = True
      except ValueError:
         print("Introduzca un valor numerico valido ")

def correctPorc(inp): # XXX
   isOk = False
   year = -1
   while not isOk:
      try:
         year = float(input(inp)) 
         isOk = True

      except ValueError:
         print("Introduzca un valor numerico valido ")
         

def solicitarDta():
    name = correctString("Introduce el nombre del lenguaje: ")
    creador = correctString("Introduzca el nombre del creador: ")
    anio = correctYear(f"Introduce el año en el que se creo {name}: ")
    porc = correctPorc("Introduce el porcentaje de uso: ")
    diff = correctPorc("Introduce la diferencia de uso: ")

    lenguaje = len.Lenguaje(name,creador,anio,porc,diff)
    return lenguaje
    

# Pruebas inserción 
"""l1 = len.Lenguaje("C", "Dennis Ritchie", 1978, 9.01, -2.76)
l2 = len.Lenguaje("Python", "Guido Van Rossum", 1991, 22.85, 8.69)
l3 = len.Lenguaje("C++", "Bjarne Stroustrup", 1983, 10.64, 0.29)"""

ls_lenguajes = []
for i in range(7):
    ls_lenguajes.append(solicitarDta())
    

print("Ranking de lenguajes más usados:")
print("===============================")

maxObj = len.Lenguaje("model","model",0,-999,-999)
for lenguaje in ls_lenguajes:
   print(lenguaje)
   print(f"Porcentaje del año pasado: {lenguaje.getLastYear()}%")
   if lenguaje.diff < 0:
      print("Este lenguaje a bajado respecto al año pasado")
   else:
      print("Este lenguaje a subido respecto al año pasado")
   if lenguaje.porc > maxObj.porc:
      maxObj = lenguaje
   print("=================")
   
print("El lenguaje más usado a sido: ",maxObj.nombre)


# Cuidado con el assert puedes usar r#dh56 con un if

# Refectoriza con metodos y crea un main

# dicionarios