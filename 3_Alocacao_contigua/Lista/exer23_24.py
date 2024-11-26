from ed import array

# Capacidade inicial alocada para a lista
CAPACIDADE_INICIAL = 4

# Fator de crescimento quanto a lista precisa crescer
FATOR_CRESCIMENTO = 2.0

class Lista:
    '''
    Uma sequência de números.

    Exemplos
    >>> lst = Lista()
    >>> lst.str()
    '[]'
    >>> lst.insere(0, 7)
    >>> lst.insere(1, 20)
    >>> lst.insere(2, 5)
    >>> lst.get(0)
    7
    >>> lst.get(2)
    5
    >>> lst.num_itens()
    3
    >>> lst.str()
    '[7, 20, 5]'
    >>> lst.set(0, 10)
    >>> lst.str()
    '[10, 20, 5]'
    >>> lst.insere(1, 8)
    >>> lst.str()
    '[10, 8, 20, 5]'
    >>> lst.remove(2)
    >>> lst.str()
    '[10, 8, 5]'
    >>> lst.insere(lst.num_itens(), 8)
    >>> lst.str()
    '[10, 8, 5, 8]'
    >>> lst.indice(8)
    1
    >>> lst.remove_item(5)
    >>> lst.str()
    '[10, 8, 8]'
    '''

    valores: array[int]
    tamanho: int

    def __init__(self) -> None:
        '''
        Cria uma nova lista vazia.
        '''
        self.valores = array(CAPACIDADE_INICIAL, 0)
        self.tamanho = 0

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de itens da lista.
        '''
        return self.tamanho

    def get(self, i: int) -> int:
        '''
        Devolve o item que está na posição *i* da lista.

        Requer que 0 <= i < self.num_itens().

        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(1, 20)
        >>> lst.insere(2, 30)
        >>> lst.get(1)
        20
        >>> lst.get(3)
        Traceback (most recent call last):
        ...
        ValueError: índice 3 fora da faixa
        '''
        if i < 0 or self.num_itens() <= i:
            raise ValueError(f'índice {i} fora da faixa')
        return self.valores[i]

    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().

        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(1, 20)
        >>> lst.insere(2, 30)
        >>> lst.set(1, 40)
        >>> lst.str()
        '[10, 40, 30]'
        >>> lst.set(3, 10)
        Traceback (most recent call last):
        ...
        ValueError: índice 3 fora da faixa
        '''
        if i < 0 or self.num_itens() <= i:
            raise ValueError(f'índice {i} fora da faixa')
        self.valores[i] = item

    def insere(self, i: int, item: int):
        '''
        Insere *item* na posição *i* da lista. Os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Requer que 0 <= i <= self.num_itens().

        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(0, 8)
        >>> lst.insere(1, 9)
        >>> lst.insere(3, 14)
        >>> lst.str()
        '[8, 9, 10, 14]'
        >>> lst.insere(10, 50)
        Traceback (most recent call last):
        ...
        ValueError: índice 10 fora da faixa

        >>> lst = Lista()
        >>> for i in range(1000):
        ...     lst.insere(i, i)
        >>> lst.get(0)
        0
        >>> lst.get(999)
        999
        '''
        if i < 0 or self.num_itens() < i:
            raise ValueError(f'índice {i} fora da faixa')

        if self.num_itens() == len(self.valores):
            self.__cresce()

        for j in range(self.tamanho, i, -1):
            self.valores[j] = self.valores[j - 1]
        self.valores[i] = item
        self.tamanho += 1

    def remove(self, i: int):
        '''
        Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...

        Requer que 0 <= i < self.num_itens().

        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(1, 20)
        >>> lst.insere(2, 30)
        >>> lst.remove(1)
        >>> lst.str()
        '[10, 30]'
        >>> lst.remove(2)
        Traceback (most recent call last):
        ...
        ValueError: índice 2 fora da faixa
        '''
        if i < 0 or self.num_itens() <= i:
            raise ValueError(f'índice {i} fora da faixa')
        for j in range(i + 1, self.tamanho):
            self.valores[j - 1] = self.valores[j]
        self.tamanho -= 1

    def remove_item(self, item: int):
        '''
        Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...

        Requer que *item* esteja na lista.

        Exemplos
        >>> lst = Lista()
        >>> lst.insere(0, 10)
        >>> lst.insere(1, 20)
        >>> lst.insere(2, 30)
        >>> lst.remove_item(20)
        >>> lst.str()
        '[10, 30]'
        >>> lst.remove_item(20)
        Traceback (most recent call last):
        ...
        ValueError: valor 20 não encontrado
        '''
        self.remove(self.indice(item))

    def indice(self, item: int) -> int:
        '''
        Devolve a posição da primeira ocorrência de *item* na lista.

        Requer que *item* esteja na lista.
        '''
        for i in range(self.num_itens()):
            if self.valores[i] == item:
                return i
        raise ValueError(f'valor {item} não encontrado')

    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        '''
        s = '['
        if self.num_itens() != 0:
            s += str(self.valores[0])
            for i in range(1, self.num_itens()):
                s += ', ' + str(self.valores[i])
        return s + ']'

    def __cresce(self):
        # Aloca um novo arranjo para valores com a capacidade aumenta por *FATOR_CRESCIMENTO*
        capacidade = int(len(self.valores) * FATOR_CRESCIMENTO)
        valores = array(capacidade, 0)
        for i in range(self.num_itens()):
            valores[i] = self.valores[i]
        self.valores = valores
