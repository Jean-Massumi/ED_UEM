from fila_arranjo_fim import Fila

class PilhaUsandoFilas:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.
    
    Exemplo
    >>> p = PilhaUsandoFilas()
    >>> p.vazia()
    True
    >>> p.push('1')
    >>> p.push('2')
    >>> p.vazia()
    False
    >>> p.pop()
    '2'
    >>> p.push('3')
    >>> p.pop()
    '3'
    >>> p.pop()
    '1'
    >>> p.vazia()
    True
    '''
    
    fila_entrada: Fila
    fila_saida: Fila
    
    def __init__(self) -> None:
        '''
        Inicializa com duas filas vazias.
        '''
    
        self.fila_entrada = Fila()
        self.fila_saida = Fila()
        
    
    def push(self, item: str) -> None:
        '''
        Insere um elemento no topo da pilha.
        '''
    
        if (self.fila_entrada.fim == len(self.fila_entrada.valores) - 1):
            raise ValueError('pilha cheia')
        
        if (self.fila_saida.fim == 0):
            self.fila_entrada.enfileira(self.fila_saida.desenfileira())
    
        self.fila_saida.enfileira(item)
    
    
    def pop(self) -> str:
        '''
        Remove e retorna o elemento no topo da pilha.
        '''
        
        if (self.vazia()):
            raise ValueError('pilha vazia')
        
        elemento = self.fila_saida.desenfileira()
        
        while  not (self.fila_entrada.vazia()):
            self.push(self.fila_entrada.desenfileira())
        
        return elemento
        
    def vazia(self) -> None:
        '''
        Verifica se a pilha está vazia.
        '''
    
        return self.fila_entrada.vazia() and self.fila_saida.vazia()