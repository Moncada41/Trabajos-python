x = input("¿Eres chico, chica u otro?")
w = "Bienvenid"
if x =="chico": 
    w +='o'
elif x== "chica":
    w += 'a'
else: 
    w += 'e'
print (w, "al mundo de los pokemon!")

y = input("¿Qué edad tienes?")
if int(y)<10:
    if x== "chico":
        print("No tienes edad", 
              "para ser entrenador")
    elif x== "chica":
        print ("No tienes edad" , 
               "para ser entrenadora")
    else:
        print ("No tienes edad" , 
               "para ser entrenadore")
    quit()
if int(y)>9:
    if x== "chico":
        print("Tienes la edad perfecta", 
              "para ser entrenador")
    elif x== "chica":
        print ("Tienes la edad perfecta" , 
               "para ser entrenadora")
    else:
        print ("Tienes la edad perfecta" , 
               "para ser entrenadore")
if int(y)>99:
    if x== "chico":
        print("Ya estás muy viejo para esto")
    elif x== "chica":
        print ("Ya estás muy vieja para esto")
    else:
        print ("Ya estás muy vieje para esto")
    quit()
    
reg =input("Necesitarás un compañero de viaje para esta aventura! ¿En qué región te encuentras: Catia o Petare?")
if reg == "catia":
        if x == "chico":
            print ("Tu compañero de viaje es John F. Kennedy!")
        if x== "chica":
            print ("Tu compañera es Maria Corina Machado!")
        elif x == "otro":
            print ("Tu compañere es Sherk!")    
if reg == "petare":
        if x == "chico":
            print ("Tu compañero de viaje es Chavez!")
        if x== "chica":
            print ("Tu compañera es Cilia Flores!")
        elif x == "otro":
            print ("Tu compañere es Sherk!") 

tipo = input("¿Con qué tipo de pokemon quieres empezar?")
if tipo == "agua":
        print("Tu pokemon es Makoa: una tortuga con traumatismo encefalocraneano")
elif tipo == "fuego":
        print("Tu pokemon es Furia: un lagarto que carece de extremidades")
elif tipo == "planta":
        print("Tu pokemon es Bob Marley: un pana que es marihuano")
else:
    print("Esa no es una clase de pokemon, aprende a escribir") and quit()
print("Una vez elegido tu pokemon," , 
            "ya estás listo para adentrarte en este emocionante mundo de las batallas ilegales de seres en peligro de extinción")
com =input("¿Estás listo para empezar?")
if com == "si":
    print ("Dale pa'lante mi pana")
else:
    print("Esa no es la respuesta que esperaba") and quit()


import random 

#batalla

PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_jugador>0 and PS_oponente>0:
    ataque_jugador = input("Ataque")
    while not ataque_jugador: ""
    if ataque_jugador == "malicioso":
        defensa_oponente -= 10
        ataque_jugador = ""
    elif ataque_jugador == "placaje":
        defensa_oponente -= 35 / defensa_oponente/100
        ataque_jugador = ""
    elif ataque_jugador == "ascuas":
        defensa_oponente -= 20
        ataque_jugador = ""
    else:
        print("Qué estás haciendo? Tus ataques son" ,
                  "malicioso, placaje y ascuas")
            
#el jugador ha atacado, ahora le toca al oponente

    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador -= 10
    elif ataque_oponente == 2:
        PS_jugador -= 35 / defensa_jugador/100
    elif ataque_oponente == 3:
        PS_jugador -= 40
        
#la batalla ha terminado

if PS_oponente <= 0 and PS_jugador <= 0:
    print("Empate")
elif PS_oponente <= 0:
    print("Felicidades, has ganado")
elif PS_jugador <=0:
    print("Lo siento, has perdido")
    