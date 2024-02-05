x = input("¿Eres chico, chica u otro? ")
w = "Bienvenid"
if x =="chico": 
    w +='o'
elif x== "chica":
    w += 'a'
else: 
    w += 'e'
print (w, "al mundo de los pokemon!")

y = input("¿Qué edad tienes? ")
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
    
reg =input("Necesitarás un compañero de viaje para esta aventura! ¿En qué región te encuentras: Catia o Petare? ")
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
            

tipo = input("¿Con qué tipo de pokemon quieres empezar? Puedes elegir de tipo fuego, agua o planta: ")
if tipo == "agua":
        print("Tu pokemon es Makoa: una tortuga con traumatismo encefalocraneano")
elif tipo == "fuego":
    print("Tu pokemon es Furia: un lagarto que carece de extremidades")
elif tipo == "planta":
    print("Tu pokemon es Bob Marley: un pana que es marihuano")
else:
    print("Esa no es una clase de pokemon, aprende a escribir")
        
print("Una vez elegido tu pokemon," , 
            "ya estás listo para adentrarte en este emocionante mundo de las batallas ilegales de seres en peligro de extinción")
com =input("¿Estás listo para empezar? ")
if com == "si":
    print ("Dale pa'lante mi pana")
else:
    print("Esa no es la respuesta que esperaba") and quit()


import random 

#batalla

print("Antes de continuar, debes tener tu primera batalla",
      "así te familiarizas con las luchas entre seres vivos")
print("Tu primer oponente va a ser: Miguel, un hombre sin futuro y desempleado que sueña son ser entrenador pokemon. "
      "Tu trabajo es quebrantar los sueños de los demás y ganarles en las batallas")

listo = input("¿Estás listo para comenzar la batalla?")

if listo == "si":
    print("Que comience la batalla")
    PS_jugador = 100
    PS_oponente = 100
    aumento_DF_jugador = 0 #aumento de la defensa(DF) del jugador, es decir, el oponente le hará menos daño con sus ataques
    turn = 0

    ataques = {"malicioso" : (10,1), "placaje" : (20,0), "ascuas" : (15,0)} #(ataque a los PS, aumento de defensa)

    while PS_oponente > 0 and PS_jugador > 0:
        ataque_jugador = input("Es tu turno de atacar: ")
        while turn == 0:
            if ataque_jugador == "malicioso":
                if aumento_DF_jugador <= 3:
                    aumento_DF_jugador = aumento_DF_jugador + ataques["malicioso"] [1]
                    print("Tu defensa a los ataques ha aumentado")
                elif aumento_DF_jugador >= 4:
                    PS_oponente = PS_oponente - ataques["malicioso"] [0]
                    print(f"PS oponente: {PS_oponente}, ya no puedes aumentar tu defensa")
                turn += 1
            elif ataque_jugador == "placaje":
                PS_oponente = PS_oponente - ataques["placaje"] [0]
                print(f"Defensa oponente: {PS_oponente}" )
                turn += 1
            elif ataque_jugador == "ascuas":
                PS_oponente = PS_oponente - ataques["ascuas"] [0]
                print(f"PS oponente: {PS_oponente}")
                turn += 1
            else:
                turn == 0
                print("Tus ataques son: ", ataques)
                ataque_jugador = input("Vuelve a intentarlo: ") 
        turn = 0        
        print("Turno del atacante:")   
        ataque_oponente = random.randrange (1,3+1)

        if ataque_oponente == 1:
            if aumento_DF_jugador == 0:
                PS_jugador -= 10
                print(f"El oponente usó látigo, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 1:
                PS_jugador -= 10/1.2
                print(f"El oponente usó látigo, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 2:
                PS_jugador -= 10/1.3
                print(f"El oponente usó látigo, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador >= 3:
                PS_jugador -= 10/1.3
                print(f"El oponente usó látigo, tus PS son: {PS_jugador}") 

        elif ataque_oponente == 2:
            if aumento_DF_jugador == 0:
                PS_jugador -= 25
                print(f"El oponente usó golpe karate, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 1:
                PS_jugador -= 25/1.2
                print(f"El oponente usó golpe karate, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 2:
                PS_jugador -= 25/1.3
                print(f"El oponente usó golpe karate, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador >= 3:
                PS_jugador -= 25/1.3
                print(f"El oponente usó golpe karate, tus PS son: {PS_jugador}") 

        elif ataque_oponente == 3:
            if aumento_DF_jugador == 0 :
                PS_jugador -= 15
                print(f"El oponente usó ácido, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 1:
                PS_jugador -= 15/1.2
                print(f"El oponente usó ácido, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador == 2:
                PS_jugador -= 15/1.3
                print(f"El oponente usó ácido, tus PS son: {PS_jugador}")
            elif aumento_DF_jugador >= 3:
                PS_jugador -= 15/1.3
                print(f"El oponente usó ácido, tus PS son: {PS_jugador}")



    #la batalla ha terminado
    if PS_oponente <= 0 and PS_jugador <= 0:
        print("Empate")
    elif PS_oponente <= 0:
        print("Felicidades, has ganado")
    elif PS_jugador <=0:
        print("Lo siento, has perdido")
    else:
        print("Bueno, nunca vas a ser un entrenador pokemon")
else:
    print("Bueno, nunca vas a ser un entrenador pokemon")
