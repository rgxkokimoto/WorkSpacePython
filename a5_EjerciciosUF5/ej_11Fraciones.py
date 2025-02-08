import funcsfracionesej11.fun_Frac as fm

'''
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente.
Salir
'''

menu = """\nIntroduce una Opción: " 
  1. Sumar dos fraciones: "
  2. Restar dos fraciones: "
  3. Dividir dos fraciones: "
  4. Mutiplicar dos fraciones: "
  5. Salir \n"""

opc = ""

while opc != "5":
    
    opc = input(menu)
    fl = []
    #fl.clear()
    match opc:
        case "1":
            for _ in range(0,2):
               fl += fm.leer_frac()
            fl = fm.sum_frac(fl)
            fl = fm.simp_frac(fl)
            fm.print_frac(fl)
        case "2":
            for _ in range(0,2):
               fl += fm.leer_frac()
            fl = fm.res_frac(fl)
            fl = fm.simp_frac(fl)
            fm.print_frac(fl)
        case "3":
            for _ in range(0,2):
               fl += fm.leer_frac()
            fl = fm.mult_frac(fl)
            fl = fm.simp_frac(fl)
            fm.print_frac(fl)
        case "4":
            for _ in range(0,2):
               fl += fm.leer_frac()
            fl = fm.div_frac(fl)
            fl = fm.simp_frac(fl)
            fm.print_frac(fl)
        case "5":
            print("Saliendo del programa...")
        case _:
            print(f"\nEl valor '{opc}'  no es valido")