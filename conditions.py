
""" Para crear un nuevo bloque 
de codigo en Python, nosotros 
utilizamos 4 espacios, no tabs. """

 # if <Bool>:

edad = int(input('Ingresa tu edad:'))

"""
también se puede generar un número entero
a partir de un string con:

edad = input('Ingresa tu edad:')
edad= int(edad)

 esto es 'tipado dinámico' -int -float """

if edad >= 1 and edad <= 5:
    print( 'Eres un bebé' )  
elif edad > 5 and edad <= 9:
    print( 'Eres un niño' )  
elif edad >= 10 and edad <= 19:
    print( 'Eres un adolecente' )  
elif edad > 19 and edad <= 29:
    print( 'Eres un adulto joven')  
elif edad >= 30 and edad <= 59:
    print( 'Eres un adulto de mediana edad ')
elif edad >= 60:
    print( 'Eres un adulto de avanzada edad' )
else:
    print( 'No eres mayor de edad. ')