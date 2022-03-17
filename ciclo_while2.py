'''
ciclo_while2.py
script python que implementa un ciclo while para sumar valores pares y multiplicar
valores impares que se le solicitaran al usuario siempre y cuando no sean 0.
el bucle se usa para solicitar los valores al usuario y multiplicara o sumara
dependiendo del caso.
'''

print('Programa que suma numeros pares y multiplica los impares')

suma = 0
multiplicacion = 1
numero = -1

while numero != 0:
    numero= int(input('Ingraese un numero (0 para salir)'))
    if numero % 2 == 0:
        suma= suma+ numero
    else:
        multiplicacion= multiplicacion*numero
    print(f'suma:{suma}')
    print(f'multiplicacion: {multiplicacion}')

print('Hasta luego!')
