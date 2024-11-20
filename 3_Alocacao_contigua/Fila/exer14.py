from pilha_arranjo import Pilha
from fila_arranjo_fim import Fila

def inverte_elementos_fila(f: Fila) -> None:
    '''
    Inverte a ordem dos elementos de uma fila.
    
    Exemplos
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira('primeiro')
    >>> f.enfileira('segundo')
    >>> f.enfileira('terceiro')
    >>> f.vazia()
    False
    >>> inverte_elementos_fila(f)
    >>> f.desenfileira()
    'terceiro'
    >>> f.desenfileira()
    'segundo'
    >>> f.desenfileira()
    'primeiro'
    >>> f.vazia()
    True
    '''

    pilha_auxiliar = Pilha()
    
    while (not (f.vazia())):
        pilha_auxiliar.empilha(f.desenfileira())
    
    while (not (pilha_auxiliar.vazia())):
        f.enfileira(pilha_auxiliar.desempilha())
    