from __future__ import annotations
from dataclasses import dataclass
from exer21_22 import lst_to_encadeamento

@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None
    
    
def troca_prox(p: No) -> None:
    '''
    Troca p de lugar com p.prox.
    
    Requer que p.prox não seja None.
    
    Examplo:
    >>> p = lst_to_encadeamento([3, 6, 9])
    >>> troca_prox(p)
    >>> p.ante
    No(ante=None, item=6, prox=No(ante=..., item=3, prox=No(ante=..., item=9, prox=None)))
    >>> p.item
    3
    >>> p.ante.item
    6
    >>> p.prox.item
    9
    '''
    
    assert p.prox is not None
    
    # remove p.prox e chama de q
    q = p.prox
    p.prox = q.prox
    
    if p.prox is not None:
        p.prox.ante = p
        
    # insere q
    q.ante = p.ante
    
    if q.ante is not None:
        q.ante.prox = q
        
    q.prox = p
    p.ante = q
    
    
    
def troca_ante(p: No) -> None:
    '''
    Troca *p* de lugar com *p.ante*.
    Requer que *p.ante* seja um No.

    Exemplos
    >>> p = lst_to_encadeamento([7, 4, 6]).prox
    >>> troca_ante(p)
    >>> p
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=6, prox=None)))
    >>> p.item
    4
    >>> p.prox.item
    7
    >>> p.prox.prox.item
    6
    '''
    
    assert p.ante is not None
    
    troca_prox(p.ante)