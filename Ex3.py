""""
Yeray Lopez
David Muñoz
Didac Lloret
11/10/23
InRange
ASIXc 1B
"""
try:
    print("Posa 5 numeros enters")
    Primnum = int(input("Primer número aquí:"))
    Secnum = int(input("Segón número aquí:"))
    Tercnum = int(input("Tercer número aquí:"))
    Quartnum = int(input("Quart número aquí:"))
    Cincnum = int(input("Número a comparar aquí:"))

    llista =  [Primnum, Secnum]
    llista2 = [Tercnum, Quartnum]

    if Cincnum in llista:
        print("True")
    elif Cincnum in llista2:
        print("True")
    else:
        print("False")

    print(Primnum<=Secnum)

except ValueError:
    print("No has posat un numero enter")

