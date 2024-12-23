from __future__ import annotations
from dataclasses import dataclass
from exer21_22 import lst_to_encadeamento

@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None
    
    
def inverte(p: No | None) -> None:
    '''
    Inverte a ordem dos elementos do encadeamento duplo de *p*
    
    Exemplo:
    >>> inverte(lst_to_encadeamento([1, 2, 3]))
    No(ante=None, item=3, prox=No(ante=..., item=2, prox=No(ante=..., item=1, prox=None)))
    >>> inverte(No(None, 1, None))
    No(ante=None, item=1, prox=None)
    >>> inverte(None) is None
    True
    '''
    
    if p is None:
        return None
    
    q = p.prox
    
    p.prox = None
    
    while q is not None:
        futuro_prox = q.prox
        
        q.ante = None 
        q.prox = p
        
        p.ante = q
        p = q
        
        q = futuro_prox
        

    return p
    
    