from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
def maximo(n: No | None) -> int:
    '''
    Encontra o valor maximo entre todos os itens do enccadeamento.
    
    Exemplo
    >>> n1 = No(11, No(4, No(7, No(1, None))))
    >>> n2 = No(14, No(43, No(67, No(21, None))))
    >>> n3 = No(42, No(77, No(48, No(101, None))))
    >>> n4 = No(4, No(213, No(2, No(213, None))))
    >>> maximo(n1)
    11
    >>> maximo(n2)
    67
    >>> maximo(n3)
    101
    >>> maximo(n4)
    213
    >>> maximo(None)
    0
    '''
    
    maior = 0
    
    while n is not None:
        if n.item > maior:
            maior = n.item
        
        n = n.prox
    
    return maior
    