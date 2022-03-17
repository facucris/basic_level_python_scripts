'''
ciclo_while3.py
script en python que simule el sistema de validacion de una plataforma digital
Se le solicitara al usuario nombre y contraseña repetidamente hasta que coincidan
los datos
'''

import os

usuario= 'Facundo'
pasw= 'f35953'

user=''
passw=''

while usuario !=user or pasw!=passw:
    os.system('cls')
    print('                     hola')
    user= input('Usuario: ')
    passw= input('Contraseña: ')
    if usuario !=user or pasw!=passw:
        print('Datos incorrectos')
        print('Intente nuevamente')
        input('Presione enter para continuar')
    else:
        print(f'Bienvenido {usuario}')

input('Nos vemos!')
