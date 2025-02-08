from datetime import date 
import math 
import random
import statistics

# TODO ver

print(math.cos(math.pi / 4))

nums = ["uno", "dos", "tres" , "cutro", "cinco"]
print(random.choice(nums))
min = 10
max = 100
print(random.randrange(min,max + 1))

alturas = [1.2 ,2.3, 4.5, 5.6, 7.5]
print("Medias de alturas: ", statistics.median(alturas))

hoy = date.today()
print(hoy.strftime("%d-%m-%Y. %d %b %Y es %A. hoy es %d de %B."))

# XXX util sys.exit()