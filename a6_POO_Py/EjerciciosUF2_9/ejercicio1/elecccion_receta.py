def solicitar_num_recetas():
    dtaOk = False
    while not dtaOk:
        try: 
            num_recetas = int(input("Indica la cantidad de recetas que se van a introducir: "))
        
            if num_recetas < 0 or num_recetas > 10:
                raise ValueError
            else:
                dtaOk = True
        except:
            print("El valor introducido no es valido")

        return num_recetas
    
def solicitar_datos_recetas(i):
    nom = input("Introduce el nombre de la receta: " + i)

    num_pasos = solicitar_pasos() # TODO
        
def main():

    num_recetas = solicitar_num_recetas()

    lista_recetas = []

    for i in range(1, num_recetas + 1):
        lista_recetas.append(solicitar_datos_recetas(i))

main()