from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:   
    item: int
    prox: No | None


def num_itens(p: No | None) -> int:
    '''
    Determina quantos itens existem no encadeamento
    que começa com *p*.
    Exemplos
    >>> num_itens(None)
    0
    >>> num_itens(No(10, None))
    1
    >>> num_itens(No(20, No(10, None)))
    2
    >>> num_itens(No(4, No(20, No(10, None))))
    3
    '''
    
    cont = 0
    
    while p is not None:
        cont += 1
        p = p.prox
    
    return cont