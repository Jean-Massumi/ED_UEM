from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None
    
    
def lst_to_encadeamento(lst: list[int]) -> No | None:
    '''
    Transforma *lst* em um encadeamento duplo com os mesmo itens da lista 
    de entrada na ordem que eles aparecem na lista.
    
    Exemplo
    >>> lst = [1, 2, 3, 4]
    >>> nodes = lst_to_encadeamento(lst)
    >>> nodes
    No(ante=None, item=1, prox=No(ante=..., item=2, prox=No(ante=..., item=3, prox=No(ante=..., item=4, prox=None))))
    >>> lst1 = []
    >>> nodes1 = lst_to_encadeamento(lst1)
    >>> nodes1 is None
    True
    '''
    
    if lst == []:
        return None
    
    nodes = No(None, lst[0], None)
    aux = nodes

    for num in lst[1:]:
        novo_no = No(None, num, None)

        aux.prox = novo_no
        novo_no.ante = aux
        aux = aux.prox
        
    return nodes  
  
  
  
  
def lst_to_encadeamento_reverse(lst: list[int]) -> No | None:
    '''
    Transforma *lst* em um encadeamento duplo com os mesmo itens da lista 
    de entrada em ordem contrária.
    
    Exemplo
    >>> lst = [1, 2, 3, 4]
    >>> nodes = lst_to_encadeamento_reverse(lst)
    >>> nodes
    No(ante=None, item=4, prox=No(ante=..., item=3, prox=No(ante=..., item=2, prox=No(ante=..., item=1, prox=None))))
    >>> lst1 = []
    >>> nodes1 = lst_to_encadeamento_reverse(lst1)
    >>> nodes1 is None
    True
    '''
    
    if lst == []:
        return None
    
    nodes = No(None, lst[0], None)

    for num in lst[1:]:
        novo_no = No(None, num, None)
        
        nodes.ante = novo_no
        novo_no.prox = nodes
        nodes = novo_no
        
    return nodes  
      