from ed import array


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> CAPACIDADE = 100
    >>> f = Fila(CAPACIDADE)
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''

    valores: array[str]
    # Indíce onde o próximo elemento será inserido
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int

    # O valor para o inicio e o fim são incrementados até chegarem em
    # CAPACIDADE, quando voltam a ser 0.
    #
    # A fila está vazia se inicio == fim e está cheia se o próximo valor para
    # fim é igual ao inicio. Dessa forma, nunca podemos preencher todos os
    # elementos de *valores*, pois senão não seria possível distinguir entre fila
    # cheia e fila vazia. Para horar o valor de CAPACIDADE, inicializamos
    # *valores* com CAPACIDADE + 1 itens.

    CAPACIDADE: int
    # Capacidade que um array terá;
    

    def __init__(self, Capacidade: int) -> None:
        '''
        Cria uma nova fila com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.CAPACIDADE = Capacidade
        self.valores = array(self.CAPACIDADE + 1, '')
        self.inicio = 0
        self.fim = 0

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.

        Requer que a quantidade de elementos na fila seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> CAPACIDADE = 100
        >>> f = Fila(CAPACIDADE)
        >>> for i in range(f.capacidade()):
        ...     f.enfileira(str(i))
        >>> f.enfileira('a')
        Traceback (most recent call last):
        ...
        ValueError: fila cheia
        >>> f.desenfileira()
        '0'
        >>> f.desenfileira()
        '1'
        '''
        if self.cheia():
            raise ValueError('fila cheia')
        
        self.valores[self.fim] = item
        
        self.fim = self.proximo_indice(self.fim)

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.

        Exemplos
        >>> CAPACIDADE = 100
        >>> f = Fila(CAPACIDADE)
        >>> f.desenfileira()
        Traceback (most recent call last):
        ...
        ValueError: fila vazia
        >>> f.enfileira('Márcia')
        >>> f.enfileira('João')
        >>> f.enfileira('Pedro')
        >>> f.desenfileira()
        'Márcia'
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        
        item = self.valores[self.inicio]

        self.inicio = self.proximo_indice(self.inicio)    
    
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.

        Exemplos
        >>> CAPACIDADE = 100
        >>> f = Fila(CAPACIDADE)
        >>> f.vazia()
        True
        >>> f.enfileira('Jorge')
        >>> f.vazia()
        False
        '''
        return self.inicio == self.fim

    def cheia(self) -> bool:
        '''
        Devolve True se a fila está vazia, isto é, a quantidade de elementos na
        fila é igual a *CAPACIDADE*, False caso contrário.
        '''
        # O próximo índice para o fim é igual ao início?
        return self.num_itens() == self.CAPACIDADE


    def num_itens(self) -> int:
        '''
        Devolve a quantidade de elementos de uma fila
        '''
        
        if (self.fim < self.inicio):
            if ((self.fim + 1) == self.inicio):
                return self.CAPACIDADE
            
            return (self.CAPACIDADE + self.fim - self.inicio)
        
        elif (self.fim > self.inicio):
            return self.fim - self.inicio
        
        else:
            return 0
                
                
    def capacidade(self) -> int:
        '''
        Devolve a capacidade da fila 
        '''            
    
        return self.CAPACIDADE
    
    
    def proximo_indice(self, indice: int) -> int:
        '''
        Calcula o próximo indice, a partir do indice atual
        '''
        
        return (indice + 1) % (self.CAPACIDADE + 1)
    
    
    def esvaziar(self) -> None:
        '''
        Esvazia uma fila em tempo constante
        
        Exemplo
        >>> f = Fila(10)
        >>> f.vazia()
        True
        >>> f.enfileira('Márcia')
        >>> f.enfileira('João')
        >>> f.enfileira('Pedro')
        >>> f.vazia()
        False
        >>> f.esvaziar()
        >>> f.vazia()
        True
        '''
    
        self.fim = 0
        self.inicio = 0