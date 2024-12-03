from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None


def copia(p: No | None) -> No | None:
    '''
    Cria e devolve uma cópia do encadeamento que inicia em *p*.
    
    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> q = copia(p)
    >>> # quando mudamos p,
    >>> # q não é alterado pois é uma cópia
    >>> p.item = 1
    >>> p.prox.item = 2
    >>> p.prox.prox.item = 3
    >>> p
    No(item=1, prox=No(item=2, prox=No(item=3, prox=None)))
    >>> q
    No(item=10, prox=No(item=20, prox=No(item=30, prox=None)))
    
    # Exemplo para o None
    >>> copia(None)
    '''
    
    q: No | None = None
    
    if p is not None:
        q = No(p.item, None)
        ref_q = q
        
        ref_p = p.prox
        
        while ref_p is not None:
            ref_q.prox = No(ref_p.item, None)
            ref_p = ref_p.prox
            ref_q = ref_q.prox

    return q