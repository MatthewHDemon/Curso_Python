# While
# For

""" # Si se mofica el valor del contador antes de imprimir, habra una lista de números del 1 al 11
contador = 0

while contador <= 10:

    contador = contador + 1

    print(contador) """




""" # Si se imprime primero y se modifica el valor después, obtenemos una lista del 1 al 10

contador = 0

while contador <= 10:

    print(contador)

    contador = contador + 1 """


# WHILE / WHILE / WHILE / WHILE

""" # Hay una manera de simplificar este codigo:
contador = 1

while contador <= 10:

    print(contador)

    contador += 1 # es igual a contador = contador + 1


else:
    print('Contador no es menor o igual a 10') 
    
    
    Utilizando el ciclo while seremos capaces de ejecutar un bloque
    una n cantidad de veces siempre y cuando la condición se cumpla, 
    después de eso, el ciclo finalizara. Opcionalmente, podemos tener
    un bloque else para cuando la condición deje de cumplirse
     """


# FOR / FOR / FOR / FOR

# String
# Listas
# Tuplas
# Diccionarios




""" mensaje = 'Un string es un objeto inmutable.'

# Warning: Después de : , toca crear un nuevo bloque con 4 espacios
for caracter in mensaje:

    print(caracter) """




""" El for nos sirve para agarrar elemento por elemento de una lista, string, o diccionario
y podemos aplicarle una misma logica por separado """

"""
# Ejemplo con una lista:

 numeros = [1, 2, 3, 4, 5]


for numero in numeros:
    print(numero) """




"""
# Ejemplo con un dupla:

 numeros = (1, 2, 3, 4, 5)

for numero in numeros:
    print(numero) """

""" # Ejemplo para imprimir llaves en el diccionario
usuario = {'username': 'eduardo_gpg', 'email': 'eduardo@codigofacilito.com'}

for key in usuario:
    print(key)  """




""" # en este caso python nos dara error por haber demasiados valores para el empaquetado (unpack)

 usuario = {'username': 'eduardo_gpg', 'email': 'eduardo@codigofacilito.com'}

for key, value in usuario:
    print(key, value)    """




""" #  Ejemplo con un diccionario. Acá iteramos sobre cada una de las llaves en el diccionario,
y a partir de las llaves obtendremos cada uno de sus valores:

usuario = {'username': 'eduardo_gpg', 'email': 'eduardo@codigofacilito.com'}

for key in usuario:
    valor = usuario[key]

    print(valor) 
"""


""" 

# En este ejemplo como la iteración nos permite acceder a cada una las llaves, dentro de los
# corchetes colocamos la llave de la cual queremos conocer su valor

usuario = {'username': 'eduardo_gpg', 'email': 'eduardo@codigofacilito.com'}

for key in usuario:
    valor = usuario[key]

    print(valor) """




""" # Si quisieramos iterar tanto llaves como valores, usamos el desempaquetado
    
usuario = {'username': 'eduardo_gpg', 'email': 'eduardo@codigofacilito.com'}
    
for llave, valor in usuario.items():
    print(llave, '-', valor) """




"""  # En este ejemplo vamos a condicionar número por número para imprimir los que son par
 
for a in range(21):
    if a % 2 == 0:
        print(a)

else:
    print("Finalizado") """








