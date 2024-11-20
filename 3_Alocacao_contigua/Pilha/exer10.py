from pilha_arranjo import Pilha

def remove_vazios(p: Pilha) -> None:
    '''
    Remove todos os espaços vazios da pilha.
    
    Exemplos
    >>> p = Pilha()
    >>> p.empilha('um')
    >>> p.empilha('')
    >>> p.empilha('carro')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> remove_vazios(p)
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'um'
    '''
    
    pilha_auxiliar = Pilha()
    
    while not(p.vazia()):
        palavra = p.desempilha()
        if (palavra != ''):
            pilha_auxiliar.empilha(palavra)
    
    while not(pilha_auxiliar.vazia()):
        p.empilha(pilha_auxiliar.desempilha())
    