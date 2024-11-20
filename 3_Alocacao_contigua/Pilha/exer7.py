from pilha_arranjo import Pilha

def esvaziar_pilha(p: Pilha) -> None:
    """
    Esvazia a pilha
    
    Exemplos
    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha("primeiro")
    >>> p.empilha("segundo")
    >>> p.empilha("terceiro")
    >>> p.vazia()
    False
    >>> esvaziar_pilha(p)
    >>> p.vazia()
    True
    """

    while not(p.vazia()):
        p.desempilha()
