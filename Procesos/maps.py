import time
import logging
from multiprocessing import Pool
from clase_pool import is_even

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')


def is_even(number):
    time.sleep(1)
    return number % 2 == 0


def show_result(results):
    logging.info(f'El resultado es: {results}')


if __name__ == '__main__':
    with Pool(processes=2) as executor:

        numbers = [ number for number in range(1, 15) ]
        
        #map_result = executor.map_async(is_even, numbers, callback=show_result) # Lo interesante es que
                                                                                # podemos hacer otras cosas en
                                                                                # lo que los resultados estan
                                                                                # listos
        
        #logging.info(f'Vamos a esperar a que los resultados esten listos')
        
        #map_result.wait(1)
        
        for element in executor.imap_unordered(is_even, numbers): # no nos retorna un objeto directamente ya que es un generador
                                                                  # internamente encontraremos yield
                            
            logging.info(element)
        
        # Aplicaremos imap_unordered cuando el orden no sea relevante




