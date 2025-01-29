from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    val: int
    prox: No | None
    
def tira_0(lst: No) -> None:
    '''
    Modifica *lst* tirando todas as ocorrências no valor 0.
    
    Exemplo
    
    >>> tira_0(None) is None
    True
    >>> lst = No(0, No(0, No(23, No(44, None))))
    >>> lst1 = No(44, No(0, No(0, No(71, None))))
    >>> lst2 = No(56, No(21, No(0, No(0, None))))
    >>> lst3 = No(31, No(0, No(0, No(90, No(0, No(56, None))))))
    >>> tira_0(lst)
    >>> tira_0(lst1)
    >>> tira_0(lst2)
    >>> tira_0(lst3)
    >>> lst
    No(val=23, prox=No(val=44, prox=None))
    >>> lst1
    No(val=44, prox=No(val=71, prox=None))
    >>> lst2
    No(val=56, prox=No(val=21, prox=None))
    >>> lst3
    No(val=31, prox=No(val=90, prox=No(val=56, prox=None)))
    '''

    if lst is None:
        return None
    
    if lst.val == 0:
        if lst.prox is not None:
            lst.val = lst.prox.val
            lst.prox = lst.prox.prox
            tira_0(lst) 
            
    else:
        if lst.prox is not None and lst.prox.val == 0:
            lst.prox = lst.prox.prox
            tira_0(lst)
            
        else:
            tira_0(lst.prox)

