'''
Created on 4 jun. 2021

@author: RSSpe
'''

import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 0

lock = threading.Lock()

# RACE CONDITION

def depositos():

    global BALANCE

    for _ in range(0, 100000):
        lock.acquire() # Indicamos que el thread toma posecion de la seccion critica y ninguno otro thread podra hacerlo
        BALANCE += 1 # Sección critica
        lock.release() # liberamos el recurso para que otros threads puedan hacer uso de el


def retiros():

    global BALANCE

    for _ in range(0, 100000):
        #lock.acquire()    Indicamos que el thread toma posecion de la seccion critica y ninguno otro thread podra hacerlo
        #BALANCE -= 1    Sección critica
        #lock.release()    liberamos el recurso para que otros threads puedan hacer uso de el

        # Podemos usar lo de arriba con with y de esta forma no usamos acquire ni release
        
        with lock:
            BALANCE -= 1
            
        # Otra forma es con try
        
        #try:
        #    lock.acquire
        #    BALANCE-=1
        #finally:
        #    lock.release
            
        # Nota: Se recomienda usar con with por la legibilidad


if __name__ == '__main__':
    thread1 = threading.Thread(target=depositos)
    thread2 = threading.Thread(target=retiros)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    logging.info(f'El valor final del balance es: {BALANCE}')


