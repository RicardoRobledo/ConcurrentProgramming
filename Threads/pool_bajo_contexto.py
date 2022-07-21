'''
Created on 4 jun. 2021

@author: RSSpe
'''

import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)


def math_operation(number1, number2):
    time.sleep(1)

    result = number1 + number2
    logging.info(f'Resultado de {number1} + {number2} = {result}')


if __name__ == '__main__':
    
    # Podemos usar el with con objetos que implementen la interface de gestor de contexto
    
    # Para controlar un contexto, se usan los "gestores de contexto" ("context manager") que son
    # objetos que tienen definidos los métodos __enter__ y __exit__. El primero para inicializar
    # el contexto, el segundo para finalizarlo.
    
    # por ejemplo:
    
    #with open("fichero.txt") as f:
        #print(f.read())
    
    # En el ejemplo de arriba el bloque abriendo el fichero y, al acabar, se cerrará el fichero
    # automáticamente, aunque no se haya indicado explícitamente.


    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='facilitos') as executor:

        executor.submit(math_operation, 10, 20)
        executor.submit(math_operation, 40, 50)
        executor.submit(math_operation, 100, 200)

        executor.submit(math_operation, 60, 70)
        
        executor.shutdown() # Con esto estamos apagando la piscina donde indicamos que despues de shutdown
                            # ninguna tarea podra ser asignada a ningun thread y los threads que esten en
                            # ejecucion no se veran interrumpidos
        
        # Nota: el metodo submit nos retorna un futuro



