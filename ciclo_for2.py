'''
ciclo_for2.py
script de python que imprima los numeros pares del 2 al 20 usando un ciclo for.
'''

print('Programa que muestra los numeros pares del 2 al 20')

print('metodo 1')

for numero in range (1, 11):
    print(f'par: {numero*2}')


print('--------------------------------------------------------------')

print('metodo 2')

for num  in range(2, 21):
    if num%2==0:
        print(f'par: {num}')

print('----------------------------------------------------------------')

print('metodo 3')

for par in range (2, 21, 2):
    print(f'par: {par}')







print('Saludos')
