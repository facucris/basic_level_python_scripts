'''
procedimiento3.py
script en pyhton que dentro de un procedimiento solicite  nombre  y edad del
usuario y en caso de que sea igual o mayor que 18 le indique que es mayor de
edad, caso contrario le indicara que es menor.
'''


def mayoria_edad():
    nombre=input('Hola como te llamas? ')
    edad= int(input('Cual es tu edad? '))
    if edad>=18:
        print(f'Ya eres mayor de edad {nombre}')
    else:
        print(f'{nombre} aun eres menor ')

mayoria_edad()

print('Nos vemos')
