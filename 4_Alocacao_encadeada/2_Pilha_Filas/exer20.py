from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None

class FilaPrioridades:
    '''
    Uma coleção de inteiros que representa uma fila de prioridades.
    
    A fila organiza as pessoas em ordem de prioridade que segue a política FIFO dentro
    de cada nível de prioridade.
    
    Os elementos com maior prioridade  (valor mais alto) são removidos antes daqueles
    com prioridade menor.
    
    Exemplos
    '''

    inicio: No | None

    def __init__(self):
        '''
        Cria um novo encadeamento.
        '''
        
        self.inicio = None


    def enfileira(self, item: int) -> None:
        '''
        Adiciona *item* na fila de acordo com a prioridade.
        
        Exemplo
        >>> f = FilaPrioridades()
        >>> f.enfileira(5)
        >>> f.enfileira(2)
        >>> f.enfileira(7)
        >>> f.enfileira(4)
        >>> f.str()
        '[7, 5, 4, 2]'
        '''
        
        if self.inicio is None:
            self.inicio = No(item, None)
            
        else:   
            inicio_aux = self.inicio    
            while (inicio_aux.prox is not None) and (item <= inicio_aux.item) and (item <= inicio_aux.prox.item):
                inicio_aux = inicio_aux.prox
            
            if item <= self.inicio.item:
                inicio_aux.prox = No(item, inicio_aux.prox)
        
            else:
                self.inicio = No(item, inicio_aux)

    def desenfileira(self) -> int:
        '''
        Remove e devolve o primeiro elemento da fila.
        
        Exemplo
        >>> f = FilaPrioridades()
        >>> f.enfileira(5)
        >>> f.enfileira(2)
        >>> f.enfileira(7)
        >>> f.enfileira(4)
        >>> f.desenfileira()
        7
        >>> f.desenfileira()
        5
        >>> f.enfileira(10)
        >>> f.enfileira(6)
        >>> f.str()
        '[10, 6, 4, 2]'
        '''

        if self.vazia():
            raise ValueError('fila vazia.')

        valor = self.inicio.item
        self.inicio = self.inicio.prox

        return valor

    def vazia(self) -> None:
        '''
        Devolve True se a fila está vazia. False caso contrario.
        
        Exemplo
        >>> f = FilaPrioridades()
        >>> f.vazia()
        True
        >>> f.enfileira(2)
        >>> f.vazia()
        False
        '''

        return self.inicio is None


    def str(self) -> str:
        '''
        Devolve uma representação de lista em string.
        
        Exemplo
        >>> f = FilaPrioridades()
        >>> f.str()
        '[]'
        '''
        
        res = '['
        aux = self.inicio
        
        if not self.vazia():
            res += str(aux.item)
            
            aux = aux.prox
            while aux is not None:
                res += ', ' + str(aux.item)
                aux = aux.prox
        
        return res + ']'
        
        