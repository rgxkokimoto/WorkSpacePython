"""
Ejercicio 14
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos
o 10 céntimos)
""" 





miMoney = input("Introduce el número de monedas que tengas de: "
                    +"\n2€"
                    +"\n1€"
                    +"\n50 centimos"
                    +"\n20 centimos"
                    +"\n10 centimos"
                    +"\n Introduce EL NÚMERO de monedas de cada tipo en el orden que te he dado" 
                    +"\nasi: 2€,1€,50c,20c,10c"
                    +"\nEjemplo: 2,3,4,5,6,"
                    +"\nAhora tu! escribe aqui: " 
                )

miMoney.strip()
listM = miMoney.split(",")

# Intente esto y no me fue muy bien 
"""for i in listM: 
    listM[float(i)]"""

total = float(listM[0]) * 2 + float(listM[1]) * 1 + float(listM[2]) * 0.50 + float(listM[3]) * 0.20 + float(listM[4]) * 0.10
print("\nTienes un total de: ",total,"€")
