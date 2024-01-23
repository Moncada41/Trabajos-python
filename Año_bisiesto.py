year = int(input("Coloca un número entre el 1900 y 2199: "))
if year>2199 or year<1900:
    print("No puedes colocar un número que salgan del rango,", 
          "ntenta otra vez")
    quit()
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        print("El año",year,"es bisiesto")
        print("Hay",int((year-1900)/4),"años bisiestos",
                "a partir del 1900")
    elif (year % 100 == 0 and year % 400 != 0): #no sé si es necesario agregar este código 
        print("El año",year,"no es bisiesto")
        print("Hay",int((year-1900)/4),"años bisiestos",
                "a partir del 1900")
    else: 
        print("El año",year,"no es bisiesto")
        print("Hay",int((year-1900)/4),"años bisiestos",
                "a partir del 1900")
