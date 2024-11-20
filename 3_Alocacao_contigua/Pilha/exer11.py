from pilha_arranjo import Pilha

def inverte_pilha(p: Pilha) -> None:
    '''
    Inverte a ordem dos elementos da *p* Pilha.
    
    Exemplos
    >>> p = Pilha()
    >>> p.empilha('banana')
    >>> p.empilha('arco')
    >>> p.empilha('mouse')
    >>> inverte_pilha(p)
    >>> p.desempilha()
    'banana'
    >>> p.desempilha()
    'arco'
    >>> p.desempilha()
    'mouse'
    '''
    
    pilha_auxiliar = Pilha()
       
    for i in range(p.topo + 1):
        pilha_auxiliar.empilha(p.valores[i])
        
    while not(p.vazia()):
        p.desempilha()     
        
    while not(pilha_auxiliar.vazia()):
        p.empilha(pilha_auxiliar.desempilha())
        