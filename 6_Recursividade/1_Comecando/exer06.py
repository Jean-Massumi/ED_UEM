from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    val: int
    prox: No | None


def valor_max(lst: No) -> int | None:
    '''
    Encontra e devolve o valor máximo de *lst*.
    
    Se *lst* for vazia, devolve None.
    
    Exemplo
    >>> lst1 = None
    >>> lst2 = No(15, No(11, No(5, None)))
    >>> lst3 = No(10, No(22, No(14, None)))
    >>> lst4 = No(55, No(44, No(67, None)))
    >>> valor_max(lst1) is None
    True
    >>> valor_max(lst2)
    15
    >>> valor_max(lst3)
    22
    >>> valor_max(lst4)
    67
    '''

    if lst is None:
        return None
    
    else:
        if lst.prox is None:
            return lst.val
        
        else:
            return max(lst.val, valor_max(lst.prox))

