from ed import array

CAPACIDADE = 100


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

    def __init__(self) -> None:
        '''
        Cria uma nova fila com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.valores = array(CAPACIDADE + 1, '')
        self.inicio = 0
        self.fim = 0

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
        if self.cheia():
            raise ValueError('fila cheia')
        self.valores[self.fim] = item
        if self.fim == CAPACIDADE:
            self.fim = 0
        else:
            self.fim += 1

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
        item = self.valores[self.inicio]
        if self.inicio == CAPACIDADE:
            self.inicio = 0
        else:
            self.inicio += 1
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
        return self.inicio == self.fim

    def cheia(self) -> bool:
        '''
        Devolve True se a fila está vazia, isto é, a quantidade de elementos na
        fila é igual a *CAPACIDADE*, False caso contrário.
        '''
        # O próximo índice para o fim é igual ao início?
        return self.fim + 1 == self.inicio or \
            self.fim == CAPACIDADE and self.inicio == 0
