from pilha_arranjo import Pilha

class FilaUsandoPilhas:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.
    
    >>> f = FilaUsandoPilhas()
    >>> f.vazia()
    True
    >>> f.enfileira('1')
    >>> f.enfileira('2')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    '1'
    >>> f.enfileira('3')
    >>> f.desenfileira()
    '2'
    >>> f.desenfileira()
    '3'
    >>> f.vazia()
    True
    '''
    
    pilha_entrada: Pilha
    pilha_saida: Pilha
    
    def __init__(self):
        '''
        Inicializa o TAD com duas pilhas.
        '''
        self.pilha_entrada = Pilha()
        self.pilha_saida = Pilha()
        
        
    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        '''
        if (self.pilha_entrada.topo >= len(self.pilha_entrada.valores) - 1):
            raise ValueError('pilha cheia')

        self.pilha_entrada.empilha(item)


    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''

        if (self.pilha_saida.vazia()):
            while (not (self.pilha_entrada.vazia())):
                self.pilha_saida.empilha(self.pilha_entrada.desempilha())

        if (self.pilha_saida.vazia()):
            raise ValueError('pilha vazia')

        elemento = self.pilha_saida.desempilha()
        
        return elemento

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        
        return self.pilha_entrada.vazia() and self.pilha_saida.vazia()
        