"""Ejercicio 11
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número
invertido. Ejemplo, si se introduce 23 que muestre 32."""

cool = False 
while cool == False :
    n2c = int(input("Introduce un numero de dos cifras: "))
    if n2c < 10 or n2c > 99:
        print("El número no es de 2 cifras")
    else :
        cool = True
        if n2c % 10 == 0 :  # en caso de que el numero sea 10,30,20
            n20 = (n2c/10)
            print("0"+str(int(n20)))
        else :
            tN2c = divmod(n2c,10)  # devuelve justo lo que queremos
            print(tN2c[1] * 10 + tN2c[0])