# OPERADORES LOGICOS
"""

Los operadores logicos en Python son utilizandos en los condicionales, cuando queremos evaluar dos o mas condiciones que nos van a dar valores Booleanos (True o False). Hay tres operadores lógicos principales: 

- and: Y
- or: O
-not: NO

A continuacion aca hay ejemplos de los mismos

"""

# OPERADOR AND
"""

- Devuelve True si ambas condiciones son verdaderas.
- Devuelve False si al menos una de las condiciones es falsa.

"""

x = 5
y = 10
resultado = (x < y) and (y != 12)
print(resultado)  # Devuelve True

# OPERADOR OR
"""

- Devuelve True si al menos una de las condiciones es verdadera.
- Devuelve False solo si ambas condiciones son falsas.

"""

edad = 25
es_estudiante = True
resultado = (edad < 18) or es_estudiante
print(resultado)  # Devuelve True

# OPERADOR NOT
"""

- Devuelve True si la condición es falsa.
- Devuelve False si la condición es verdadera.

"""

x = 5
resultado = not (x == 10)
print(resultado)  # Devuelve True