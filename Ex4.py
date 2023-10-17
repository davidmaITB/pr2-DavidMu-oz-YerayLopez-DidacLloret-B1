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
    edattreball = list(range(16, 66))  # Crear una llista de edats permitides de 16 a 65 anys
    if edat in edattreball:
        print("Pots treballar")
    else:
        print("No pots treballar")
except ValueError:
    print("Posa un nombre enter")