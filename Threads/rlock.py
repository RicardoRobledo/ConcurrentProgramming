'''
Created on 4 jun. 2021

@author: RSSpe
'''

# Uno de los problemas de la clase lock es que el recurso solo
# puede ser adquirido una sola vez hasta que sea liberado

import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 100

# Lock y RLock
lock = threading.RLock()
# Usamos RLock porque hay casos donde usamos Lock para indicar que esta ocupado, pero al volver a hacerlo
# nuestro programa no hace nada porque encontramos que esta a la espera de que se libere y se quedan
# sin hacer nada porque esa ocupado y mientras esperamos que se libere, pero no ha sido liberado donde
# RLock indica que puede ser adquirido multiples veces por el mismo thread


if __name__ == '__main__':

    lock.acquire() # Estado: Ocupado

    lock.acquire() # A la espera de que sea liberado

    BALANCE -= 10

    lock.release() # Liberado

    lock.release() # Liberado
    
    # Nota: La misma cantidad de veces adquiridas es liberadas

    logging.info(f'Finalizamos el thread principal con el balance: {BALANCE}')


