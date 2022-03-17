'''
funciones1.py
script python que implemente una funcion para calcular el area de un triangulo.
'''

def area():
    base=float(input('ingrese valor de la base: '))
    altura=float(input('ingrese valor de la altura: '))
    area = (base*altura)/2
    return area

print('Programa para calcular el area de un triangulo')

a= area()
print(f'Area = {a}')

print('nos vemos')
