'''
funciones3.py
script python que implementa una funcion para convertir grados fahrenheit a celsius.
'''

def grados():
    f=float(input('Grados fahrenheit: '))
    c=(f-32)/1.8
    return c

celsius= grados()
print(f'celsius= {celsius :.2f}')

print('Hasta la proxima!')
