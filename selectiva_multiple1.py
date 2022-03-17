'''
selectiva_multiple1.py
script en python que solicite al usuario una calificacion y una cantidad de asistencias a un curso
si la calificacion y cantidad de asitencias son aprobatorias, se le felicita por su logro, caso contrario se le indicara en que fallo
calificacion minima aprobatoria = 60
cantidad minima asistencias = 24
'''

min_cal = 60
min_asis = 24

print('Por favor ingresa los isguientes datos: ')
cal = int(input('Calificacion: '))
asis = int(input('Asistencias: '))

if cal>=min_cal and asis>=min_asis:
    print('Felicitaciones! Aprobaste!!')

elif cal<min_cal and asis>=min_asis:
    print(f'Calificacion insuficiente, el minimo es: {min_cal}')

elif cal>=min_cal and asis<min_asis:
    print(f'Asistencias insuficientes, el minimo es: {min_asis}')

else:
    print('Calificacion y asistencias insuficientes')

print('Buenos dias')
