#!/usr/bin/env python3
'''
usar 4 veces la funcion async_comprehension y retornar el tiempo que se demora
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    medir el tiempo que se demora en ejecutar 4 veces la funcion
    '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
