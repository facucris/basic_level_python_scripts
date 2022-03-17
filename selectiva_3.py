'''
selectiva_3.py
script en python que solicite la calificacion y cantidad de asistencias a un curso.
 Si la calificacion es mayor o igual que 60 y la cantidad de asistencias es mayor que 20 entonces que inidique que ha aprobado
'''
calificacion = int(input('¿Cual es tu calificacion?'))
asistencias = int(input('¿Cuantas asistencias tienes?'))

if calificacion >= 60 and asistencias >=20:
    print('Felicidades! Aprobaste el curso!')
    if calificacion >=95:
        print('Sobresaliente!')

print('¡Sigue avanzando!')
