from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    topo: No | None

    def __init__(self) -> None:
        '''
        Cria uma pilha vazia
        '''
        self.topo = None

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        self.topo = No(item, self.topo)

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.
        '''
        if self.topo is None:
            raise ValueError('pilha vazia')
        
        item = self.topo.item
        self.topo = self.topo.prox
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.
        '''
        return self.topo is None


    def inverte(self) -> None:
        '''
        Inverte a ordem dos elementos da pilha
        >>> p = Pilha()
        >>> p.empilha('1')
        >>> p.empilha('2')
        >>> p.empilha('3')
        >>> p.empilha('4')
        >>> p.inverte()
        >>> p.desempilha()
        '1'
        >>> p.desempilha()
        '2'
        >>> p.desempilha()
        '3'
        >>> p.desempilha()
        '4'
        '''
        
        pilha_aux = None
        
        while not self.vazia():
            pilha_aux = No(self.desempilha(), pilha_aux)
            
        self.topo = pilha_aux
    
    