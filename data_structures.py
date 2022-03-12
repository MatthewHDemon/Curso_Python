# Listas
# Tuplas
# Diccionarios

""" Un arreglo es lo mismo que un array, en python pueden
moficiar su longitud (crecer y decrecer) """




""" números = [1, 2, 3, 4, 5, 'String', 7.5, True, [1, 2, 3, 4, 5]]
print(números)
print(type(números)) """

# es aconsejable que nuestras listas almacenen solo un tipo de dato 




""" # Si queremos modificar el valor de un indice:
# indice: 0, 1, 2, 3, 4
números = [1, 2, 3, 4, 5]
números[1] = 100
print(números[1]) """




""" Podemos generar sub-listas:

#            0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[0:3] # start y end. Warning: la lista solo imprimiria hasta el inidice número 2
print(primeros_cursos) """




""" 
# si solo colcamos el : mas el end(4), python por dafault empieza desde el indice número 0:

#            0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[:4]
print(primeros_cursos) """




"""
# si quisieramos imprimir el último indice, tendriamos que poner el end(6) que vendría después del final.
en el caso de este ejemplo, si nuestro indice es de número 5, entonces debemos poner como indice final el número 6:

 #            0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[1:6]
print(primeros_cursos) """




"""
# si queremos todos los elementos después del start(1), descartariamos el end:

 #           0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[1:]
print(primeros_cursos) """




"""
# también podemos generar sub-listas con saltos. El último número representa
 el número de salto al momento de imprimir los indices: 

  #          0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[1:6:3]
print(primeros_cursos) """




""" # Si quisieramos invertir el orden de los indices, aplciariamos valores negativos al número de saltos
 #           0         1        2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
primeros_cursos = cursos[::-1]
print(primeros_cursos)  """




""" # si queremos saber la longitud de nuestro arreglo
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
print(len(cursos)) """




""" # si queremos ordenar nuestro valores:
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
cursos.sort()
print((cursos))
# En este caso con nuestros indices son strings, python los ordenara alfabeticamente """




"""  # si queremos ordenar nuestro valores de forma inversa/descendente (de la 'Z' a la 'A'):
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
cursos.sort(reverse=True)
print((cursos)) """




"""  # si queremos añadir un elemento al final de la lista:
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']

cursos.append('MongoDB')
print(cursos) """




"""  # si queremos insetar un valor a partir de un indice:
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']

cursos.insert(0, 'MySQL')
print(cursos)  """




""" # si queremos remover un valor del arreglo
#            0         1         2        3       4
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']
cursos.remove('Django')
print(cursos) """




""" DUPLAS
 Una dupla es una estructura de datos que nos permiten almacenas diferentes
 tipos de datos. Su diferencia con las listas que estas son inmutables, lo
 que quiere decir que cuando definamos un dupla, esta seguira igual por el
 resto del programa. No pueden crecer ni decrecer"""



""" # Ejemplos

# En vez de usar corchetes como haciamos con las listas, en duplas utilizamos
# parentesis. También al no varias sus valores, se da una consulta más rapida
configuración = (27019, True, 'localhost')

print(configuración)

#es aconsejable utilizar un solo tipo de datos en duplas """




""" DICCIONARIOS a diferencia de las listas y las duplas, en los diccionarios 
estos no se rigen por indices, en cambio se mofican sus valores por llaves."""




""" usuario = {'nombre': 'Eduardo'}
Las
# llaves regularmente se definen con un string, y posteriormente ponemos el valor
# que la llave posea"
print(usuario) """




""" Objetos inmutables:

    - Strings
    - Enteros
    - FLotantes
    - Bool
    - Tuplas

usuario = {
    'nombre': 'Eduardo',
    'edad': 27,
    (1, 2, 3): 'Esta es una tupla',
    10: 'Entero',
    3.14: 'Flotante'
 """


""" 
# Si quisieramos imprimir el valor de las llaves:
usuario = {
    'nombre': 'Eduardo',
    'edad': 27,
    (1, 2, 3): 'Esta es una tupla',
    10: 'Entero',
    3.14: 'Flotante'
}

print(usuario.keys()) """




""" 
# Si quisieramos imprimirlas por duplas:

usuario = {
    'nombre': 'Eduardo',
    'edad': 27,
    (1, 2, 3): 'Esta es una tupla',
    10: 'Entero',
    3.14: 'Flotante'
}

print(usuario.keys()) """




""" # Si quisieramos imprimir los valores de las llaves:

usuario = {
    'nombre': 'Eduardo',
    'edad': 27,
    (1, 2, 3): 'Esta es una tupla',
    10: 'Entero',
    3.14: 'Flotante'
}

print(usuario.values()) """




""" Si quisieramos obtener el par "llave, valor":

usuario = {
    'nombre': 'Eduardo',
    'edad': 27,
    (1, 2, 3): 'Esta es una tupla',
    10: 'Entero',
    3.14: 'Flotante'
}

print(usuario.items()) 
# este imprime cada par por duplas. Repito: las duplas son inmutables """















