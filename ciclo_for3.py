'''
ciclo_for3.py
script python que muestra una cuenta regresiva con un ciclo for
'''

import os
import time

for num in range(10, -1, -1):
    os.system('cls')
    print(f'num: {num}')
    time.sleep(1)
else:
    print('boom!')

print('nos vemos')
