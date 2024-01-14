# OPERADORES ASIGNACION
"""
Los operadores de asignación se utilizan para asignar valores a variables. Estos operadores combinan la operación de asignación con una operación aritmética.

Los operadores de asignacion en Python son los siguientes:

- Asignacion simple (=): Se utiliza para asignar el valor de la expresión a la derecha a la variable a la izquierda.

- Asignacion con Operadores aritmeticos: Estos pueden ser:
    - (+=)
    - (-=)

"""

edad = 34
print(edad)

edad += 4
# Es lo mismo que hacer edad = edad + 4
print(edad)

edad -= 10
# Es lo mismo que hacer edad = edad - 10
print(edad)

# OPERADORES DE DECREMENTO E INCREMENTO
"""

En otros lenguajes de programacion (como C, C++ o Java), un operador de incremento y decremento es un operador especial para aumentar y disminuir el valor de una variable numerica en 1. Para realizarlo se utilizan estos operadores especiales que tienen la siguiente forma: ++ (para incremento) y -- (para decremento).

En Python, no existen estos operadores en especifico, sin embergo, para realizar dichos incrementos o decrementos simplemente nos podemos valer de los operadores de asignacion.

"""

x = 5
x += 1  # Incremento de x en 1
print(x)  # Salida: 6

y = 8
y -= 1  # Decremento de y en 1
print(y)  # Salida: 7
