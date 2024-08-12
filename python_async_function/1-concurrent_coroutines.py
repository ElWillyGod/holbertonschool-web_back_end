#!/usr/bin/env python3
'''
importar el otro modulo y hacer n llamadas a el
retornar los tiempos de espera en una lista ordenada
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    hace n llamadas a wait_random y retorna una lista con los tiempos de espera
    '''
    # return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    asyncr = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(asyncr)]
