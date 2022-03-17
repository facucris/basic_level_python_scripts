'''
funciones6.py
script de python que implement una funcion encargada de convertir una cantidad
de segundos a minutos y segundos. La funcion recibira como argumentos una cantidad de segundos
y debera devolver la cantidad de minutos y segundos equivalente
'''

def seg_a_min(segundos):
    m=segundos//60
    s=segundos%60
    return m, s


print('Programa que convierte segundos a minutos y segundos')

seg= int(input('Introduce los segundos: '))

min, segu = seg_a_min(seg)
print(f'el equivalente es: {min}:{segu}')

print('Nos vemos')
