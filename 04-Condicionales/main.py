# CONDICIONALES

"""
A la hora de hacer un programa en Python, sabemos que no existen solamente los resultados lineales, es decir, que solo existe un solo camino. 
Por lo general, el programa tiene que tomar decisiones ya que se presentan ciertas CONDICIONES que, dependiendo de la misma, el programa debe realizar una accion u otra. 

Estas condiciones son evaluadas com VERDADERAS o FALSAS.

En Python existen expresiones para realizar una estrcutura condicional que son 
IF: Si
ELSE: sino
ELIF (abreviatura de else if): o si

"""


"""

Condicional IF/ELSE

En términos sencillos, estas estructuras condicionales permiten que un programa ejecute cierto bloque de código si se cumple una condición específica y, opcionalmente, ejecute un bloque diferente si la condición no se cumple.
 
SI se_cumple_esta_condicion:
    Ejecuto el grupo de instruccions
SI NO:
    Ejecuto este grupo de instrucciones

En Python utilizamos 

if condicion_1:
    Bloque de código si condicion_1 es verdadera
else:
    Bloque de código si condicion_1 es falsa

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

"""

IFs Anidados
 
Son estructucturas condiciones dentro de otras estructuras condicionales 

SI condicion_1:
    Ejecuto estas instrucciones si condicion_1 es verdadera 
    SI condicion_2:
         Ejecuto estas instrucciones si condicion_1 y condicion_2 son verdaeras verdaderas
    SI NO:
        Ejecuto estas instruciones si la condicion_2 NO es verdadera
SI NO:
    Ejecuto este grupo de instrucciones si la condicion_1 es FALSA

En Python utilizamos 

if condicion_externa:

    Bloque de código si la condición_externa es verdadera

    if condicion_interna_1:
        # Bloque de código si ambas condiciones son verdaderas
    else:
        # Bloque si la condicion interna no es verdadera
else:
    # Bloque de código si la condicion_externa es falsa

"""

nombre = "Pepe"
edad = 60
mayoria_edad = 18;
nacionalidad = "Argentino"

# Analizamos primero la condicion de mayoria de edad
if edad > mayoria_edad:

    print(f"{nombre} es mayor de edad")

    # Dentro de la condicion, hacemos otro analisis de la nacionalidad
    if nacionalidad != "Argentino":
        print(f"{nombre} NO es Argentino")
    else:
        print(f"{nombre} es Argentino")
else :
     print(f"{nombre} NO  es mayor de edad")

"""

Elif

Cuando tenemos que evaluar multiples condiciones, existe una estructura que nos sirve para realizar dicha evaluacion multiple, el ELIF que se usa de la sigueinte manera 

Si condicion_1:
    Bloque de código si condicion_1 es verdadera
Sino si condicion_2:
    Bloque de código si condicion_1 es falsa, pero condicion_2 es verdadera
Sino si condicion_3:
    Bloque de código si condicion_1 y condicion_2 son falsas, pero condicion_3 es verdadera
Sino
    Bloque de código si ninguna de las condiciones anteriores es verdadera

if condicion_1:
    Bloque de código si condicion_1 es verdadera
elif condicion_2:
    Bloque de código si condicion_1 es falsa, pero condicion_2 es verdadera
elif condicion_3:
    Bloque de código si condicion_1 y condicion_2 son falsas, pero condicion_3 es verdadera
else:
    Bloque de código si ninguna de las condiciones anteriores es verdadera

"""

edad_establecida = 25

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres un adulto mayor.")