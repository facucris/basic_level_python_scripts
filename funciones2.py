'''
script python que implemente una funcion que calcule el indice de
masa corporal.
'''

def imc():
    peso=float(input('ingrese su peso: '))
    altura= float(input('ingrese su altura: '))
    imc= peso/(altura**2)
    return imc

print('Vamos a calcular tu indice de masa corporal')
imc= imc()
print(f'Tu IMC es : {imc :.2f}')

print('nos vemos')
