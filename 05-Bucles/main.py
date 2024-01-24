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
    # 0, 1, 2, 3, 4

"""
Como vemos al establecer una variable CONTADOR, cuyo valor empieza en 0, al utilizar el range(5) estoy diciendo que el valor maximo que puede tomar la variable CONTADOR es 4. 

0 primera iteracion
1 segunda iteracion
2 tercera iteracion
3 cuarta iteracion
4 quinta iteracion
"""

"""
Tambien a la funcion range podemos agregarle mas parametros de la sigiuente manera
"""

for i in range(0,10,2):
    print(i)
    # 0, 2, 4, 6, 8

"""
Cada paramentro indica lo siguiente
Se toma primero como variable la variable i
0: Indica el valor inicial que va a tener la variable i, en este caso 0
10: Indica el valor maximo que puede tomar i, en este caso sera desde el 0 hasta el 9. CUIDADO!!!! A LA HORA DE HACER LA ITERACION EL LIMITE ES 10 PERO NO SE INCLUYE
2: por cada iteracion el valor de i va a ir incrementando de 2 en 2.
"""

# USANDO EL FOR PARA UNA LISTA
