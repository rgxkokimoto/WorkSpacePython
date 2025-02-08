DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

cool = False

while not cool: # cool == False
    u = int(input("Introduce un número del mes: "))

    if u >= 13 or u <= 0 :
        print("Introduce un dia del mes valido entre 1-12")
    else:
        u -= 1
        print(f"{MESES[u]} tiene {DIAS_MES[u]} dias")
        cool = True