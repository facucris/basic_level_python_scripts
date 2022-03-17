'''
ciclo_for5.py
script en python que muestr las tblas de multiplicar del 1 al 10. Con cada
tabla se muetra hasta el decimo multiplo.
'''
import os

for numero in range(1,11):
    os.system('cls')
    print(f'             tabla de multiplicar de {numero}')
    for multiplo in range(1,11):
        print(f'{numero}x{multiplo} = {numero * multiplo}')
    input('Presiona enter para continuar...')
print('nos vemos')
