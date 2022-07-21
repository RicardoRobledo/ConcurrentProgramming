'''
Created on 4 jun. 2021

@author: RSSpe
'''

# Los callbacks son para acciones que queremos que se realicen en un futuro

import logging
import requests
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def get_pokemon_name(response_json):
    name = response_json.get('forms')[0].get('name')
    logging.info(f'El nombre del pokemon es:{name}')


def get_name_random(response_json):
    name = response_json.get('results')[0].get('name').get('first')
    logging.info(f'El nombre es:{name}')


def error():
    logging.error('No es posible completar la operacion')


# Holywood
def generate_requests(url, success_callback, error_callback):

    response = requests.get(url)
    
    if response.status_code==200:
        success_callback(response.json())
    else:
        error_callback()


if __name__ == '__main__':

    thread1 = threading.Thread(target=generate_requests, kwargs={'url': 'https://pokeapi.co/api/v2/pokemon/1/',
                                                                'success_callback': get_pokemon_name,
                                                                'error_callback': error
                                                                })

    thread1.start()
    
    # Los mensajes que vemos si no tenemos impresiones son porque requests implementa logging y muestra los
    # mensajes al hacer peticiones con APIS, podemos cambiar el nivel para que no nos aparezcan

    thread2 = threading.Thread(target=generate_requests, kwargs={'url': 'https://randomuser.me/api',
                                                                'success_callback': get_name_random,
                                                                'error_callback': error
                                                                })
    thread2.start()

