'''
selectiva_multiple1.py
script de pyhton que muestre un menu con un listado de paises de America y si el Usuario
selecciona alguno del menu se le mostrara el nombre de la capital de dicho pais
'''

Brasil = 1
Argentina= 2
Peru= 3
Bolivia= 4
Chile= 5
Uruguay= 6

print('''                        Paises de America:
1)Brasil
2)Argentina
3)Peru
4)Bolivia
5)Chile
6) Uruguay
''')
opc = int(input('Selecciona una opcion'))

if opc== Brasil:
    print('Brasilia')
elif opc== Argentina:
    print('Buenos Aires')
elif opc==Peru:
    print('Lima')
elif opc==Bolivia:
    print('La Paz')
elif opc==Chile:
    print('Santiago')
elif opc==Uruguay:
    print('Montevideo')
else:
    print('Opcion no valida')
