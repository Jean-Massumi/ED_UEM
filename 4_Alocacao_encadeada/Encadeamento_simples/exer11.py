from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
def lst_to_encadeado(lista: list[int]) -> No | None:
    '''
    Transforma uma lista de números em um encadeamento de números.
    
    Exemplo
    >>> lista = [1, 2, 3, 4, 5]
    >>> n = lst_to_encadeado(lista)
    >>> n
    No(item=1, prox=No(item=2, prox=No(item=3, prox=No(item=4, prox=No(item=5, prox=None)))))
    >>> n1 = lst_to_encadeado([])
    >>> n1
    >>> n1 is None
    True
    '''
    
    no: No | None = None
    
    if (len(lista) > 0):
        no = No(lista[0], None)
        q = no
        
        for i in range(1, len(lista)):
            q.prox = No(lista[i], None)
            q = q.prox
            
    return no