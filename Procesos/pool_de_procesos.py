'''
Created on 5 jun. 2021

@author: RSSpe
'''

import logging
from concurrent.futures import ProcessPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:

        future = executor.submit(is_even, 10)
        future.add_done_callback(
            lambda future: logging.info(f'El numero es par? {future.result()}')
        )
        
        future = executor.submit(is_even, 1895)
        future.add_done_callback(
            lambda future: logging.info(f'El numero es par? {future.result()}')
        )


