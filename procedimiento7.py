'''
procedimiento7.py
script python que implemente un procedimiento dentro del cual
se muestre la tabla de multipilicar de un numero recibido como argumento que indicara
hasta que multiplo se mostrara dicha tabla, el segundo argunmento  omitira el valor 10.

'''


def tabla(numero, limite=10):
    print(f'                        Tabla de multiplicar del numero {numero}')
    for i in range(1,limite+1):
        print(f'{numero}x{i}={numero*i}')

tabla(7)
tabla(5,13)
print('''



''')

print('Nos vemos!')
