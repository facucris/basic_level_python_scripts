'''
funciones5.py
script en python que implemente una funcion para calcular el IMC
del usuario: la funcion debe recibir la altura y peso del usuario y entrgara
como resultado el IMC.
'''

def imc(peso, altura):
    return peso/(altura**2)

print('Programa para calcular el IMC')
print('Ingresa los siguientes datos: ')
p=float(input('peso: '))
a= float(input('altura: '))

print(f'IMC: {imc(p,a)}')
