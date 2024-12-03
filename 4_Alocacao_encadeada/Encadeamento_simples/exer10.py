from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
def adiciona_final(n: int, p: No | None) -> None:
    '''
    Adiciona o *n* em um novo Nó no fim do encadeamento.
    
    Exemplo
    >>> p = No(3, No(1, No(8, None)))
    >>> n = 5
    >>> adiciona_final(n, p)
    >>> p
    No(item=3, prox=No(item=1, prox=No(item=8, prox=No(item=5, prox=None))))
    '''
    
    q = p
    
    if q is not None:
        while q.prox is not None:
            q = q.prox
            
        q.prox = No(n, None)
    
    else:
        q = No(n, None)
