from ed import array

CAPACIDADE = 10000


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
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
    # Indíce do último elemento da fila, -1 se a fila está vazia.
    fim: int

    # O início da fila é sempre na posição 0. Em enfileira o fim é incrementado
    # e em desenfileira decrementado e todos os elementos são movidos para a
    # posição anterior.

    def __init__(self) -> None:
        '''
        Cria uma nova fila com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.valores = array(CAPACIDADE, '')
        self.fim = -1

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.

        Requer que a quantidade de elementos na fila seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> f = Fila()
        >>> for i in range(CAPACIDADE):
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
        if self.fim >= CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.

        Exemplos
        >>> f = Fila()
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
        item = self.valores[0]
        for i in range(1, self.fim + 1):
            self.valores[i - 1] = self.valores[i]
        self.fim -= 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.

        Exemplos
        >>> f = Fila()
        >>> f.vazia()
        True
        >>> f.enfileira('Jorge')
        >>> f.vazia()
        False
        '''
        return self.fim == -1
