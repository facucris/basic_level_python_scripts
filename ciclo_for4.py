'''
ciclo_for4.py
script python que muestra la tabla  de multiplicar de un numero que ingrese el usuario.
el usuario tmabien elegira hasta que numero se realiza el ciclo.
'''

numero=int(input('de qu numero quieres ver su tabla de multiplos?'))
limite= int(input('HAsta que  numero quieres ver?'))
print(f'                                           tabla del {numero}')
for num in range (1, limite+1):
    print(f'numero  por multiplo:  {num}+{numero}= {num*numero}')

print('Nos vemos!')
