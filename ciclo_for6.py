'''
ciclo_for6.py
script en python que muestre uno a uno los caracteres de una palabra o frase.
Por ejemplo si fuese "Hola" se deberia imprimir:
H
o
l
a

'''
frase= input('Ingresa una frase o palabra: ')
print('Los caracteres de tu frase o palabra son: ')
for caracteres in frase :
    print(f'{caracteres}')
