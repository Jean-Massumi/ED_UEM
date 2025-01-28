from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    val: int
    prox: No | None

def positivos(lst: No) -> No | None:
    '''
    Devolve uma nova lista encadeada somente com os elementos positivos de *lst*.
    
    Exemplo
    >>> positivos(None) is None
    True
    >>> novo_lst = positivos(No(-1, No(-16, No(5, No(-21, No(77, None))))))
    >>> novo_lst
    No(val=5, prox=No(val=77, prox=None))
    '''
    
    if lst is None:
        return None
    
    else:
        if lst.val > 0:
            return No(lst.val, positivos(lst.prox))
        
        else:
            return positivos(lst.prox)



