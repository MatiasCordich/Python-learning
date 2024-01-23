# VARIABLES 
"""
Una variable es un contenedor de informacion, es decir, dentro de la misma se guardara un dato. 
Las variables pueden ser de distintos tipos de datos.
"""

# String
texto = "Hola mundo"
print(texto)


# Concatenacion

"""
La concatenacion es una forma de poder unir distintos valores de diferentes variables. 
Existen dos formas de concatenar 
"""

nombre = "Pepe"
apellido = "Esculapio"

# Primera forma

"""
Esta es la forma es la mas comun donde se concatenan mediante los signo de suma, pero OJO que en la concatenacion de strings tambien es necesario sumar los espacios ya que cuentan como caracteres. 
"""
print(nombre + " " + apellido)

# Segunda forma
"""
Esta segunda forma es mas facil y sencilla porque simplemente tenemos que poner las variables cuyo valores tienen onde comenzamos con la letra "f" y seguido entre comillas los valores de cada variable, dichos valores deberan estar entre llaves {}
"""
print(f"{nombre} {apellido}")

# Concatenacion insertando valores
"""
Tambien se pueden insertar valores cuando se muestra por consola un texto informativo donde se tiene que concatenar la cadena de texto con el valor de la variable. 
Para realizar eso tengo que utilizar la funcion .format()
"""

edad = 21

print("Hola, me llamo {} {} y tengo {} anios".format(nombre, apellido, edad))

"""
Como vemos en cada espacio donde hay llaves {} seran llenados con lo que pongamos en format()
OJO es importante el orden para que el texto tenga sentido
"""
