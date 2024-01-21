# ENTRADA DE DATOS
"""

Para realizar una entrada de datos por teclado, simplemente tenemos que aplicar la funcion input(). Donde adentro de la misma llevara un string con el texto para preguntar que dato vamos a ingresar. 

"""

nombre = input("Cual es tu nombre?: ")

# SALIDA DE DATOS
"""

La salida de datos es simplemente aplicar la  funcion print() que hemos estado utilizando

"""

print(f"Su nombre es: {nombre}")

# ENTRADA DE DATOS TIPO ENTERO
"""

Supongamos que tenemos que ingresar una edad

"""

edad = input("Cual es tu edad?:")

print(f"Su nombre es: {nombre} y su edad es {edad}")

"""

Recordemos que al ingresar cualquier dato por consola, este  lo toma como string, el problema es cuando tenemos que ingresar un numero por consola y queremos hacer una operacion con dicho numero, al ingresarlo me lo toma como String y no podemos hacer operaciones aritmeticas con strings.
Para eso tenemos que convertir el dato que ingresemos con el metodo int() de la siguiente manera

"""

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

print(f"La suma de {num_1} + {num_2} es {num_1 + num_2}")

"""

De esta manera el numero que ingresemos por teclado se convierte en un dato de tipo entero y podemos realizar operaciones matematicas. 

"""