'''
selectiva_e1.py
script en python que implemente un sistema de redondeo de calificaciones
el usuario ingresara su calificacion, si esta  le falta 4 puntos o menos para el
proximo multiplo de 10 se redondeara hacia arriba, caso contrario, no se redondea.
ejemplo:
si obtiene 66, sera 70
si obtiene 65, sera 65
'''

calificacion = int(input('Que calificacion obtuviste?'))
residuo = calificacion % 10
mensaje = 'Tu calificacion no amerita redondeo'

if 0 <=calificacion <= 100 and residuo >= 6:
    calificacion = calificacion + (10 - residuo)
    mensaje = f'Tu calificacion es {calificacion}'

print(mensaje)
print('Ten un buen dia')
