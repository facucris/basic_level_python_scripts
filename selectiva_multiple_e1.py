'''
selectiva_multiple_e1.py
script en python que simula una calculadora con todas las operaciones aritmeticas basicas
menu que se mostrara:
1)suma
2)resta
3)multiplicacion
4)division
5)division entera
6)modulo
7)potencia

'''

suma =1
resta= 2
multiplicacion = 3
division = 4
division_entera= 5
modulo= 6
potencia = 7

print(f'''                      Calculadora
{suma})suma
{resta})resta
{multiplicacion})multiplicacion
{division})division
{division_entera})division_entera
{modulo})modulo
{potencia})potencia

''')

opc= int(input('Selecciona una opcion: '))
if suma<=opc<=potencia:
    op_1= int(input('Primer operando: '))
    op_2= int(input('Primer operando: '))
    if opc ==suma:
        print(f'{op_1}+{op_2}={op_1+op_2}')
    elif opc==resta:
        print(f'{op_1}-{op_2}={op_1-op_2}')

    elif opc==multiplicacion:
        print(f'{op_1}*{op_2}={op_1*op_2}')
    elif opc==division:
        if op_2 != 0:
            print(f'{op_1}/{op_2}={op_1/op_2}')
        else:
            print('Operacion no definida')
    elif opc==division_entera:
        if op_2 != 0:
            print(f'{op_1}//{op_2}={op_1//op_2}')
        else:
            print('Operacion no valida')
    elif opc==modulo:
        if op_2 != 0:
            print(f'{op_1}%{op_2}={op_1% op_2}')
        else:
            print('Operacion no valida')
    elif opc==potencia:
        print(f'{op_1}**{op_2}={op_1**op_2}')


else:
    print('Opcion no valida')

print('Nos vemos!')
