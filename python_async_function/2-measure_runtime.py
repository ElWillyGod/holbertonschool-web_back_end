#!/usr/bin/env python3
'''
tiempo medio de ejecucion de las async function
'''
import time
import asyncio

wait_n = __import__('2-measure_runtime.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    retorna el tiempo de ejecucion de wait_n
    '''

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
