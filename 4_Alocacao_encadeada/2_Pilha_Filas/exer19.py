from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


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

    # Invariantes:
    #   - Se inicio é None, então fim é None
    #   - Se inicio é um No, então fim é o nó no fim do encadeamento que começa
    #     em inicio
    inicio: No | None
    fim: No | None

    def __init__(self) -> None:
        '''Cria uma nova fila vazia'''
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        '''
        if self.fim is None:
            assert self.inicio is None
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is None:
            raise ValueError('fila vazia')
        
        item = self.inicio.item
        self.inicio = self.inicio.prox
        
        if self.inicio is None:
            self.fim = None
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None


    def junta(self, outra_fila: Fila) -> None:
        '''
        Passa em ordem, todos os elementos da *outra_fila* para o final da fila que a chamou.
        
        Exemplo
        # CASO 1: AMBOS VAZIOS
        >>> f1 = Fila()
        >>> f1.vazia()
        True
        >>> f2 = Fila()
        >>> f2.vazia()
        True
        >>> f1.junta(f2)
        >>> f1.vazia()
        True
        >>> f2.vazia()
        True
        
        # CASO 2: UMA COM VALORES E OUTRA VAZIA
        >>> f1 = Fila()
        >>> f1.enfileira('a')
        >>> f1.enfileira('b')
        >>> f1.vazia() 
        False
        >>> f2 = Fila()
        >>> f2.vazia()
        True
        >>> f1.junta(f2)
        >>> f1.vazia() 
        False
        >>> f2.vazia()
        True
        >>> f1.desenfileira()
        'a'
        >>> f1.desenfileira()
        'b'
        >>> f1.vazia()
        True

        # CASO 3: UMA VAZIA E OUTRA COM VALORES.
        >>> f1 = Fila()
        >>> f1.enfileira('a')
        >>> f1.enfileira('b')
        >>> f1.vazia() 
        False
        >>> f2 = Fila()
        >>> f2.vazia()
        True
        >>> f2.junta(f1)
        >>> f1.vazia() 
        False
        >>> f2.vazia()
        False
        >>> f2.desenfileira()
        'a'
        >>> f2.desenfileira()
        'b'
        >>> f2.vazia()
        True
        
        # CASO 4: AMBOS COM VALORES
        >>> f1 = Fila()
        >>> f1.enfileira('1')
        >>> f1.enfileira('2')
        >>> f2 = Fila()
        >>> f2.enfileira('3')
        >>> f2.enfileira('4')
        >>> f2.junta(f1)
        >>> f1.vazia()
        False
        >>> f2.vazia()
        False
        >>> while not f2.vazia():
        ...     f2.desenfileira()
        '3'
        '4'
        '1'
        '2'
        >>> f2.vazia()
        True
        '''
        
        if self.vazia():
            self.inicio = outra_fila.inicio
            self.fim = outra_fila.fim
            
        else:
            assert self.fim is not None
            self.fim.prox = outra_fila.inicio
            self.fim = outra_fila.fim

        
        