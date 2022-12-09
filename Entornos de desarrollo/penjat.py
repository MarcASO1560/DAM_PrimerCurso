import random #per a generar un nombre aleatoriament
import time #per a generar un nombre aleatoriament

#inicialitzacio de variables

#variable per emmagatzemar les paraules
paraules = ["formiga", "moix", "elefant", "cavall", "cocodril", "jaguar", "hipopotam", "pantera", "tigre"]
#variable per controlar quines lletres ens han encertat
trobada = []
#num. maxim d'intents
maxintents = 7
#num. intents que ha fet servir l'usari en la partida
numintents = 0
#paraula triada a l'atzar que l'usuari a d'endevinar
paraula = 0
#si la paraula ha estat encertada ja
encertada = False
#lletra que ficara l'usuari
lletra = ""
#si s'ha trobat la lletra (serveix per controlar el nombre d'intents)
lletratrobada = False
#contant el nombre de lletres encertades control si has guanyat
#has guanyat si: numencertades == total lletre paraula
numencertades = 0
#variables per fer servir d'index en bucles
i = 0

#inicialitzacio de la llavor que genera nombres aleatoris
random.seed(time.time())

#trii una paraula a l'atzar
paraula = random.randint(0, len(paraules) - 1) 

#inicialitzacio de la variable trobada a false
#segons la paraula triada a l'atzar (llista
#amb tants de False com lletres tengui la paraula,
#aquests False es posaran a True quan l'usuari
#encerti la lletra)
for i in range(len(paraules[paraula])):
    trobada += [False]

while not encertada and numintents < maxintents:
    #esborrar la pantalla
    #se podria fer sense esborrar i tornant a escriure el text
    #os.system("clear") # windows: os.system("cls")
    
    #imprimir lletres o - segons estigui encertada
    #la lletra o no
    i = 0
    while i < len(paraules[paraula]):
        if trobada[i]:
            print (paraules[paraula][i]),
        else:
            print ("-"),
        i += 1
    
    #imprimir nombre d'intents
    print ("\nNum. intents: %d ") % numintents
    
    lletra = str(raw_input("Introdueixi una lletra: "))
    
    lletratrobada = False
    
    for i in range(len(paraules[paraula])):
        if not trobada[i] and paraules[paraula][i] == lletra:
            trobada[i] = True
            lletratrobada = True
            numencertades += 1
    
    if not lletratrobada:
        numintents = numintents + 1
        
    if numencertades == len(paraules[paraula]):
        encertada = True
 
if encertada:
    print ("Enhorabona! Has guanyat")
else:
    print ("Has perdut. La paraula era: %s" % paraules[paraula])
