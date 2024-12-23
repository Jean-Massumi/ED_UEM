from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
def soma1(p: No | None):
    '''
    Modifica cada nó do encadeamento que começa em *p* somando
    1 ao item do nó.
    
    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> soma1(p)
    >>> p
    No(item=11, prox=No(item=21, prox=No(item=31, prox=None)))
    '''
    
    q = p
    while q is not None:
        q.item += 1
        q = q.prox
    