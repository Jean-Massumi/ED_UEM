from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    palavra: str
    prox: No | None
    
    
def mesmo_tamanho_n(lst: No, n: int) -> None:
    '''
    Modifica cada elemento *lst* fazendo com que todas as palavras fiquem com o mesmo
    tamanho *n*.
    
    Se o tamanho da palavra for maior que *n*, os caracteres final devem ser descartados.
    Se o tamanho da palavra for menor que *n*, espaços em brancos devem ser adicionados 
    no final da string.
    
    Exemplo
    >>> lst = None
    >>> lst1 = No("mundo", No("paralelepido", No("estrutura", None)))
    >>> mesmo_tamanho_n(lst, 4) is None
    True
    >>> mesmo_tamanho_n(lst1, 9)
    >>> lst1
    No(palavra='mundo    ', prox=No(palavra='paralelep', prox=No(palavra='estrutura', prox=None)))
    '''


    if lst is None:
        return None
    
    else:
        if len(lst.palavra) > n:
            lst.palavra = lst.palavra[:n]

        elif len(lst.palavra) < n:
            espacos = n - len(lst.palavra)
            lst.palavra = lst.palavra + " " * espacos

    mesmo_tamanho_n(lst.prox, n)
    
    