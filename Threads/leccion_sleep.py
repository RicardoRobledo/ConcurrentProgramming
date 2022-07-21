'''
Created on 4 jun. 2021

@author: RSSpe
'''

import time
import logging
import threading

#sleep(segundos)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s : %(message)s'
)

def task():
    logging.info('Nos encontramos ejecutando una nueva tarea')
    time.sleep(2)
    logging.info('Tarea finalizada')


if __name__ == '__main__':

    #thread = threading.Thread(target=task)
    #thread.start()
    
    # --------------------------------------------
    
    # Una buena practica con el modulo time es realizar un reloj digital
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(thread)s %(threadName)s : %(message)s'
    )
    
    contador = 0
    
    while True:
        time.sleep(1)
        contador += 1
        logging.info(f'Tiempo transcurrido: {contador} segundos')


