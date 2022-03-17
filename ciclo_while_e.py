'''
ciclo_while_e.py
script de python que implemente el juego de adivinar un numero pero esta vez
modo competitivo. La computadora debera generar un numero aleatorio entre 1 y 100
 y tanto el usuario como la computadora, deberan adivinar dicho numero. Para que el juego sea
 retador el jugador maquina debera ser "inteligente" y competir para ganar.
 el juego se realizara por turnos, primero la maquina y luego el usuario y por cada
 intento la computadora indicara si es mayor o menor que el numero secreto
'''

import os
import random
inferior = 1
superior = 100
secreto = random.randint(1,100)
usuario = -1
maquina = -1

while usuario!= secreto and maquina !=secreto:
    os.system('cls')
    print('maquina ¿cual crees que es el numero secreto?')
    maquina = random.randint(inferior, superior)
    print(f'maquina:{maquina}')
    if maquina < secreto:
        print('Tu numero es menor')
        inferior = maquina + 1
    elif maquina > secreto:
        print('Tu numero es mayor')
        superior= maquina - 1
    else:
        print('La maquina ha ganado')
    if maquina !=secreto:
        usuario = int(input('Usuario ¿Cual crees que es el numero secreto?'))
        if usuario < secreto:
            print('Tu numero es menor')
            if usuario > inferior:
                inferior = usuario+1
        elif usuario > secreto:
            print('Tu numero es mayor')
            if usuario > secreto:
                superior = usuario-1
        else:
            print('el usuario ha ganado!')
        input('Presiona una tecla para continuar')

input('Nos vemos')
