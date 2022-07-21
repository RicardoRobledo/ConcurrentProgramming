'''
Created on 4 jun. 2021

@author: RSSpe
'''

import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


# Timer
# Con timer seremos capaces de decir cuando queremos que un callback se ejecute
def callback():
    
    logging.info('Hola, soy un callback que no ejecuta de forma inmediata')


if __name__ == '__main__':
    
    thread = threading.Timer(3,callback) # Nos retorna un thread
    thread.start()
    
    logging.info('Hola, soy el thread principal')
    logging.info('Estamos a la espera de la ejecuacion del callback')




