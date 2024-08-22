#!/usr/bin/env python3
'''
generador de async
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Generador de numeros aleatorios
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
