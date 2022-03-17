'''
procedimiento4.py
script python que muestre un menu ciclico, dicho menu sera implementado en un procedimiento
'''
import os

esp= 1
ing=2
no_subs=3
salir=4

def menu():
    print(f'''                      Subtitulos
    {esp})español
    {ing})ingles
    {no_subs})sin subtitulos
    {salir})salir''')

continuar= True
while continuar:
    os.system('cls')
    menu()
    opc=int(input('Selecciona una opcion: '))
    os.system('cls')
    if opc== esp:

        print('Subtitulos en español')
    elif opc==ing:

        print('Subtitulos en ingles')
    elif opc==no_subs:
        print('Sin subtitulos')
    elif opc==salir:
        continuar = False
    else:
        print('Opcion no valida')

    input('Presione una tecla para continuar')

print('Hasta la proxima!')
