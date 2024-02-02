#FUNCIONES
"""
Una funcion es un conjunto agrupado de instrucciones que pueden realizarse invocando la funcion tantas veces como sea necesario. 

Para definiar una funcion utilizamos la palabra reservada def 

def nombreDeMiFuncion(parametros):
    BLOQUE / CONJUNTO DE INSTRUCIONES

nombreDeMiFuncion(mi_parametro)

No es necesario que las funciones tenga parametros, mas adelante se explica que son los parametros en una funcion
"""

# DEFINIR FUNCION
def mostarSaludo():
    print("Hola")

# INVOCAR FUNCION
mostarSaludo()

# PARAMETROS
"""
Supongamos que tenemos una funcio donde me pide mostrar la edad
"""

def mostrarEdad():
    print("Tu edad es de 27 años")

mostrarEdad()

"""
El problema surje cuando quiero mostrar una edad dinámica, es decir, lo que se muestre al utilizar el print sea un numero diferente a 27. Para eso existen los parametros.

Los parámetros son datos que recibe una función y que servirán para que el bloque de código pueda funcionar con los datos recibidos por la función. 
Aca lo vemos en un ejemplo
"""

def mostrarEdadParametro(edad):
    print(f"Tu edad es de {edad} años")

"""
Como vemos, al poner EDAD como parametro estamso diciendo que esa función recibe un valor y que dicho valor será usado para la ejecución del código, en este caso mostrar por pantalla el numero que ingresamos. 
"""

mostrarEdadParametro(34)
mostrarEdadParametro(21)
mostrarEdadParametro(55)

# EJEMPLO 2. FUNCION CON PARAMETROS MEDIANTE INPUT

def presentarPersona(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y mi edad es de {edad} años")

nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = int(input("Ingrese su edad: "))

presentarPersona(nombre_ingresado, edad_ingresada)