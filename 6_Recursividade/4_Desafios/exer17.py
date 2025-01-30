from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    val: int
    prox: No | None
    
    
def eh_prefixo(lsta: No | None, lstb: No | None) -> bool:
    '''
    Devolve True se *lsta* é prefixo de *lstb*, isto é *lstb* começa com *lsta*.
    
    Exemplos
    >>> prefixo(None, None)
    True
    >>> prefixo(None, No(4, No(7, No(1, No(11, None)))))
    True
    >>> prefixo(No(1, No(3, None)), None)
    False
    >>> prefixo(No(2, No(7, None)), No(2, No(7, No(15, None))))
    True
    >>> prefixo(No(2, No(7, None)), No(4, No(7, No(1, No(11, None)))))
    False
    '''
    if lsta is None:
        return True
    
    elif lstb is None:
        return False
    
    else:
        return lsta.val == lstb.val and eh_prefixo(lsta.prox, lstb.prox)









