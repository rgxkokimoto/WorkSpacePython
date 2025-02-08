import random as r

pais_dic = {
"Albania":"Tirana",
"Alemania":"Berlín",
"Austria":"Viena",
"Bélgica":"Bruselas",
"Bosnia y Herzegovina":"Sarajevo",
"Bulgaria":"Sofía",
"Croacia":"Zagreb",
"Dinamarca":"Copenhague",
"Eslovaquia":"Bratislava",
"Eslovenia":"Liubliana",
"España":"Madrid",
"Estonia":"Tallín",
"Finlandia":"Helsinki",
"Francia":"París",
"Grecia":"Atenas",
"Hungría":"Budapest",
"Irlanda":"Dublín",
"Islandia":"Reikiavik",
"Italia":"Roma",
"Letonia":"Riga",
"Lituania":"Vilna",
"Luxemburgo":"Luxemburgo",
"Malta":"La Valeta",
"Moldavia":"Chisinau",
"Montenegro":"Podgorica",
"Noruega":"Oslo",
"Países Bajos":"Ámsterdam",
"Polonia":"Varsovia",
"Portugal":"Lisboa",
"Reino Unido":"Londres",
"República Checa":"Praga",
"Rumanía":"Bucarest",
"Serbia":"Belgrado",
"Suecia":"Estocolmo",
"Suiza":"Berna",
"Ucrania":"Kiev"}

contryAlea_dic = {
1:"Albania",
2:"Alemania",
3:"Austria",
4:"Bélgica",
5:"Bosnia y Herzegovina",
6:"Bulgaria",
7:"Croacia",
8:"Dinamarca",
9:"Eslovaquia",
10:"Eslovenia",
11:"España",
12:"Estonia",
19:"Italia",
20:"Letonia",
21:"Lituania",
22:"Luxemburgo",
23:"Malta",
24:"Moldavia",
25:"Montenegro",
26:"Noruega",
27:"Países Bajos",
28:"Polonia",
29:"Portugal",
30:"Reino Unido",
13:"Finlandia",
14:"Francia",
15:"Grecia",
16:"Hungría",
17:"Irlanda",
18:"Islandia",
31:"República Checa",
33:"Serbia",
34:"Suecia",
35:"Suiza",
36:"Ucrania"
}

# XXX
'''
El programa deberá generar 10 números aleatorios distintos entre 1 y el 36.
Para cada aleatorio generado se preguntará por la capital del país correspondiente.
El usuario deberá introducir la capital.
El programa le deberá decir si es correcta o no, y tras preguntarle por 10 países
deberá decir la nota obtenida sumando un punto por cada capital acertada y
restando 0.2 por cada capital fallada.'''

def generar_alea():
    num = r.randint(1,36)
    return num

def preg_capital():
    
    nr = generar_alea()
    contry = contryAlea_dic.get(nr)
        
    inp_capy = input(f"\nIndica la capital de {contry}? ").strip().capitalize()
    reps_good = pais_dic.get(contry)

    if reps_good != inp_capy:
        print(f"\n¡No es correcto! La capital de {contry} es {reps_good}")
        return -0.2
    else:
        print(f"\nCorrecto!")
        return + 1
        

def main():

    result = 0
    c_correct = 0
    for i in range(0,10):
        accert = preg_capital()
        result += accert
        if accert == 1:
            c_correct += 1
        

    print(f"Has contestado correctamente {c_correct} capitales,\n obtienes una puntuación de {result:.2f}")

main()

# EJERCICIO 2 

