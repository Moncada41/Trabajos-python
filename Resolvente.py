import math

a = int(input("Introduce tu a: "))
b = int(input("Introduce tu b: "))
c = int(input("Introduce tu c: "))
discriminante = b*b - 4*a*c
if discriminante < 0:
    quit(print("Estos números dan como resultado un imaginario"))
else: 
    raiz = math.sqrt(discriminante)
    x1 = round(-b + raiz /(2*a))
    if discriminante != 0:
        x2 = round(-b - raiz /(2*a))
    print("Los valores al aplicar la resolvente son",x1, "y",x2,)
    

