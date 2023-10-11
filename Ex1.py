""""
Yeray Lopez
David Muñoz
Didac Lloret
11/10/23
HowsBigsIsMyPizza
ASIXc 1B
"""
#Importar math per posar el pi rapidament
import math
#try en cas de que l'usuari no utilitzi un numero
try:
    #Pedir el diametre de la pizza
    pizza_diam = float(input("Quin es el diàmentre de la pizza en cm?: "))

    #Dividir el diametre entre 2 per calcular el radi
    pizza_radi = pizza_diam / 2

    #Calcular la solució i mostrar el resultat
    solucio = math.pi * pizza_radi ** 2
    print("el diàmetre de la pizaa és:", solucio,("m"))

#except ValueError per indicar que només es pot fer servir numeros
except ValueError:
    print("Només es poden posar números")
