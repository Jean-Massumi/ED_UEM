from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
def soma_itens(n: No | None) -> int:
    '''
    Soma todos os itens do do encadeamento e devolve o valor final.
    
    >>> p1 = No(1, No(2, No(3, None)))  
    >>> p2 = No(6, No(9, No(23, None)))  
    >>> p3 = No(99, No(11, No(27, None)))  
    >>> soma_itens(p1)
    6
    >>> soma_itens(p2)
    38
    >>> soma_itens(p3)
    137
    '''
    soma = 0
    
    while n is not None:
        soma += n.item
        n = n.prox
        
    return soma    
    