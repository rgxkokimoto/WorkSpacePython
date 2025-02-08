import clase_proposito as cp


'''Se solicite la cantidad de propósitos que se van a introducir.
• Almacene en una lista la información de los propósitos, de manera que,
para cada propósito se solicitarán los datos necesarios.
• Y cuando se haya acabado de introducir los propósitos, muestre los
datos almacenados.
• El programa deberá informar de cuántos propósitos hay de cada tipo y
cuántos tienen prioridad alta.
• Mostrar el propósito de Salud con mayor prioridad.'''

def correctInt(inp):
   isOk = False
   num = -1
   while not isOk:
      try:
         num = int(input(inp))
         assert num >= 0 # XXX las condiciónes de assert funcionan si es True 
         isOk = True
         return int(num)
      except ValueError:
         print("Introduzca un valor entero numérico")
      except AssertionError:
         print("El valor no puede ser negativo ni 0")

def correctDes(int):
   isOk = False 
   
   while not isOk:
      try: 
        des = input(int)

        assert len(des.strip().split(" ")) >= 3
        
        if len(des) == 0:
            raise ValueError
        else: 
           return des
      except ValueError:
        print("La descripcion no puede estar vacia: ")
      except AssertionError:
         print("la cadena debe contener por lo menos 3 palabras")

def correctRange(inp):
    isOk = False 
    while not isOk:
        try: 
            num = int(input(inp))
            if num not in range(1,6): # jaja se puede hacer esto ;)
                raise IndexError
            isOk = True
            return num 
        except IndexError:
            print("El numero esta fuera de rango")
        except ValueError:
            print("Introduzca un numero")

def solic_prop():
    des = correctDes("Introduce una descripción valida que no este vacia: ")
    clasi = correctRange("introduce una  clasificación valida del rango 1-5 :  la clasificación: Salud-1, Amigos-2, \nFamilia-3, Viajes-4, Deporte o Trabajo-5: ")
    prio  = correctRange("introduce una  prioridad valida del rango 1-5:  ")
    p = cp.Proposito(des,clasi,prio)
    return p
    
def dataAnalisis(lista_propositos):
   
   c_pri_alta = 0
   c_S = 0
   c_A = 0
   c_F = 0
   c_V = 0
   c_D = 0


   maxObj_Salud = cp.Proposito("Ir a Budapest antes de septiembre del 2025",1,-1)
   for p in lista_propositos:
      
      if p.clasificacion == 1 and p.prioridad > maxObj_Salud.prioridad:
         maxObj_Salud = p
      
      if p.prioridad == 5:
         c_pri_alta += 1
      
      if p.clasificacion == 1:
         c_S += 1
      elif p.clasificacion == 2:  
         c_A += 1
      elif p.clasificacion == 3:  
         c_F += 1
      elif p.clasificacion == 4:  
         c_V += 1
      elif p.clasificacion == 5:  
         c_D += 1

      
      
    
   print(f"\nhay {c_pri_alta} propositos con la prioridad mas alta") # XXX
   print(f"hay {c_S} propositos en la categoria de salud")
   print(f"hay {c_A} propositos en la categoria de amigos")
   print(f"hay {c_F} propositos en la categoria de familia")
   print(f"hay {c_V} propositos en la categoria de viajes")
   print(f"hay {c_D} propositos en la categoria de trabajo")

   if maxObj_Salud.prioridad != -1:
      print("\nEl objeto de tipo salud con la prioridad mas alta fue:\n")
      print(maxObj_Salud)
   
def main():
    n_prop = correctInt("introduzca el número de propositos que desea introducir: ")
    ls_prop = []
    
    for i in range (0,n_prop):
        ls_prop.append(solic_prop())
    
    for i in range (0,n_prop):
      print("\n===============================")
      print(ls_prop[i])
      print("===============================")
    
    '''p = cp.Proposito("Ir a Budapest antes de septiembre del 2025",1,4)
    p2 = cp.Proposito("Aprender a hacer meditación antes",1,3)
    p3 = cp.Proposito("Dominar el lenguaje de python antes de febrero de 2025",1,5)

    ls_prop.append(p)
    ls_prop.append(p2)
    ls_prop.append(p3)'''

    dataAnalisis(ls_prop)

main()

