#!/usr/bin/env python3
'''
complext types
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    retorna una tupla
    '''

    return (k, v * v)
