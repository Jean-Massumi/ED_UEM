from __future__ import annotations
from dataclasses import dataclass
from exer21_22 import lst_to_encadeamento

@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None
    

def palindromo(inicio: No | None, fim: No | None) -> bool:
    '''
    Devolve True se o encadeamento é palindromo. False caso contrário.
    
    Exemplo:
    >>> inicio =  lst_to_encadeamento([3, 3])
    >>> fim = inicio.prox
    >>> palindromo(inicio, fim)
    True
    >>> inicio =  lst_to_encadeamento([3, 1])
    >>> fim = inicio.prox
    >>> palindromo(inicio, fim)
    False
    >>> inicio =  lst_to_encadeamento([1, 3, 1])
    >>> fim = inicio.prox.prox
    >>> palindromo(inicio, fim)
    True
    >>> inicio =  lst_to_encadeamento([3, 4, 5])
    >>> fim = inicio.prox.prox
    >>> palindromo(inicio, fim)
    False
    >>> palindromo(None, None)
    True
    '''
    
    while (inicio is not fim) and (inicio.item == fim.item):
        inicio = inicio.prox
        fim = fim.ante
        
    return inicio is fim
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    