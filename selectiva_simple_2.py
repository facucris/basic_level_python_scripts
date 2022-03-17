'''
selectiva_simple_2.py
script de python que genere un numero aleatorio entre 1 y 10 y pida al usuario adivinarlo. si lo logra lo felicita
'''
import random

secreto = random.randint(1,10)

print('Acabo de generar un numero aleatorio entre 1 y 10, intenta adivinarlo')

numero = int(input('¿Cual crees que sea mi numero?'))
if numero == secreto:
    print('Lo adivinaste!!')

print(f'el numero secreto es: {secreto})
print('Ten un buen dia!')
