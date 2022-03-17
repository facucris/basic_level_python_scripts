'''
ciclo_while4.py
script en python que muestre un menu con personajes de un juego, al seleccionar
uno se mostraran sus caracteristicas, el programa sera ciclico hasta que el
usuario indique que quiere salir
'''


import os
mago= 1
guerrero = 2
elfa=3
salir=4

#bandera
continuar= True

while continuar:
    os.system('cls')
    print(f'''                          Personajes
    {mago})Mago
    {guerrero})Guerrero
    {elfa})Elfa
    {salir})Salir
    ''')

    opc= int(input('Selecciona tu personaje: '))

    if opc== mago:
        print('''
        Fuerza: 15
        Agilidad: 20
        Energia: 25
        ''')
    elif opc== guerrero:
        print('''
        Fuerza: 25
        Agilidad: 15
        Energia: 10
        ''')
    elif opc== elfa:
        print('''
        Fuerza: 10
        Agilidad: 25
        Energia: 20
        ''')
    elif opc== salir:
        continuar = False
    else:
        print('Opcion no valida')
    input('Presiona enter para continuar')

input('Nos Vemos!')
