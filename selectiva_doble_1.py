'''
seleciva_doble_1.py
script en python que solicita que el ususario adivine un numero del 1 al 10
si adivina, lo felicita, sino, muetra el numero que era

'''

import random

print('Acbo de generar un numero secreto entre 1 y 10')

secreto = random.randint(1,10)
usuario = int(input('¿Cual crees que es el numero secreto?'))
if usuario==secreto:
    print('Lo lograste! Felicidades!')
else:
    print(f'Mi numero es {secreto}')

print('Ten un buen dia')
