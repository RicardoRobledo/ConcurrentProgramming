'''
Created on 4 jun. 2021

@author: RSSpe
'''

# Hay varias formas de comunicar threads entre si, como lo seria una variale global
# aunque hay muchas mas para esto podemos usar eventos 

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def thread_1(event):

    logging.info('Estoy a la espera de la señal!')
    
    event.wait()
    
    logging.info('La señal fue dada, la bandera es True')
    print(f"asdsad {event.is_set()}")


def thread_2(event):

    while not event.is_set(): # is_set() es para saber si la señal fue dada
        logging.info('A la espera de la señal')
        time.sleep(0.5)


if __name__ == '__main__':
    
    event = threading.Event() # Con Event podemos comunicar threads
    # Nuestro evento internamente funciona mediante una bandera como verdadero o falso
    # Bandera = True o False
        
    thread1 = threading.Thread(target=thread_1, args=(event,))
    thread2 = threading.Thread(target=thread_2, args=(event,))

    thread1.start()
    thread2.start()
    
    time.sleep(2)

    event.set() # Estaremos dando la señal
    
    event.clear() #Es para colocar la bandera otra vez en False



