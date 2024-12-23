from ed import array

class FilaDupla:
    '''
    Uma coleção de string que insere e remove no início e 
    no fim da fila.
    
    >>> f = FilaDupla(4)
    >>> f.vazia()
    True
    >>> f.cheia()
    False
    >>> f.queue_start('Python')
    >>> f.queue_end('Java')
    >>> f.queue_end('Rust')
    >>> f.queue_start('C++')
    >>> f.vazia()
    False
    >>> f.cheia()
    True
    >>> f.dequeue_end()
    'Rust'
    >>> while not(f.vazia()):
    ...     f.dequeue_start()      
    'C++'
    'Python'
    'Java'

    '''
    valores: array[str]
    # Estrutura de armazenamento

    Capacidade: int
    # Capacidade de elementos que um array irá suportar

    inicio: int
    # Índice do início da fila.

    fim: int    
    # Índice do fim da fila.

    tamanho: int
    # Quantidade atual de elementos da fila.
    
    def __init__(self, capacidade: int):
        '''
        Cria uma nova fila com *capacidade* para armazenar elementos.
        '''
        self.valores = array(capacidade + 1, '')
        self.Capacidade = capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0 
    
    
    def queue_start(self, item: str) -> None:
        '''
        Insere um elemento no início da fila.
        
        Exemplos
        >>> f = FilaDupla(2)
        >>> f.queue_start('1')
        >>> f.queue_start('2')
        >>> f.queue_start('3')
        Traceback (most recent call last):
        ...
        ValueError: Fila cheia
        >>> f.dequeue_start()
        '2'
        >>> f.dequeue_end()
        '1'
        '''
        
        if (self.cheia()):
            raise ValueError('Fila cheia')
        
        self.inicio = (self.inicio - 1) % self.Capacidade
        self.valores[self.inicio] = item
        self.tamanho += 1
        
        
        
    def dequeue_start(self) -> str:
        '''
        Remove e devolve um elemento no início da fila.
        
        Exemplos
        >>> f = FilaDupla(4)
        >>> f.queue_start('1')
        >>> f.queue_start('2')
        >>> f.dequeue_start()
        '2'
        >>> f.dequeue_start()
        '1'
        >>> f.dequeue_start()
        Traceback (most recent call last):
        ...
        ValueError: Fila vazia
        '''
        
        if (self.vazia()):
            raise ValueError('Fila vazia')
        
        elemento = self.valores[self.inicio]
        self.inicio = (self.inicio + 1) % self.Capacidade
        self.tamanho -= 1
        
        return elemento
        
        
    def queue_end(self, item: str) -> None:
        '''
        Insere um elemento no fim da fila.
        
        Exemplos
        >>> f = FilaDupla(2)
        >>> f.queue_end('1')
        >>> f.queue_end('2')
        >>> f.queue_end('oi')
        Traceback (most recent call last):
        ...
        ValueError: Fila cheia
        >>> f.dequeue_start()
        '1'
        >>> f.dequeue_end()
        '2'
        '''
        
        if (self.cheia()):
            raise ValueError('Fila cheia')
        
        self.valores[self.fim] = item
        self.fim = (self.fim + 1) % self.Capacidade 
        self.tamanho += 1
        
        
    def dequeue_end(self) -> str:
        '''
        Remove e devolve um elemento do fim da fila.
        
        Exemplos
        >>> f = FilaDupla(3)
        >>> f.queue_end('Salve')
        >>> f.queue_end('Bora')
        >>> f.queue_end('bill')
        >>> f.dequeue_end()
        'bill'
        >>> f.dequeue_end()
        'Bora'
        >>> f.dequeue_end()
        'Salve'
        >>> f.dequeue_end()
        Traceback (most recent call last):
        ...
        ValueError: Fila vazia
        '''
        
        if (self.vazia()):
            raise ValueError('Fila vazia')
        
        self.fim = (self.fim - 1) % self.Capacidade
        elemento = self.valores[self.fim]
        self.tamanho -= 1
        
        return elemento
        
        
    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        
        Exemplos
        >>> f = FilaDupla(4)
        >>> f.vazia()
        True
        >>> f.queue_end('3')
        >>> f.vazia()
        False
        '''
        
        return self.tamanho == 0
        
    
    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia, False caso contrário.
        
        Exemplo
        >>> f = FilaDupla(2)
        >>> f.cheia()
        False
        >>> f.queue_start('1')
        >>> f.queue_end('2')
        >>> f.cheia()
        True
        '''
    
        return self.tamanho == self.Capacidade
    
    
    