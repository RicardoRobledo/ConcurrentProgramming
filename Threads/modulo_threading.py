'''
Created on 4 jun. 2021

@author: RSSpe
'''

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def nueva_tarea():
    
    current_thread = threading.current_thread()
    name = current_thread.getName()
    id = threading.get_ident()
    
    
    logging.info(f'El thread actual es: {current_thread}, su nombre es: {name}')
    print(f'su id es:{id}')


if __name__ == '__main__':
    
    thread1 = threading.Thread(target=nueva_tarea, name='thread-facilito')
    thread1.start()
    
    # Obtener threads vivos
    
    #logging.info(f'Los threads vivos son: {threading.enumerate()}')
    
    for thread in threading.enumerate():
        logging.info(thread)
        if thread==threading.main_thread():
            logging.info('Nos encontamos en el thread principal')



