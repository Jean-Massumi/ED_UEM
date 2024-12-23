from __future__ import annotations
from dataclasses import dataclass
from exer21_22 import lst_to_encadeamento

@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None
    
    
def insere_ordenado(num: float, p: No | None) -> No | None:
    '''
    Insere *num* em um novo nó no encadeamento *p*, mantendo os itens
    em ordem não decrescente. 
    Retorna o novo início do encadeamento. 
    
    Exemplo:
    >>> insere_ordenado(78, None)
    No(ante=None, item=78, prox=None)
    >>> insere_ordenado(5, lst_to_encadeamento([1, 2, 3]))
    No(ante=None, item=1, prox=No(ante=..., item=2, prox=No(ante=..., item=3, prox=No(ante=..., item=5, prox=None))))
    >>> insere_ordenado(7, lst_to_encadeamento([4, 9, 14]))
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=9, prox=No(ante=..., item=14, prox=None))))
    >>> insere_ordenado(31, lst_to_encadeamento([45, 67, 122]))
    No(ante=None, item=31, prox=No(ante=..., item=45, prox=No(ante=..., item=67, prox=No(ante=..., item=122, prox=None))))
    '''
    
    novo_no = No(None, num, None)    

    if p is None or num < p.item:
        novo_no.prox = p
        
        if p:
            p.ante = novo_no
        
        return novo_no
    
    q = p
    
    while (q.prox is not None) and (num >= q.prox.item):
        q = q.prox


    novo_no.prox = q.prox
    if q.prox is not None:
        q.prox.ante = novo_no
        
    novo_no.ante = q
    q.prox = novo_no
        
    return p
        