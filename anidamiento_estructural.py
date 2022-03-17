'''
anidamiento_estructural.py
script en python que simula un juego de preguntas y respustas
si el usuario responde corretamente, puede continuar de lo contrario
se termina el juego, en caso de responder todas se lo felicita
'''
print('Bienvenid@ pongamos a prueba tu conocimiento: ')
respuesta= int(input('¿Cual es la velocidad de la luz en m/s? '))
if respuesta == 299792458:
    print('¡Correcto!')
    respuesta== int(input('¿Cuanto es 8+8/8*8=?'))
    if  respuesta == 16:
        print('¡Correcto!')
        respuesta =(input('¿De que color eran las mangas del chaleco de Napoleon?'))
        if respuesta == 'Los chalecos no tienen mangas':
            print('¡Correcto! HAz terminado el juego!')

        else:
            print('Respuesta incorrecta ====>GAME OVER')
    else:
        print('Respuesta incorrecta ====>GAME OVER')
else:
    print('Repuesta incorrecta ====>GAME OVER')

print('Buenos dias!')
