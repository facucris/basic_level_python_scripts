'''
funcion_main.py
script pyhton que implementa un procedimiento para saludar al ususario de manera
personalizada, el procedimiento debera recibir el nombre del usuario como argumento.
Se debera realizar otro procedimiento llamado "main" desde e cual se da inicio al programa y
 primer procedimiento descrito
 '''

def saludo(nombre):
    print(f'Gusto en conocerte, {nombre}')

def main():
    usuario= input('Hola, como te llamas? ')
    saludo(usuario)


if __name__ == '__main__':
    main()
