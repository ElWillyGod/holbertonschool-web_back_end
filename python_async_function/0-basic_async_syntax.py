#!/usr/bin/env python3
'''
no se que tiene que hacer esto
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    espera un tiempo aleatorio
    '''

    retraso = random.uniform(0, max_delay)
    await asyncio.sleep(retraso)
    return retraso
