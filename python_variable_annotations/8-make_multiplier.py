#!/usr/bin/env python3
'''
una funcion que retorna una funcion que multiplica un numero por otro?
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    retorna una funcion que multiplica un numero por otro
    '''

    def f(n: float) -> float:
        '''
        retorna el producto de dos numeros
        '''
        return n * multiplier

    return f
