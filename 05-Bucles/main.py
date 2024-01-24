# BUCLES

"""
Un bucle es una estructura que nos permite REPETIR una instrucion (bloques de codigo) varias veces. 
En Python existen dos bucles principales:

- WHILE
- FOR
"""

# FOR

"""
Este bucle sirve para poder recorrer e iterar sobre una lista, tupla, rango o cualquier objeto iterable. 

Su sintaxis es la siguiente

for variable in objeto_a_iterar: 
"""

# USANDO EL FOR PARA HACER UN CONTADOR

"""
En Pytnon podemos hacer un contador que se incremente con cada iteracion para eso tenemos que iterar sobre un RANGO para eso utiizamos la funcion range()
"""

contador = 0

for contador in range(5):
    print(contador)

"""
Como vemos al establecer una variable CONTADOR, cuyo valor empieza en 0, al utilizar range lo que hago es incrementar 5 veces dicho valor

0 primera iteracion
1 segunda iteracion
2 tercera iteracion
3 cuarta iteracion
4 quinta iteracion
"""

# USANDO EL FOR PARA UNA LISTA