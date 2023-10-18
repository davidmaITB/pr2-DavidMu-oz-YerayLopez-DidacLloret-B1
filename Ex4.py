""""
Yeray Lopez
David Muñoz
Didac Lloret
11/10/23
WorkingAge
ASIXc 1B
"""
try:
    edat = int(input("Posa la teva edat: "))
    # Crear el rang d'edat on es pot treballar
    edattreball = range(16, 66)
    if edat in edattreball:
        print("Pots treballar")
    else:
        print("No pots treballar")
except ValueError:
    print("Posa un nombre enter")