# Arepas.py
agua = int(input("¿Cuántas tazas de agua necesitas?"))
harina = int(input("¿Cuántas tazas de harina necesitas?"))
sal = int(input("¿Cuántas cucharaditas de sal necesitas?"))
aceite = int(input("¿Cuántas cucharadas de aceite necesitas?"))
S1 = float(sal/48)
S2 = float(aceite/16)
mezcla = round(agua + harina + S1 + S2)
total = f"{mezcla} tazas"
print (total)
