""""
Yeray Lopez
David Muñoz
Didac Lloret
11/10/23
AirVolumeCalculator
ASIXc 1B
"""

try:
    #Demanar les dades de l'habitació
    ample = float(input("el ample del aula en (m) és:"))
    longitud = float(input("la longitud del aula en (m)"))
    alçada = float(input("l'alçada del aula en (m) és:"))

    #Calcular el volum
    solucio = ample * alçada * longitud
    print ("El volum de l'aula és", solucio,"m³")

except ValueError:
    print("només números cara anchoa")
