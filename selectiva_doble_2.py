'''
selectiva_doble_2.py
script en pyhton que simule un sistema de validacion de una plataforma digital
el usuario debera proporcionar usuario y contraseña, si coinciden los valores
se le dara la bienvenida, sino marcara error
'''
user = 'facundo'
password = '1234'

print('Proporciona los siguientes datos')
user1 = input('Usuario: ')
password1 = input('Contraseña: ')
if user == user1 and password == password1:
    print('Bienvenido!')
else:
    print('Datos incorrectos')

print('Buen dia!')
