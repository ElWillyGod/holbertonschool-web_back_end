#!/usr/bin/env python3
'''
    tenemos que retornar en una lista los 10 numeros aleatorios
'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Generador de numeros aleatorios
    '''
    return [i async for i in async_generator()]
