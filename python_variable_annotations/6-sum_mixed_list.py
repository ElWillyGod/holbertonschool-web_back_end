#!/usr/bin/env python3
'''
retornar la suma de los elementos de una lista
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    sumar de todos lo elementos de float de la lista
    '''

    return sum(mxd_list)
