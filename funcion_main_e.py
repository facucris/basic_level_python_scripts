'''
funcion_main_e.py
script en python que implemente un programa que realice las siguientes conversiones:
-segundos a minutos: recibe segundos y devuelve minutos y segundos.
-segundos a horas: recibe segundos y devuelve horas, minutos y segundos.
-minutos a segundos: recibe minutos y segundos y devuelve segundos.
-minutos a horas: recibe minutos y devuelve horas, minutos y segundos.
Ademas debera implementar un programa que imprima un menu de opciones y la
ejecucion del programa debera comenzar desde una funcion "main" y el programa seguira en ejecucion
mientras el usuario no elija salir.
'''

import os
segundos_por_minutos=60
minutos_por_hora=60
segundos_a_minutos= 1
segundos_a_horas=2
minutos_a_segundos=3
minutos_a_horas=4
salir=0

def seg_min(segundos):
    mins= segundos//segundos_por_minutos
    segs=segundos%segundos_por_minutos
    return mins,segs

def min_seg(minutos):
    segu=minutos*segundos_por_minutos+segundos
    return segu

def min_hora(minutos,segundos):
    hrs=minutos//minutos_por_hora
    minu=minutos%minutos_por_hora
    segs= segundos
    return hrs, minu, segs

def seg_hora(segundos):
    mins, segs = seg_min(segundos)
    hrs, mins,segs =min_hora(mins, segs)
    return hrs, mins, segs

def menu():
    print(f'''                                conversiones
    {segundos_a_minutos}) Segundos a minutos
    {segundos_a_horas}) Segundos a horas
    {minutos_a_segundos}) Minutos a segundos
    {minutos_a_horas}) Minutos a horas
    {salir}) Salir


    ''')

def main():
    continuar= True
    while continuar:
        os.system('cls')
        menu()
        opc= int(input('Selecciona una opcion: '))
        os.system('cls')
        if opc==segundos_a_minutos:
            s= -1
            while 0>s:
                s=int(input('Cantidad de segundos a convertir: '))
            mins, segs=seg_min(s)
            print(f'el equivalente es: {mins}:{segs}')
        elif opc==segundos_a_horas:
            s=-1
            while 0>s:
                s=int(input('Cantidad de segundos a convertir: '))
                hrs, mins, segs=seg_hora(s)
                print(f'el equivalente es: {hrs}:{mins}:{segs}')
        elif opc==minutos_a_segundos:
            m=-1
            while 0>m:
                m=int(input('Cantidad de minutos a convertir: '))
            s=-1
            while 0>s or s>= segundos_por_minutos:
                s=int(input('Cantidad de segundos a convertir: '))
            segs= min_seg(m, s)
            print(f'el equivalente es: {segs}')
        elif opc==minutos_a_horas:
            m=-1
            while 0>m:
                m= int(input('Cantidad de minutos a convertir: '))
            s=-1
            while 0>s or s>segundos_por_minutos:
                s=int(input('Cantidad de segundos a convertir: '))
            hrs, mins, segs=min_hora(m,s)
            print(f'el equivalente es: {hrs}:{mins}:{segs}')
        elif opc==salir:
            print('Nos vemos!')

            continuar=False
        else:
            print('Opcion no valida')

        input('Presiona una tecla para continuar')

if __name__=="__main__":
    main()
