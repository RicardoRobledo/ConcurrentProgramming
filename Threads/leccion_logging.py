'''
Created on 4 jun. 2021

@author: RSSpe
'''

import logging

# Debug (10), Info (20), Warning (30), Error (40), Critical (50)

# logging solo muestra mensajes de nivel 30 o superior
# vamos a configurarla
logging.basicConfig(
    #level=10   mensaje a partir del nivel 10
    level=logging.DEBUG, # podemos usar constantes
    format='%(filename)s - %(message)s - %(asctime)s - %(funcName)s - %(levelname)s - %(lineno)s - %(module)s - %(name)s - %(pathname)s - %(thread)s -  %(threadName)s', # Dando formato
    #datefmt='%H:%M:%S',
    #filename='messages.txt' Podemos guardar los mensajes en un archivo para despues inspeccionarlos
)

def mis_mensajes():

    logging.debug('Este es un mensaje de tipo Debug')
    logging.info('Este es un mensaje de tipo Info')
    logging.warning('Este es un mensaje de tipo Warning')
    logging.error('Este es un mensaje de tipo Error')
    logging.critical('Este es un mensaje de tipo Critical')


if __name__ == '__main__':
    mis_mensajes()

