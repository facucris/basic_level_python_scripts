'''
procedimiento6.py
script python que implemente un procedimiento  que reciba nombre y edad del usuario
y que indique si es mayor o menor de edad
'''

def mayoria_edad(nombre,edad):
    print(f'Hola {nombre}, que bueno volverte a ver!')
    if edad>=18:
        print('Ya eres mayor de edad!')
    else:
        print('Aun eres menor')

mayoria_edad('Facundo',30)
