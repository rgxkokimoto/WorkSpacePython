"""
Ejercicio 12
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo
que determine la hora de llegada a la ciudad B.
"""

str_hs = input("Introduzca la hora de salida a en este formato: hor,min,seg"
      +"\n ejemplo 13,45,2"
      +"\nAhora tu!: ")
str_hs.strip()  # similar al trim()
tupStr_hs = str_hs.split(",")

hh = int(tupStr_hs[0])
mm = int(tupStr_hs[1])
ss = int(tupStr_hs[2])

t = int(input("Ahora introduce la hora de llegada en segundos: "))

# como calculamos esto?
# hh * 60 --> mm * 60 --> ss or hh * 3600 --> ss
# tiempo de llegada mas tiempo de salida
tll_s = ((hh * 3600) + (mm * 60) + 34) + t

# conversion de segundos a horas 
tm = divmod(tll_s,60)  # tupm = (minutos, segundos) pero claro sin hallar aun las horas 
th = divmod(tm[0],60)  # tuph (horas ,minutos)

# Literales de cadenas {} no te olvides de la f
print(f"LLegada a las --> {th[0]} Horas {th[1]} minutos y {tm[1]} segundos")

