#!/usr/bin/env python3
'''
rango de una pagian
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
