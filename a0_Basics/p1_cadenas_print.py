# Cadenas

cadena = "Esto es una cadena"
cadena2 = 'Esto tambien esta bien'
cadena_multyLine = """ """
""" esta es una cadena con mas de una linea """
' esta es una cadena con mas de una linea '


# Cadenas con formatos literales
num2 = 2
print(f"Hola 2 + {num2} es {2 + 2}") 


#Formatos por consolas 
n3 = 3
n4 = 12
print(f'{n3:8} - {n4:6d}') # el prefijo d es para poner espacios por delante
print(f'{n3:4}')
print(f'{n3:5d}')  

# XXX que útil 
dec45 = 1.254435
print(f"{dec45:.2f}") # impresion con redondeo