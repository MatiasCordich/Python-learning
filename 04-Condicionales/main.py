"""

Condicional IF
 
SI se_cumple_esta_condicion:
    Ejecuto el grupo de instruccions
SI NO:
    Ejecuto este grupo de instrucciones

En Python utilizamos 

if condicion:
    instrucciones
else:
    otras instrucciones

"""

# EJEMPLO 1

color = "rojo"

if color == "rojo":
    print(f"El color es {color}")
else:
    print("Es color NO es rojo ")

# EJEMPLO 2

color_favorito = "verde"

color_adivinar = input("Adivina mi color favorito: ")

if color_adivinar == "verde":
    print("Felicitaciones, adiviniste el color!!!")
else:
    print("No has adivinado mi color favorito :( ")