#!/usr/bin/env python3
'''
parecido a el 1 sin el wait_random
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    hace n llamadas a wait_random y retorna una lista con los tiempos de espera
    '''
    # return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    return [await task for task in asyncio.as_completed(
        [task_wait_random(max_delay) for _ in range(n)])]
