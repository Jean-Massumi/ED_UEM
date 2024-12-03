from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    >>> n = No(7, None)
    >>> n
    No(item=7, prox=None)
    >>> n = No(1 , n)
    >>> n
    No(item=1, prox=No(item=7, prox=None))
    >>> n = No(2, n)
    >>> n
    No(item=2, prox=No(item=1, prox=No(item=7, prox=None)))
    
    # ou
    >>> n = No(7, None)
    >>> p = n
    >>> n
    No(item=7, prox=None)
    >>> p.prox = No(1, None)
    >>> n
    No(item=7, prox=No(item=1, prox=None))
    >>> p.prox.prox = No(2, None)
    >>> n
    No(item=7, prox=No(item=1, prox=No(item=2, prox=None)))

    '''
    
    item: int
    prox: No | None
    
    


