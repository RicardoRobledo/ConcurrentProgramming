'''
Created on 4 jun. 2021

@author: RSSpe
'''
import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor

# Debemos evitar generar threads de forma indiscriminada porque es muy costoso

# Con pool de threads podemos generar la n cantidad de threads que necesitemos donde los podremos utilizar cuando
# los necesitemos y podremos reutilizarlos

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)


def math_operation(number1, number2):
    time.sleep(1)

    result = number1 + number2
    logging.info(f'Resultado de {number1} + {number2} = {result}')


if __name__ == '__main__':
    
                                                # podemos poner un prefijo a nuestros threads 
    executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix='facilitos') # Cantidad de threads que queremos generar

    executor.submit(math_operation, 10, 20) # Para poder utilizar un thread usamos submit
    executor.submit(math_operation, 40, 50)

    executor.submit(math_operation, 100, 200)
    executor.submit(math_operation, 60, 70)
    
    # Si queremos ejecutar una tarea, pero los threads estan oupados los threads se agendan
