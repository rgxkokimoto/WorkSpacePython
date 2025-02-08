


'''
leer_fracción: La tarea de esta función es leer por teclado el numerador 
y el denominador. Cuando leas una fracción debes simplificarla.
'''

#El pep8 recomienda que si la condición es muy grande 

def leer_frac():
    lista = []
    isvalid = False
    while not isvalid:
        f = input("Introduce una Fracción: ej: 1/2 -> ").strip() # el operador in es muy util para controlar entradas 
        if (
            # TODO prueba hacer con el modulo format # TODO oh con partition
            f.replace("/","").isdigit() # que no contenga letras
            and "0" not in f # que no contega 0
            and f.count("/") == 1 # que no halla mas de 1 /
            and not f.startswith("/") # que no empieze ni acabe con /
            and not f.endswith("/")
            ):       
            lista += f.split("/") # te retorna  una lista en orden el denominador y el # TODO prueba a hacer con tupla
            return lista
        else:
            print("Porfavor introduce un valor válido n/d Fración con numerador y denominador")

leer_frac()

'''
escribir_fracción: Esta función escribe en pantalla la fracción. 
Si el dominador es 1, se muestra sólo el numerador.
'''
def print_frac(lista):
    n = str(lista[0])
    d = str(lista[1])
    if d == '1' or n == d:
        print("1")
    else:
        print("\nEl resultado de esta Operación es: ",n+'/'+d) 

#escribir_Fracion(leer_fraccion())
    
# TODO duda este metodo tambien se puede hacer dividiendo pero 
# que es mas eficiente oh a nivel de procesamiento es lo mismo?
'''
while b != 0:
    a, b = b, a % b
return a
'''

'''
calcular_mcd: Esta función recibe dos números y devuelve el máximo común divisor.
simplificar_fraccion: Esta función simplifica la fracción, para ello 
hay que dividir numerador y dominador por el MCD del numerador y denominador.
'''
def mcd(a,b):
    save = 0 

    if a < b: # Es necesario ordenar al mayor con el menor me gusta esto!
        save = b
        b = a 
        a = save
    
    res = 1
    while a - b != 0:

        if a < b: 
            save = b
            b = a 
            a = save

        res = a - b
        a = res
    
    return res 
    
'''
Queremos encontrar el mínimo comun multiplo 
para poder simplificar una fración
Algoritmo de Euclides 
casos de prueba: 

#reglas del algoritmo 
el número más grande se resta con el menor 
el menor se convierte en el mayor
el  resultado entre la resta se convierte en el menor 
si la resta es 0 menor se acaba.

18,24 = 6
14, 21 = 7
13 , 7 = 1
mcd(48,180) = 12
'''


'''
Esta función simplifica la fracción, para ello 
hay que dividir numerador y dominador por el MCD del numerador y denominador.'''
def simp_frac(li):
    n, d = int(li[0]), int(li[1])# XXX el Pep8 acepta este formato de asignación siempre y cuando el número no sea    
    # de variables no sea muy elevado pero si no te mola me comentas. 
    m = mcd(n,d)
    li[0] = int(n/m)
    li[1] = int(d/m)
    return li

# escribir_Fracion(simplificar_fraccion(leer_fraccion()))  
# TODO hacer un metodo que permita varias funciones en una sola entrada

def sum_frac(li4):
    n1, d1, n2, d2 = int(li4[0]), int(li4[1]), int(li4[2]), int(li4[3])

    nf = n1 * d2 + d1 * n2
    df = d1 * d2

    frac = [nf,df]
    simp_frac(frac)
    return frac

li = []
'''for i in range(0,2):
    li += leer_fraccion()
sumar_fracciones(li)'''

'''
restar_fracciones: Función que resta dos fracciones: 
numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
'''

def res_frac(li4):
    n1, d1, n2, d2 = int(li4[0]), int(li4[1]), int(li4[2]), int(li4[3])

    nf = n1 * d2 - d1 * n2 # TODO unir los dos métodos en uno
    df = d1 * d2

    frac = [nf,df]
    simp_frac(frac)
    return frac

'''for i in range(0,2):
    li += leer_fraccion()
restar_fraciones(li)'''


'''
multiplicar_fracciones: Función que recibe dos fracciones y 
calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar 
la fracción resultado.
'''
def mult_frac(li4):
    n1, d1, n2, d2 = int(li4[0]), int(li4[1]), int(li4[2]), int(li4[3])

    nf = n1 * n2
    df = d1 * d2

    frac = [nf,df]
    simp_frac(frac)
    return frac


'''
dividir_fracciones: Función que recibe dos fracciones y 
calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar 
la fracción resultado.
'''

def div_frac(li4):
    n1, d1, n2, d2 = int(li4[0]), int(li4[1]), int(li4[2]), int(li4[3])

    nf = n1 * d2
    df = d1 * n2

    frac = [nf,df]
    simp_frac(frac)
    return frac


'''for i in range(0,2):
    li += leer_frac()
div_frac(li)'''

