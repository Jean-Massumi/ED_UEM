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
    
        if (self.fila_saida.fim == len(self.fila_saida.valores) - 1):
            raise ValueError('pilha cheia')
        
        # Adiciona o item na fila_entrada
        self.fila_entrada.enfileira(item)

        # Transfere todos os elementos de fila_saida para fila_entrada
        while not self.fila_saida.vazia():
            self.fila_entrada.enfileira(self.fila_saida.desenfileira())

        # Troca as referências de fila_entrada e fila_saida
        self.fila_entrada, self.fila_saida = self.fila_saida, self.fila_entrada
    
    
    def pop(self) -> str:
        '''
        Remove e retorna o elemento no topo da pilha.
        '''
        
        if (self.vazia()):
            raise ValueError('pilha vazia')
        
        # Remove o elemento do início da fila_saida, que é o topo da pilha
        return self.fila_saida.desenfileira()
        
    def vazia(self) -> None:
        '''
        Verifica se a pilha está vazia.
        '''
    
        return self.fila_saida.vazia()