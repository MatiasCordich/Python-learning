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

# EJEMPLO 3. USO DEL RETURN EN UNA FUNCION
"""
El uso del return en una funcion especifica que, una vez hecho toda la operacion, el resultado obtenido sea "devuelto" o "retornado" para que se pueda usar en otro lugar de mi programa. 
Vamos con un ejemplo
"""

def suma(a, b):
    resultado = a + b
    return resultado

"""
Como vemos dicha funcion hace la suma de dos numeros, cuyos paramentros son "a" y "b" y al utilizarse, se hace la operacion aritmetica y da como resultado un valor que es retornado en una variable llamada "resultado"
"""

"""
ES IMPORTANTE ENTENDER QUE EL RESULTADO FINAL NO SE VERA EN LA PANTALLA A NO SER QUE SE HAGA UN PRINT DEL RESULTADO QUE RETORNE LA FUNCION. 
"""
print(suma(5,6))

"""
O puedo guardar el valor que me retorne la funcion en una variable y despues imprimir dicho valor
"""

resultado_suma = suma(6,9)

print(f"El resultado es: {resultado_suma}")

# FUNCIONES ANIDADAS 
"""
Podemos anidar funciones, es decir, podemos hacer una funcion "madre" que englobe otras funciones "hijas" con el proposito de solo llamar a la funcion madre que a su vez llamara a las funciones hijas para ejecutar toda la instruccion. 
Veamos con un ejemplo
"""

def getNombre(nombre):
    texto = f"Mi nombre es: {nombre}\n"
    return texto

def getApellidos(apellidos):
    texto = f"Mis apellidos son : {apellidos}\n"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(getNombre("Pepe"), getApellidos("Esculapio"))
print(devuelveTodo("Pepe", "Esculapio"))

# FUNCIONES LAMBDA
"""
Es una forma concisa de definir funciones ANONIMAS, es decir, funciones que son utiles cuando se necesita una funcion rapida para ejecutar un bloque de codigo muy sencillo sin tener que utilizar la palabra "def" 
Un ejemplo seria
"""

multiplicar_por_dos = lambda x : x * 2

"""
La funcion se define como una variable cuyos componentes son
- lambda: la palabra reservada para definir que esa es una funcion lambda
- el parametro que recibe, en este caso definido como "x"
- lo que viene despues de los dos puntos ":" es el pequeño bloque de instruccion de lo que se hace con dicho valor pasado por parametro "x * 2"
"""

resultado_doble = multiplicar_por_dos(8)

print(resultado_doble)