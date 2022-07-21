'''
Created on 4 jun. 2021

@author: RSSpe
'''

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


class ThreadFacilito(threading.Thread):
    
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)


    def run(self):
        
        while True:
            logging.info('Aqui debemos colocar todas las tares que queremos que se ejecuten de forma concurrente')
            time.sleep(1)


if __name__ == '__main__':
    
    thread = ThreadFacilito('Thread-facilito', True)
    thread.start()
    
    time.sleep(3)
    logging.info('Fin del programa')




