'''
ciclo_for7.py
script en python que pregunte al usuario una cantidad de numeros a ingresar, le
solicite dichos valores y finalmente imprima el promedio de los mismos
'''

acumulador= 0
print('Vamos a calcuar un promedio: ')
total_datos= int(input('Cuantos datos deseas registrar?'))

for valores in range(total_datos):
    numero= int(input(f'Ingresa el valor : {valores +1}'))
    acumulador += numero


promedio =acumulador / total_datos
print(f'el promedio es: {promedio}')

print('nos vemos')
