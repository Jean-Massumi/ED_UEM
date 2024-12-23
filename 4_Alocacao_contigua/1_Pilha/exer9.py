from ed import array

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(50)
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    valores: array[str]
    # O índice do elemento que está no topo da pilha,
    # -1 se a pilha está vazia.
    topo: int

    def __init__(self, CAPACIDADE) -> None:
        '''
        Cria uma nova pilha com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.capacidade = CAPACIDADE
        self.valores = array(self.capacidade, '')
        self.topo = -1

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> capacidade = 50
        >>> p = Pilha(capacidade)
        >>> for i in range(capacidade):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.desempilha() == str(capacidade - 1)
        True
        '''
        
        if self.cheia():
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha(50)
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
        '''
        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(50)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1

    def cheia(self) -> bool:
        """
        Devolver True se a pilha está cheia, False caso contrário.
        
        Exemplos
        >>> p = Pilha(50)
        >>> p.cheia()
        False
        >>> for i in range(50):
        ...     p.empilha(i)
        >>> p.cheia()
        True
        """
    
        return self.topo >= self.capacidade - 1
    

    def capacidade_restante(self) -> int:
        '''
        Devolve a capacidade restante da pilha.
        
        Exemplos
        >>> p = Pilha(50)
        >>> p.empilha(1)
        >>> p.empilha(2)
        >>> p.empilha(3)
        >>> p.capacidade_restante()
        47
        '''
        
        return (self.capacidade - 1) - self.topo
    
    
    def esvazia(self) -> None:
        '''
        Esvazia a pilha por completo em tempo constante.
        
        Exemplos
        >>> p = Pilha(50)
        >>> p.vazia()
        True
        >>> p.empilha(1)
        >>> p.empilha(2)
        >>> p.vazia()
        False
        >>> p.esvazia()
        >>> p.vazia()
        True
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        '''
        self.topo = -1
        