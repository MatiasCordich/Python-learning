# TIPOS DE DATOS 
"""
Los tipos de datos hace referencia al tipo de dato que puede contener una variable. 

En Pytnon existen los siguientes tipos de datos
"""

# STRING (STR)
"""
Practicamente es un texto, o tambien como se dice, una cadena de caracteres
"""

string = "Hola a todos"
print(string)

# ENTERO (INT)
"""
Hace referencia a los numeros enteros
"""

entero = 23
print(entero)

# FLOTANTE (FLOAT)
"""
Hace referencia a los numeros decimales
"""

flotante = 7.8
print(flotante)

# BOOLEANO (TRUE O FALSE)
"""
Hace referencia a solo dos valores posibles VERDARO (True) o FALSO (False)
"""

boleano = True
print(boleano)

# LISTA (LIST)
"""
Es un tipo de dato mas complejo que permite guardar una coleccion de datos. 
Las listas tienen la siguiente caracteristica
- Son ordenadas
- Son editables
- Pueden contener distintos tipos de datos
- Puede contener elementos duplicados
"""

lista = ["Banana", "Manzana", "Pera", "Kiwi"]
print(lista)

listaVariada = ["Queso", 43, 2, "Atun", "Cerveza", True]
print(listaVariada)

# TUPLA (TUPLE)
"""
Es igual a la lista pero a diferencia de esta, su contenido es INMUTABLE, es decir, NO PUEDE CAMBIAR
"""

tupla = ("Hola", "Soy", "Matias")
print(tupla)

# DICCIONARIO (DICT)
"""
Los diccionarios en Python son una estructura de datos donde permite organizar los datos y organizarlos de manera mas flexible. 
A diferencia de las tuplas o listas, los diccionarios NO ESTAN INDEXADOS. 
Los elementos de un diccionario estan estructurados en conjuntos de pares clave valor
("clave1": valor)
"""

diccionario = {
    "nombre": "Pepe",
    "apellido": "Esculapio",
    "edad": 23  
}
print(diccionario)

# SABER EL TIPO DE DATO DE UNA VARIABLE
"""
Para saber el tipo de dato de una variable, simplemente utilizamos la funcion type(variable)
"""

print(type(string))
print(type(entero))
print(type(flotante))
print(type(lista))
print(type(tupla))
print(type(diccionario))

# CONVERTIR DE UN TIPO DE DATO A OTRO
"""
Supongamos que tenemos este ejemplo
"""

texto = "Hola soy un texto"
numerito = 123

# print(texto + " " + numerito) --> ESTO DA ERROR

"""
Si yo quiero correr el programa me va a dar error porque no se pueden concatenar el valor de texto con el valor de numerito porque numerito es de tipo int. Para resolver esto debemos utilizar el str()
"""

numerito_a_string = str(123)

print(texto + " " + numerito_a_string)

"""
Tambien podemos convertir dicho variable a otro tipo de dato con int(), float()
"""

numerito_a_string = int(123)
print(type(numerito_a_string))

numerito_a_string = float(123)
print(type(numerito_a_string))
print(numerito_a_string)
