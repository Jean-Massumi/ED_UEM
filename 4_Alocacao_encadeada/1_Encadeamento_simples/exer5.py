from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None
    
    
def lst_to_encadeado(lista: list) -> No | None:    
    '''
    Transforma uma lista de números que devolve em um encadeamento 
    com os mesmo itens da lista, só que em ordem contraria
    
    Exemplo
    >>> lista = (1, 2, 3, 4)
    >>> No = lst_to_encadeado(lista)
    >>> No
    No(item=4, prox=No(item=3, prox=No(item=2, prox=No(item=1, prox=None))))
        
    >>> lista = ()
    >>> No = lst_to_encadeado(lista)
    >>> No
    >>> No is None
    True
    '''
    
    no: No | None = None
    
    for elem in lista:
        no = No(elem, no)
            
    return no
    