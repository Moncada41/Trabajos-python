year = int(input("Coloca un número entre el 1900 y 2199: "))

if int(year)>2199 or int(year)<1900:
    print("No puedes colocar un número que salgan del rango, intenta otra vez")
    
def bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)

for year in range(1900, year):
    if bisiesto(year):
        print(year, end=' ')
print("es la cantidad de años bisiestos entre 1900 y" , year+1,)
