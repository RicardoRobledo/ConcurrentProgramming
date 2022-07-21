'''
Created on 4 jun. 2021

@author: RSSpe
'''

# Otra forma de comunicar threads es mediante estructuras de datos
# Listas o Colas, estas fueron diseñadas para trabajar de forma concurrente y segura

import time
import queue
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def show_elements(queue):

    while not queue.empty():
        item = queue.get()

        logging.info(f'El elemento es: {item}')
        
        # Ejecutamos esto cuando dejemos de usar nuestra cola para que se libere de ella y otro thread pueda usarla
        queue.task_done()
        
        time.sleep(0.5)


if __name__ == '__main__':

    queue = queue.Queue() # FIFO
    
    for val in range(1, 20):
        queue.put(val)
    
    logging.info('La cola ya posee elementos')
    
    for _ in range(4):
        thread = threading.Thread(target=show_elements, args=(queue,))
        thread.start()



