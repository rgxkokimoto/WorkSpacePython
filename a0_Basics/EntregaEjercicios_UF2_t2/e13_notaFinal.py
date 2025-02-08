"""Ejercicio 13
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco
0. Imprime el resultado obtenido por el estudiante."""

# TODO 

cool = False 

while cool == False :
    nPreg = int(input("Cual es el número de preguntas del examen? :"))
    nRC = int(input("número de preguntas acertadas :"))
    nRX = int(input("número de preguntas falladas :"))
    nRB = int(input("número de preguntas acertadas :"))

    totalP = nRB + nRC + nRX

    if totalP <= nPreg :
        cool = True
        notaCool = nPreg * 5
        notaFinal = (nRC * 5) - nRX
        print(f"La nota final es {notaFinal}/{notaCool}")
    else :
        print("\nValla igual insertaste algun dato mal el número de preguntas totales"
            +"\n no coincide con el número de preguntas que introduciste...")
