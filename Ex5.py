""""
Yeray Lopez
David Muñoz
Didac Lloret
11/10/23
Encript12345
ASIXc 1B
"""

paraula1 = input("Ingresa una paraula: ")

#Transformar les lletres majúscules en minúscules
paraula = paraula1.lower()
canvi1 = paraula.replace("a", "1")
canvi2 = canvi1.replace("e","2")
canvi3 = canvi2.replace("i","3")
canvi4 = canvi3.replace("o","4")
canvi5 = canvi4.replace("u","5")


print("Paraula amb vocals reemplaçades:", canvi5)