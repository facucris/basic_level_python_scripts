'''
funciones4.py
script de python que implementa una funcion para calcular el area de un triangulo.
Dicha funcion recibe como argumentos la base y la altura del triangulo y regresa el area ya calculada.
'''


def area(altura, base):
    return (base*altura)/2

print('Programa para calcular el area de un triangulo: ')
print('Ingresa los siguientes valores')
altura=float(input('altura: '))
base=float(input('base: '))

print(f'area= {area(altura,base)}')
print('nos vemos')
