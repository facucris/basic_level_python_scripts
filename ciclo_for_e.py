'''
ciclo_for_e.py
script en python que muestre un cronometro en formato de 24hs, el despliegue sera en h:m:s
Comenzar en 00:00:00 y llegara hasta 23:59:59. Implementa limpieza de pantalla y retardo de 1 segundo
para que solo se vea una hora en pantalla.
'''
import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('cls')
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)
