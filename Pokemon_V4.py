import random

print("Que comience la batalla")
PS_jugador = 100
Defensa_jugdador = 50
PS_oponente = 100
Defensa_oponente = 50

turn = 0

ataques = {"malicioso" : (30,0), "placaje" : (0,20), "ascuas" : (15,0)} #(ataque a los PS, ataque a la defensa)

while (Defensa_oponente and PS_oponente) > 0 and (Defensa_jugdador and PS_jugador) > 0:
    ataque_jugador = input("Es tu turno de atacar: ")
    while turn == 0:
        if ataque_jugador == "malicioso":
            PS_oponente = PS_oponente - ataques["malicioso"] [0]
            print(f"PS oponente: {PS_oponente}")
            turn += 1
        elif ataque_jugador == "placaje":
            Defensa_oponente = Defensa_oponente - ataques["placaje"] [1]
            print(f"Defensa oponente: {Defensa_oponente}" )
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
        PS_jugador -= 15
        print(f"El oponente usó látigo, tu defensa es: {Defensa_jugdador}")
    elif ataque_oponente == 2:
        Defensa_jugdador -= 25
        print(f"El oponente usó golpe karate, tus PS son: {PS_jugador}")
    elif ataque_oponente == 3:
        PS_jugador -= 20
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
