'''
Ejercicio 4
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la
cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los
datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada
consulta el programa nos preguntará si queremos hacer otra consulta.
'''

diFrut = {'melon' : 5.3 , 'pera' : 4.0 , 'piña' : 6.5}

# TODO

fin = False 
while fin == False:
    frut = input("Introduce el nombre de la Fruta: ")
    cant = int(input("Cuanta cantidad se vendio: "))
    frut.lower
    
    if diFrut.get(frut) != None:
        print(f"Precio final {frut}: {diFrut[frut] * cant}")
    else: 
        print("La Frtua",frut,"no esta guardada en el diccionario")
    

    rep = input("\nDesea realizar otra consulta pulse r para repetir y cualquier tecla para finalizar ")
    if rep != 'r':
        fin = True


    