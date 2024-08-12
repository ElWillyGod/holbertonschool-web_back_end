#!/usr/bin/env python3
'''
colocar las annotate variables
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    retorna una lista de tuplas con la secuencia y su longitud
    '''
    
    return [(i, len(i)) for i in lst]
