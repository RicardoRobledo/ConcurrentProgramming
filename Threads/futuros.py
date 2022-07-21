'''
Created on 4 jun. 2021

@author: RSSpe
'''

import time
import logging
import threading


from concurrent.futures import Future


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Futures = Abstracción de un resultado
# Javascript = Promesas

# Un futuro representa un valor eventual

def callback_future(future):

    logging.info('Hola, soy un callback que se ejecuta hasta que el futuro posea un valor')
    logging.info(f'El futuro es: {future.result()}')


if __name__ == '__main__':

    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: logging.info('Hola soy un lambda')
    )
    
    logging.info('Comenzamos una tarea muy compleja')
    
    time.sleep(2)

    logging.info('Terminamos la tarea compleja')
    
    logging.info('Vamos a asignar un valor al futuro')
    
    future.set_result('CodigoFacilito') # Los callbacks se ejecutan cuando el futuro tenga un valor
    
    logging.info('El futuro ya posee un valor')

    



